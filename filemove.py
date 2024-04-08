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
    sql += " FROM"
    sql += "`templist`"
    sql += " ORDER BY"
    sql += " CreationDate"
    sql += ";"
    print(sql)

    #SQL実行
    cursor.execute(sql)

    result=cursor.fetchall()

    for item in result:
        sendfn = '/home/kazuhiro/Downloads/'
        recefn = '/mnt/rsp_nas/ras_backup'

        sendfn += item[0]
        #recefn += item[0]
        
        print(sendfn)
        print(recefn)

        shutil.copy2(sendfn, recefn)

        os.remove(sendfn)
    
if __name__ == "__main__":
    main()