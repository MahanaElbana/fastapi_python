#! uvicorn library_api:app --host 0.0.0.0 --port 8899  --reload
#! uvicorn library_api:app --port 8899 --reload
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

from library_database import*

app = FastAPI()

@app.get("/item/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

dataCategory = get_all_categories()
@app.get("/allcategories/")
def return_all_categories():
    '''http://127.0.0.1:8899/allcategories/'''
    return dataCategory

#insert_books("dark","ali",2)

databook = get_all_books()
@app.get("/allbooks/")
def read_item():
    '''http://127.0.0.1:8899/allbooks/'''
    return databook

#insert_category("states")



#cinsert_book(NameBOOK , auther_name , CatID ):
class Item(BaseModel):
    NameBOOK: str
    auther_name: Optional[str] = None
    CatID: int

book_name = ""
auther_name =""
cat_id = 0
@app.post("/post_book/")
async def create_book(item: Item):
    '''http://127.0.0.1:8899/post_book/'''
    book_name = item.NameBOOK
    auther_name = item.auther_name
    cat_id = item.CatID
    if book_name != "" or auther_name !="" :
        insert_book(book_name , auther_name , cat_id)
    return item

if book_name != "" or auther_name !="" :
    insert_book(book_name , auther_name , cat_id) 

