from django.db import models

# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    iva = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ["descripcion"]

    def __str__(self):
        return self.descripcion

class Cliente(models.Model):
    ruc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=300)
    direccion = models.TextField(blank=True, null=True)
    producto = models.ManyToManyField(Producto)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ["-nombre"]

    def __str__(self):
        return str(self.nombre)

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    fecha = models.DateField()
    total = models.FloatField(default=0)

class DetalleFactura(models.Model):
    factura=models.ForeignKey(Factura, on_delete= models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete= models.CASCADE)
    cantidad = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    subtotal = models.FloatField(default=0)
#Ingresar
#Modelo Producto
#P = Producto(descripcion='Aceite Girazol',precio=1.50,stock=2000)
#P.save()
#Producto.objects.create(descripcion='Coca Cola',precio=0.90,stock=10000)

#Modelo Cliente
#C = Cliente(ruc='0967456789001',nombre='Emily Anahi',direccion='Av. Juan Montalvo')
#C.save()
#C.producto.add(1)
#C2 = Cliente(ruc='0987654321001',nombre='Pedro Almeida',direccion='Pedro Carbo y Amazonas')
#C2.save()
#C2.producto.add(2)
#Cliente.objects.create(ruc='0987656788001',nombre='Vicente Mendoza',direccion='Los Helechos')
#C3 = Cliente.objects.get(id=3)
#C3.producto.add(1)

#Modelo Factura
#F = Factura(cliente=C,fecha='2019-04-27',total=15.80)
#F.save()
#F = Factura(cliente=C2,fecha='2020-03-22',total=35.90)
#F.save()
#F2 = Factura(cliente=C,fecha='2019-06-23',total=25.80)
#F2.save()
#Factura.objects.create(cliente=C2,fecha='2020-06-25',total=5.80)

#Modelo Detallefactura

#DT = DetalleFactura(factura=F,producto=P,cantidad=3,precio=11.97,subtotal=20)
#DT.save()
#DetalleFactura.objects.create(factura=F2,producto=P2,cantidad=2,precio=2.90,subtotal=5.8)

#Modificar
#Modelo Producto
#p = Producto.objects.get(id=1)
#p.precio=1.13
#p.save()
#Producto.objects.filter(id=1).update(precio=1.7)

#Modelo Cliente
#cli = Cliente.objects.get(id=1)
#cli.nombre = 'Anahi Yuxan'
#cli.save()
#Cliente.objects.filter(id=2).update(nombre='Juan Moran')


#Modulo Factura

#factu = Factura.objects.get(id=1)
#factu.total=23.90
#factu.save()
#Factura.objects.filter(id=2).update(total=55.88)


#Modulo factura
#detfac = DetalleFactura.objects.get(id=1)
#detfac.cantidad=1
#detfac.save()
#DetalleFactura.objects.filter(id=2).update(cantidad=2)

#Eliminar

#Modelo Producto
#ep = Producto.objects.get(id=1)
#ep.delete()
#Producto.objects.filter(id=2).delete()

# Modelo Cliente
#ec = Cliente.objects.get(id=1)
#ec.delete()
#Cliente.objects.filter(id=2).delete()

#Modelo Factura
#ef = Factura.objects.get(id=1)
#ef.delete()
#Factura.objects.filter(id=2).delete()


#Modelo DetalleFactura
#edp=DetalleFactura.objects.get(id=1)
#edp.delete()
#DetalleFactura.objects.filter(id=2).delete()

#Query de un Modelo
#DetalleFactura.objects.create(factura=F2,producto=Producto.objects.get(id=4),cantidad=2,precio=2.90,subtotal=5.8)
#p= Producto.objects.get(id=3)
#Producto.objects.filter(id__lte=3)
#Producto.objects.exclude(descripcion__icontains='Cola')
#Producto.objects.filter(id__gte=4)
#Producto.objects.filter(id__gte=4).values('id','descripcion')
#Producto.objects.filter(descripcion='Coca Cola').values('id','descripcion')

#Query de varios modelos relacionados
#DetalleFactura.objects.create(factura=F2,producto=Producto.objects.get(id=4),cantidad=2,precio=2.90,subtotal=5.8)
#p= Producto.objects.get(id=3)
#Producto.objects.filter(id__lte=3)
#Producto.objects.exclude(descripcion__icontains='Cola')
#Producto.objects.filter(id__gte=4)
#Producto.objects.filter(id__gte=4).values('id','descripcion')
#Producto.objects.filter(descripcion='Coca Cola').values('id','descripcion')
#Factura.objects.filter(cliente__nombre='Emily Anahi')
#c= Cliente.objects.get(nombre='Emily Anahi')
#c.factura_set.all()
#c.factura_set.filter(id=5)
#Factura.objects.select_related('cliente').filter(cliente__nombre='Emily Anahi')
#Cliente.objects.prefetch_related('producto').filter(nombre='Emily Anahi').values('nombre','producto__descripcion')
