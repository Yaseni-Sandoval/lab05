from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Categoria, Producto, Cliente


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'Categoria', 'precio', 'stock', 'pub_date')  
    change_list_template = 'admin/producto_change_list.html'  

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('set_stock_to_twenty/', self.set_stock_to_twenty_view, name='tienda_producto_set_stock_to_twenty_view'),
            path('update_stock/', self.update_stock_view, name='tienda_producto_update_stock_view'),
        ]
        return my_urls + urls

    def set_stock_to_twenty_view(self, request):

        productos = Producto.objects.all()
        for producto in productos:
            producto.stock = 20
            producto.save()
        
        self.message_user(request, 'El stock de todos los productos ha sido actualizado.')
        return HttpResponseRedirect(reverse('admin:tienda_producto_changelist'))

    def update_stock_view(self, request):
        if request.method == 'POST':
            new_stock = request.POST.get('new_stock')
            if new_stock:

                Producto.objects.all().update(stock=new_stock)
                self.message_user(request, f'El stock de todos los productos ha sido actualizado a {new_stock} unidades.')
                return HttpResponseRedirect(reverse('admin:tienda_producto_changelist'))
        

        return render(request, 'admin/update_stock_form.html')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pub_date')  


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'dni', 'telefono', 'direccion', 'email', 'fecha_nacimiento', 'pub_date')  

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClienteAdmin)
