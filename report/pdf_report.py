from django.http import HttpResponse
from .report_generator import ReportGenerator
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from order.models import Order
from django.shortcuts import get_object_or_404


class PdfOrden(ReportGenerator):
    def generate_report(self, data):

        order = get_object_or_404(Order, order_id=data)

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
        #contenido.append(f'Productos: {order.products}')
        

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
        doc.build([tabla_contenido])


        return response