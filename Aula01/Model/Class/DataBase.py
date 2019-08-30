import sqlite3


class Database:
    def test_connection():
        try:
            conn = sqlite3.connect('email_telephone_db')
            return "Conexão realizada com sucesso..."
        except Exception as e:
            print(e)
            return e

    def create_db():
        Database.test_connection()
        try:
            Database.record_db()
        except Exception as e:
            print(e)
            return e

    def record_db():
        from Aula01.Utils.Config import conn_sqlite
        try:
            conn = conn_sqlite()
            cur = conn.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS USER(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    EMAIL TEXT NOT NULL,
                    TELEPHONE TEXT NOT NULL
                    )''')
            conn.commit()
            conn.close()
            return 'Table User Created in Database', 200
        except Exception as e:
            print(e)
            return e


if __name__ == "__main__":
    Database.create_db()
