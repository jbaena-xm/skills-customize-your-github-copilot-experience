from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
]


class BookCreate(BaseModel):
    title: str
    author: str
    year: int


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API"}


@app.get("/books")
def list_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(new_book: BookCreate):
    next_id = max((book["id"] for book in books), default=0) + 1
    created = {"id": next_id, **new_book.model_dump()}
    books.append(created)
    return created
