import sqlite3


class Database():
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.c = self.conn.cursor()

    def data_type_transform(self, arg):
        output = ""
        if type(arg) is str:
            output = output+"'"+str(arg)+"', "
        elif type(arg) is int or float:
            output = output+str(arg)+", "
        return output

    def create_table(self, database_name_QaZwSx, **kwargs):
        # weird name of argument is to reduce chance of using this variable

        output = ""
        for arg in kwargs:
            output = output + str(arg)
        output = output[0:len(output)-2]

        syntax = """CREATE TABLE IF NOT EXISTS {} (
            {}
        )""".format(database_name_QaZwSx, output)

        self.c.execute(syntax)
        self.conn.commit()

    def insert(self, table_name_QaZwSx, *args):
        output = ""

        for arg in args:
            output = output + self.data_type_transform(arg)
        output = output[0:len(output)-2]

        syntax = "INSERT INTO {} VALUES ({})".format(table_name_QaZwSx, output)
        self.c.execute(syntax)
        self.conn.commit()

    def insert_into(self, table_name_QaZwSx, *args):
        output = ""

        for arg in args:
            output = output + self.data_type_transform(arg)
        output = output[0:len(output)-2]

        syntax = "INSERT INTO {} VALUES ({})".format(table_name_QaZwSx, output)
        self.c.execute(syntax)
        self.conn.commit()

    def print_table(self, table_name):
        syntax = """SELECT * FROM {}""".format(table_name)
        self.c.execute(syntax)
        print(self.c.fetchall())

    def print_table_all(self, table_name):
        syntax = """SELECT * FROM {}""".format(table_name)
        self.c.execute(syntax)
        print(self.c.fetchall())

    def print_table_one(self, table_name):
        syntax = """SELECT * FROM {}""".format(table_name)
        self.c.execute(syntax)
        print(self.c.fetchone())

    def print_table_many(self, table_name, size):
        syntax = """SELECT * FROM {}""".format(table_name)
        self.c.execute(syntax)
        print(self.c.fetchmany(int(size)))
