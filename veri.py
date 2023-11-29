import sqlite3 as sql
def tablo_yarat():
    conn=sql.connect("veriler.db")
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS VERİLER(
    Kullanıcı_adı TEXT,
    Şifre TEXT
    )""")
    conn.commit()
    conn.close()
def tablo_sil():
    conn=sql.connect('veriler.db')
    cursor=conn.cursor()
    cursor.execute("""DROP TABLE IF EXISTS VERİLER""")
    conn.commit()
    conn.close()
def tabloya_veri_ekle(username,password):
    conn=sql.connect('veriler.db')
    cursor=conn.cursor()
    datas=[(username,password)]
    add_command="""INSERT INTO VERİLER VALUES (?,?)"""
    cursor.executemany(add_command,datas)
    conn.commit()
    conn.close()
def tablodan_veri_sil(username,password):
    conn=sql.connect('veriler.db')
    cursor=conn.cursor()
    datas=(username,password)
    delete_command="""DELETE from VERİLER WHERE '{}'"""
    cursor.execute(delete_command.format(datas))
    conn.commit()
    conn.close()
def tablo_veri_username_update(username_eski,username_yeni,password):
    conn = sql.connect('veriler.db')
    cursor = conn.cursor()
    datas=[(username_eski),(username_yeni),(password)]
    cursor.execute("""UPDATE VERİLER SET Kullanıcı_adı='{}' WHERE Kullanıcı_adı='{}' AND Şifre='{}'""".format(datas[0],datas[1],datas[2]))
    conn.commit()
    conn.close()
def tablo_veri_yazma_kullanici(a,b):
    conn=sql.connect('veriler.db')
    cursor=conn.cursor()
    cursor.execute("""SELECT Kullanıcı_adı from VERİLER WHERE Kullanıcı_adı='{}' AND Şifre='{}'""".format(a,b))
    list_all=cursor.fetchall()
    for yazi1 in list_all:
        return yazi1
    conn.commit()
    conn.close()
def tablo_veri_yazma_sifre(a,b):
    conn = sql.connect('veriler.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT Şifre from VERİLER WHERE Kullanıcı_adı='{}' AND Şifre='{}'""".format(a,b))
    list_all = cursor.fetchall()
    for yazi2 in list_all:
        return yazi2
    conn.commit()
    conn.close()