import mysql.connector

def dacquisition(sql):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ghcrxw7k",
        db='webbackup',
        charset='utf8'
    )
    # カーソルを取得
    cursor = conn.cursor()
    cursor.execute(sql)
    result=cursor.fetchall()

    return result

def main():
    # MySQLに接続

    #SQL
    sql = "SELECT"
    sql += " `id`"
    sql += ",`hostname`"
    sql += ",`port`"
    sql += ",`user`"
    sql += ",`keysfolder`"
    sql += ",`keyfile`"
    sql += ",`passphrase`"
    sql += ",`copy_source`"
    sql += ",`Copy_to`"
    sql += ",`Storage`"
    sql += ",`created_at`"
    sql += ",`updated_at`"
    sql += " FROM"
    sql += " `hostlist`;"
    print (sql)
    result = dacquisition(sql)

    for item in result:
        print(item[0])

if __name__ == "__main__":
    main()