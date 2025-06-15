# LLM-Powered Ticket Management System

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005580?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev/)
![MongoDB](https://img.shields.io/badge/MongoDB-%234EA94B.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-34A853?style=for-the-badge&logo=langchain&logoColor=white)
![Auth0](https://img.shields.io/badge/Auth0-E01C5F?style=for-the-badge&logo=auth0&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

## Table of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This project is a full-stack ticket management system designed to streamline the process of submitting, classifying, and resolving support tickets.  It features a React-based frontend and a FastAPI-based backend.  A core component is the intelligent ticket routing mechanism, leveraging LangChain and LLMs to categorize incoming tickets and route them to the appropriate expert agent (React, Java, Python, or SQL).  Authentication and authorization are handled via Auth0, ensuring secure access and role-based permissions.

## Key Features

*   **Ticket Submission:** Users can easily submit support tickets via an intuitive React frontend.
*   **Intelligent Ticket Routing:**  An LLM-powered agent classifies tickets and routes them to the relevant development team (React, Java, Python, SQL) using a LangChain StateGraph.
*   **Automated Analysis:** Specialized agents utilize LLMs to analyze ticket content, generate summaries, assess priority, and suggest potential solutions.
*   **Role-Based Access Control:** Auth0 integration provides secure authentication and authorization, with role-based access control enforced on both the frontend and backend.
*   **Ticket Management:**  Administrators and developers can view, manage, and close tickets.
*   **Real-time Updates:**  The system provides real-time updates on ticket status and progress.

## Technology Stack

*   **Frontend:**
    *   React
    *   React Router
    *   Auth0
    *   Axios
    *   Tailwind CSS
*   **Backend:**
    *   Python
    *   FastAPI
    *   MongoDB
    *   LangChain
    *   Pydantic
    *   Auth0
    *   pytz
    *   datetime

## Project Structure

```
.
├── frontend/
│   ├── src/
│   │   ├── App.js            # Main application component
│   │   ├── Tickets.js        # Ticket list component
│   │   ├── ticketDetails.js  # Detailed ticket view component
│   │   ├── authWrapper.js    # Auth0 authentication wrapper
│   │   ├── useApi.js         # Custom hook for API requests
│   │   ├── Login.js          # Login component
│   │   ├── roleRequirer.js   # Role-based access control component
│   │   ├── roleBasedRedirect.js # Role based redirection component
│   │   ├── api.js            # API fetching functions
│   │   └── config.js         # Auth0 configuration
│   ├── public/
│   └── ...
├── backend/
│   ├── ticket_agent.py   # LLM-powered ticket classification and routing
│   ├── schemas.py        # Data schemas for tickets and messages
│   ├── route.py          # API endpoints for ticket management
│   ├── auth.py           # Authentication and authorization logic
│   ├── model.py          # Pydantic models for data structures
│   ├── main.py           # Main FastAPI application
│   └── ...
├── .env                # Environment variables
├── README.md           # This file
└── ...
```

## Installation

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
    cd frontend
    npm install
    ```

## Usage

1.  **Configure environment variables:**

    Create a `.env` file in both the `frontend` and `backend` directories and populate it with the necessary environment variables (see [Environment Variables](#environment-variables) section).

2.  **Run the backend:**

    ```bash
    cd backend
    uvicorn main:app --reload
    ```

3.  **Run the frontend:**

    ```bash
    cd frontend
    npm start
    ```

4.  **Access the application:**

    Open your web browser and navigate to the address where the frontend is running (usually `http://localhost:3000`).

## Environment Variables

The following environment variables are required:

**Backend (`backend/.env`):**

*   `AUTH0_DOMAIN`: Your Auth0 domain.
*   `AUTH0_CLIENT_ID`: Your Auth0 client ID.
*   `AUTH0_API_IDENTIFIER`: Your Auth0 API Identifier.
*   `DATABASE_URL`: MongoDB connection string.
*   `MONGODB_DATABASE_NAME`: MongoDB database name.
*   `OPENAI_API_KEY`: OpenAI API Key
    
**Frontend (`frontend/.env`):**

*   `REACT_APP_AUTH0_DOMAIN`: Your Auth0 domain.
*   `REACT_APP_AUTH0_CLIENT_ID`: Your Auth0 client ID.
*   `REACT_APP_AUTH0_AUDIENCE`: Your Auth0 API Identifier.

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear, concise messages.
4.  Submit a pull request.

## License

[MIT](LICENSE)

## Contact

If you have any questions or issues, please contact us at <your_email@example.com>.