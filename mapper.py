import pymysql
from main import*

class sqlMapper:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "123"
        self.db = "test"
        self.connection = pymysql.connect(host=self.host,
                             user=self.user,
                             password=self.password,
                             db=self.db)

        self.cursor = self.connection.cursor()
        
    def insert_locations(self):
        sql_location_insert = "INSERT INTO `test`.`covid_nz_locations`\
                        (`id`,\
                        `locations`,\
                        `address`,\
                        `day`,\
                        `time`,\
                        `location_update`)\
                        VALUES (%s,%s,%s,%s,%s,%s);"
        value = statementData()
        locations_list = value.get_locations()

        for lo in locations_list:
            if self.check_id_unique(lo[0]):
                self.cursor.execute(sql_location_insert, lo)
        self.connection.commit()
            

    def check_id_unique(self, curr_id):
        sql = "SELECT id FROM test.covid_nz_locations WHERE id = %s"

        self.cursor.execute(sql, curr_id)
        
        result = self.cursor.fetchall()

        if len(result) == 0:
            return True
        else:
            return False

    def get_locations(self):
        sql = "SELECT* FROM test.covid_nz_locations"

        self.cursor.execute(sql)

        result = self.cursor.fetchall()

        return result

    def close_connection(self):
        self.connection.close()

