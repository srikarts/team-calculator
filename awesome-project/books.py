from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    id : int
    title : str 
    author : str 
    year : int

class BookCreate(BaseModel):
    title : str
    author : str
    year : int

books = [Book(id=1,title='Atmoic Habits',author='James Clear',year=2011),
         Book(id=2,title='Swami Friends',author='RK Narayan',year=2005),
         Book(id=3,title='The Wings of Fire',author='APJ Abdul Kalam',year=2000)]

@app.get('/books/')
def show_books(author: str = None):
    if author:
        return [book for book in books if author.lower()==book.author.lower()]
    return books

@app.get('/books/{book_id}')
def get_book(book_id:int):
    for book in books:
        if book.id == book_id:
            return book
    return {"message":"No book found with the given id"}

# @app.post('/books/')
# def add_book(book:Book):
#     if book not in books:
#         books.append(book)
#         return book
#     else:
#         raise HTTPException(status_code=404,detail=f"Invalid book details provided")

@app.post('/books/')
def add_book(book:BookCreate):
    new_id = max((b.id for b in books),default=0)+1
    new_book = Book(id=new_id, **book.dict())
    books.append(new_book)
    return new_book
    # else:
    #     return {'message':'Invalid book details provided'}
