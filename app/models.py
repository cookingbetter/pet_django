from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    name = models.CharField(max_length=30, default='123')
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, default='ужин')
    # в конечном итоге можно наследоваться от другой модели, у которой будут определенные значени, нпример: 30, 35, 40 и там далее минут
    cooking_time = models.CharField(max_length=30, default='123')
    # добавить user, котороый создал эту запись о блюде
    img = models.ImageField(upload_to='images/', default='images/1.jpg') # 
    # add instruction
    #instruction = 
    # may be ingridients

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Posts'

# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_posted = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

