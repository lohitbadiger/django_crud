from django.db import models

# Create your models here.
class AllInfo(models.Model):
    name=models.CharField(max_length=12)
    work=models.CharField(max_length=15)
    experience=models.IntegerField()
    total_salery=models.DecimalField(max_digits=10,decimal_places=2)
    email=models.EmailField()
    
    class Meta:
       
        verbose_name = 'Details'
        verbose_name_plural = 'All Informations'
    
    def __str__(self):
        return self.name 
    
       