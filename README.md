# ⚔️ CodeForge

**CodeForge** is a full-stack competitive programming platform designed for practicing programming problems, submitting solutions, tracking performance, and receiving personalized problem recommendations.

The platform combines a **React frontend**, **FastAPI backend**, **PostgreSQL database**, JWT-based authentication, an online C++ execution service, and user-performance analytics into a single coding-practice environment.

---

## 🚀 Features

### 👤 User Authentication & Account Management

* User registration and login
* Secure password hashing
* JWT-based authentication
* Protected API routes
* Persistent user sessions
* User profile management
* Account deletion

### 🧩 Problem Solving

* Browse available programming problems
* View complete problem statements
* View problem constraints and test cases
* Submit C++ solutions directly from the platform
* Receive compilation/runtime/judging results
* Track previous submissions

### ⚙️ Online Code Execution

CodeForge integrates an external online compiler/execution service to execute submitted C++ programs.

The backend:

1. Receives the submitted source code.
2. Sends it to the configured execution service.
3. Executes the program against test cases.
4. Processes the execution result.
5. Returns the verdict and execution information to the frontend.

This keeps the execution API key on the backend instead of exposing it to the React client.

### 📊 Performance Dashboard

The dashboard provides a personalized overview of the user's coding activity, including:

* Solved/problem performance information
* Weakness analysis
* Recommended problems
* Personalized progress information

### 🧠 Weakness Analysis

CodeForge analyzes a user's previous submissions to identify areas where they may need additional practice.

The system groups unsuccessful/problem-solving activity by topic and uses the resulting information to identify weaker areas.

For example, if a user repeatedly struggles with problems belonging to a particular topic, that topic can receive higher priority in future recommendations.

### 🤖 Personalized Problem Recommendations

The recommendation system uses the user's submission history and identified weaknesses to recommend problems for further practice.

Recommendations prioritize:

* Weak topics
* Previously attempted problems
* Problem difficulty
* User solving history

This creates a personalized practice path instead of showing the same static problem list to every user.

### 🏆 Contest Section

The frontend includes a dedicated contests section for organizing and presenting competitive-programming contest information.

### 👤 Profile

Users can view their account information and manage their profile from the platform.

---

## 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │      React UI        │
                    │      Frontend        │
                    │      Port 3000        │
                    └──────────┬───────────┘
                               │
                         REST API / JSON
                               │
                               ▼
                    ┌──────────────────────┐
                    │      FastAPI         │
                    │      Backend         │
                    │      Port 8000       │
                    └───────┬───────┬──────┘
                            │       │
                 ┌──────────┘       └──────────────┐
                 ▼                                 ▼
        ┌─────────────────┐              ┌──────────────────┐
        │ PostgreSQL/Neon │              │ Online Compiler  │
        │    Database     │              │ / C++ Execution  │
        └─────────────────┘              └──────────────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Recommendation &    │
                 │ Weakness Analysis   │
                 └─────────────────────┘
```

---

## 🛠️ Tech Stack

### Frontend

* React
* JavaScript
* React Router
* Axios / Fetch API
* CSS

### Backend

* Python
* FastAPI
* Uvicorn
* SQLAlchemy
* Pydantic
* Python-JOSE
* Passlib / bcrypt

### Database

* PostgreSQL
* Neon PostgreSQL
* SQLAlchemy ORM

### Authentication

* JWT access tokens
* Password hashing
* Protected FastAPI routes

### Code Execution

* Online C++ execution API
* Backend-managed API authentication

### Algorithms / Intelligent Features

* Submission-based weakness analysis
* Topic-based problem recommendations
* User performance analysis
* Personalized problem selection

### Deployment

* Backend: Render
* Database: Neon PostgreSQL
* Frontend: React production build / static hosting

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Coding_platform_project
```

---

## 🔧 Backend Setup

### Create and activate a virtual environment

Windows:

