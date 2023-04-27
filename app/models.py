from django.db import models
from django.contrib.auth.models import User


class Type(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Receipt(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    
    name = models.CharField(max_length=30)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, default='Ужин')
    # в конечном итоге можно наследоваться от другой модели, у которой будут определенные значени, нпример: 30, 35, 40 и там далее минут
    cooking_time = models.CharField(max_length=30, default='30')
    # добавить user, котороый создал эту запись о блюде
    img = models.ImageField(upload_to='images/', default='images/1.jpg') # 
    instruction = models.TextField(default='Пока не добавлено')
    # may be ingridients

    def __str__(self):
        return self.name
    

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}.{self.receipt}'


class Purchased(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}.{self.receipt}'
    

class Subscription(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    subscribed_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')