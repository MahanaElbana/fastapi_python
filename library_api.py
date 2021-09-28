#! uvicorn library_api:app --host 0.0.0.0 --port 8899  --reload
#! #! uvicorn library_api:app --reload
#! uvicorn library_api:app --port 8899 --reload
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn

from library_database import*

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool]=None

@app.get("/use_model/")
async def use_model_post(item: Item):
    return item


@app.get("/item/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

dataCategory = get_all_categories()
@app.get("/allcategories/")
def return_all_categories():
    '''http://127.0.0.1:8000/allcategories/'''
    return dataCategory

#insert_books("dark","ali",2)

databook = get_all_books()
@app.get("/allbooks/")
def read_item():
    '''http://127.0.0.1:8899/allbooks/'''
    return databook

#insert_category("states")



#cinsert_book(NameBOOK , auther_name , CatID ):
# class Item(BaseModel):
#     NameBOOK: str
#     auther_name: Optional[str] = None
#     CatID: int

# book_name = ""
# auther_name =""
# cat_id = 0
# @app.post("/post_book/")
# async def create_book(item: Item):
#     '''http://127.0.0.1:8899/post_book/'''
#     book_name = item.NameBOOK
#     auther_name = item.auther_name
#     cat_id = item.CatID
#     if book_name != "" or auther_name !="" :
#         insert_book(book_name , auther_name , cat_id)
#     return item

# if book_name != "" or auther_name !="" :
#     insert_book(book_name , auther_name , cat_id) 

@app.get('/trial/{id_header:int}/')
def query_header(id_header ,limit:int =50, published:bool=True , name:Optional[str]=None):
    """how to use header {id_header}"""
    """how to use {Query} in FastAPI"""
    """ %20 for left space with one later between two words """
    """http://127.0.0.1:8000/trial/35/?limit=500&published=true&name=%20hello%20%20world !"""
    """http://127.0.0.1:8000/trial/ """

    if limit == 50 and published == True :
        return {"default": f"""values are {limit} for limit and 
                                        {published} for published and name ={name}"""}
    else : 
        return {"new values": f"""values are {limit} for limit and {published} 
                                        for published  and name ={name}and number {id_header} """}  

# -- python3 library_api.py
if __name__ =="__main__":
        print(__name__)
        uvicorn.run(app, port = 8000 ,host='127.0.0.1')
