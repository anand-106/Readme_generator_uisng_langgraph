```markdown
# Ticket Triage and Management System

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005580?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Auth0](https://img.shields.io/badge/Auth0-E34D26?style=for-the-badge&logo=auth0&logoColor=white)](https://auth0.com/)
![LangChain](https://img.shields.io/badge/LangChain-34A853?style=for-the-badge&logo=langchain&logoColor=white)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://www.javascript.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)

## Table of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [Contribution](#contribution)
- [Support](#support)

## Introduction

This project is a full-stack ticket triage and management system designed to streamline the process of handling and resolving technical support requests. It features a React-based frontend for user interaction and a Python backend built with FastAPI for API services. Leveraging LangChain and Large Language Models (LLMs), the system intelligently classifies, routes, and summarizes tickets for efficient handling by specialized teams. Authentication and authorization are managed using Auth0, ensuring secure access and role-based control.

## Key Features

-   **Automated Ticket Triage:** LLMs classify incoming tickets (React, Java, Python, SQL).
-   **Intelligent Routing:** Tickets are automatically routed to the appropriate team based on classification.
-   **Summarization & Analysis:** LLMs provide summaries and technical analysis of tickets.
-   **Role-Based Access Control (RBAC):** Secure access based on user roles managed by Auth0.
-   **React Frontend:** A user-friendly interface for submitting and managing tickets.
-   **FastAPI Backend:** Robust and scalable API for data management and processing.
-   **Asynchronous Operations:**  Efficient handling of API calls and background tasks.
-   **MongoDB Integration:** Persistent storage for ticket data.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Backend Setup (Python):**

    *   Navigate to the backend directory: `cd backend`
    *   Create a virtual environment: `python3 -m venv venv`
    *   Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
    *   Install dependencies: `pip install -r requirements.txt`

3.  **Frontend Setup (JavaScript):**

    *   Navigate to the frontend directory: `cd ../frontend`
    *   Install dependencies: `npm install` or `yarn install`

## Usage

1.  **Configure Environment Variables:**

    *   Create `.env` files in both the `backend` and `frontend` directories.
    *   Populate the `.env` files with the necessary environment variables (see [Environment Variables](#environment-variables) section for details).

2.  **Run the Backend:**

    *   Navigate to the `backend` directory.
    *   Ensure the virtual environment is activated.
    *   Run the FastAPI server: `uvicorn main:app --reload`

3.  **Run the Frontend:**

    *   Navigate to the `frontend` directory.
    *   Run the React development server: `npm start` or `yarn start`

4.  **Access the Application:**

    *   Open your web browser and navigate to the address where the React frontend is running (usually `http://localhost:3000`).

## File Structure

```
.
├── backend/               # FastAPI backend
│   ├── main.py            # Main application entry point
│   ├── route.py           # API routes and endpoints
│   ├── model.py           # Pydantic data models
│   ├── schemas.py         # Data serialization
│   ├── auth.py            # Authentication and authorization logic
│   ├── ticket_agent.py    # LLM-powered ticket routing and analysis
│   ├── requirements.txt   # Python dependencies
│   └── .env               # Backend environment variables
│
├── frontend/              # React frontend
│   ├── src/               # Source code
│   │   ├── App.js         # Main application component
│   │   ├── components/    # React components
│   │   │   ├── Header.js
│   │   │   ├── TicketInput.js
│   │   │   ├── TicketList.js
│   │   │   ├── TicketDetails.js
│   │   │   ├── Login.js
│   │   │   ├── AuthWrapper.js
│   │   │   ├── RoleRedirect.js
│   │   │   └── RoleRequirer.js
│   │   ├── hooks/         # Custom hooks
│   │   │   └── useApi.js
│   │   ├── api.js           # API calls
│   │   ├── auth/          # Auth0 config
│   │   │   └── config.js
│   │   ├── index.js       # React entry point
│   │   └── reportWebVitals.js # Web vitals reporting
│   ├── public/            # Static assets
│   ├── package.json       # Node.js dependencies
│   ├── .env               # Frontend environment variables
│   └── ...
├── .gitignore           # Git ignore file
├── README.md            # This file
└── ...
```

## API Endpoints

The backend provides the following API endpoints:

*   `POST /tickets`: Create a new ticket.
*   `GET /tickets/{ticket_no}`: Retrieve a specific ticket by its ticket number.
*   `GET /tickets`: Retrieve all tickets.
*   `GET /my-tickets`: Retrieve tickets assigned to the current user.
*   `PATCH /tickets/{ticket_no}/close`: Close a ticket.

Authentication is required for all endpoints except possibly a login/registration endpoint.  Role-based access control is enforced on specific endpoints.

## Environment Variables

The following environment variables need to be set in both the `backend/.env` and `frontend/.env` files:

**Backend (.env):**

*   `MONGODB_URI`: The connection string for the MongoDB database.
*   `AUTH0_DOMAIN`: The Auth0 domain.
*   `AUTH0_CLIENT_ID`: The Auth0 client ID.
*   `AUTH0_CLIENT_SECRET`: The Auth0 client secret (for backend use only).
*   `AUTH0_AUDIENCE`: The Auth0 API audience.
*   `AUTH0_NAMESPACE`: The namespace for custom claims (roles) in the JWT.
*   `OPENAI_API_KEY`: The API Key for OpenAI

**Frontend (.env):**

*   `REACT_APP_AUTH0_DOMAIN`: The Auth0 domain.
*   `REACT_APP_AUTH0_CLIENT_ID`: The Auth0 client ID.
*   `REACT_APP_AUTH0_AUDIENCE`: The Auth0 API audience.
*   `REACT_APP_AUTH0_NAMESPACE`: The namespace for custom claims (roles) in the JWT.
*   `REACT_APP_API_URL`: The URL of the backend API.

*Note:  Prefix React environment variables with `REACT_APP_`.*

## Contribution

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear and descriptive commit messages.
4.  Submit a pull request.

## Support

For any questions, issues, or feature requests, please open an issue on GitHub.
```