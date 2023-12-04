import mysql.connector

class Connectserver:

    def __init__(object, host: str, user: str, password: str, port: str | None=None):

        if port is not None:
            object.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                port=port
            )
        else:
            object.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password
            )
        object._cursor = object.connection.cursor()

    def select(object, database: str, table: str, columns: list, condition: str | None=None):

        cursor = object._cursor
        columns = ", ".join(columns)
        if condition is not None:
            cursor.execute(f"SELECT {columns} FROM {database}.{table} WHERE ({condition})")
        else:
            cursor.execute(f"SELECT {columns} FROM {database}.{table}")
        return cursor.fetchall()
    
    def insert(object, database: str, table: str, columns: list, row: tuple):

        cursor = object._cursor
        columns = ", ".join(columns)

        try:
            cursor.execute(f"INSERT INTO {database}.{table} ({columns}) VALUES {row}")
            object.connection.commit()
            return [True]
        except Exception as error:
            return [False, error]
        
    def delete(object, database: str, table: str, condition: str):

        cursor = object._cursor
        try:
            cursor.execute(f"DELETE FROM {database}.{table} WHERE ({condition})")
            return [True]
        except Exception as error:
            return[False, error]
        
    def update(object, database: str, table: str, columns: list, values: list, condition: str):

        if len(columns) != len(values):
            return [False, 'O número de colunas a serem atualizadas deve ser igual ao número de novos valores.']
        else:

            try:
                cursor = object._cursor
                for index in range(len(columns)):
                    if isinstance(values[index], int):
                        cursor.execute(f"UPDATE {database}.{table} SET {columns[index]} = {values[index]} WHERE ({condition})")
                    else:
                        cursor.execute(f"UPDATE {database}.{table} SET {columns[index]} = '{values[index]}' WHERE ({condition})")
                object.connection.commit()
                return [True]
            except Exception as error:
                return [False, error]
            

if __name__ == "__main__":
    get_connection = Connectserver('localhost', 'root', '', '3306')
    connection = get_connection.connection
    cursor = get_connection._cursor