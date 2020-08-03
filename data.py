import mysql.connector
import simplejson as json

from urllib.parse import unquote
from configs import DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE

def open_db():
    mydb = mysql.connector.connect(
    host = DB_HOST,
    user = DB_USER,
    passwd = DB_PASSWORD,
    database = DB_DATABASE
    )
    return mydb


def get_item(encodeName):
    item_name = unquote(encodeName)
    print(item_name)


    mydb = open_db()
    myDBcursor = mydb.cursor()
    table = 'ItemsList'
    sql = """ SELECT * FROM {} WHERE ItemName = "{}" """.format(table, item_name)
    print(sql)
    myDBcursor.execute(sql)
    item_got = myDBcursor.fetchall()
    myDBcursor.close()
    mydb.close()
    return item_got

def get_all_items():
    mydb = open_db()
    myDBcursor = mydb.cursor()
    table = 'ItemsList'
    sql = "SELECT * FROM %s" % (table)
    myDBcursor.execute(sql)
    items_got = myDBcursor.fetchall()
    myDBcursor.close()
    mydb.close()
    return items_got

def get_arb_tab():
    mydb = open_db()
    myDBcursor = mydb.cursor()
    table = 'ArbTable'
    sql = "SELECT * FROM %s" % (table)
    myDBcursor.execute(sql)

    row_headers=[x[0] for x in myDBcursor.description] #this will extract row headers
    arbtab = myDBcursor.fetchall()
    myDBcursor.close()
    mydb.close()
    json_data=[]
    for result in arbtab:
        json_data.append(dict(zip(row_headers,result)))

    return json_data # List

def update_like_num(item_name, input_rate):
    mydb = open_db()
    myDBcursor = mydb.cursor()
    table = 'ItemsList'
    sql = f"SELECT LikeNumber FROM {table} WHERE ItemName = '{item_name}' "
    try:
        myDBcursor.execute(sql)
        current_rate = myDBcursor.fetchall()
        new_rate = current_rate[0][0] + input_rate
        sql = f"UPDATE ItemsList SET LikeNumber= {new_rate} WHERE ItemName= '{item_name}'"
        myDBcursor.execute(sql)
    except:
        print('Error, pretty much no item like this to do things like I have stopped fearing and love the bomb')
        return False # No a valid item


    mydb.commit()
    myDBcursor.close()
    mydb.close()
    return True

def fetch_comment(item_name):
    mydb = open_db()
    myDBcursor = mydb.cursor()
    table = 'Comments'
    try:
        sql = f""" SELECT * FROM {table} WHERE ItemName="{item_name}" """
        myDBcursor.execute(sql)
        toReturn = myDBcursor.fetchall()
    except:
        toReturn = None
    return toReturn
    

def write_comment(item_name, body, create_time):
    mydb = open_db()
    myDBcursor = mydb.cursor()
    table = 'Comments'
    sql = f""" INSERT INTO {table} (ItemName, Body, CreatedAt) VALUES ("{item_name}","{body}",{create_time}) """
    print(sql)
    wroteStatus = True
    try:
        myDBcursor.execute(sql)
        mydb.commit()
        myDBcursor.close()
        mydb.close()
    except:
        wroteStatus = False
    
    return wroteStatus
    



