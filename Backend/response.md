# <p align="center">Ticket Management Portal</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI"></a>
  <a href="#"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React"></a>
  <a href="#"><img src="https://img.shields.io/badge/Auth0-E34F26?style=for-the-badge&logo=auth0&logoColor=white" alt="Auth0"></a>
  <a href="#"><img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB"></a>
  <a href="#"><img src="https://img.shields.io/badge/LangChain-343A40?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAJtSURBVHgBvZLdSgJhAIDVQOwjN2E4gBGYi0jMOgUjMS0lC7hI9gIxMhN7DGyX6JZnw6nS+P///e97s+T5lB0QEEB/5z4g9BfJ/V2gN6hO+GvX/I7/c29w9v74u1I8Lz9fM5837+2H3V1Wz+4r7i2O9+6/7vV03/7tV3/0TfI57J7F8f9rM7f3n98o9m/8g7oB0w2z9N3gX36o1c8O8P1j7eP6t/xLd9t8O7Jd399/v74w+wH4878K83rJ0v6r55t87y2/jM397/6yv7i8P890834n74H8XgB7b+W+a+r8S466g/5695f+V88Q8U2D8T7z4c4i4O9T6X9X4U5s9H7n/8T9695t0r5r704v507E8G9n6t79v9o9l85897l/8g6oB0g47+M+b3h2h3d5e1H8I8f4vj2c4a0B6l54b3h2X3n6p9a/B2l1R7v72j977v8z4u9z/zH69/V7n8I7b9t9t56/3n+x9z8n6B6M/O6+e/7+y+P9b5s/zP9j6x5h753w7n8I7d8R4L4M6o+K1U+c8E9p7v13v6X3v4N9t6W9h4D+Q/B6+C/e/sPlv2/r7i/5c7v8Y2/18/Y/l/y08Y9L5w9q+M6+4h0v5P7i+W+t+t5804g+M7J/g+C8z4P6D5z6o8v1A/P6v6p4Z7D3C56+y8V5u8/7YvP/wNq43+X/d8l9/63y/+g+B9h9455R7z0T2PsvY/x/T7T958n4b448Y/I9T7D8h6j6J8d6v/2z967y+R8U509G83+B5n8H6j6B9o7D7X738I+T6z7W/77x/8n0v77/Y8Z+u81+v4b637J/2/h/G/r/I/M/xPpP5PxX4b6o8W5W9A6n7H2/6/9D9N8D9h9i5r8B536N97+B7n6o9U416N2/2t2v6z3f7H5Pq/P8/+X7P1P3T1x7Y8H8d5v+H+p8J9U+L86+77Z7P1P3T2n756/+x6o8Z+28r8Z55792z8L8u6D8X638X438n4n8H5n+J/D/d/j//f/2/6f8z+n/N/y/2f8f+v/N/zP9f8v8b/v/0v4v8H8Z/h/B/u/wf/f/o=" alt="LangChain"></a>
</p>

## Introduction

This project is a comprehensive ticket management portal designed to streamline internal support and task assignment. It leverages a modern tech stack including React for the frontend, FastAPI for the backend, and MongoDB for the database. It uses Langchain to classify tickets automatically. The application features role-based access control to ensure secure access and efficient workflow management.

## Table of Contents

