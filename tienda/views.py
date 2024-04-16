from django.http import HttpResponse

from tienda import admin

class ProductoAdmin(admin.ModelAdmin):
    # Otras configuraciones del admin...

    def set_stock_to_value_view(self, request):
        stock_value = request.GET.get('stock_value')
        if stock_value:
            # Lógica para establecer el stock aquí
            return HttpResponse('Stock value updated successfully')
        else:
            return HttpResponse('No stock value provided')

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        if request.path.endswith('/set_stock_to_twenty/'):  # Corregir la URL aquí
            return self.set_stock_to_value_view(request)
        return response


