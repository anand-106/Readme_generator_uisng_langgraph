from Parser.python_parser import analyze_codebase_with_folders
from chunker.chunker import prepare_chunks
from summerize.summerizer import summerize_chunks,generate_final_summary
from pprint import pprint
from Parser.code_walker import walk_codebase
from Parser.analyzer import analyze_codebase

structure = walk_codebase("C:/Users/gamin/Documents/projects/Ticket_classifier_using_LangGraph/")
#result  = analyze_codebase_with_folders("C:/Users/gamin/Documents/projects/Ticket_classifier_using_LangGraph/")

result = analyze_codebase("C:/Users/gamin/Documents/projects/Ticket_classifier_using_LangGraph/")

chunks = prepare_chunks(result)

summary = summerize_chunks(chunks)

readme = generate_final_summary(chunk_summaries=summary,project_structure=structure)

pprint(readme)



