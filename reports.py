from reportlab.pdfgen import canvas
from datetime import datetime

class ReportGenerator:
    def generate_sales_report(self, sales_data, filename):
        c = canvas.Canvas(filename)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 800, "تقرير المبيعات - مكتبة البر والتقوى")
        
        # إضافة تفاصيل التقرير
        c.save()
    
    def generate_inventory_report(self, inventory_data, filename):
        c = canvas.Canvas(filename)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 800, "تقرير المخزون - مكتبة البر والتقوى")
        
        # إضافة تفاصيل المخزون
        c.save()