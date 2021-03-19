import pymysql


class DB_Helper:

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "dataak"

    def __connect__(self):

        try:
            self.con = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                       cursorclass=pymysql.cursors.DictCursor)
            self.cur = self.con.cursor()

        except pymysql.Error as e:
            print(e.args[0], e.args[1])
            print("Error while connecting to MySQL", e)

    def __disconnect__(self):
        self.con.close()

    def __commit__(self):
        self.con.commit()

    def __rollback__(self):
        self.con.rollback()

    def fetch(self, sql):
        try:
            self.__connect__()
            self.cur.execute(sql)
            result = self.cur.fetchall()
            self.__disconnect__()
        except:
            self.__rollback__()
        return result

    def execute(self, sql):
        try:
            self.__connect__()
            self.cur.execute(sql)
            # self.__disconnect__()
        except pymysql.DatabaseError:
            self.__rollback__()

    def execute_bulk(self, sql, data):
        try:
            self.cur.executemany(sql, data)
        except pymysql.DatabaseError:
            self.__rollback__()

    def show_table(self):
        self.__connect__()
        self.cur.execute("SELECT Table_name as TablesName from information_schema.tables "
                         "where table_schema ='dataak';")
        result = self.cur.fetchall()
        return result

    def create_table(self, create_list):

        for table_name in create_list:
            table_description = create_list[table_name]
            try:
                print("Creating table {}:".format(table_name), end='')
                self.execute("ALTER TABLE table_name CONVERT TO CHARACTER SET utf8 COLLATE utf8_persian_ci;")
                self.execute(table_description)
            except pymysql.err.InternalError:
                print(table_name + " " + 'already exist')
            self.__commit__()
            self.__disconnect__()

    def insert_into_table(self, add_tables, data):
        try:
            self.__connect__()
            self.execute_bulk(add_tables, data)
        except pymysql.err.InternalError as err:
            return err

    def updating_rows(self, sql, data):
        try:
            self.execute_bulk(sql, data)
        except pymysql.err.InternalError as err:
            return err
