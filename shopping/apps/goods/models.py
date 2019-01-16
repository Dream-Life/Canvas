from django.db import models

# Create your models here.

class GoodsCategory(models.Model):
    """
    商品类别
    """
    name = models.CharField()
    code = models.CharField()
    desc = models.CharField()
    categroy_type = models.CharField()