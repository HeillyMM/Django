from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        db_table = 'tbl_categoria'

    def __str__(self):
        return self.nombre