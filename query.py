from db_helper import DB_Helper


class Query:
    def __init__(self, data):
        self.data = data
        self.db_helper = DB_Helper()

    def tables(self):
        add_tables = ("INSERT INTO tables "
                      "(title) "
                      "VALUES (%s)")
        self.insert(add_tables)

    def community(self):
        add_community = ("INSERT INTO community "
                         "(community_title, url, g_id) "
                         "VALUES ((%s, %s, select last_insert_id() from table)")
        # g_id = "INSERT INTO tab_student (name_student, id_teacher_fk) VALUES ('rich man', LAST_INSERT_ID())"

        self.insert(add_community)

    def user(self):
        add_users = ("INSERT INTO users "
                     "(url) "
                     "VALUES (%s)")
        self.insert(add_users)

    def sub_community(self):
        add_sub_community = ("INSERT INTO sub_community "
                             "(community, title, url, text,u_id, c_id) "
                             "VALUES ( %s,%s, %s, %s, select last_insert_id(),"
                             " from user, select last_insert_id() from community)")
        self.insert(add_sub_community)

    def insert(self, add_query):
        self.db_helper.insert_into_table(add_query, self.data)

    def update(self, add_query):
        sql1 = "update post set date=%s"
        self.db_helper.updating_rows(add_query, self.data)


