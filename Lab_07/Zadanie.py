import sqlite3
# Tworzenie połączenia z bazą danych – gdy nie ma – tworzy nowy plik.
conn = sqlite3.connect('studenci.db')

# Stworzenie tabeli:
create_table_query = '''CREATE TABLE IF NOT EXISTS books (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 title TEXT,
 author TEXT,
 price REAL,
 category TEXT
 )'''
conn.execute(create_table_query)