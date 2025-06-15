import google.generativeai as genai
import os
from tqdm import tqdm
import json
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


def convert_paths(obj):
    if isinstance(obj, dict):
        return {k: convert_paths(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_paths(i) for i in obj]
    elif isinstance(obj, Path):
        return str(obj)
    else:
        return obj



def summerize_chunks(chunks):



    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

    model = genai.GenerativeModel(model_name='gemini-2.0-flash')
    summaries=[]

    for idx,chunk in tqdm(enumerate(chunks),total=len(chunks),desc="summerizing chunks"):

        chunk_data = json.dumps(chunk)

        prompt = f"""
                You are an AI code summarizer.

                Below is a list of Python code symbols (functions, classes, etc.), including their type, names, and raw source code.

                Summarize the entire chunk based on this structured information. Include:
                - what is the path to all the files
                - what are the framework or libraries used if any
                - What the functions and classes are doing overall.
                - How they might be used in the context of a project.
                - Any special behaviors or logic patterns you notice.

                Use professional, concise, and technical language suitable for a developer-oriented README.

                Symbols chunk:
                {chunk_data}

                Summary:
                """
        
        try:
            respone = model.generate_content(prompt)
            summaries.append({
                'index':idx,
                'summary':respone.text.strip()
            })
        except Exception as e:
            summaries.append({
                "chunk_index": idx,
                "summary": f"[ERROR summarizing chunk {idx}]: {str(e)}"
            })
    
    return summaries

def generate_final_summary(chunk_summaries, project_structure=None,preferences={},project_description=""):
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))  
    model = genai.GenerativeModel(model_name='gemini-2.0-flash')

    # Format the summaries
    combined_summary = "\n\n".join(
        f"### Chunk {item['index']} Summary:\n{item['summary']}"
        for item in chunk_summaries
    )

    converted_structure = convert_paths(project_structure)
    file_structure = json.dumps(converted_structure, indent=2)


    # Prompt for the final README-level summary
    prompt = f"""
You are a senior developer tasked with writing a high-level README summary for a project.
Create a professional, modern README for the project's GitHub repository.
give only the markdown rawcode.
 Include markdown badges using shields.io.
Use normal shields.io badge URLs like:

![LangChain](https://img.shields.io/badge/LangChain-34A853?style=for-the-badge&logo=langchain&logoColor=white)

Below is a series of code chunk summaries extracted from the project. Use this information to:

- Summarize what the project does overall.
- Highlight the core functionality, structure, and unique design choices.
- Mention important modules, agents, or workflows if applicable.
- Use technical, developer-friendly language in a professional tone.

1. **Getting Started**:
   - Provide clear setup instructions for cloning the project, installing dependencies, and running the FastAPI server.
   - Mention `.env` variables if applicable (e.g., Auth0 credentials, DB URI).

2. **Technology Stack / Badges**:
   - Include markdown badges for key technologies like FastAPI, MongoDB, LangChain, Auth0, Python, etc.
   - Use `shields.io` badge format.

The structure of the project is {file_structure}
Include the file structure of the project.


Chunk Summaries:
{combined_summary}

The generated README contains all the essential sections that every README should have - 

Title

Table of Contents

Introduction

Key Features

Installation Guide

Usage

API

Environment Variables

Contribution Guide

Support & Contact

Furthermore, add or remove the sections based upon the whole working and structure of the provided codebase.
Return the README content as raw Markdown, without wrapping it in code fences.
README-Level Project Summary:
"""

    try:
        print("Started generating readme.md")
        response = model.generate_content(prompt)
        
        print("Succesfully generated readme.md")
        content = response.text.strip()

        if content.startswith("```markdown"):
           content = content[len("```markdown"):].lstrip()
        if content.endswith("```"):
           content = content[:-3].rstrip()
        
        f = open("response.md",'w',encoding='utf-8')
        f.write(content)

        return content
        
    except Exception as e:
        return f"[ERROR generating final summary]: {str(e)}"


