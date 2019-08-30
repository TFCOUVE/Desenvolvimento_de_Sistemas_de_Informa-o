import sqlite3


def conn_sqlite():
    conn = sqlite3.connect('email_telephone_db')
    return conn