```bat
cd backend

python -m venv .venv
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create:

```text
backend/.env
```

The `.env` file should contain your local/private configuration:

```env
DATABASE_URL=your_postgresql_connection_string
JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60
ONLINECOMPILER_API_KEY=your_online_compiler_api_key
FRONTEND_URL=http://localhost:3000
```

**Never commit the real `.env` file to GitHub.**

### Start the backend

From the `backend` directory:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI's interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

## 💻 Frontend Setup

Open another terminal:

```bash
cd frontend
npm install
npm start
```

The React development server will start at:

```text
http://localhost:3000
```

The frontend API base URL is configured through:

```text
REACT_APP_API_URL
```

If it is not provided during local development, the application falls back to:

```text
http://127.0.0.1:8000
```

---

## ⚙️ Environment Configuration

### Backend

The following values are kept outside the repository:

| Variable                          | Purpose                                        |
| --------------------------------- | ---------------------------------------------- |
| `DATABASE_URL`                    | PostgreSQL/Neon database connection            |
| `JWT_SECRET_KEY`                  | Secret used to sign JWT tokens                 |
| `JWT_ALGORITHM`                   | JWT signing algorithm                          |
| `JWT_ACCESS_TOKEN_EXPIRE_MINUTES` | JWT expiration duration                        |
| `ONLINECOMPILER_API_KEY`          | Authentication for the online compiler service |
| `FRONTEND_URL`                    | Frontend origin allowed by CORS                |

### Frontend

The frontend can use:

```env
REACT_APP_API_URL=https://your-backend-url
```

For local development:

```env
REACT_APP_API_URL=http://127.0.0.1:8000
```

> **⚠️ Security:** Never put database passwords, JWT secrets, compiler API keys, or other private credentials directly into frontend source code.

---

## 🔌 API Reference

### Health Check

| Method | Endpoint | Description                      |
| ------ | -------- | -------------------------------- |
| `GET`  | `/`      | Check whether the API is running |

### Authentication

| Method   | Endpoint         | Description                        | Authentication |
| -------- | ---------------- | ---------------------------------- | -------------- |
| `POST`   | `/auth/register` | Create a new account               | ❌              |
| `POST`   | `/auth/login`    | Authenticate a user                | ❌              |
| `GET`    | `/auth/me`       | Get authenticated user information | ✅              |
| `DELETE` | `/auth/account`  | Delete the authenticated account   | ✅              |

### Problems

| Method | Endpoint         | Description                 | Authentication |
| ------ | ---------------- | --------------------------- | -------------- |
| `GET`  | `/problems/`     | Retrieve available problems | ❌              |
| `GET`  | `/problems/{id}` | Retrieve a specific problem | ❌              |

### Submissions

| Method | Endpoint                       | Description                      | Authentication |
| ------ | ------------------------------ | -------------------------------- | -------------- |
| `POST` | `/submissions/`                | Submit a solution                | ✅              |
| `GET`  | `/submissions/`                | Retrieve submission history      | ✅              |
| `GET`  | `/submissions/weaknesses`      | Analyze weak areas               | ✅              |
| `GET`  | `/submissions/recommendations` | Get personalized recommendations | ✅              |

### Authentication Header

Protected endpoints require a JWT access token:

```http
Authorization: Bearer <your_jwt_token>
```

---

## 🧠 Recommendation Pipeline

CodeForge uses a multi-stage approach to personalize practice:

```text
User Submissions
       │
       ▼
Submission History
       │
       ▼
Weakness Analysis
       │
       ▼
Identify Weak Topics
       │
       ▼
Problem Recommendation
       │
       ▼
Personalized Practice
```

The recommendation service is separated from the API routes, making the recommendation logic easier to extend independently.

---

## ⚖️ Submission & Judging Pipeline

```text
C++ Source Code
      │
      ▼
POST /submissions/
      │
      ▼
Backend Validation
      │
      ▼
Online C++ Execution
      │
      ▼
Test Case Evaluation
      │
      ▼
Submission Result
      │
      ▼
Database
      │
      ▼
