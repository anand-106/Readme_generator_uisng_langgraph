```markdown
# Ticket Classifier using LangGraph

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005580?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
![LangChain](https://img.shields.io/badge/LangChain-34A853?style=for-the-badge&logo=langchain&logoColor=white)
[![Auth0](https://img.shields.io/badge/Auth0-E53935?style=for-the-badge&logo=auth0&logoColor=white)](https://auth0.com/)
[![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://reactjs.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)

## Introduction

This project is a full-stack ticket submission and management portal designed to streamline the process of creating, classifying, and resolving support tickets. It leverages a combination of cutting-edge technologies, including FastAPI for the backend, React for the frontend, LangChain for intelligent ticket routing and analysis, and Auth0 for secure authentication and authorization. The system employs role-based access control, ensuring that users have appropriate permissions based on their assigned roles.

## Key Features

*   **Intelligent Ticket Routing:** Utilizes LangChain to classify and route tickets to specialized agents (e.g., Python, SQL, React) based on the ticket's content.
*   **Role-Based Access Control:** Implements secure access control using Auth0, restricting access to certain features based on user roles (e.g., admin vs. user).
*   **Full-Stack Architecture:** Employs a modern full-stack architecture with a FastAPI backend and a React frontend for a seamless user experience.
*   **Asynchronous Operations:**  Utilizes asynchronous operations throughout the codebase for improved performance and responsiveness.
*   **Structured Output:** Employs Pydantic models in conjunction with LangChain agents to ensure structured and predictable LLM responses.
*   **Authentication and Authorization:** Secures the application with Auth0, providing robust authentication and authorization capabilities.
*   **API Endpoints:** Provides a comprehensive set of API endpoints for ticket creation, retrieval, and management.
*   **Frontend Components:** Features a rich set of React components for submitting, viewing, and managing tickets.

## Project Structure

```
Ticket_classifier_using_LangGraph/
├── Backend/
│   ├── main.py
│   ├── ticket_agent.py
│   ├── Auth/
│   │   └── auth.py
│   ├── Database/
│   │   ├── config/
│   │   │   └── database.py
│   │   ├── models/
│   │   │   └── model.py
│   │   ├── routes/
│   │   │   └── route.py
│   │   └── schema/
│   │       └── schemas.py
├── frontend/
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   ├── src/
│   │   ├── api.js
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── reportWebVitals.js
│   │   ├── setupTests.js
│   │   ├── ticketDetails.js
│   │   ├── Tickets.js
│   │   ├── Auth/
│   │   │   ├── authWrapper.js
│   │   │   ├── config.js
│   │   │   ├── Login.js
│   │   │   ├── roleBasedRedirect.js
│   │   │   ├── roleRequirer.js
│   │   │   └── API/
│   │   │       └── useApi.js
```

## Getting Started

Follow these steps to set up and run the project locally:

### Prerequisites

*   Python 3.7+
*   Node.js and npm
*   MongoDB installed and running

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd Ticket_classifier_using_LangGraph
    ```

2.  **Backend Setup:**

    ```bash
    cd Backend
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Frontend Setup:**

    ```bash
    cd ../frontend
    npm install
    ```

4.  **Environment Variables:**

    Create `.env` files in both the `Backend` and `frontend` directories.  Populate them with the necessary environment variables.  Example `.env` for the backend:

    ```
    DATABASE_URL="mongodb://localhost:27017/ticket_classifier"
    AUTH0_DOMAIN="your_auth0_domain"
    AUTH0_CLIENT_ID="your_auth0_client_id"
    AUTH0_CLIENT_SECRET="your_auth0_client_secret"
    AUTH0_AUDIENCE="your_auth0_audience"
    ```

    Example `.env` for the frontend:

    ```
    REACT_APP_AUTH0_DOMAIN="your_auth0_domain"
    REACT_APP_AUTH0_CLIENT_ID="your_auth0_client_id"
    REACT_APP_AUTH0_AUDIENCE="your_auth0_audience"
    ```

    **Note:** Replace the placeholder values with your actual Auth0 credentials and MongoDB connection string.

### Running the Application

1.  **Start the Backend:**

    ```bash
    cd Backend
    uvicorn main:app --reload
    ```

2.  **Start the Frontend:**

    ```bash
    cd ../frontend
    npm start
    ```

The frontend will typically be accessible at `http://localhost:3000`, and the backend at `http://localhost:8000`.

## API

The backend provides the following key API endpoints:

*   `POST /add-ticket`: Creates a new ticket. Requires authentication.
*   `GET /tickets`: Retrieves a list of all tickets. Requires authentication.
*   `GET /my-tickets`: Retrieves a list of tickets assigned to the current user. Requires authentication.
*   `GET /ticket/{ticketNo}`: Retrieves details for a specific ticket. Requires authentication.
*   `PATCH /ticket/{ticketNo}`: Closes a specific ticket. Requires admin role.

Consult the FastAPI documentation for detailed API specifications.

## Modules and Agents

*   **`ticket_agent.py`:**  This module defines the LangChain agents responsible for classifying and routing tickets.  It includes agents for Python, SQL, and potentially other technologies.  The core function, `run_chatbot`, orchestrates the interaction between the user input, the router, and the appropriate agent.
*   **`auth.py`:** This module implements the token verification logic using Auth0, ensuring that only authenticated users can access protected API endpoints.
*   **Frontend `AuthWrapper` & `useApi.js`**: These Components provide the authentication wrapper and the custom hook responsible for providing Auth0 authentication to the routes and APIs of this project.

## Contributing

We welcome contributions to this project! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Push your changes to your fork.
5.  Submit a pull request to the main repository.

## License

[MIT](LICENSE)
```