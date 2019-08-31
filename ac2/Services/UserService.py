from contextlib import closing


def verify_value(id, value):
    from ac2.Utils.Config import conn_sqlite as connect
    string = '''
    SELECT ID, VALUE, CONFIRMED_STATUS
    FROM RECORD
    WHERE ID = ?
        AND VALUE = ?;
    '''
    with closing(connect()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(string, (id, value))
        row = cursor.fetchone()
        print(row)
        return row
