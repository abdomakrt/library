import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime
import barcode
from barcode.writer import ImageWriter
from reportlab.pdfgen import canvas

class BookstoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("مكتبة البر والتقوى - نظام إدارة المبيعات")
        self.root.geometry("1200x700")
        
        # إنشاء قاعدة البيانات
        self.create_database()
        
        # إنشاء واجهة المستخدم
        self.create_gui()
    
    def create_database(self):
        self.conn = sqlite3.connect('bookstore.db')
        self.cur = self.conn.cursor()
        
        # إنشاء جداول قاعدة البيانات
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                barcode TEXT UNIQUE,
                title TEXT,
                author TEXT,
                price REAL,
                quantity INTEGER
            )
        ''')
        
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY,
                book_id INTEGER,
                quantity INTEGER,
                total_price REAL,
                date TEXT,
                FOREIGN KEY (book_id) REFERENCES books (id)
            )
        ''')
        
        self.conn.commit()
    
    def create_gui(self):
        # إنشاء التبويبات
        self.notebook = ttk.Notebook(self.root)
        
        # تبويب المبيعات
        self.sales_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.sales_frame, text="المبيعات")
        
        # تبويب المخزون
        self.inventory_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.inventory_frame, text="المخزون")
        
        # تبويب التقارير
        self.reports_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.reports_frame, text="التقارير")
        
        self.notebook.pack(expand=True, fill="both")
        
        # إضافة عناصر واجهة المستخدم
        self.setup_sales_tab()
        self.setup_inventory_tab()
        self.setup_reports_tab()
    
    def setup_sales_tab(self):
        # إضافة حقل إدخال الباركود
        tk.Label(self.sales_frame, text="الباركود:").grid(row=0, column=0, padx=5, pady=5)
        self.barcode_entry = tk.Entry(self.sales_frame)
        self.barcode_entry.grid(row=0, column=1, padx=5, pady=5)
        self.barcode_entry.bind('<Return>', self.scan_barcode)
    
    def setup_inventory_tab(self):
        # إضافة جدول المخزون
        columns = ('الباركود', 'العنوان', 'المؤلف', 'السعر', 'الكمية')
        self.inventory_tree = ttk.Treeview(self.inventory_frame, columns=columns, show='headings')
        
        for col in columns:
            self.inventory_tree.heading(col, text=col)
        
        self.inventory_tree.pack(expand=True, fill="both")
    
    def setup_reports_tab(self):
        # أزرار التقارير
        tk.Button(self.reports_frame, text="تقرير المبيعات اليومية", 
                 command=self.daily_sales_report).pack(pady=5)
        tk.Button(self.reports_frame, text="تقرير المخزون", 
                 command=self.inventory_report).pack(pady=5)
    
    def scan_barcode(self, event=None):
        barcode = self.barcode_entry.get()
        # البحث عن الكتاب في قاعدة البيانات
        self.cur.execute("SELECT * FROM books WHERE barcode=?", (barcode,))
        book = self.cur.fetchone()
        if book:
            # عرض معلومات الكتاب وإضافته إلى السلة
            pass
        else:
            tk.messagebox.showerror("خطأ", "الكتاب غير موجود في قاعدة البيانات")
    
    def daily_sales_report(self):
        # إنشاء تقرير المبيعات اليومية
        pass
    
    def inventory_report(self):
        # إنشاء تقرير المخزون
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = BookstoreApp(root)
    root.mainloop()