import sqlite3

# DO NOT USE IS YET ... NOT DONE --- AXEL
# Fungsi untuk membuat koneksi ke database SQLite
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
        return None

# Fungsi untuk login pengguna
def login(conn, email, password):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = c.fetchone()
        if user:
            print(f"Selamat datang, {user[1]}!")
            print(f"ID Pengguna Anda: {user[4]}")
            return True
        else:
            print("Email atau password salah.")
            return False
    except sqlite3.Error as e:
        print("Error:", e)
        return False

# Contoh penggunaan
if __name__ == '__main__':
    database = r"User.sql"  # Nama file database SQLite

    # Buat koneksi ke database
    conn = create_connection(database)
    
    if conn is not None:
        # Contoh login
        email = input("Masukkan email: ")
        password = input("Masukkan password: ")
        login(conn, email, password)
        conn.close()
    else:
        print("Koneksi ke database gagal.")
