from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import interrupt, Command
from typing import TypedDict, List, Any, Dict, Literal
from api.utils.github_utils import clone_repo,webhook_clone_repo
from pprint import pprint
import os
from dotenv import load_dotenv
import shutil

class ReadmeState(TypedDict, total=False):
    codebase_path: str
    structure: List[Any]
    full_structure: List[Any]
    ast: Dict[str, Any]
    chunks: List[Any]
    summary: List[Any]
    readme: str
    preferences: Dict[str, Any]
    project_description: str
    action: Literal["regenerate", "end"]
    
class WebhookReadmeState(TypedDict, total=False):
    codebase_path: str
    structure: List[Any]
    full_structure: List[Any]
    ast: Dict[str, Any]
    chunks: List[Any]
    summary: List[Any]
    readme: str
    preferences: Dict[str, Any]
    project_description: str


def walk_codebase_node(state: ReadmeState):
    from Parser.code_walker import walk_codebase,walk_full_codebase
    state["structure"] = walk_codebase(state["codebase_path"])
    state["full_structure"]=walk_full_codebase(state["codebase_path"])
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
    state["readme"] = generate_final_summary(state["summary"], preferences=state["preferences"], project_description=state["project_description"],project_structure=state["structure"],full_structure=state["full_structure"])
    return state

def user_feedback_node(state: ReadmeState):
    value = interrupt({"readme": state["readme"]})
    print("In interrept node")
    return value

def should_continue(state: ReadmeState):
    print("checking should continue or not")
    print(f'In state it is : {state.get("action", "end")}')
    return state.get("action", "end")

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

    return builder.compile(checkpointer=InMemorySaver())

def webhook_graph():
    builder = StateGraph(WebhookReadmeState)
    builder.add_node("WalkCodebase", walk_codebase_node)
    builder.add_node("ASTParser", parser_node)
    builder.add_node("Chunker", chunker_node)
    builder.add_node("Summarizer", summarizer_node)
    builder.add_node("ReadmeGenerator", readme_node)

    builder.set_entry_point("WalkCodebase")
    builder.add_edge("WalkCodebase", "ASTParser")
    builder.add_edge("ASTParser", "Chunker")
    builder.add_edge("Chunker", "Summarizer")
    builder.add_edge("Summarizer", "ReadmeGenerator")
    builder.add_edge("ReadmeGenerator",END)
    
    return builder.compile()



def webhook_pipeline(url:str, description: str, preferences: dict):
    
    load_dotenv()
    token = os.getenv("TOKEN")
    codebase_path = webhook_clone_repo(url=url,token=token)
    
    graph = webhook_graph()
    
    input_state = {
        "codebase_path": codebase_path,
        "project_description": description,
        "preferences": preferences,
    }
    
    state = graph.invoke(input_state)
    
    
    try:
        shutil.rmtree(codebase_path)
        print("Successfully removed the temp repo")
    except Exception as e:
        print(f"error removing tree: {e}")
        
    
    
    
    return state
    
    

SESSION_CACHE: Dict[str, Any] = {}

def run_readme_pipeline(url: str, description: str, preferences: dict, session_id: str):
    codebase_path = clone_repo(url)
    input_state = {
        "codebase_path": codebase_path,
        "project_description": description,
        "preferences": preferences,
        "action": "regenerate"
    }
    graph = readme_graph()
    config = {"configurable": {"thread_id": session_id}}

    iterator = graph.invoke(input_state, config=config)
    
    SESSION_CACHE[session_id] = {
    "graph": graph,
    "state": input_state,
    "ended": False
}
    try:
        shutil.rmtree(codebase_path)
        print("Successfully removed the temp repo")
    except Exception as e:
        print(f"error removing tree: {e}")

    pprint(iterator.keys())
    return iterator

def resume_readme_pipeline(session_id: str,description: str, preferences: dict ,action: str = "end" ):
    session = SESSION_CACHE.get(session_id)
    if not session:
        raise ValueError("Session not found")
    if session.get("ended", False):
        raise RuntimeError("This session has already ended and cannot be resumed.")

    graph = session["graph"]
    previous_state = session["state"]
    previous_state["action"] = action
    previous_state["preferences"] = preferences
    previous_state["project_description"] = description

    config = {"configurable": {"thread_id": session_id}}
    new_state = graph.invoke(Command(resume=previous_state), config=config)

    SESSION_CACHE[session_id]["state"] = new_state

    if action == "end":
        SESSION_CACHE[session_id]["ended"]=True
        try:
            path = new_state["codebase_path"]
            shutil.rmtree(path)
            print(f"Successfully removed the folder at {path}")
        except Exception as e:
            print(f'Removing folder failed: {e}')

    pprint(new_state.keys())
    return new_state

