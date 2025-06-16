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
You are a senior software engineer tasked with writing a modern, professional, high-level `README.md` for a GitHub project.

Use the provided code chunk summaries and project structure to:
- Clearly explain what the project does.
- Highlight core features, unique architecture, and technical insights.
- Mention important agents, workflows, or modules when relevant.
- Use concise, developer-friendly language with technical precision.

🧩 **Formatting Requirements**:
- The project title and badges **must be centered** using `<p align="center"> ... </p>`.
- Use heading syntax like: `# <p align="center">Your Title Here</p>` the # should always be outside the <p> tag , must make sure of that.
- Insert all badges **inside** the centered `<p>` block. Use proper shields.io badge URLs.
- Do **not** wrap the output in triple backticks (raw markdown only).
- Maintain proper markdown formatting with bold text, headers, bullet points, and links where appropriate.

📦 **Content Requirements**:

### 1. Title & Centered Badges (Required)
- Use: `# <p align="center">Project Name</p>` the # should be always outside the <p> tag.
- Below it, place badges using standard shields.io badge markdown (in the another centered <p>).
- Include relevant tech badges: FastAPI, Python, MongoDB, LangChain, React, Tailwind, Auth0, etc.

### 2. Introduction
- Briefly describe the project in 2–4 lines.
- Mention its purpose, use case, and target users.

### 3. Table of Contents (if the README is long)

### 4. Key Features
- List major features, components, workflows, or capabilities.

### 5. Installation Guide
- Step-by-step instructions: clone, install dependencies, run the FastAPI server.
- Mention `.env` variables like Auth0 credentials, DB URI, etc.

### 6. Usage
- Briefly explain how developers or users interact with it.
- Mention API endpoints, frontend/backend interaction, or CLI tools if applicable.

### 7. API Reference (Optional, if present)

### 8. Environment Variables
- List required env vars and what they are used for.

### 9. Project Structure
- Include the project’s file structure for context. The structure is: {file_structure}


### 10. Technologies Used
- Use `shields.io` badges to represent the stack visually.
- Mention backend, frontend, database, auth, and tools.

### 11. Contribution Guide
- Instructions for contributing, PR guidelines, etc.

### 12. Support & Contact
- How users can raise issues or reach out.

### 13. License
- Mention and badge (e.g., MIT).

Use or skip sections based on the actual project and its complexity.

---

Below are the code chunk summaries for the project:

{combined_summary}

Now, generate the entire `README.md` as **raw Markdown**.
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


