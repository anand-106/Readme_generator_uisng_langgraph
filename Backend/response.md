# <p align="center">Ticket Submission and Management Portal</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python&logoColor=white" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/FastAPI-0.70.0-blue?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"></a>
  <a href="#"><img src="https://img.shields.io/badge/MongoDB-4.4-blue?style=flat-square&logo=mongodb&logoColor=white" alt="MongoDB"></a>
  <a href="#"><img src="https://img.shields.io/badge/LangChain-blue?style=flat-square" alt="LangChain"></a>
  <a href="#"><img src="https://img.shields.io/badge/React-17.0.2-blue?style=flat-square&logo=react&logoColor=white" alt="React"></a>
  <a href="#"><img src="https://img.shields.io/badge/Tailwind_CSS-blue?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind CSS"></a>
  <a href="#"><img src="https://img.shields.io/badge/Auth0-blue?style=flat-square&logo=auth0&logoColor=white" alt="Auth0"></a>
</p>

## Introduction

This project is a full-stack ticket submission and management portal designed to streamline support requests. It allows users to submit tickets, and administrators can view, manage, and triage them efficiently. The application utilizes a React frontend and a FastAPI backend, leveraging Auth0 for authentication and role-based access control.

## Table of Contents

1.  [Key Features](#key-features)
2.  [Installation Guide](#installation-guide)
3.  [Usage](#usage)
4.  [Environment Variables](#environment-variables)
5.  [Project Structure](#project-structure)
6.  [Technologies Used](#technologies-used)
7.  [Contribution Guide](#contribution-guide)
8.  [Support & Contact](#support--contact)
9.  [License](#license)

## Key Features

*   **Ticket Submission:** Users can easily submit support tickets with detailed descriptions.
*   **Ticket Management:** Administrators can view, update, and close tickets.
*   **Role-Based Access Control (RBAC):** Different user roles (e.g., admin, user, developer) have varying levels of access.
*   **Intelligent Ticket Triage:** Uses Langchain-powered agents to classify and route tickets to the appropriate development team (React, Java, Python, SQL).
*   **Authentication:** Secure authentication using Auth0.
*   **Real-time Updates:** The frontend dynamically updates upon ticket submission or status changes.
*   **API Endpoints:** RESTful API built with FastAPI for managing tickets.

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

    *   Create `.env` files in both the `Backend` and `frontend` directories.
    *   Populate the `.env` files with the necessary variables (see [Environment Variables](#environment-variables) section).

5.  **Run the FastAPI server:**

    ```bash
    cd Backend
    uvicorn main:app --reload
    ```

6.  **Run the React frontend:**

    ```bash
    cd ../frontend
    npm start
    ```

## Usage

1.  **Access the application:** Open your web browser and navigate to the address where the React frontend is running (usually `http://localhost:3000`).

2.  **Authentication:** Log in using your Auth0 credentials.

3.  **Ticket Submission:** Submit new tickets through the provided form.

4.  **Ticket Management (Admin):** Administrators can access a dedicated dashboard to view and manage all tickets.

5.  **API Endpoints:** The backend provides the following API endpoints:

    *   `GET /tickets`: Retrieves all tickets (admin/developers only).
    *   `POST /tickets`: Creates a new ticket (user, admin, developers).
    *   `GET /tickets/{ticketNo}`: Retrieves a specific ticket.
    *   `PATCH /tickets/{ticketNo}`: Closes a specific ticket (admin/developers only).
    *   `GET /my-tickets`: Retrieves tickets belonging to the logged-in user.

## Environment Variables

**Backend (`Backend/.env`):**

*   `DATABASE_URL`: MongoDB connection string.
*   `AUTH0_DOMAIN`: Auth0 domain.
*   `AUTH0_CLIENT_ID`: Auth0 client ID.
*   `AUTH0_CLIENT_SECRET`: Auth0 client secret.
*   `AUTH0_API_IDENTIFIER`: Auth0 API identifier.
*   `AUTH0_MANAGEMENT_API_CLIENT_ID`: Auth0 Management API client ID
*   `AUTH0_MANAGEMENT_API_CLIENT_SECRET`: Auth0 Management API client secret
*   `OPENAI_API_KEY`: OpenAI API Key

**Frontend (`frontend/.env`):**

*   `REACT_APP_AUTH0_DOMAIN`: Auth0 domain.
*   `REACT_APP_AUTH0_CLIENT_ID`: Auth0 client ID.
*   `REACT_APP_AUTH0_AUDIENCE`: Auth0 API identifier.
*    `REACT_APP_API_URL`: Backend API URL

## Project Structure

```
├── Backend/
│   ├── main.py               # Main FastAPI application file
│   ├── ticket_agent.py       # Langchain agents for ticket triage
│   ├── Auth/
│   │   └── auth.py           # Authentication logic (token verification)
│   ├── Database/
│   │   ├── config/
│   │   │   └── database.py   # MongoDB connection configuration
│   │   ├── models/
│   │   │   └── model.py      # Pydantic data models (Ticket, Message, CloseTicket)
│   │   ├── routes/
│   │   │   └── route.py      # API endpoint definitions
│   │   └── schema/
│   │       └── schemas.py    # Data schemas
├── frontend/
│   ├── postcss.config.js    # PostCSS configuration
│   ├── tailwind.config.js   # Tailwind CSS configuration
│   ├── src/
│   │   ├── api.js           # API call to get tickets
│   │   ├── App.js           # Main React application component
│   │   ├── index.js         # Entry point for React application
│   │   ├── reportWebVitals.js# Reports web vitals for performance monitoring
│   │   ├── setupTests.js    # Setup for testing environment
│   │   ├── ticketDetails.js # Component for displaying/managing ticket details
│   │   ├── Tickets.js       # Component for displaying list of tickets
│   │   ├── Auth/
│   │   │   ├── authWrapper.js  # Higher-order component for authentication
│   │   │   ├── config.js       # Auth0 configuration settings
│   │   │   ├── Login.js        # Login component
│   │   │   ├── roleBasedRedirect.js # Redirects users based on roles
│   │   │   ├── roleRequirer.js # Component for role-based authorization
│   │   │   └── API/
│   │   │       └── useApi.js   # Custom hook for making API calls
```

## Technologies Used

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python&logoColor=white" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/FastAPI-0.70.0-blue?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"></a>
  <a href="#"><img src="https://img.shields.io/badge/MongoDB-4.4-blue?style=flat-square&logo=mongodb&logoColor=white" alt="MongoDB"></a>
  <a href="#"><img src="https://img.shields.io/badge/LangChain-blue?style=flat-square" alt="LangChain"></a>
  <a href="#"><img src="https://img.shields.io/badge/React-17.0.2-blue?style=flat-square&logo=react&logoColor=white" alt="React"></a>
  <a href="#"><img src="https://img.shields.io/badge/Tailwind_CSS-blue?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind CSS"></a>
  <a href="#"><img src="https://img.shields.io/badge/Auth0-blue?style=flat-square&logo=auth0&logoColor=white" alt="Auth0"></a>
</p>

*   **Backend:** Python, FastAPI, Pydantic, MongoDB, Langchain
*   **Frontend:** React, Auth0, Axios, Tailwind CSS
*   **Authentication/Authorization:** Auth0

## Contribution Guide

We welcome contributions to this project! To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Submit a pull request.

Please follow the existing code style and conventions.

## Support & Contact

For questions or support, please open an issue on the GitHub repository.

## License

[MIT License](LICENSE)