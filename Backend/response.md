# Support Ticket Management Portal

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev/)
[![Auth0](https://img.shields.io/badge/Auth0-E34D8F?style=for-the-badge&logo=auth0&logoColor=white)](https://auth0.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![LangChain](https://img.shields.io/badge/LangChain-34A853?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-e44d26?style=for-the-badge&logo=python&logoColor=white)](https://pydantic.dev/)

## Table of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [File Structure](#file-structure)
- [Installation Guide](#installation-guide)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [Contribution Guide](#contribution-guide)
- [Support & Contact](#support--contact)

## Introduction

This project is a full-stack support ticket management portal designed to streamline the process of submitting, triaging, and resolving user issues. Built with a modern technology stack including React, FastAPI, MongoDB, Auth0, and LangChain, it offers a robust and scalable solution for managing support workflows.  The system leverages Language Models (LLMs) for intelligent ticket routing and analysis, improving efficiency and accuracy.

## Key Features

*   **Authentication and Authorization:** Secure user authentication and role-based access control (RBAC) powered by Auth0.
*   **Ticket Submission:**  Users can submit support tickets via a user-friendly interface.
*   **Automated Ticket Classification & Routing:** Utilizes LangChain and LLMs to automatically classify and route tickets to the appropriate team (React, Java, Python, SQL) based on ticket content.
*   **Intelligent Ticket Analysis:** LLMs generate summaries, technical analysis, priority assessments, and suggested approaches for each ticket.
*   **Role-Based Access Control:** Different user roles (e.g., admin, developers, users) have varying permissions, controlling access to features and data.
*   **Ticket Management:**  Administrators and developers can view, update, and close tickets.
*   **API-Driven Architecture:**  A RESTful API built with FastAPI provides a clear and consistent interface for interacting with the backend.
*   **Frontend (React):** A responsive and intuitive user interface built with React and Tailwind CSS.

## File Structure

```
├── frontend/
│   ├── src/
│   │   ├── App.js                 # Main application component
│   │   ├── Login.js               # Login component using Auth0
│   │   ├── roleRequirer.js        # Role-based access control component
│   │   ├── roleBasedRedirect.js   # Role-based redirection component
│   │   ├── authWrapper.js         # Authentication API wrapper
│   │   ├── useApi.js              # Custom hook for API calls
│   │   ├── ticketDetails.js       # Component for viewing/closing tickets
│   │   ├── reportWebVitals.js     # Performance monitoring
│   │   ├── config.js              # Auth0 configuration
│   │   ├── api.js                 # API function definitions
│   │   └── ...
│   ├── public/
│   │   └── ...
│   ├── package.json
│   └── ...
├── backend/
│   ├── main.py                # FastAPI application entry point
│   ├── route.py               # API endpoint definitions
│   ├── model.py               # Pydantic data models
│   ├── auth.py                # Authentication and authorization logic
│   ├── schemas.py             # Data serialization schemas
│   ├── ticket_agent.py        # Ticket classification and routing logic (LLM)
│   └── ...
├── .env                     # Environment variables (Auth0 credentials, DB URI, etc.)
├── README.md
└── ...
```

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
    cd ..
    ```

3.  **Install frontend dependencies:**

    ```bash
    cd frontend
    npm install
    cd ..
    ```

4.  **Create and configure `.env` file:**

    Create a `.env` file in the root directory with the necessary environment variables (see [Environment Variables](#environment-variables)).  Example:

    ```
    AUTH0_DOMAIN=your_auth0_domain
    AUTH0_CLIENT_ID=your_auth0_client_id
    AUTH0_CLIENT_SECRET=your_auth0_client_secret
    AUTH0_AUDIENCE=your_auth0_audience
    DATABASE_URI=mongodb://user:password@host:port/database
    ```

## Usage

1.  **Start the backend server:**

    ```bash
    cd backend
    uvicorn main:app --reload
    cd ..
    ```

2.  **Start the frontend development server:**

    ```bash
    cd frontend
    npm start
    cd ..
    ```

3.  **Access the application:**

    Open your web browser and navigate to the address where the frontend server is running (usually `http://localhost:3000`).

## API Endpoints

The backend API provides the following endpoints:

*   `GET /tickets`: Retrieves all tickets (admin/developer only).
*   `GET /tickets/{ticket_number}`: Retrieves a specific ticket by ticket number.
*   `POST /tickets`: Creates a new ticket.
*   `PATCH /tickets/{ticket_number}`: Closes a ticket.

## Environment Variables

The following environment variables are required for the application to function correctly:

*   **Auth0 Configuration:**
    *   `AUTH0_DOMAIN`: Your Auth0 domain.
    *   `AUTH0_CLIENT_ID`: Your Auth0 client ID.
    *   `AUTH0_CLIENT_SECRET`: Your Auth0 client secret.
    *   `AUTH0_AUDIENCE`: Your Auth0 API audience.
*   **Database Configuration:**
    *   `DATABASE_URI`:  The MongoDB connection URI.

## Contribution Guide

Contributions are welcome! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Write clear and concise commit messages.
4.  Submit a pull request with a detailed description of your changes.

## Support & Contact

If you encounter any issues or have questions, please open an issue on the GitHub repository.