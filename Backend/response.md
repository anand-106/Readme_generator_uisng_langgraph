# <p align="center">AI-Powered README Generator</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI"></a>
  <a href="#"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React"></a>
  <a href="#"><img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS"></a>
  <a href="#"><img src="https://img.shields.io/badge/LangChain-343434?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain"></a>
</p>

## Introduction

This project is an AI-powered README generator that automates the creation of comprehensive documentation for software projects. It analyzes a codebase, extracts relevant information, and uses a GenAI model to generate a well-structured README file. This tool aims to simplify the documentation process for developers, saving time and improving project understanding.

## Table of Contents

1.  [Key Features](#key-features)
2.  [Installation Guide](#installation-guide)
3.  [Usage](#usage)
4.  [Environment Variables](#environment-variables)
5.  [Project Structure](#project-structure)
6.  [Technologies Used](#technologies-used)
7.  [License](#license)

## Key Features

*   **Automated Code Analysis:** Analyzes the project's codebase to extract project metadata, file structure, dependencies, and API endpoints.
*   **Intelligent Chunking:** Divides the codebase into smaller chunks for efficient summarization by the GenAI model.
*   **AI-Powered Summarization:** Leverages a GenAI model (e.g., Gemini) to generate summaries for each code chunk.
*   **Customizable README Generation:** Allows users to customize the generated README by selecting which sections to include and providing a project description.
*   **Frontend Interface:** Provides a user-friendly React interface for inputting the GitHub URL, setting preferences, and previewing the generated README.
*   **Langchain Integration:** Uses Langchain to orchestrate the README generation process through a state graph, allowing for flexible and extensible workflows.
*   **Multi-language Support**: Supports both Python and JavaScript codebases, using `tree-sitter` for parsing.

## Installation Guide

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install backend dependencies:**

    ```bash
    cd Backend
    pip install -r requirements.txt
    ```

3.  **Install frontend dependencies:**

    ```bash
    cd ../frontend
    npm install
    ```

4.  **Configure environment variables:**

    Create a `.env` file in the `Backend` directory and set the following variables:

    ```
    GOOGLE_API_KEY=<your_google_api_key>
    # Add other necessary environment variables here
    ```

5.  **Run the FastAPI server:**

    ```bash
    cd ../Backend
    uvicorn main:app --reload
    ```

6.  **Run the React frontend:**

    ```bash
    cd ../frontend
    npm start
    ```

## Usage

1.  Open the frontend application in your browser (usually at `http://localhost:3000`).
2.  Enter the GitHub repository URL in the provided text box.
3.  Navigate to the README generation page.
4.  Customize the README by selecting the desired sections and providing a project description.
5.  Click the "Generate README" button to initiate the generation process.
6.  Preview the generated README and copy or download it as needed.
7.  You can regenerate the README with different preferences if needed.

## Environment Variables

*   `GOOGLE_API_KEY`:  The API key for the GenAI model (e.g., Gemini).  Required for summarizing code chunks and generating the final README content.

## Project Structure

```
├── Backend/
│   ├── main.py            # FastAPI application entry point
│   ├── agent/
│   │   └── agent.py       # Core logic of the README generation process
│   ├── api/
│   │   ├── model.py       # Pydantic data models
│   │   └── router.py      # FastAPI API endpoints
│   │   └── utils/
│   │       └── github_utils.py # Utility functions for interacting with GitHub
│   ├── chunker/
│   │   ├── chunker.py     # Code chunking logic
│   │   └── token_estimator.py # Token estimation for code chunks
│   ├── Parser/
│   │   ├── analyzer.py    # Codebase analyzer
│   │   ├── code_walker.py # Codebase traversal
│   │   ├── js_parser.py   # JavaScript code parser
│   │   ├── python_parser.py # Python code parser
│   │   └── full/         # parser for code
│   │       ├── AST_parser.py # AST parser
│   │       ├── build_library.py # Build Parser Library
│   │       ├── parser_setup.py # Parser setup
│   │       ├── sample.js     # Sample javascript file
│   │       ├── sample.py     # Sample python file
│   │       └── test.py       # Test
│   ├── summerize/
│   │   └── summerizer.py  # Code summarization and README generation
├── frontend/
│   ├── src/
│   │   ├── App.js         # React application entry point
│   │   ├── index.js       # React index file
│   │   ├── components/
│   │   │   ├── home/
│   │   │   │   ├── LinkTextBox.js  # GitHub URL input component
│   │   │   │   └── Title.js       # Title component
│   │   │   └── ReadmePage/
│   │   │       ├── markdownComp.js   # Markdown display and download component
│   │   │       └── preferencesComp.js # README preferences component
│   │   ├── pages/
│   │   │   ├── HomePage.js      # Home page component
│   │   │   └── ReadmePage.js    # README generation page component
│   │   ├── utils/
│   │   │   └── api/
│   │   │       └── ApiCaller.js   # API calling utility
│   ├── tailwind.config.js # Tailwind CSS configuration
```

## Technologies Used

<p align="left">
    <a href="#"><img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI"></a>
    <a href="#"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
    <a href="#"><img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React"></a>
    <a href="#"><img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS"></a>
    <a href="#"><img src="https://img.shields.io/badge/LangChain-343434?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain"></a>
    <a href="#"><img src="https://img.shields.io/badge/Tree--sitter-000000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTEyLjM3NSAxLjc1YS42MjUuNjI1IDAgMCAwLS42MjUtLjYyNWgtMy41Yy0uMzQ1IDAtLjYyNS4yODEtLjYyNS42MjV2Ni41NjNjMCAuMzQ0LjI4LjYyNC42MjUuNjI0aDMuNWMuMzQ1IDAgLjYyNS0uMjguNjI1LS42MjRWMS43NXpNOC4zNzUgNy44NzVhLjYyNS42MjUgMCAwIDAtLjYyNS0uNjI1aC0zLjVjLS4zNDUgMC0uNjI1LjI4LS42MjUuNjI1djYuNTYyYzAgLjM0NS4yOC42MjUuNjI1LjYyNWgzLjVjLjM0NSAwIC42MjUtLjI4LjYyNS0uNjI1Vjc4NzVaTTQuMzc1IDQuMzYyYS42MjUuNjI1IDAgMCAwLS42MjUtLjYyNWgtMy41Yy0uMzQ1IDAtLjYyNS4yOC0uNjI1LjYyNXY2LjU2M2MwIC4zNDQuMjguNjI0LjYyNS42MjRoMy41Yy4zNDUgMCAuNjI1LS4yOC42MjUtLjYyNFY0LjM2M1oiLz48L3N2Zz4=" alt="Tree-sitter"></a>
    <a href="#"><img src="https://img.shields.io/badge/Pydantic-e83d88?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic"></a>
    <a href="#"><img src="https://img.shields.io/badge/axios-5A29E4?style=for-the-badge&logo=axios&logoColor=white" alt="Axios"></a>
    <a href="#"><img src="https://img.shields.io/badge/GitPython-F05032?style=for-the-badge&logo=git&logoColor=white" alt="GitPython"></a>

</p>

*   **Backend:** FastAPI, Python, Langchain, Tree-sitter, Pydantic, GitPython
*   **Frontend:** React, React Router DOM, Axios, DOMPurify, Tailwind CSS
*   **GenAI Model:** Google Gemini (via `google.generativeai`)

## License

MIT License

<p align="left">
    <a href="#"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"></a>
</p>