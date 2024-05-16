import csv
from django.http import HttpResponse
from .report_generator import ReportGenerator
from product.models import Product


class CsvInv(ReportGenerator):
    def generate_report(self, data):
        
        products = Product.objects.all()

        columns = ['ID', 'Name', 'Price', 'Description', 'Brand', 'Category', 'Created_at']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products.csv"'

        csv_writer = csv.writer(response)

        csv_writer.writerow(columns)

        if data == 1:
            
            for product in products:
                row = [product.product_id, product.name, product.price, product.description, product.brand, product.category, product.created_at]
                csv_writer.writerow(row)

            return response
        else:
            i = 0
            for producs in products:
                if i <= data:
                    row = [product.product_id, product.name, product.price, product.description, product.brand, product.category, product.created_at]
                    csv_writer.writerow(row)
                i = i + 1
