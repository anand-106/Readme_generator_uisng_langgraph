from langgraph.graph import StateGraph,START,END
from pprint import pprint
from typing import TypedDict,List,Any,Dict
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class ReadmeState(TypedDict):
    codebase_path:str
    structure: List[Any]
    ast: Dict[str,Any]
    chunks: List[Any]
    summary: List[Any]
    readme: str

def walk_codebase_node(state:ReadmeState):
    from Parser.code_walker import walk_codebase
    state["structure"]=walk_codebase(state["codebase_path"])
    return state

def parser_node(state:ReadmeState):
    from Parser.analyzer import analyze_codebase
    state["ast"]= analyze_codebase(state["codebase_path"])
    return state

def chunker_node(state:ReadmeState):
    from chunker.chunker import prepare_chunks
    state["chunks"] = prepare_chunks(state["ast"])
    return state

def summarizer_node(state:ReadmeState):
    from summerize.summerizer import summerize_chunks
    state["summary"] = summerize_chunks(state["chunks"])
    return state

def readme_node(state:ReadmeState):
    from summerize.summerizer import generate_final_summary
    state["readme"] = generate_final_summary(state["summary"])
    return state

def readme_graph():

    builder = StateGraph(ReadmeState)

    builder.add_node("WalkCodebase",walk_codebase_node)
    builder.add_node("ASTParser",parser_node)
    builder.add_node("Chunker",chunker_node)
    builder.add_node("Summarizer",summarizer_node)
    builder.add_node("ReadmeGenerator",readme_node)

    builder.add_edge(START,"WalkCodebase")
    builder.add_edge("WalkCodebase","ASTParser")
    builder.add_edge("ASTParser","Chunker")
    builder.add_edge("Chunker","Summarizer")
    builder.add_edge("Summarizer","ReadmeGenerator")
    builder.add_edge("ReadmeGenerator",END)

    return builder.compile()

if __name__ == "__main__" :

    graph = readme_graph()

    input_state = {"codebase_path": "C:/Users/gamin/Documents/projects/Ticket_classifier_using_LangGraph/"}

    final_state = graph.invoke(input_state)

    pprint(final_state["readme"])

