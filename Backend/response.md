# <p align="center">Ticket Triage and Management System</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI"></a>
  <a href="#"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=yellow" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/MongoDB-%234EA94B.svg?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB"></a>
  <a href="#"><img src="https://img.shields.io/badge/LangChain-000000?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain"></a>
  <a href="#"><img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React"></a>
  <a href="#"><img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS"></a>
  <a href="#"><img src="https://img.shields.io/badge/Auth0-EB5424?style=for-the-badge&logo=auth0&logoColor=white" alt="Auth0"></a>
</p>

## Introduction

This project is a full-stack ticket triage and management system designed to streamline the process of handling user-submitted issues. It leverages a React-based frontend, a Python/FastAPI backend, Auth0 for authentication, and Langchain for intelligent ticket classification and routing. The system aims to efficiently categorize and assign tickets to the appropriate development teams (React, Java, Python, and SQL).

## Table of Contents

1.  [Key Features](#key-features)
2.  [Installation Guide](#installation-guide)
3.  [Usage](#usage)
4.  [Environment Variables](#environment-variables)
5.  [License](#license)

## Key Features

*   **Ticket Submission:** Users can submit detailed tickets through a user-friendly React interface.
*   **Intelligent Triage:** Langchain is used to automatically classify and route tickets based on their content to specific development teams.
*   **Role-Based Access Control (RBAC):** Auth0 integration enables secure authentication and authorization, with role-based access to different functionalities.
*   **API Endpoints:** FastAPI provides robust API endpoints for creating, retrieving, and closing tickets.
*   **Real-time Ticket Updates:** The frontend dynamically updates to reflect the latest ticket status.
*   **Team-Specific Agents:** Specialized agents (e.g., `react_agent`, `java_agent`, `python_agent`, `sql_agent`) triage issues and provide team-specific documentation.
*   **Secure API Calls:** Custom `useApi` hook ensures authenticated API requests from the frontend to the backend.

## Installation Guide

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Install backend dependencies:**

    ```bash
    cd backend
    pip install -r requirements.txt
    ```

3.  **Install frontend dependencies:**

    ```bash
    cd ../frontend
    npm install
    ```

4.  **Configure environment variables:**

    *   Create `.env` files in both the `backend` and `frontend` directories.
    *   Populate the `.env` files with the necessary environment variables (see [Environment Variables](#environment-variables) section).

5.  **Run the FastAPI backend:**

    ```bash
    cd backend
    uvicorn main:app --reload
    ```

6.  **Run the React frontend:**

    ```bash
    cd ../frontend
    npm start
    ```

## Usage

1.  **Access the application:** Open your browser and navigate to the frontend URL (usually `http://localhost:3000`).

2.  **Authentication:** Log in using your Auth0 credentials.  New users may need to register through Auth0.

3.  **Ticket Submission:** Submit new tickets via the provided form.  The system will automatically classify and route the ticket.

4.  **Ticket Management:** View, filter, and close tickets based on your role.  Administrators have the ability to close tickets.

5.  **API Interaction:** Developers can interact with the backend API endpoints for more advanced ticket management functionalities.

## Environment Variables

**Backend (`backend/.env`):**

*   `DATABASE_URL`: The connection string for the MongoDB database (e.g., `mongodb://user:password@host:port/database`).
*   `AUTH0_DOMAIN`: Your Auth0 domain (e.g., `your-domain.auth0.com`).
*   `AUTH0_CLIENT_ID`: Your Auth0 client ID.
*   `AUTH0_CLIENT_SECRET`: Your Auth0 client secret.
*   `AUTH0_AUDIENCE`: Your Auth0 API audience.
*   `ALGORITHM`: The algorithm used for JWT encoding and decoding (e.g., `RS256`).

**Frontend (`frontend/.env`):**

*   `REACT_APP_AUTH0_DOMAIN`: Your Auth0 domain.
*   `REACT_APP_AUTH0_CLIENT_ID`: Your Auth0 client ID.
*   `REACT_APP_AUTH0_AUDIENCE`: Your Auth0 API audience.
*   `REACT_APP_BACKEND_URL`: The URL of the FastAPI backend (e.g., `http://localhost:8000`).

## License

<p align="left">
  <a href="#"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
</p>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.