# Ticket Management System

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Auth0](https://img.shields.io/badge/Auth0-E34D26?style=for-the-badge&logo=auth0&logoColor=white)](https://auth0.com/)
[![LangChain](https://img.shields.io/badge/LangChain-34A853?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-e44d26?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)

## Table of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [File Structure](#file-structure)
- [Contribution](#contribution)
- [Support & Contact](#support--contact)

## Introduction

The Ticket Management System is a full-stack application designed to streamline the process of submitting, triaging, and resolving support tickets. It features a React-based frontend and a Python backend built with FastAPI. The system incorporates role-based access control via Auth0 for secure authentication and authorization.  Leveraging LangChain, tickets are automatically classified and routed to appropriate support teams (React, Java, Python, SQL) based on the ticket content.

## Key Features

*   **Automated Ticket Triage:** Utilizes LangChain and LLM agents to classify incoming tickets and route them to the relevant team.
*   **Role-Based Access Control:** Securely manages user access using Auth0, with different roles for users and administrators.
*   **RESTful API:** Provides a comprehensive API for managing tickets, users, and roles.
*   **Real-time Updates:** Provides ticket lists and details through the React front end.
*   **Modern Tech Stack:** Built with React, FastAPI, MongoDB, and other modern technologies for performance and scalability.
*   **Ticket Submission and Display:** Enables users to submit tickets via a user-friendly interface, and displays ticket details including status and team assignment.
*   **Ticket Closing:** Authorized users (admins) can close tickets.
*   **Secure API calls:** Uses the `useApi` custom hook, providing API calls with access token.

## Installation

Follow these steps to set up the project locally:

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Backend Setup (Python):**

    ```bash
    cd backend
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Frontend Setup (React):**

    ```bash
    cd frontend
    npm install
    ```

4.  **Environment Variables:**

    Create `.env` files in both the `backend` and `frontend` directories, and populate them with the necessary environment variables. See the [Environment Variables](#environment-variables) section for details.

5.  **Run the Backend:**

    ```bash
    cd backend
    uvicorn main:app --reload
    ```

6.  **Run the Frontend:**

    ```bash
    cd frontend
    npm start
    ```

## Usage

1.  **Access the application:** Open your web browser and navigate to the frontend URL (typically `http://localhost:3000`).

2.  **Authentication:** Log in using your Auth0 credentials.

3.  **Submit a ticket:** Use the ticket submission form to create a new ticket.  The ticket will be automatically triaged and routed to the appropriate team.

4.  **View tickets:**  Browse the list of tickets or view details for a specific ticket.

5.  **Admin actions:**  Administrators can close tickets and manage user roles through the appropriate interfaces (if implemented).

## API Endpoints

The backend provides the following API endpoints:

*   `POST /tickets/`: Create a new ticket.
*   `GET /tickets/`: Retrieve all tickets.
*   `GET /tickets/{ticket_no}`: Retrieve a specific ticket by ticket number.
*   `PUT /tickets/{ticket_no}`: Close a ticket.
*   `GET /mytickets`: Retrieves the tickets associated with the current user

Authentication is required for all endpoints.  Include the Auth0 access token in the `Authorization` header as `Bearer <access_token>`.  Role-based access control is enforced for certain endpoints.

## Environment Variables

The following environment variables are required:

**Backend (.env):**

*   `MONGODB_URI`: The MongoDB connection string.
*   `AUTH0_DOMAIN`: Your Auth0 domain.
*   `AUTH0_CLIENT_ID`: Your Auth0 client ID.
*   `AUTH0_CLIENT_SECRET`: Your Auth0 client secret.
*   `AUTH0_API_IDENTIFIER`: Your Auth0 API identifier.
*   `OPENAI_API_KEY`: Your OpenAI API key.

**Frontend (.env):**

*   `REACT_APP_AUTH0_DOMAIN`: Your Auth0 domain.
*   `REACT_APP_AUTH0_CLIENT_ID`: Your Auth0 client ID.
*   `REACT_APP_AUTH0_AUDIENCE`: Your Auth0 API identifier.
*   `REACT_APP_BACKEND_URL`: The URL of your backend API.

## File Structure

```
├── backend/
│   ├── main.py          # Main FastAPI application file
│   ├── route.py         # Defines FastAPI routes for managing tickets
│   ├── model.py         # Defines Pydantic models for data
│   ├── schemas.py       # Defines data serialization functions
│   ├── auth.py          # Implements authentication and authorization functions
│   ├── ticket_agent.py  # Contains functions for classifying messages and routing them to agents
│   └── requirements.txt # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── App.js            # Main React application component
│   │   ├── Login.js          # React component for the login page
│   │   ├── TicketDetails.js  # React component for fetching and displaying ticket details
│   │   ├── Tickets.js        # React component for displaying a list of tickets.
│   │   ├── authWrapper.js    # Function for calling authenticated APIs
│   │   ├── useApi.js         # Custom hook for making API calls with authentication
│   │   ├── roleRequirer.js   # React component for requiring specific roles for access control
│   │   ├── roleBasedRedirect.js # React component for redirecting users based on their roles
│   │   ├── config.js         # Manages Auth0 configuration
│   │   └── reportWebVitals.js # Reports web vitals for performance monitoring
│   ├── package.json       # Frontend dependencies
│   └── public/
│       └── index.html       # Main HTML file
├── .env                # Environment variables (should NOT be committed)
└── README.md           # This file
```

## Contribution

We welcome contributions to the Ticket Management System! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and write tests.
4.  Submit a pull request with a clear description of your changes.

## Support & Contact

If you encounter any issues or have questions, please contact us by opening an issue on GitHub.