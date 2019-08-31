import sqlite3


def test_connection():
    try:
        conn = sqlite3.connect('email_telephone_db')
        return "Conexão realizada com sucesso..."
    except Exception as e:
        print(e)
        return e


def create_db():
    test_connection()
    try:
        create_table_record()
    except Exception as e:
        print(e)
        return e


def create_table_record(self):
    from ac2.Utils.Config import conn_sqlite
    try:
        conn = conn_sqlite()
        cur = conn.cursor()
        cur.execute('''
                CREATE TABLE IF NOT EXISTS RECORD(
                ID               INTEGER PRIMARY KEY AUTOINCREMENT,
                [VALUE]          TEXT NOT NULL,
                FLAG_TELEGRAM    BOOLEAN,
                FLAG_TELEPHONE   BOOLEAN,
                FLAG_EMAIL       BOOLEAN,
                CONFIRMED_STATUS TEXT)''')
        conn.commit()
        conn.close()
        return 'Table User Created in Database', 200
    except Exception as e:
        print(e)
        return e

# if __name__ == "__main__":
#     Database.create_db()
