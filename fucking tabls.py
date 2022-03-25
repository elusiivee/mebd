import sqlite3
from sqlite3 import Error
from exer import Pilot


#
#
# def sql_connection():
#     try:
#
#         con = sqlite3.connect('mydatabase.db')
#
#         return con  # обьект соединения
#
#     except Error:
#
#         print(Error)
#
#
#
# def sql_insert(con, entities):
#     cursorObj = con.cursor()
#
#     cursorObj.execute(
#         'INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
#
#     con.commit()
#
#
# entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
# con=sql_connection()
# sql_insert(con, entities)
def make_connection():
    '''
    this function shood make conaction with cursor and table
    '''
    try:
        con = sqlite3.connect("FUcking_table.db")
        cur = con.cursor()
        return cur
    except Error:
        print(Error)




def create_table(table_name:str, obj):
    '''
    this fuc=nction creat a table
    '''
    con = sqlite3.connect("FUcking_table.db")
    cur = con.cursor()

    # keys,values = tuple(kwargs.keys()), tuple(kwargs.values())
    # data = [keys,values]



    cur.executemany(f"create table {table_name} (?, ?, ?, ?, ?,?)", obj.values()) #як йоготут передати
    con.commit()


def select_table():                                                 #select hz chi pravilno
    '''
    this function shood try to select information
    '''
    con = sqlite3.connect("FUcking_table.db")
    cursorObj = con.cursor()

    cursorObj.execute('SELECT name FROM testing WHERE salary > 800.0')

    rows = cursorObj.fetchall()

    for row in rows:
        print(row)




initialization_data = Pilot.make_info()
obj = Pilot(*initialization_data)
create_table("FUcking_table.db",obj)
sel=select_table()
print(sel)
