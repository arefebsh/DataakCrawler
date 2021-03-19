import pymysql
from test import DB_Helper


class Create_Table():

    def query_create(self):
        TABLES = {}

        TABLES['tables'] = (
            "CREATE TABLE `tables`("
            "  `g_id` int NOT NULL AUTO_INCREMENT,"
            "  `title` VARCHAR (50),"
            "PRIMARY KEY (`g_id`)"
            ")ENGINE=InnoDB")

        TABLES['community'] = (
            "CREATE TABLE `community`("
            "  `c_id` int NOT NULL AUTO_INCREMENT,"
            "  `community_title` VARCHAR (50),"
            "  `url` VARCHAR (255),"
            "  `g_id` int NOT NULL,"
            "  FOREIGN KEY (`g_id`) REFERENCES tables(`g_id`),"
            "PRIMARY KEY (`c_id`)"
            ")ENGINE=InnoDB")

        TABLES['users'] = (
            "CREATE TABLE `users`("
            "  `u_id` int NOT NULL AUTO_INCREMENT,"
            "  `url` VARCHAR (255),"
            "PRIMARY KEY (`u_id`)"
            ")ENGINE=InnoDB")

        TABLES['sub_community'] = (
            "CREATE TABLE `sub_community`("
            "  `s_id` int NOT NULL AUTO_INCREMENT,"
            "  `community` VARCHAR (50),"
            "  `title` VARCHAR (50),"
            "  `url` VARCHAR (255),"
            "  `text` VARCHAR (255),"
            "  `u_id` int,"
            "  FOREIGN KEY (`u_id`) REFERENCES users(`u_id`),"
            "  `c_id` int,"
            "  FOREIGN KEY (`c_id`) REFERENCES community(`c_id`),"
            "PRIMARY KEY (`s_id`)"
            ")ENGINE=InnoDB")

        result = DB_Helper()
        result.create_table(TABLES)


re = Create_Table()
re.query_create()


