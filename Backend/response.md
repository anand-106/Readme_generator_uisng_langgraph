```markdown
# Ticket Classifier with LangGraph

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005580?style=for-the-badge&logo=fastapi&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-34A853?style=for-the-badge&logo=langchain&logoColor=white)
![Auth0](https://img.shields.io/badge/Auth0-E01F36?style=for-the-badge&logo=auth0&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

## Table of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a full-stack application designed for ticket management, featuring an AI-powered triage system. It combines a React frontend with a Python backend built on FastAPI. The application utilizes LangChain and state graphs to classify and route incoming support tickets to the appropriate development team (React, Java, Python, or SQL), streamlining the support process. Auth0 is integrated for robust authentication and role-based authorization, ensuring secure access to different application features.

## Key Features

- **AI-Powered Ticket Triage:** Uses LangChain and LLMs (Language Model Models) to automatically classify and route support tickets.
- **Role-Based Access Control:** Leverages Auth0 to provide secure, role-based access to application features (user, admin, developer).
- **Full-Stack Architecture:** Combines a React frontend for user interaction with a FastAPI backend for API services and data processing.
- **Real-time Ticket Management:** Allows users to submit tickets, view ticket details, and track ticket status.
- **Automated Analysis:** Provides automated analysis of tickets by specialized agents, increasing efficiency.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Backend Setup:**

    *   Navigate to the `Backend` directory:

        ```bash
        cd Backend
        ```

    *   Create a virtual environment (recommended):

        ```bash
        python -m venv venv
        source venv/bin/activate  # On Linux/macOS
        venv\Scripts\activate  # On Windows
        ```

    *   Install dependencies:

        ```bash
        pip install -r requirements.txt
        ```

3.  **Frontend Setup:**

    *   Navigate to the `frontend` directory:

        ```bash
        cd ../frontend
        ```

    *   Install dependencies:

        ```bash
        npm install
        ```

4.  **Environment Configuration:**

    *   Create a `.env` file in both the `Backend` and `frontend` directories.
    *   Populate the `.env` files with the necessary environment variables (see [Environment Variables](#environment-variables) section).

5.  **Database Setup:**

    *   Ensure MongoDB is installed and running.
    *   Configure the MongoDB URI in the `.env` file.

## Usage

1.  **Backend:**

    *   Navigate to the `Backend` directory.
    *   Run the FastAPI server:

        ```bash
        python main.py
        ```

    *   The API will be accessible at `http://localhost:8000` (or the configured host and port).

2.  **Frontend:**

    *   Navigate to the `frontend` directory.
    *   Start the React development server:

        ```bash
        npm start
        ```

    *   The frontend will be accessible at `http://localhost:3000` (or the configured host and port).

3.  **Accessing the Application:**

    *   Open your browser and navigate to the frontend URL.
    *   Log in using your Auth0 credentials.
    *   Submit and manage support tickets through the user interface.

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

## Environment Variables

The following environment variables are required for the application to function correctly:

**Backend (.env):**

-   `AUTH0_DOMAIN`: Auth0 domain.
-   `AUTH0_CLIENT_ID`: Auth0 client ID.
-   `AUTH0_CLIENT_SECRET`: Auth0 client secret.
-   `AUTH0_AUDIENCE`: Auth0 API audience.
-   `MONGODB_URI`: MongoDB connection string.
-   `ALGORITHM`: The Algorithm to use.
-   `LLM_API_KEY`: API key for the LLM
    ```
    Example:
    AUTH0_DOMAIN=your_auth0_domain
    AUTH0_CLIENT_ID=your_auth0_client_id
    AUTH0_CLIENT_SECRET=your_auth0_client_secret
    AUTH0_AUDIENCE=your_auth0_audience
    MONGODB_URI=mongodb://localhost:27017/ticket_db
    ALGORITHM=RS256
    LLM_API_KEY=sk-...
    ```

**Frontend (.env):**

-   `REACT_APP_AUTH0_DOMAIN`: Auth0 domain.
-   `REACT_APP_AUTH0_CLIENT_ID`: Auth0 client ID.
-    `REACT_APP_AUTH0_AUDIENCE`: Auth0 API audience.
-   `REACT_APP_API_URL`: API url

    ```
    Example:
    REACT_APP_AUTH0_DOMAIN=your_auth0_domain
    REACT_APP_AUTH0_CLIENT_ID=your_auth0_client_id
    REACT_APP_AUTH0_AUDIENCE=your_auth0_audience
    REACT_APP_API_URL=http://localhost:8000
    ```

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes.
4.  Submit a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```