Dashboard / Analytics
```

This separates the frontend interface from the actual code-execution infrastructure.

---

## 📊 Database

CodeForge uses PostgreSQL through SQLAlchemy.

The primary entities include:

* Users
* Problems
* Test Cases
* Submissions

SQLAlchemy provides the ORM layer between the FastAPI application and PostgreSQL.

The production database is hosted using **Neon PostgreSQL**.

---

## 🚢 Deployment

### Backend

The backend is configured for deployment using:

* Python 3.12
* FastAPI
* Uvicorn
* Render

The repository contains:

```text
backend/Procfile
backend/runtime.txt
backend/requirements.txt
```

The deployment environment must provide the required environment variables securely.

### Frontend

Create a production build with:

```bash
cd frontend
npm run build
```

The generated `build/` directory contains the optimized static React application.

The production frontend should be configured with:

```env
REACT_APP_API_URL=https://your-deployed-backend-url
```

---

## 📁 Project Structure

```text
Coding_platform_project/
│
├── backend/
│   ├── Procfile
│   ├── requirements.txt
│   ├── runtime.txt
│   │
│   └── app/
│       ├── config.py
│       ├── database.py
│       ├── dependencies.py
│       ├── main.py
│       ├── security.py
│       │
│       ├── models/
│       │   ├── user.py
│       │   ├── problem.py
│       │   ├── submission.py
│       │   └── test_case.py
│       │
│       ├── schemas/
│       │   ├── user.py
│       │   ├── problem.py
│       │   ├── submission.py
│       │   └── test_case.py
│       │
│       ├── routes/
│       │   ├── auth.py
│       │   ├── problems.py
│       │   └── submissions.py
│       │
│       └── services/
│           ├── cpp_executor.py
│           ├── judge.py
│           ├── recommender.py
│           └── weakness_analyzer.py
│
├── frontend/
│   ├── public/
│   ├── package.json
│   ├── package-lock.json
│   │
│   └── src/
│       ├── components/
│       │   └── Navbar.js
│       │
│       ├── pages/
│       │   ├── Home.js
│       │   ├── Login.js
│       │   ├── Signup.js
│       │   ├── Problems.js
│       │   ├── ProblemDetails.js
│       │   ├── Dashboard.js
│       │   ├── Profile.js
│       │   └── Contests.js
│       │
│       ├── api.js
│       ├── App.js
│       ├── App.css
│       └── index.js
│
├── .gitignore
├── README.md
└── comands to start any machinne.txt
```

---

## 🔐 Security

CodeForge follows several basic security practices:

* Passwords are stored as hashes rather than plaintext.
* Authentication uses signed JWT tokens.
* Protected endpoints validate the authenticated user.
* Database credentials are loaded through environment variables.
* Online compiler credentials remain on the backend.
* `.env` files are excluded from Git.
* Local virtual environments are excluded from Git.
* Frontend builds and dependency directories are excluded from Git.

**Never commit:**

```text
.env
.env.local
database passwords
JWT secrets
API keys
private connection strings
```

---

## 🧪 Local Testing

For local development, run the backend and frontend simultaneously.

### Terminal 1 — Backend

```bat
cd backend
.venv\Scripts\activate
uvicorn app.main:app --reload
```

### Terminal 2 — Frontend

```bat
cd frontend
npm start
```

Then open:

```text
http://localhost:3000
```

The backend API documentation can be accessed at:

```text
http://127.0.0.1:8000/docs
```

---

## 👨‍💻 Author

**Prince Raj**

B.Tech — Electrical Engineering
Indian Institute of Technology Ropar

GitHub: **Prince-Raj-20**

---

## 📌 Project Highlights

CodeForge demonstrates a complete full-stack workflow:

* REST API development with FastAPI
* React-based frontend development
* PostgreSQL database integration
* SQLAlchemy ORM
* JWT authentication
* Secure password hashing
* Protected API routes
* Online C++ code execution
* Automated submission/judging pipeline
* Submission history tracking
* Weakness analysis
* Personalized problem recommendations
* User dashboard and analytics
* Profile and account management
* Production deployment configuration

---

## ⚠️ Disclaimer

CodeForge is a portfolio/educational project developed to demonstrate full-stack development, backend API design, database integration, authentication, code execution, and personalized learning features.

---

**Built with ❤️ by Prince Raj**

**Code. Submit. Analyze. Improve. ⚔️**
