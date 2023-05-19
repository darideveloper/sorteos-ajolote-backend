from django.db import models

class Lottery (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="nombre", help_text="Nombre del sorteo", unique=True)
    details = models.TextField(verbose_name="detalles", help_text="Detalles del sorteo", null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio total", help_text="Precio total del sorteo (el costo de los boletos será: precio total / cantidad de boletos)")
    image = models.ImageField (upload_to="lottery", verbose_name="imagen", help_text="Imagen del sorteo", null=True, blank=True)
    end_date = models.DateField (auto_now_add=True, verbose_name="fecha de cierre", help_text="Fecha de cierre del sorteo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación", help_text="Fecha de creación del sorteo", editable=False)
    numbers = models.IntegerField(verbose_name="cantidad de números", help_text="Cantidad de números que se pueden elegir en el sorteo")
    is_open = models.BooleanField(default=True, verbose_name="abierto", help_text="Indica si el sorteo está abierto")
    
    def __str__ (self):
        return self.name
    
    class Meta:
        verbose_name = "sorteo"
        verbose_name_plural = "sorteos"
        
class Ticket (models.Model):
    id = models.AutoField(primary_key=True)
    lottery = models.ForeignKey(Lottery, on_delete=models.CASCADE, verbose_name="sorteo", help_text="Sorteo al que pertenece el boleto")
    number = models.IntegerField(verbose_name="número", help_text="Número del boleto")
    buyer_name = models.CharField(max_length=200, verbose_name="dueño", help_text="Nombre del comprador del boleto")
    buyer_email = models.EmailField(verbose_name="correo electrónico", help_text="Correo electrónico del comprador del boleto")    
    buy_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de apartado", help_text="Fecha de apartado del boleto", editable=False)
    is_paid = models.BooleanField(default=False, verbose_name="pagado", help_text="Indica si el boleto ha sido pagado")
    active = models.BooleanField(default=True, verbose_name="activo", help_text="Indica si el boleto está activo")
    
    def __str__ (self):
        return f"{self.lottery.name} - {self.number} - {self.buyer_name}"
    
    class Meta:
        verbose_name = "boleto"
        verbose_name_plural = "boletos"
        unique_together = [['lottery', 'number']]