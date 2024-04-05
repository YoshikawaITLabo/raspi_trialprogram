import paramiko
paramiko.util.log_to_file('paramiko.log', level='DEBUG')


HOSTNAME = "yoshisyou.com"
PORT = 22
USER = "ubuntu"
PRIVATE_KEY = "/home/kazuhiro/Documents/Key/id_ed25519"
PASSPHRASE = "WIb_.7pxv1D08yhK"
cnx = None

def main():
    #取得したホストに接続する
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    allow_agent=False
    # 秘密鍵を読み込む
    #private_key = paramiko.Ed25519Key(filename=PRIVATE_KEY, password=PASSPHRASE)
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