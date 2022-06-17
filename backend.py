import sqlite3

def connect():

    conn=sqlite3.connect('record.db')

    cur=conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS INFO (id integer primary key, foodname text ,type text ,cost int)")

    conn.commit()

    conn.close()



def insert(foodname,type,cost):

    conn=sqlite3.connect('record.db')

    cur=conn.cursor()

    cur.execute("INSERT INTO INFO VALUES (NULL,?,?,?)",(foodname,type,cost))

    conn.commit()

    conn.close()



def view():

    conn=sqlite3.connect('record.db')

    cur=conn.cursor()

    cur.execute("SELECT * FROM INFO")

    result=cur.fetchall()

    conn.commit()

    conn.close()

    return result



def delete(id):

    conn=sqlite3.connect('record.db')

    cur=conn.cursor()

    cur.execute("DELETE FROM INFO WHERE id=?",(id,))

    conn.commit()

    conn.close()



def search(foodname='',type='',cost=''):

    conn=sqlite3.connect('record.db')

    cur=conn.cursor()

    cur.execute('SELECT * FROM INFO WHERE foodname=? or type=? OR  cost=?',(foodname,type,cost))

    result=cur.fetchall()

    conn.commit()

    conn.close()

    return result




# connect()
# insert('bpm','veg',120)
# print(view())