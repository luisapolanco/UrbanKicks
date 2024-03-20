from django.http import HttpResponse
from django.shortcuts import render
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from .models import Order
from user.models import Customer, User
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect, get_object_or_404
# Create your views here.

class OrderCreate(View):
    def get(self,request, *args, **kwargs):
        user = request.user
        customer = get_object_or_404(Customer, user = user) 

        Order.objects.create()
        return redirect('order_detail')
    
    def generate_pdf(request, order_id):
        # Obtén la order desde la base de datos
        order = get_object_or_404(Order, order_id=order_id)

        # Creamos el objeto HttpResponse con el encabezado de PDF apropiado.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="order_{order.order_id}.pdf"'

        # Creamos el documento PDF, utilizando la respuesta como archivo.
        doc = SimpleDocTemplate(response, pagesize=letter)

        # Construimos el contenido de la order
        contenido = []
        contenido.append(f'Número de order: {order.order_id}')
        contenido.append(f'Fecha de Emisión: {order.date_created}')
        contenido.append(f'Cliente: {order.customer.user.username}')
        contenido.append(f'Detalles: {order.status}')
        

        # Creamos una tabla para la order
        tabla_contenido = Table([contenido])

        # Aplicamos estilos a la tabla
        estilo_tabla = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)])

        tabla_contenido.setStyle(estilo_tabla)

        # Adjuntamos la tabla al documento
        contenido.append(tabla_contenido)

        # Construimos el PDF
        doc.build(contenido)
        return response