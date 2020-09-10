from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=300)
    budget_price = models.IntegerField(null=True, blank=True)
    last_price = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=200)
    discount_price = models.CharField(max_length=100,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
