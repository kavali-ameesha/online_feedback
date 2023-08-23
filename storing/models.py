from django.db  import models

class storingmodel(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.PositiveBigIntegerField()
    desc=models.TextField(max_length=500)
