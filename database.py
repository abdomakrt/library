import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('bookstore.db')
        self.cur = self.conn.cursor()
    
    def add_book(self, barcode, title, author, price, quantity):
        self.cur.execute('''
            INSERT INTO books (barcode, title, author, price, quantity)
            VALUES (?, ?, ?, ?, ?)
        ''', (barcode, title, author, price, quantity))
        self.conn.commit()
    
    def update_quantity(self, barcode, quantity):
        self.cur.execute('''
            UPDATE books SET quantity = quantity + ?
            WHERE barcode = ?
        ''', (quantity, barcode))
        self.conn.commit()
    
    def record_sale(self, book_id, quantity, total_price):
        self.cur.execute('''
            INSERT INTO sales (book_id, quantity, total_price, date)
            VALUES (?, ?, ?, datetime('now'))
        ''', (book_id, quantity, total_price))
        self.conn.commit()