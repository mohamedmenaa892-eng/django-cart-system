from django.contrib import admin
from . import models


class CartAdmin(admin.ModelAdmin):
    list_display = ('user','session_key','create_at')
    search_fields = ('user',)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart','product','quantity','create_at')
    search_fields = ('product',)

admin.site.register(models.Cart,CartAdmin)
admin.site.register(models.CartItem,CartItemAdmin)