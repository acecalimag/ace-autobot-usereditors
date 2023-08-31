import mysql.connector
from robot.api import logger


class Database:
    """Closing the created connection will be the users' responsibility.
    Suggested usage is to create single instance during the initialization of a global library.
    Then pass the instance only to library components that needs db connection.
    """

    def __init__(self, host: str, user: str, password: str, port: str, database: str):
        self.__connection = None
        self.__host = host
        self.__user = user
        self.__password = password
        self.__port = port
        self.__database = database

    def execute(self, *args, **kwargs):
        self.__create_connection()

        cursor = self.__connection.cursor(dictionary=True)
        cursor.execute(*args, **kwargs)
        logger.info(f"Executed query: {cursor.statement}")
        result = cursor.fetchall()
        cursor.close()
        logger.trace(f"Query Result: {result}")
        return result

    def __create_connection(self):
        if self.__connection is None:
            logger.info("Creating a new connection.")
            self.__connection = mysql.connector.connect(host=self.__host, user=self.__user, password=self.__password,
                                           port=self.__port, database=self.__database)
            self.__connection.autocommit = True
        else:
            logger.info(f"Using an existing connection {str(self.__connection)}.")

    def close_connection(self):
        if self.__connection is not None:
            logger.info(f"Closing {str(self.__connection)}.")
            self.__connection.close()
            self.__connection = None
        else:
            logger.info(f"There is no open database connection to close.")

