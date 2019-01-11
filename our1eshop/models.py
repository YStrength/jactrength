from django.db import models


# Create your models here.
class EshopCommodityInfo(models.Model):
    # 商品编号
    # 描述信息
    # 商品种类
    # 图片dir
    comId = models.IntegerField(unique=True)
    com_description = models.CharField(max_length=256)
    com_type = models.CharField(max_length=64)
    com_image_dir = models.CharField(max_length=64)

    class Meta:
        db_table = 'e_shop_commodity_info'
        ordering = ['id']

