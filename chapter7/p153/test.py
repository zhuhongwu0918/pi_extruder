import sqlite3
from sqlite3 import Error
def charu(data):
    open_file=sqlite3.connect('./test.db') #创建数据库
    cur = open_file.cursor()
    # sql='CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)'#指定sql语句
    # cur.execute(sql)
    try:
        cur.execute('INSERT INTO test VALUES (?,?,?)',data)
    # cur.execute('INSERT INTO test VALUES(?,?,?)',(6,"zqg",20))
    # cur.executemany('INSERT INTO test VALUES(?,?,?)',[(3,'name',19),(4,'name',26)])
        open_file.commit()
    except Error as e:
        # print(str(e).split(' ')[0])
        if str(e).split(' ')[0] == 'UNIQUE':
            cur.execute("DELETE FROM test WHERE id="+str(data[0]))
            cur.execute('INSERT INTO test VALUES (?,?,?)',data)
            open_file.commit()
    finally:
        cur.close()
        open_file.close()
    if chaxun(str(data[0]))==data:
        return "ok"
def chaxun(id):
    open_file=sqlite3.connect('./test.db') #创建数据库
    cur = open_file.cursor()
    cur.execute('SELECT * FROM test WHERE id='+id)
    return_data =cur.fetchone()
    cur.close()
    open_file.close()
    return return_data
def shanchu(id):
    open_file=sqlite3.connect('./test.db') #创建数据库
    cur = open_file.cursor()
    try:
        cur.execute('DELETE FROM test WHERE id='+id)
        open_file.commit()
        cur.close()
        open_file.close()
    except Error as e:
        if str(e)[-1]=="range":
            cur.close()
            open_file.close()
            return "ok"
    if chaxun(id) == None:
        return "ok"
    else:
        return "fail"

print(charu((4,"ijo",22)))
print(chaxun("4"))
print(shanchu("4"))
data_insert=[1,"",1]
for i in range(1,100,1):
    data_insert[0]=i
    data_insert[1]=str(i)
    data_insert[2]=i
    # print(tuple(data_insert))
    print(charu(tuple(data_insert)))
    # print(i)