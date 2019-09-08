import sqlite3


def conn_sqlite():
    return "sqlite:///C:\\Users\\Boca_\\OneDrive\\Impacta\\Faculdade\\Semestre5\\WorkSpacePython\\Desenvolvimento_de_Sistemas_de_Informa-o\\database.db"


def generic_response(status, message, data):
    return {"Status": status, "Message": message, "Data": data}