1.  [Key Features](#key-features)
2.  [Installation Guide](#installation-guide)
3.  [Usage](#usage)
4.  [Environment Variables](#environment-variables)
5.  [Project Structure](#project-structure)
6.  [Technologies Used](#technologies-used)
7.  [License](#license)

## Key Features

-   **Ticket Submission:** Users can submit new tickets with detailed descriptions.
-   **Ticket Management:** Admins can view, assign, and close tickets.
-   **Role-Based Access Control:** Different user roles (admin, developers, users) have different levels of access.
-   **Authentication & Authorization:** Secure authentication using Auth0.
-   **Automated Ticket Triage:** Langchain-powered chatbot classifies incoming tickets and assigns them to the appropriate team (React, Java, Python, SQL).
-   **Real-time Updates:** The frontend provides a dynamic and responsive user experience.
-   **Detailed Ticket View:** Users can view detailed information about each ticket, including status, priority, and team assignment.

## Installation Guide

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <project_directory>
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

    -   Create a `.env` file in the `Backend` directory.
    -   Add the following environment variables:

        ```
        AUTH0_DOMAIN=<your_auth0_domain>
        AUTH0_CLIENT_ID=<your_auth0_client_id>
        AUTH0_CLIENT_SECRET=<your_auth0_client_secret>
        AUTH0_AUDIENCE=<your_auth0_audience>
        DATABASE_URL=<your_mongodb_connection_string>
        MONGODB_DATABASE_NAME=<your_database_name>
        ```

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

-   **Frontend:** Access the application in your browser at `http://localhost:3000`.
    -   Log in using your Auth0 credentials.
    -   Submit new tickets via the input form on the home page.
    -   View ticket details by clicking on a ticket in the list.
    -   Admins can close tickets from the ticket details view.

-   **Backend:** The FastAPI backend provides API endpoints for managing tickets.
    -   API endpoints are documented using Swagger/OpenAPI at `http://localhost:8000/docs`.

## Environment Variables

The following environment variables are required for the application to run correctly:

-   `AUTH0_DOMAIN`: The domain of your Auth0 application. Used for authentication.
-   `AUTH0_CLIENT_ID`: The client ID of your Auth0 application. Used for authentication.
-   `AUTH0_CLIENT_SECRET`: The client secret of your Auth0 application. Used for authentication.
-   `AUTH0_AUDIENCE`: The API identifier in Auth0.  Used for authentication.
-   `DATABASE_URL`: The MongoDB connection string. Used to connect to the database.
-   `MONGODB_DATABASE_NAME`: The MongoDB database name.

## Project Structure

```
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

## Technologies Used

<p align="left">
  <a href="#"><img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI"></a>
  <a href="#"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React"></a>
  <a href="#"><img src="https://img.shields.io/badge/Auth0-E34F26?style=for-the-badge&logo=auth0&logoColor=white" alt="Auth0"></a>
  <a href="#"><img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB"></a>
    <a href="#"><img src="https://img.shields.io/badge/LangChain-343A40?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAJtSURBVHgBvZLdSgJhAIDVQOwjN2E4gBGYi0jMOgUjMS0lC7hI9gIxMhN7DGyX6JZnw6nS+P///e97s+T5lB0QEEB/5z4g9BfJ/V2gN6hO+GvX/I7/c29w9v74u1I8Lz9fM5837+2H3V1Wz+4r7i2O9+6/7vV03/7tV3/0TfI57J7F8f9rM7f3n98o9m/8g7oB0w2z9N3gX36o1c8O8P1j7eP6t/xLd9t8O7Jd399/v74w+wH4878K83rJ0v6r55t87y2/jM397/6yv7i8P890834n74H8XgB7b+W+a+r8S466g/5695f+V88Q8U2D8T7z4c4i4O9T6X9X4U5s9H7n/8T9695t0r5r704v507E8G9n6t79v9o9l85897l/8g6oB0g47+M+b3h2h3d5e1H8I8f4vj2c4a0B6l54b3h2X3n6p9a/B2l1R7v72j977v8z4u9z/zH69/V7n8I7b9t9t56/3n+x9z8n6B6M/O6+e/7+y+P9b5s/zP9j6x5h753w7n8I7d8R4L4M6o+K1U+c8E9p7v13v6X3v4N9t6W9h4D+Q/B6+C/e/sPlv2/r7i/5c7v8Y2/18/Y/l/y08Y9L5w9q+M6+4h0v5P7i+W+t+t5804g+M7J/g+C8z4P6D5z6o8v1A/P6v6p4Z7D3C56+y8V5u8/7YvP/wNq43+X/d8l9/63y/+g+B9h9455R7z0T2PsvY/x/T7T958n4b448Y/I9T7D8h6j6J8d6v/2z967y+R8U509G83+B5n8H6j6B9o7D7X738I+T6z7W/77x/8n0v77/Y8Z+u81+v4b637J/2/h/G/r/I/M/xPpP5PxX4b6o8W5W9A6n7H2/6/9D9N8D9h9i5r8B536N97+B7n6o9U416N2/2t2v6z3f7H5Pq/P8/+X7P1P3T1x7Y8H8d5v+H+p8J9U+L86+77Z7P1P3T2n756/+x6o8Z+28r8Z55792z8L8u6D8X638X438n4n8H5n+J/D/d/j//f/2/6f8z+n/N/y/2f8f+v/N/zP9f8v8b/v/0v4v8H8Z/h/B/u/wf/f/o=" alt="LangChain"></a>
</p>

-   **Backend:**
    -   FastAPI
    -   Python
    -   Pydantic
    -   uvicorn
    -   pymongo
    -   python-dotenv
    -   Langchain
    -   pytz

-   **Frontend:**
    -   React
    -   Auth0
    -   Axios
    -   react-router-dom
    -   web-vitals
    -   TailwindCSS

## License

<p align="left">
  <a href="#"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"></a>
</p>

MIT License