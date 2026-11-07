from django.db import models

# Create your models here.

class marca (models.Model):
    nombre = models.CharField(max_length=50)
    pais_origen = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre}'

class moto(models.Model): 
    nombre = models.CharField(max_length=50)
    marca = models.ForeignKey (
        marca, 
        on_delete= models.CASCADE,
        related_name="motos",
         null= True,
         blank=True,
     )
    cilindraje = models.IntegerField ()
    potencia = models.CharField(max_length=50)
    velocidad_maxima = models.CharField(max_length=50)
    precio = models.DecimalField (
    )
    
    def __str__(self):
        return f'{self.nombre}-{self.marca}-{self.cilindraje}-{self.potencia}-{self.velocidad_maxima}-{self.precio}'


class resena (models.Model):
    moto = models.ForeignKey (
        moto, 
        on_delete= models.CASCADE,
        related_name="resenas",
        null= True,
        blank=True,
    )
 
    autor = models.CharField(max_length=20)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)


    def __str__(self):
            return f'{self.moto}-{self.autor}-{self.comentario}-{self.fecha}-'
