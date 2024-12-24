# Expense Tracker Application

An Expense Tracker application built with a **Node.js** backend and a **React.js** frontend. This application helps users manage their expenses efficiently.

---

## Features

- User authentication (register, login, and logout).
- Expense management (add, update, and delete expenses).
- Validation middleware for secure user inputs.
- RESTful APIs for user and expense data management.
- Responsive frontend design.
- Backend API deployment ready with **Vercel**.

---

## Repository Structure

### Backend
- **Controllers/**
  - `AuthController.js`: Handles authentication logic like login and registration.
  - `ExpenseController.js`: Manages expense-related operations like creating, updating, and deleting expenses.
  
- **Middlewares/**
  - `Auth.js`: Middleware for verifying user authentication tokens.
  - `AuthValidation.js`: Middleware for validating user input.

- **Models/**
  - `User.js`: User schema for MongoDB.
  - `db.js`: Database connection setup.

- **Routes/**
  - `AuthRouter.js`: Routes for authentication endpoints.
  - `ExpenseRouter.js`: Routes for expense-related endpoints.
  - `ProductRouter.js`: Routes for product-related functionality.

- **Other Files**
  - `.env`: Environment configuration file.
  - `index.js`: Main entry point for the backend server.
  - `package.json`: Contains backend dependencies.
  - `vercel.json`: Configuration for deploying the backend with Vercel.

### Frontend
- **public/**
  - Static assets such as `favicon.ico`, `index.html`, and icons.

- **src/pages/**
  - `App.js`: Entry point for the React application.
  - `RefrshHandler.js`: Handles refresh token management.
  - `index.js`: Renders the React app.
  - Other utility files for styling (`App.css`, `index.css`) and setup (`reportWebVitals.js`, `setupTests.js`).

- **Other Files**
  - `.env`: Environment configuration file for frontend.
  - `README.md`: Project documentation.
  - `package.json`: Contains frontend dependencies.
  - `vercel.json`: Configuration for deploying the frontend with Vercel.

---

## Installation and Setup

### Prerequisites
- Node.js and npm installed on your system.
- MongoDB database.

### Clone the Repository
```bash
git clone <repository-url>
cd expense-tracker
