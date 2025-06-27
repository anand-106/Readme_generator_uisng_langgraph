# <p align="center">Automated README Generator</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI"></a>
  <a href="#"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React"></a>
  <a href="#"><img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"></a>
  <a href="#"><img src="https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS"></a>
</p>

## Introduction

The Automated README Generator is a tool designed to streamline the documentation process for software projects. By analyzing the codebase and leveraging user preferences, it automatically generates comprehensive and informative README files. This project targets developers seeking to automate documentation and quickly provide essential project information.

## Table of Contents

1.  [Key Features](#key-features)
2.  [Installation Guide](#installation-guide)
3.  [Usage](#usage)
4.  [Environment Variables](#environment-variables)
5.  [Project Structure](#project-structure)
6.  [Technologies Used](#technologies-used)
7.  [License](#license)

## Key Features

*   **Automated Code Analysis:** Parses Python and JavaScript code to extract key information, including functions, classes, and dependencies, leveraging `tree-sitter`.
*   **AI-Powered Summarization:** Employs the Gemini AI model to generate concise summaries of code chunks, enabling automated documentation.
*   **Customizable README Generation:** Allows users to define preferences (title, badges, sections) to tailor the README to their specific needs.
*   **GitHub Repository Cloning:** Clones repositories directly from GitHub using a provided URL.
*   **Real-time Preview:** Provides a live preview of the generated README with rendered markdown.
*   **Token Estimation:** Uses token estimation to ensure that chunks passed to the Gemini AI model does not exeed the API limits.
*   **State Management:** Manages the README generation workflow using a state graph, ensuring a smooth and consistent process.
*   **API Endpoint Detection:** Automatically detects API endpoints in Python code based on decorators like `@app.get` and `@app.post`.

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
    GEMINI_API_KEY=<your_gemini_api_key>
    # Add other necessary environment variables here
    ```

5.  **Run the FastAPI server:**

    ```bash
    cd Backend
    python main.py
    ```

6.  **Run the React frontend:**

    ```bash
    cd ../frontend
    npm start
    ```

## Usage

1.  Open the frontend application in your browser (usually at `http://localhost:3000`).
2.  Enter the URL of the GitHub repository you want to document.
3.  Add a project description to provide context for the generated README.
4.  Customize the README content using the preference settings.  You can select which sections to include (e.g., Installation, Usage, API Reference).
5.  Click the "Generate README" button.
6.  Preview the generated README in the "Preview" tab.
7.  Copy the markdown code or download the README file using the provided buttons.

## Environment Variables

The following environment variables are required for the backend application:

*   `GEMINI_API_KEY`: Your API key for the Gemini AI model. This is used for code summarization and README generation.

## Project Structure

```
├── Backend/
│   ├── main.py             # FastAPI application entry point
│   ├── chunker/
│   │   └── chunker.py       # Code chunking logic
│   │   └── token_estimator.py  # Estimates tokens in text
│   ├── summerize/
│   │   └── summerizer.py    # README summarization logic using AI
│   ├── agent/
│   │   └── agent.py         # Orchestrates the README generation process
│   ├── Parser/
│   │   ├── analyzer.py      # Analyzes the codebase (language, files, etc.)
│   │   ├── js_parser.py     # JavaScript code parser using tree-sitter
│   │   ├── python_parser.py # Python code parser
│   │   ├── code_walker.py   # Traverses the codebase directory structure
│   │   └── full/           # Contains sample code and parser setup
│   ├── api/
│   │   ├── model.py         # Data models (Pydantic)
│   │   └── router.py        # FastAPI API routes
│   │   └── utils/
│   │       └── github_utils.py # Utility functions for interacting with GitHub
├── frontend/
│   ├── src/
│   │   ├── App.js           # Main React application component
│   │   ├── index.js         # React entry point
│   │   ├── components/      # Reusable React components
│   │   │   ├── ReadmePage/ # Components specific to readme page
│   │   │   │   ├── markdownComp.js  # Displays the generated README in markdown
│   │   │   │   └── preferencesComp.js # UI for setting README generation preferences
│   │   │   ├── home/       # Components specific to home page
│   │   │   │   ├── Title.js       # Title component
│   │   │   │   └── LinkTextBox.js  # Input box for GitHub repo URL
│   │   ├── pages/           # React pages
│   │   │   ├── ReadmePage.js # Page to display and customize the generated README
│   │   │   └── HomePage.js   # Main landing page
│   │   ├── utils/           # Utilities
│   │   │   └── api/
│   │   │       └── ApiCaller.js  # Handles API calls to the backend
│   ├── tailwind.config.js # Tailwind CSS configuration
```

## Technologies Used

<p align="left">
  <a href="#"><img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI"></a>
  <a href="#"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React"></a>
  <a href="#"><img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"></a>
  <a href="#"><img src="https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS"></a>
</p>

*   **Backend:** FastAPI (Python)
*   **Frontend:** React (JavaScript)
*   **Code Parsing:** tree-sitter
*   **AI Summarization:** Google Gemini AI Model
*   **Token Estimation:** tiktoken

## License

This project is licensed under the MIT License.

<p align="left">
  <a href="#"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"></a>
</p>
