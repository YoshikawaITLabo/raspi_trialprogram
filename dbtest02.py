from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding as sym_padding
import os
import mysql.connector
import base64

#pip install cryptography

SALT = ""
KEY = ""

def dbconnect():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ghcrxw7k",
        db='webbackup',
        charset='utf8'       
    )
    return conn

def select_state(sql,params):
    #SELECT文の戻り値があるSQLの実行。パラメータ付きも可
    conn = dbconnect()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    result=cursor.fetchall()
    conn.close()
    
    return result

def non_select_state(sql,params):
    #INSERT DELETE UPDATEなど値が戻らないSQLの実行。パラメータ付きも可
    conn = dbconnect()
    cursor = conn.cursor()
    cursor.execute(sql,params)
    conn.commit()
    conn.close()

def Createtable():
    params=[]

    sql = "CREATE TABLE `hostlist02`"
    sql += "("
    sql += " `id` int(11) NOT NULL AUTO_INCREMENT"
    sql += ",`hostname` varchar(32) DEFAULT NULL"
    sql += ",`port` smallint(6) DEFAULT NULL"
    sql += ",`user` varchar(32) DEFAULT NULL"
    sql += ",`keysfolder` varchar(64) DEFAULT NULL"
    sql += ",`keyfile` varchar(64) DEFAULT NULL"
    sql += ",`passphrase` varchar(64) DEFAULT NULL"
    sql += ",`copy_source` varchar(64) DEFAULT NULL"
    sql += ",`Copy_to` varchar(64) DEFAULT NULL"
    sql += ",`Storage` varchar(64) DEFAULT NULL"
    sql += ",`created_at` timestamp NOT NULL DEFAULT current_timestamp()"
    sql += ",`updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()"
    sql += ",PRIMARY KEY (`id`)"
    sql += ")"
    sql += " ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;"
    
    non_select_state(sql,params)

def insertdata():
    
    params=[]
    sql = "INSERT INTO `hostlist02`"
    sql += "("
    sql += " `hostname`"
    sql += ",`port`"
    sql += ",`user`"
    sql += ",`keysfolder`"
    sql += ",`keyfile`"
    sql += ",`passphrase`"
    sql += ",`copy_source`"
    sql += ",`Copy_to`"
    sql += ",`Storage`"
    sql += ")"
    sql += " VALUES"
    sql += "("
    sql += "'yoshisyou.com'"
    sql += ",22"

    # 暗号化器を設定
    cipher1 = Cipher(algorithms.AES(KEY), modes.CBC(SALT), backend=default_backend())
    encryptor1 = cipher1.encryptor()
    padder1 = sym_padding.PKCS7(128).padder()
    data1 = b'ubuntu'
    padded_data1 = padder1.update(data1) + padder1.finalize()
    cipher_text1 = encryptor1.update(padded_data1) + encryptor1.finalize()
    sql += ",'" + base64.b64encode(cipher_text1).decode('utf-8') + "'"

    sql += ",'/home/kazuhiro/Documents/Key/'"
    sql += ",'id_ed25519'"

    cipher2 = Cipher(algorithms.AES(KEY), modes.CBC(SALT), backend=default_backend())
    encryptor2 = cipher2.encryptor()
    padder2 = sym_padding.PKCS7(128).padder()
    data2 = b'WIb_.7pxv1D08yhK'
    padded_data2 = padder2.update(data2) + padder2.finalize()
    cipher_text2 = encryptor2.update(padded_data2) + encryptor2.finalize()
    sql += ",'" + base64.b64encode(cipher_text2).decode('utf-8') + "'"
    
    sql += ",'/home/backup/'"
    sql += ",'/home/kazuhiro/Downloads/'"
    sql += ",'/mnt/rsp_nas/ras_backup/'"
    sql += ");"

    non_select_state(sql,params)

def selectdate():
    params=[]
    sql = "SELECT"
    sql += " `hostname`"
    sql += ",`port`"
    sql += ",`user`"
    sql += ",`keysfolder`"
    sql += ",`keyfile`"
    sql += ",`passphrase`"
    sql += ",`copy_source`"
    sql += ",`Copy_to`"
    sql += ",`Storage`"
    sql += " FROM"
    sql += " hostlist02"
    sql += ";"
    
    print(sql)
    result = select_state(sql,params)

    for item in result:
        TXT = item[0] + " : "
        TXT += str(item[1]) + " : "

        # Create a new cipher for each decryption
        cipher3 = Cipher(algorithms.AES(KEY), modes.CBC(SALT), backend=default_backend())
        decryptor1 = cipher3.decryptor()
        coltext1 = item[2]
        dccoltext1 = base64.b64decode(coltext1)
        decrypted_padded_data1 = decryptor1.update(dccoltext1) + decryptor1.finalize()
        unpadder1 = sym_padding.PKCS7(128).unpadder()
        decrypted_data1 = unpadder1.update(decrypted_padded_data1) + unpadder1.finalize()
        TXT += decrypted_data1.decode() + " : "

        TXT += item[3] + " : "
        TXT += item[4] + " : "

        # Create a new cipher for each decryption
        cipher4 = Cipher(algorithms.AES(KEY), modes.CBC(SALT), backend=default_backend())
        decryptor2 = cipher4.decryptor()
        coltext2 = item[5]
        dccoltext2 = base64.b64decode(coltext2)
        decrypted_padded_data2 = decryptor2.update(dccoltext2) + decryptor2.finalize()
        unpadder2 = sym_padding.PKCS7(128).unpadder()
        decrypted_data2 = unpadder2.update(decrypted_padded_data2) + unpadder2.finalize()
        TXT += decrypted_data2.decode() + " : "
        
        TXT += item[6] + " : "
        TXT += item[7] + " : "
        TXT += item[8] + " : "
        
        print(TXT)
    
def Droptable():
    params=[]
    sql = "DROP TABLE IF EXISTS `hostlist02`;"
    non_select_state(sql,params)

def main():

    #テキストファイルからソルトとキーを取り出す
    f = open('salt_key.txt', 'r', encoding='UTF-8')

    line = f.readline()
    global SALT
    SALT= base64.b64decode(line.replace('s:',''))
    line = f.readline()
    global KEY
    KEY= base64.b64decode(line.replace('k:',''))

    f.close()

    #テーブルを作成
    Createtable()

    #データ投入
    insertdata()
    
    #データを検索
    selectdate()
    
    #テーブルを削除
    Droptable()

if __name__ == "__main__":
    main()