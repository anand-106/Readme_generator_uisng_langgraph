from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import interrupt, Command
from typing import TypedDict, List, Dict, Any, Literal
from api.utils.github_utils import clone_repo
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Define the pipeline state
class ReadmeState(TypedDict, total=False):
    codebase_path: str
    structure: List[Any]
    ast: Dict[str, Any]
    chunks: List[Any]
    summary: List[Any]
    readme: str
    preferences: Dict[str, Any]
    project_description: str
    action: Literal["regenerate", "end"]

# Nodes
def walk_codebase_node(state: ReadmeState):
    from Parser.code_walker import walk_codebase
    state["structure"] = walk_codebase(state["codebase_path"])
    return state

def parser_node(state: ReadmeState):
    from Parser.analyzer import analyze_codebase
    state["ast"] = analyze_codebase(state["codebase_path"])
    return state

def chunker_node(state: ReadmeState):
    from chunker.chunker import prepare_chunks
    state["chunks"] = prepare_chunks(state["ast"])
    return state

def summarizer_node(state: ReadmeState):
    from summerize.summerizer import summerize_chunks
    state["summary"] = summerize_chunks(state["chunks"])
    return state

def readme_node(state: ReadmeState):
    from summerize.summerizer import generate_final_summary
    state["readme"] = generate_final_summary(
        state["summary"],
        preferences=state["preferences"],
        project_description=state["project_description"]
    )
    return state

def user_feedback_node(state: ReadmeState):
    return interrupt({"readme": state["readme"], "message": "Review and choose to regenerate or end."})

def should_continue(state: ReadmeState):
    return state.get("action", "end")

# Build LangGraph
def readme_graph():
    builder = StateGraph(ReadmeState)

    builder.add_node("WalkCodebase", walk_codebase_node)
    builder.add_node("ASTParser", parser_node)
    builder.add_node("Chunker", chunker_node)
    builder.add_node("Summarizer", summarizer_node)
    builder.add_node("ReadmeGenerator", readme_node)
    builder.add_node("UserFeedback", user_feedback_node)

    builder.set_entry_point("WalkCodebase")
    builder.add_edge("WalkCodebase", "ASTParser")
    builder.add_edge("ASTParser", "Chunker")
    builder.add_edge("Chunker", "Summarizer")
    builder.add_edge("Summarizer", "ReadmeGenerator")
    builder.add_edge("ReadmeGenerator", "UserFeedback")
    builder.add_conditional_edges("UserFeedback", should_continue, {
        "regenerate": "ReadmeGenerator",
        "end": END
    })

    checkpoint = InMemorySaver()
    return builder.compile(checkpointer=checkpoint)

# Session store
SESSION_CACHE: Dict[str, Any] = {}
config = {"configurable": {"thread_id": "1"}}

# First-time run
def run_readme_pipeline(url: str, description: str, preferences: dict, session_id: str):
    codebase_path = clone_repo(url)
    input_state = {
        "codebase_path": codebase_path,
        "project_description": description,
        "preferences": preferences,
        "action": "regenerate"
    }

    graph = readme_graph()
    iterator = graph.stream(input_state, config=config)

    # Run until first interrupt
    for _ in range(5):
        step = next(iterator)

    SESSION_CACHE[session_id] = iterator
    return step["ReadmeGenerator"]  # Includes intermediate state like readme

# Resume with user input
def resume_readme_pipeline(session_id: str, action: str = "end"):
    iterator = SESSION_CACHE.get(session_id)

    if not iterator:
        raise ValueError("Session not found")

    try:
        step = iterator.send({"action": action})
        SESSION_CACHE[session_id] = iterator
        step=next(iterator)
        return step["ReadmeGenerator"]
    except StopIteration as e:
        SESSION_CACHE.pop(session_id, None)
        return e.value
