# Ticketing System with AI-Powered Triage and Role-Based Access Control

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005580?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Auth0](https://img.shields.io/badge/Auth0-EB5424?style=for-the-badge&logo=auth0&logoColor=white)](https://auth0.com/)
[![LangChain](https://img.shields.io/badge/LangChain-34A853?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://www.javascript.com/)

## Table of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [Contribution](#contribution)
- [Support](#support)

## Introduction

This project is a comprehensive ticketing system that combines a React-based frontend with a FastAPI backend, featuring AI-powered ticket triage and role-based access control. It allows users to submit, track, and manage support tickets, while leveraging LangChain for automated ticket classification and routing.  Auth0 handles authentication and authorization, providing secure access based on user roles.

## Key Features

*   **Role-Based Access Control:** Different user roles (admin, developer, user) have varying levels of access to the system's functionalities, enforced through Auth0 and JWT validation.
*   **AI-Powered Ticket Triage:** Utilizes LangChain and LLMs to automatically classify incoming tickets and route them to appropriate specialized agents.
*   **Secure Authentication:** Implements secure authentication using Auth0, ensuring only authenticated users can access protected resources.
*   **Automated Ticket Classification:** Uses LLMs to categorize and triage incoming support requests, streamlining the support process.
*   **Real-time Ticket Management:** Allows users to submit tickets and view their progress.
*   **Detailed Ticket View:** Display detailed information for each ticket, and enable authorized users to close tickets.

## File Structure

```
├── frontend/                 # React Frontend
│   ├── src/
│   │   ├── components/        # Reusable React components
│   │   │   ├── Login.js       # Login Page
│   │   │   ├── Header.js      # Header Component
│   │   │   ├── TicketDetails.js# Detailed Ticket View
│   │   │   ├── Tickets.js     # Ticket List Component
│   │   ├── AuthWrapper.js     # Authentication Wrapper Component
│   │   ├── useApi.js          # Custom hook for API calls
│   │   ├── roleRequirer.js    # Component for role-based access control
│   │   ├── roleBasedRedirect.js # Redirects users based on roles after login
│   │   ├── config.js          # Auth0 configuration settings
│   │   ├── App.js             # Main Application Component
│   │   ├── index.js           # Entry point for the React application
│   ├── public/
│   ├── package.json
│   └── ...
├── backend/                 # FastAPI Backend
│   ├── main.py              # Entry point for the FastAPI application
│   ├── route.py             # API routes for managing tickets
│   ├── model.py             # Pydantic data models (Ticket, Message, CloseTicket)
│   ├── schemas.py           # Data serialization functions for tickets
│   ├── auth.py              # Role-based authorization using JWT tokens
│   ├── ticket_agent.py      # Functions for classifying and routing tickets using LLMs
│   ├── .env                 # Environment variables
│   └── ...
├── README.md               # This README file
```

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Install frontend dependencies:**

    ```bash
    cd frontend
    npm install
    ```

3.  **Install backend dependencies:**

    ```bash
    cd backend
    pip install -r requirements.txt
    ```

## Usage

1.  **Configure environment variables:**

    *   Create a `.env` file in the `backend` directory.
    *   Add the necessary environment variables (see [Environment Variables](#environment-variables) section).

2.  **Run the backend server:**

    ```bash
    cd backend
    python main.py
    ```

3.  **Run the frontend application:**

    ```bash
    cd frontend
    npm start
    ```

4.  **Access the application:**

    *   Open your web browser and navigate to the address where the frontend is running (usually `http://localhost:3000`).

## API Endpoints

The backend API provides the following endpoints:

*   `GET /tickets`: Retrieves a list of all tickets.
*   `GET /tickets/{ticket_id}`: Retrieves a specific ticket by ID.
*   `POST /tickets`: Creates a new ticket.
*   `PUT /tickets/{ticket_id}`: Updates an existing ticket.
*   `PATCH /tickets/{ticket_id}/close`: Closes a specific ticket.

Refer to the `route.py` file for complete details on API endpoints, request parameters, and response formats.

## Environment Variables

The following environment variables need to be configured in the `.env` file within the `backend` directory:

*   `AUTH0_DOMAIN`: Your Auth0 domain.
*   `AUTH0_CLIENT_ID`: Your Auth0 client ID.
*   `AUTH0_CLIENT_SECRET`: Your Auth0 client secret.
*   `AUTH0_AUDIENCE`: Your Auth0 API audience.
*   `MONGODB_URI`: The connection string for your MongoDB database.
*   `DATABASE_NAME`: The name of the MongoDB database to use.
*   `OPENAI_API_KEY`: The API key for OpenAI (used by LangChain).

## Contribution

We welcome contributions to this project! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive commit messages.
4.  Push your changes to your forked repository.
5.  Submit a pull request to the main repository.

## Support

For any questions, issues, or feedback, please open an issue in the GitHub repository.