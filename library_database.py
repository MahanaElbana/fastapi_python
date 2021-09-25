
import sqlite3
from http import HTTPStatus


con = sqlite3.connect('trial.db')
cur = con.cursor()

#* Save (commit) the changes
def savedatabase():
    con.commit()

#* close database
def closddatabase():   
    con.close()   

#* ---- Get all categories from databas ---#
def get_all_categories():
    query_category = cur.execute('''SELECT * FROM Category''')
    allcategories = query_category.fetchall()
    listData = []
    for i in allcategories:
        listData.append({"id": i[0], "categoryName": i[1]})
    return listData

#* ---- Get all books from databas ---#
def get_all_books():
    query_book = cur.execute('''SELECT * FROM book''')
    allbooks = query_book.fetchall()
    listData = []
    for i in allbooks:
        listData.append({
            "BookID": i[0],
            "NameBOOK": i[1],
            "auther_name": i[2], 
            "CatID": i[3]})
    return listData

#* ---- insert books in databas ---#
def insert_book(NameBOOK , auther_name , CatID ):
        query_book = cur.execute('''SELECT * FROM book''')
        allbooks = query_book.fetchall()
        BookID = len(allbooks)+1
        cur.execute(f"""
        INSERT INTO book
        (BookID,NameBOOK, auther_name, CatID )
        VALUES
        ({BookID},'{NameBOOK}','{auther_name}',{CatID})
        """) 
        savedatabase()
        print({"💙 ✨": HTTPStatus.ACCEPTED})       

#* ---- insert category in databas ---#
def insert_category(categoryName):
        query_category = cur.execute('''SELECT * FROM Category''')
        allCategories = query_category.fetchall()
        CategoryID = len(allCategories)+1
        cur.execute(f"""
        INSERT INTO Category
        (CategoryID ,Name )
        VALUES
        ({CategoryID},'{categoryName}')
        """) 
        savedatabase()
        print({"💙 ✨": HTTPStatus.ACCEPTED})        