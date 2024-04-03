import mysql.connector
import shutil
import os

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

    #SQL組み立て
    sql = "SELECT "
    sql += " `FileName`"
    sql += ",`FileSize`"
    sql += ",`CreationDate`"
    sql += ",`ProcessedDate`"
    sql += " FROM"
    sql += "`templist`"
    sql += ";"

    #SQL実行
    cursor.execute(sql)

    result=cursor.fetchall()

    for item in result:
        fn = '/home/kazuhiro/Downloads/'
        fn += item[0]
        shutil.copy2(fn, "/mnt/rasp_nas/ras_backup/")

        os.remove(fn)
        print(fn)

    
if __name__ == "__main__":
    main()