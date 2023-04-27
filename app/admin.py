from django.contrib import admin

from app.models import Type, Receipt, Favorite, Purchased, Subscription

# Register your models here.


admin.site.register(Receipt)
admin.site.register(Type)
admin.site.register(Favorite)
admin.site.register(Purchased)
admin.site.register(Subscription)