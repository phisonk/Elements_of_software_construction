import sqlite3

def return_zero():
    return 0
def login():
    user_in = input('Username: ')
    passw_in = input('Password: ')
def verify(user,passw):
    cursor.execute('SELECT * FROM `member` WHERE `username` = ? AND `password` = ?',(user,passw))

    if cursor.fetchone() is None:
        print('False')
        return 0
    else:
        print('True')
        return 1

def database():
    global conn, cursor
    conn = sqlite3.connect('usphison.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member`(mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT,username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin')")
        conn.commit()

def gg():
    cursor.execute("INSERT INTO 'member' (username,password) VALUES('phison','gg')")
    for row in cursor.execute('SELECT * FROM member'):
        print(row)

database()
gg()
