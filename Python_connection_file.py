import sqlite3  # imporing sqlite module
from sqlite3 import Error  # importing error objects


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def create_table(conn, sql_statment):
    """ This function creates table 
        conn = connection object
        sql_statment = sql query being executed
        """
    try:
        c = conn.cursor()
        c.execute(sql_statment)

    except Error as e:
        print(e)


def insert_into_movies(conn, values):
    """ This function creates table 
        conn = connection object
        sql_statment = sql query being executed
        """

    try:
        sql = "INSERT INTO MOVIES(ID, NAME, L_ACTOR, L_ACTRESS, YoR, DIRECTOR) VALUES (?,?,?,?,?,?)"
        c = conn.cursor()
        c.execute(sql, values)
        conn.commit()
        return c.lastrowid

    except Error as e:
        print(e)


def read_all_movies(conn):
    """ This function creates table 
        conn = connection object
        """
    try:
        c = conn.cursor()
        c.execute("select * from Movies")
        rows = c.fetchall()
        for row in rows:
            print(row)

    except Error as e:
        print(e)


def main():


    DATABASE_NAME = "MoviesDB.db"
    CREATE_MOVIES_STATEMENT = ''' CREATE TABLE MOVIES(
                                    ID INT PRIMARY KEY NOT NULL, 
                                    NAME TEXT NOT NULL,
                                    L_ACTOR TEXT NOT NULL,
                                    L_ACTRESS TEXT NOT NULL,
                                    YoR INT(4) NOT NULL,
                                    DIRECTOR TEXT NOT NULL);
                                    '''
    VALUES1 = (1, 'AmericanPsycho', 'ChristianBale',
            'CaraSeymour', 2000, 'MaryHarron')
    VALUES2 = (2, 'Titanic', 'LeonardoDiCaprio',
            'KateWinslet', 1997, 'JamesCameron')
    VALUES3 = (3, 'Drive', 'RyanGosling', 'CareyMulligan',
            2011, 'NicolasWindingRefn')

    conn = create_connection(DATABASE_NAME)
    if conn:
        create_table(conn, CREATE_MOVIES_STATEMENT)

        r1 = insert_into_movies(conn, VALUES1)
        r2 = insert_into_movies(conn, VALUES2)
        r3 = insert_into_movies(conn, VALUES3)

        read_all_movies(conn)


    else:
        print('connetion error')


if __name__ == '__main__':
    main()
