import pyodbc

class Connection():
    '''connection to db via pyodbc'''

    con_str = (
        'DRIVER={PostgreSQL ODBC Driver(UNICODE)};'
        'Server=localhost;'
        'Port=5432;'
        'Database=test;'
        'Uid=user;'
        'Pwd=user;'
    )

    cnxn = None

    def __init__(self):
        self.cnxn = pyodbc.connect(self.con_str)
        self.cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
        self.cnxn.setencoding(encoding='utf-8')

    def add(self, item, value):
        cursor = self.cnxn.cursor()
        cursor.execute("insert into items(name, value) values (?, ?)",
        item, int(value))
        self.cnxn.commit()



#cursor.execute('insert into test values (\'memes\')')
#cnxn.commit();

#cursor.execute('select * from test')
#print(cursor.fetchone())
