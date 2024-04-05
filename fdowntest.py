import mysql.connector
import paramiko

HOSTNAME = None
PORT = None
USER = None
PRIVATE_KEY = None
PASSPHRASE = None
cnx = None

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

    #取得するホストの情報をデータベースから取得
    sql = "SELECT `hostname`,`port`,`user`,`keysfolder`,`keyfile`,`passphrase` FROM `hostlist`;"
    cursor.execute(sql)

    result=cursor.fetchall()

    for item in result:
        HOSTNAME = item[0]
        PORT = item[1]
        USER = item[2]
        PRIVATE_KEY = item[3] + item[4]
        PASSPHRASE = item[5]

    #取得したホストに接続する
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 秘密鍵を読み込む
    private_key = paramiko.Ed25519Key(filename=PRIVATE_KEY, password=PASSPHRASE)

    # ホスト名を使用して接続
    client.connect(HOSTNAME, port=PORT, username=USER, pkey=private_key)

    sftp_connection = client.open_sftp()
    sftp_connection.chdir("/home/backup/")

        #ファイルを取得する
    #取得するホストの情報をデータベースから取得
    sql = "SELECT `FileName` FROM `templist`;"
    cursor.execute(sql)

    result=cursor.fetchall()

    for item in result:
        FILENAME = item[0]
        sftp_connection.get('/home/backup/' + FILENAME, FILENAME)

if __name__ == "__main__":
    main()