import sqlite3 as sq
def insert_deal(name, product, price, amount):
    with sq.connect("saper.db") as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS deals (
                            name TEXT,
                            товар TEXT,
                            price INTEGER,
                            amount INTEGER)""")
        cur.execute("""INSERT INTO deals VALUES(?,?,?,?)""", (name, product, price, amount))
def show_deals():
    with sq.connect("saper.db") as con:
        cur = con.cursor()
        cur.execute("""SELECT rowid,* FROM deals""")
        result = cur.fetchall()
        for row in result:
            print(row)
def delete_all_data():
    with sq.connect("saper.db") as con:
        cur = con.cursor()
        cur.execute("DROP TABLE deals")
def update_price(product, price):
    with sq.connect("saper.db") as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS prices (
                    product TEXT,
                    price INTEGER)""")
        cur.execute("""SELECT * FROM prices WHERE product = ?""", (product,))
        res = cur.fetchall()
        if len(res)>0:
            cur.execute("""UPDATE prices SET price = ? WHERE product = ?""", (price, product))
        else:
            cur.execute("""INSERT INTO prices VALUES(?,?)""", (product, price))
def show_prices():
    with sq.connect("saper.db") as con:
        cur = con.cursor()
        cur.execute("""SELECT rowid,* FROM prices""")
        result = cur.fetchall()
        for row in result:
            print(row)
def delete_product(product):
    with sq.connect("saper.db") as con:
        cur = con.cursor()
        cur.execute("""DELETE FROM prices WHERE product = ?""", (product,))