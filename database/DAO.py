from database.DB_connect import DBConnect
from model.aeroporto import Aeroporto
from model.tratta import Tratta


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllAeroporti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "select ID, AIRPORT from airports"

        cursor.execute(query)

        for row in cursor:
            result.append(
                Aeroporto(row["ID"], row["AIRPORT"]))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getAllTratte(distanza_minima):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID, AVG(DISTANCE) as AVG
                   from extflightdelays.flights where DISTANCE>%s group by ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID"""

        cursor.execute(query, (distanza_minima,))

        for row in cursor:
            result.append(
                Tratta(row["ORIGIN_AIRPORT_ID"], row["DESTINATION_AIRPORT_ID"], row["AVG"]))

        cursor.close()
        conn.close()
        return result
