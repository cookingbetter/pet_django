from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Receipt(models.Model):
    name = models.CharField(max_length=30)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, default='Ужин')
    # в конечном итоге можно наследоваться от другой модели, у которой будут определенные значени, нпример: 30, 35, 40 и там далее минут
    cooking_time = models.CharField(max_length=30, default='30')
    # добавить user, котороый создал эту запись о блюде
    img = models.ImageField(upload_to='images/', default='images/1.jpg') # 
    instruction = models.TextField(default='Пока не добавлено')
    # may be ingridients
    favorite = models.BooleanField(default=False)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Receipts'

