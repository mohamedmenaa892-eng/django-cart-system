from django.db import models
from django.conf import settings
from stor.models import Product

# CREATE MODEL CART 
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    session_key = models.CharField(max_length=30,null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-create_at']
    
    @property
    def total_price(self):
        return sum(item.total_price for item in self.cartitem_set.all())


# CREATE MODEL CARTITEM 
class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-create_at']
        constraints = [
            models.UniqueConstraint(
            fields=['cart','product'],
            name="unique_cart_product"
        )]
    
    @property
    def total_price(self):
        return self.product.price * self.quantity