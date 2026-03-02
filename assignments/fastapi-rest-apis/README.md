# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI to practice creating endpoints, validating request data, and returning structured JSON responses.

## 📝 Tasks

### 🛠️	Create Core API Endpoints

#### Description
Use FastAPI to build an API for managing a simple in-memory collection of books.

#### Requirements
Completed program should:

- Create a `GET /` endpoint that returns a welcome message.
- Create a `GET /books` endpoint that returns the full list of books.
- Create a `GET /books/{book_id}` endpoint that returns one book by ID or an error message if not found.


### 🛠️	Add Book Creation with Validation

#### Description
Implement a `POST` endpoint that allows users to add a new book and validates the input with a Pydantic model.

#### Requirements
Completed program should:

- Define a Pydantic model with `title`, `author`, and `year` fields.
- Create a `POST /books` endpoint that accepts JSON and adds a new book with a unique ID.
- Return the created book in the response and preserve all books in memory while the server runs.
