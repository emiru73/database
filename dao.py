import pymysql.cursors

def connect():

# データベースに接続
    connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'pybase',
    cursorclass = pymysql.cursors.DictCursor,

)
    return connection

def find_all():

    with connect() as con:
        with con.cursor() as cursor:
            sql = 'SELECT * FROM ranking'
            cursor.execute(sql)
            # fetchall全て読み込む
            result = cursor.fetchall()
    return result

def insert_one(user):
    with connect() as con:
        with con.cursor() as cursor:
           sql = 'INSERT INTO ranking(name,score) VALUES(%s,%s)'
           cursor.execute(sql,(user['name'],user['score']))
        #    変更がある場合書く
        con.commit()
        