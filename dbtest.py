import mysql.connector

def main():
    # MySQLに接続
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ghcrxw7k",
        db='webbackup',
        charset='utf8'
    )
    # カーソルを取得
    cursor = conn.cursor()

    #SQL
    sql = "SELECT `serial`,`hostname`,`port`,`user`,`passphrase`,`keysfolder`,`keysfile`,`sourcefolder`,`destinationfolder`,`ProcessedDate` FROM `hostlist`;"

    cursor.execute(sql)

    result=cursor.fetchall()

    for item in result:
        print(item[0])

if __name__ == "__main__":
    main()