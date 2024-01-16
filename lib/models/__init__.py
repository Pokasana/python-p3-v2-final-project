import sqlite3

CONN = sqlite3.connect('ledger.db')
CURSOR = CONN.cursor()
