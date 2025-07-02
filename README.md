# <p align="center">AI-Powered README Generator</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI"></a>
  <a href="#"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React"></a>
  <a href="#"><img src="https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS"></a>
  <a href="#"><img src="https://img.shields.io/badge/LangGraph-blue?style=for-the-badge" alt="LangGraph"></a>
</p>

## Introduction

This project is an AI-powered README generator that automates the creation of `README.md` files for GitHub repositories. It analyzes the codebase, extracts relevant information, and utilizes a large language model (LLM) to generate comprehensive and professional-looking documentation. The target users are developers who want to quickly generate high-quality READMEs for their projects.

## Table of Contents

1.  [Key Features](#key-features)
2.  [Project Workflow](#project-workflow)
3.  [Installation Guide](#installation-guide)
4.  [Usage](#usage)
5.  [Environment Variables](#environment-variables)
6.  [Project Structure](#project-structure)
7.  [Technologies Used](#technologies-used)  
8.  [License](#license)

## Key Features

*   **Automated README Generation:** Automatically generates README files from GitHub repositories.
*   **Codebase Analysis:** Analyzes Python and JavaScript codebases using `tree-sitter` to extract relevant metadata.
*   **AI-Powered Summarization:** Leverages Google's Gemini AI model to generate concise and informative summaries of code components.
*   **Customizable Preferences:** Allows users to customize the generated README content based on their preferences.
*   **Interactive Frontend:** Provides a dynamic and interactive user experience with React.
*   **Session Management:** Maintains state between requests using session cookies, allowing users to regenerate or resume README generation.
*   **Human-in-the-Loop:** The LangGraph workflow allows for user feedback to regenerate the README with updated preferences.
*   **Code Complexity Analysis:** Calculates the complexity of code nodes to help with summarization and identify important parts of the codebase.

## Project Workflow

The AI-Powered README Generator employs a structured workflow, orchestrated using LangGraph, to transform a GitHub repository into a comprehensive README.md file. This workflow encompasses codebase analysis, parsing, chunking, summarization, and final README generation, incorporating a human-in-the-loop for refinement.

1.  **Repository Input:** The user provides a GitHub repository URL via the frontend.
2.  **Codebase Cloning:** The backend clones the specified repository to a temporary directory using `git clone`.
3.  **Codebase Walking:** The `walk_codebase_node` explores the cloned repository and identifies all code files. This step generates a file structure representation that guides subsequent analysis.
4.  **Code Parsing:** The `parser_node` leverages `tree-sitter` to parse the identified code files, extracting Abstract Syntax Trees (ASTs). These ASTs provide a structured representation of the code, facilitating symbol extraction (functions, classes, etc.) and dependency analysis.  Dedicated parsers handle both Python (`python_parser.py`) and JavaScript (`js_parser.py`) code.
5.  **Chunking:** The `chunker_node` divides the extracted ASTs into smaller, manageable chunks.  This is crucial for accommodating the token limits of the LLM used in the summarization step. The goal is to create semantically coherent chunks that can be effectively summarized.
6.  **Summarization:** The `summarizer_node` uses the Google Gemini model to generate summaries for each code chunk. The summarization process focuses on identifying key functionalities, frameworks used, usage context, and design patterns within the code.
7.  **README Generation:** The `readme_node` aggregates the generated summaries and user preferences to construct the initial README.md content. This stage also incorporates elements like the project title, description, table of contents, and other customizable sections based on user input.
8.  **User Feedback (Human-in-the-Loop):** The generated README is presented to the user via the frontend's `MarkdownViewer` component. The user can then provide feedback and modify their preferences (e.g., include/exclude specific sections, adjust the project description).
9.  **Regeneration (Optional):** If the user provides feedback, the workflow loops back to the summarization stage, incorporating the updated preferences. This iterative process allows for refining the README until it meets the user's requirements.
10. **Final README Output:** Once the user is satisfied, the final README.md content is presented, and the user can copy it to the clipboard or download it. The temporary repository is then deleted.
11. **LangGraph Orchestration:** The entire process is managed by a LangGraph graph defined in `agent.py`. Each step (walking, parsing, chunking, summarizing, etc.) is represented as a node in the graph.  The graph defines the flow of execution and the dependencies between the nodes, allowing for a robust and maintainable workflow. The `should_continue` node determines the next step based on user feedback.

## Installation Guide

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install backend dependencies:**

    ```bash
    cd Backend
    python3 -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    pip install -r requirements.txt
    cd ..
    ```

3.  **Install frontend dependencies:**

    ```bash
    cd frontend
    npm install
    cd ..
    ```

4.  **Configure environment variables:**

    Create a `.env` file in the root directory with the following variables:

    ```
    GOOGLE_API_KEY=<your_google_api_key>
    # Add any other necessary environment variables here
    ```

5.  **Run the FastAPI server:**

    ```bash
    cd Backend
    uvicorn main:app --reload
    ```

6.  **Run the React frontend:**

    ```bash
    cd frontend
    npm start
    ```

## Usage

1.  Open your web browser and navigate to the frontend application (usually `http://localhost:3000`).
2.  Enter the GitHub repository URL in the provided text box.
3.  Optionally, provide a project description.
4.  Select your preferences for the README content (e.g., include table of contents, key features).
5.  Click the "Generate README" button.
6.  The generated README will be displayed in the `MarkdownViewer` component, where you can preview it and copy or download it.

## Environment Variables

The following environment variables are required for the application to run correctly:

*   `GOOGLE_API_KEY`: Your Google API key for accessing the Gemini AI model.

## Project Structure

```
.
├── Backend/
│   ├── api/
│   │   ├── model.py
│   │   ├── router.py
│   │   └── utils/
│   │       └── github_utils.py
│   ├── chunker/
│   │   ├── chunker.py
│   │   └── token_estimator.py
│   ├── Parser/
│   │   ├── analyzer.py
│   │   ├── code_walker.py
│   │   ├── js_parser.py
│   │   └── python_parser.py
│   ├── summerize/
│   │   └── summerizer.py
│   ├── agent/
│   │   └── agent.py
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── home/
│   │   │   │   ├── LinkTextBox.js
│   │   │   │   └── Title.js
│   │   │   ├── ReadmePage/
│   │   │   │   ├── markdownComp.js
│   │   │   │   └── preferencesComp.js
│   │   ├── pages/
│   │   │   ├── Aurora/
│   │   │   │   └── Aurora.jsx
│   │   │   ├── GradientText/
│   │   │   │   └── GradientText.jsx
│   │   │   ├── HomePage.js
│   │   │   └── ReadmePage.js
│   │   ├── utils/
│   │   │   └── api/
│   │   │       └── ApiCaller.js
│   │   ├── animations/
│   │   │   ├── SlidePageWrapperExit.js
│   │   │   └── SlidePageWrapper.js
│   │   ├── App.js
│   │   ├── index.css
│   │   └── index.js
│   ├── package-lock.json
│   ├── package.json
│   ├── tailwind.config.js
│   └── tsconfig.json
├── README.md
└── render.yaml
```

## Technologies Used

*   **Backend:** FastAPI, Python
*   **Frontend:** React, Tailwind CSS
*   **Code Analysis:** Tree-sitter
*   **AI Model:** Google Gemini
*   **Utilities:** Axios, LangGraph


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
