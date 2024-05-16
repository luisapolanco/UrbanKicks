from .models import Order
from user.models import Customer
from django.views import View
from django.shortcuts import get_object_or_404
from report.pdf_report import PdfOrden
# Create your views here.

class OrderCreateView(View):
    def get(self,request, *args, **kwargs):
        user = request.user
        customer = get_object_or_404(Customer, user = user) 
        status = "active"
        products = user.old_cart
        
        order=Order.objects.create(customer = customer, status = status, products = products)
        #ReportGenerator.generate_report(order.order_id)
        generator = PdfOrden()
        pdf = generator.generate_report(order.order_id)

        return pdf#self.generate_pdf(order.order_id)