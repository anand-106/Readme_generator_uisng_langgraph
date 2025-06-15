# AI-Powered Ticket Triage System

[![FastAPI](https://img.shields.io/badge/FastAPI-005580?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-%234EA94B.svg?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![LangChain](https://img.shields.io/badge/LangChain-34A853?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![Auth0](https://img.shields.io/badge/Auth0-E22300?style=for-the-badge&logo=auth0&logoColor=white)](https://auth0.com/)
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://www.javascript.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Axios](https://img.shields.io/badge/Axios-5A29E4?style=for-the-badge&logo=axios&logoColor=white)](https://axios-http.com/)

## Table of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [File Structure](#file-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
- [Backend Details](#backend-details)
- [Frontend Details](#frontend-details)
- [Contribution](#contribution)
- [License](#license)

## Introduction

This project is a full-stack ticket triage and management system designed to streamline the process of handling user-submitted support requests.  It features a React-based frontend for ticket submission and display, and a Python backend powered by FastAPI and LangChain for automated ticket classification and routing. Auth0 is integrated for secure authentication and role-based access control.  The system leverages OpenAI's language models to intelligently classify tickets and route them to the appropriate development team (React, Java, Python, or SQL).

## Key Features

*   **AI-Powered Ticket Triage:** Automatically classifies and routes tickets to the appropriate team using LangChain and OpenAI's language models.
*   **Secure Authentication:** Utilizes Auth0 for user authentication and authorization, ensuring secure access to the application.
*   **Role-Based Access Control (RBAC):** Implements RBAC to restrict access to sensitive features and data based on user roles.
*   **RESTful API:** Provides a well-defined RESTful API built with FastAPI for seamless communication between the frontend and backend.
*   **Asynchronous Operations:** Leverages `async/await` for efficient handling of API requests and background tasks.
*   **Real-time Ticket Management:** Provides a user-friendly interface for submitting, viewing, and managing tickets.

## File Structure

```
.
├── backend/                    # Python Backend (FastAPI)
│   ├── auth.py                 # Authentication logic
│   ├── model.py                # Data models (e.g., MongoDB schema)
│   ├── route.py                # API routes and handlers
│   ├── schemas.py              # Pydantic schemas for data validation and serialization
│   ├── ticket_agent.py         # AI chatbot and ticket routing logic
│   └── ...
├── frontend/                   # React Frontend
│   ├── src/                    # Source code
│   │   ├── api.js              # API interaction functions
│   │   ├── App.js              # Main application component
│   │   ├── authWrapper.js      # Auth0 authentication wrapper
│   │   ├── Login.js            # Login component
│   │   ├── config.js             # Configuration settings for Auth0
│   │   ├── reportWebVitals.js   # Performance monitoring
│   │   ├── roleBasedRedirect.js # Role-based redirection logic
│   │   ├── roleRequirer.js     # Role-based access control component
│   │   ├── ticketDetails.js     # Ticket details component
│   │   ├── Tickets.js          # Ticket list component
│   │   ├── useApi.js            # Custom hook for making authenticated API calls
│   │   └── ...
│   ├── public/                 # Static assets
│   └── ...
├── .env                        # Environment variables (API keys, URIs, etc.)
├── README.md                   # This file
└── ...
```

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

*   Python 3.7+
*   Node.js and npm
*   MongoDB

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Install backend dependencies:**

    ```bash
    cd backend
    pip install -r requirements.txt
    cd ..
    ```

3.  **Install frontend dependencies:**

    ```bash
    cd frontend
    npm install
    cd ..
    ```

### Environment Variables

Create a `.env` file in the root directory of the project and populate it with the necessary environment variables.  Example:

```
# Backend
AUTH0_DOMAIN=<your_auth0_domain>
AUTH0_CLIENT_ID=<your_auth0_client_id>
AUTH0_CLIENT_SECRET=<your_auth0_client_secret>
AUTH0_AUDIENCE=<your_auth0_audience>
MONGODB_URI=<your_mongodb_uri>
OPENAI_API_KEY=<your_openai_api_key>

# Frontend
REACT_APP_AUTH0_DOMAIN=<your_auth0_domain>
REACT_APP_AUTH0_CLIENT_ID=<your_auth0_client_id>
REACT_APP_AUTH0_AUDIENCE=<your_auth0_audience>
```

**Note:** Replace the placeholder values with your actual credentials and configurations.

### Running the Application

1.  **Start the backend:**

    ```bash
    cd backend
    uvicorn main:app --reload
    cd ..
    ```

2.  **Start the frontend:**

    ```bash
    cd frontend
    npm start
    cd ..
    ```

The frontend will typically be accessible at `http://localhost:3000`, and the backend API at `http://localhost:8000`.

## Usage

1.  Access the application through your web browser.
2.  Log in using your Auth0 credentials.
3.  Submit a new ticket using the provided form.
4.  View existing tickets and their details.
5.  Admins can close tickets using the `TicketDetails` component.

## Backend Details

The backend is built using FastAPI and leverages several key modules:

*   **`auth.py`:** Handles authentication and authorization using Auth0. Includes functions for verifying JWT tokens and checking user roles.
*   **`ticket_agent.py`:** Contains the core logic for ticket triage.  The `run_chatbot` function orchestrates the process, classifying messages and routing tickets to appropriate agents (e.g., `python_agent`, `sql_agent`).
*   **`schemas.py`:** Defines Pydantic schemas for data validation and serialization.
*   **`route.py`:** Defines API endpoints for creating, retrieving, and managing tickets.

The backend uses OpenAI's `langchain` to power the AI-driven ticket classification and routing.

## Frontend Details

The frontend is built using React and utilizes the following key components:

*   **`App.js`:** Sets up the React Router and provides the main application structure.
*   **`AuthWrapper`:** Handles authentication using Auth0.
*   **`TicketInput`:** Provides a form for users to submit new tickets.
*   **`TicketList`:** Displays a list of tickets.
*   **`TicketDetails`:** Displays detailed information for a single ticket and allows admins to close tickets.
*   **`useApi.js`:** A custom hook that provides a function to make authenticated API calls.

The frontend interacts with the backend API to retrieve and manage ticket data.

## Contribution

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).