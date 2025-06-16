# <p align="center">AI-Powered Ticket Management System</p>

<p align="center">
  <a href="https://shields.io/badge/Python-3.9-blue"><img src="https://img.shields.io/badge/Python-3.9-blue" alt="Python Version"></a>
  <a href="https://shields.io/badge/FastAPI-latest-green"><img src="https://img.shields.io/badge/FastAPI-latest-green" alt="FastAPI Version"></a>
  <a href="https://shields.io/badge/MongoDB-latest-orange"><img src="https://img.shields.io/badge/MongoDB-latest-orange" alt="MongoDB Version"></a>
  <a href="https://shields.io/badge/LangChain-latest-purple"><img src="https://img.shields.io/badge/LangChain-latest-purple" alt="LangChain Version"></a>
  <a href="https://shields.io/badge/React-latest-blueviolet"><img src="https://img.shields.io/badge/React-latest-blueviolet" alt="React Version"></a>
  <a href="https://shields.io/badge/Tailwind_CSS-latest-lightblue"><img src="https://img.shields.io/badge/Tailwind_CSS-latest-lightblue" alt="Tailwind CSS Version"></a>
  <a href="https://shields.io/badge/Auth0-latest-red"><img src="https://img.shields.io/badge/Auth0-latest-red" alt="Auth0 Version"></a>
</p>

## Introduction

This project is a comprehensive ticket management system designed to streamline the process of submitting, triaging, and resolving technical support tickets. It leverages AI-powered agents for automated ticket classification and routing, enhancing efficiency for development teams. Target users include developers, support staff, and end-users.

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

*   **AI-Powered Ticket Triage:** Automatically classifies and routes tickets using Langchain and OpenAI's LLM, saving time and resources.
*   **Role-Based Access Control (RBAC):** Securely manages access with Auth0 integration, ensuring only authorized users can view or modify tickets.
*   **Real-time Ticket Updates:** Frontend updates dynamically via API calls, providing a seamless user experience.
*   **Comprehensive Ticket Details:** Displays all relevant information, including AI-generated summaries, technical analysis, and priority scores.
*   **Multi-Team Support:** Routes tickets to specialized agents (React, Java, Python, SQL) for targeted expertise.
*   **Secure Authentication:** Utilizes Auth0 for secure user authentication and authorization.

## Installation Guide

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_name>
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

    *   Create a `.env` file in both the `Backend` and `frontend` directories.
    *   Populate the `.env` files with the necessary credentials (see [Environment Variables](#environment-variables) section).

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

*   **Frontend:** Access the application in your browser (usually at `http://localhost:3000`). Authenticate using Auth0, and you can begin submitting, viewing, and managing tickets.
*   **Backend:** The FastAPI server exposes API endpoints for ticket management. The frontend interacts with these endpoints to perform operations.
    *   `POST /add-ticket`: Creates a new ticket.
    *   `GET /tickets`: Retrieves all tickets.
    *   `GET /tickets/{ticket_id}`: Retrieves a specific ticket.
    *   `PATCH /tickets/{ticket_id}/close`: Closes a ticket.

## Environment Variables

The following environment variables are required:

**Backend (.env):**

*   `MONGODB_URI`: The connection string for your MongoDB database.
*   `AUTH0_DOMAIN`: Your Auth0 domain.
*   `AUTH0_CLIENT_ID`: Your Auth0 client ID.
*   `AUTH0_CLIENT_SECRET`: Your Auth0 client secret.
*   `AUTH0_AUDIENCE`: Your Auth0 API audience.
*   `OPENAI_API_KEY`: Your OpenAI API key.

**Frontend (.env):**

*   `REACT_APP_AUTH0_DOMAIN`: Your Auth0 domain.
*   `REACT_APP_AUTH0_CLIENT_ID`: Your Auth0 client ID.
*   `REACT_APP_AUTH0_AUDIENCE`: Your Auth0 API audience.
*   `REACT_APP_API_URL`: URL of the backend API (e.g., `http://localhost:8001`).

## Project Structure

```
├── Backend/
│   ├── main.py          # FastAPI application entry point
│   ├── ticket_agent.py  # AI agent for ticket classification and routing
│   ├── Auth/
│   │   └── auth.py      # Authentication and authorization logic
│   ├── Database/
│   │   ├── config/
│   │   │   └── database.py # MongoDB configuration
│   │   ├── models/
│   │   │   └── model.py    # Pydantic models for data validation
│   │   ├── routes/
│   │   │   └── route.py    # FastAPI routes for ticket management
│   │   └── schema/
│   │       └── schemas.py  # Data serialization schemas
├── frontend/
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   ├── src/
│   │   ├── api.js            # API interaction functions
│   │   ├── App.js            # Main application component
│   │   ├── index.js          # React entry point
│   │   ├── reportWebVitals.js
│   │   ├── setupTests.js
│   │   ├── ticketDetails.js  # Component for displaying ticket details
│   │   ├── Tickets.js        # Component for listing tickets
│   │   ├── Auth/
│   │   │   ├── authWrapper.js # Authentication wrapper
│   │   │   ├── config.js      # Auth0 configuration
│   │   │   ├── Login.js       # Login page component
│   │   │   ├── roleBasedRedirect.js # Role-based redirection component
│   │   │   ├── roleRequirer.js  # Role-based access control component
│   │   │   └── API/
│   │   │       └── useApi.js  # Custom hook for API calls
```

## Technologies Used

<p align="center">
  <a href="https://shields.io/badge/Python-3.9-blue"><img src="https://img.shields.io/badge/Python-3.9-blue" alt="Python Version"></a>
  <a href="https://shields.io/badge/FastAPI-latest-green"><img src="https://img.shields.io/badge/FastAPI-latest-green" alt="FastAPI Version"></a>
  <a href="https://shields.io/badge/MongoDB-latest-orange"><img src="https://img.shields.io/badge/MongoDB-latest-orange" alt="MongoDB Version"></a>
  <a href="https://shields.io/badge/LangChain-latest-purple"><img src="https://img.shields.io/badge/LangChain-latest-purple" alt="LangChain Version"></a>
  <a href="https://shields.io/badge/React-latest-blueviolet"><img src="https://img.shields.io/badge/React-latest-blueviolet" alt="React Version"></a>
  <a href="https://shields.io/badge/Tailwind_CSS-latest-lightblue"><img src="https://img.shields.io/badge/Tailwind_CSS-latest-lightblue" alt="Tailwind CSS Version"></a>
  <a href="https://shields.io/badge/Auth0-latest-red"><img src="https://img.shields.io/badge/Auth0-latest-red" alt="Auth0 Version"></a>
</p>

*   **Backend:** FastAPI, Python, Langchain, OpenAI, MongoDB, Pydantic, python-jose, PyJWT, pytz
*   **Frontend:** React, react-router-dom, Auth0 React, Axios, Tailwind CSS, web-vitals
*   **Authentication:** Auth0

## Contribution Guide

We welcome contributions to this project! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Write clear and concise commit messages.
4.  Submit a pull request with a detailed description of your changes.
5.  Ensure all tests pass before submitting your pull request.

## Support & Contact

If you encounter any issues or have questions, please open an issue on GitHub.

## License

[MIT License](LICENSE)