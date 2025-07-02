import google.generativeai as genai
import os
from tqdm import tqdm
import json
from pathlib import Path
from dotenv import load_dotenv
import re
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

def generate_final_summary(chunk_summaries, project_structure=None,preferences={},project_description="",full_structure=None):

    preferences = preferences.dict()

    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))  
    model = genai.GenerativeModel(model_name='gemini-2.0-flash')

    # Format the summaries
    combined_summary = "\n\n".join(
        f"### Chunk {item['index']} Summary:\n{item['summary']}"
        for item in chunk_summaries
    )

    converted_structure = convert_paths(project_structure)
    file_structure = json.dumps(converted_structure, indent=2)

    full_converted_structure = convert_paths(full_structure)
    full_file_structure = json.dumps(full_converted_structure, indent=2)


    section_blocks = []

    if preferences["title"]:
        section_blocks.append("""
### 1. Title & Centered Badges (Required)
- Use: `# <p align="center">Project Name</p>` the # should be always outside the <p> tag.""")

    if preferences["badge"]:
        section_blocks.append("""
### 2. Centered Badges
- Place badges using standard shields.io badge markdown (in another centered <p>).
- Include relevant tech badges: for example FastAPI, Python, MongoDB, LangChain, React, Tailwind, Auth0, etc. that are used in the project only""")

    if preferences["introduction"]:
        section_blocks.append("""
### 3. Introduction
- Briefly describe the project in 2–4 lines.
- Mention its purpose, use case, and target users.""")

    if preferences["table_of_contents"]:
        section_blocks.append("""
### 4. Table of Contents
- Add links to each section of the README.""")

    if preferences["key_features"]:
        section_blocks.append("""
### 5. Key Features
- List major features, components, workflows, or capabilities.""")

    if preferences["install_guide"]:
        section_blocks.append("""
### 6. Installation Guide
- Step-by-step instructions: clone, install dependencies, run the FastAPI server.
- Mention `.env` variables like Auth0 credentials, DB URI, etc.""")

    if preferences["usage"]:
        section_blocks.append("""
### 7. Usage
- Explain how developers or users interact with it.
- Mention API endpoints, frontend/backend interaction, or CLI tools if applicable.""")

    if preferences["api_ref"]:
        section_blocks.append("""
### 8. API Reference (Optional, if present)
- Document important endpoints and request/response formats.""")

    if preferences["env_var"]:
        section_blocks.append("""
### 9. Environment Variables
- List required env vars and what they are used for.""")

    if preferences["project_structure"]:
        section_blocks.append(f"""
### 10. Project Structure
- Include the project's file structure for context. The structure is: {full_file_structure}""")
    if preferences["tech_used"]:
        section_blocks.append("""
### 11. Technologies Used
- Use `shields.io` badges to represent the stack visually.
- Mention backend, frontend, database, auth, and tools.""")

    if preferences["licenses"]:
        section_blocks.append("""
### 12. License
- Mention the license (e.g., MIT) and include a badge.""")

    # Combine everything
    content_requirements = "\n".join(section_blocks)

    # Final prompt
    prompt = f"""
You are a senior software engineer tasked with writing a modern, professional, high-level `README.md` for a GitHub project.

Use the provided code chunk summaries and project structure to:
- Clearly explain what the project does.
- Highlight core features, unique architecture, and technical insights.
- Mention important agents, workflows, or modules when relevant.
- Use concise, developer-friendly language with technical precision.

**Formatting Requirements**:

- The project **title and badges must be centered** using `<p align="center"> ... </p>` syntax.
- The **title must use this exact format**: `# <p align="center">Your Title Here</p>` — `#` must always be outside the `<p>` tag.
- The **badges block** must appear in a **separate** line after the title like:
  <p align="center">
    <a href="#"><img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI"></a>
    <a href="#"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  </p>
- Use only supported logos from Shields.io. **Do not embed base64 images** in the badge `logo=` fields. If no logo exists, omit the logo field entirely.

**Content Requirements**:
{content_requirements}

do not add or remove extra sections other than these.

also take into account : {project_description}

---

Below are the code chunk summaries for the project:

{combined_summary}

Now, generate the entire `README.md` as **raw Markdown**.

"""



    # print(f'the prompt is : {prompt}')
    

    try:
        print("Started generating readme.md")
        response = model.generate_content(prompt)
        
        print("Succesfully generated readme.md")
        content = response.text.strip()
        content = re.sub(r'logo=data:image/[^&"\')>]+', '', content)


        if content.startswith("```markdown"):
           content = content[len("```markdown"):].lstrip()
        if content.endswith("```"):
           content = content[:-3].rstrip()
        
        # f = open("response.md",'w',encoding='utf-8')
        # f.write(content)

        return content
        
    except Exception as e:
        return f"[ERROR generating final summary]: {str(e)}"


