import sqlite3
import pandas as pd

def get_connection():
    """Veritabanı bağlantısı oluşturur."""
    return sqlite3.connect('aquamind.db', check_same_thread=False)

def init_db():
    """
    Veritabanını ve tabloları başlatır. 
    Program ilk çalıştığında bir kez çağrılması yeterlidir.
    """
    conn = get_connection()
    c = conn.cursor()
    # Öğrenciler Tablosu: Kullanıcı adı, toplam harcanan su, bakiye ve verimlilik puanı
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (username TEXT PRIMARY KEY, 
                  total_water REAL DEFAULT 0, 
                  money INTEGER DEFAULT 100, 
                  efficiency_score INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()

def update_or_add_student(username, water, money, score):
    """
    Öğrenci verisini kaydeder. 
    Eğer öğrenci zaten varsa verilerini günceller (INSERT OR REPLACE).
    """
    conn = get_connection()
    c = conn.cursor()
    try:
        c.execute('''INSERT OR REPLACE INTO students (username, total_water, money, efficiency_score)
                     VALUES (?, ?, ?, ?)''', (username, water, money, score))
        conn.commit()
    except Exception as e:
        print(f"Veritabanı hatası: {e}")
    finally:
        conn.close()

def get_leaderboard():
    """
    Liderlik tablosunu getirir.
    En az su tüketen öğrenci en üstte görünecek şekilde sıralar (ASC).
    """
    conn = get_connection()
    # Pandas ile veriyi çekmek analiz yapmayı ve tablo oluşturmayı kolaylaştırır
    query = "SELECT username AS 'Öğrenci Adı', total_water AS 'Toplam Su (L)', money AS 'Bakiye (TL)' FROM students ORDER BY total_water ASC"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def get_all_data_for_admin():
    """
    Yönetici paneli için tüm ham veriyi getirir.
    """
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM students", conn)
    conn.close()
    return df

def clear_database():
    """
    (Opsiyonel) Test aşamasında verileri sıfırlamak istersen kullanılır.
    """
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM students")
    conn.commit()
    conn.close()
