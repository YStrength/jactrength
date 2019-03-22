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

class EshopUserInfo(models.Model):
    userId = models.IntegerField(unique=True)       #用户ID
    #头像dir
    username = models.CharField(max_length=15)      #用户名
    password = models.CharField(max_length=16)      #密码
    tel = models.IntegerField(max_length=11)        #手机号
    email = models.CharField(max_length=32)                      #邮箱
    locainfo = models.TextField(max_length=50)                   #地域信息
    reg_time = models.TimeField(max_length=8)                   #注册日期
    #权限
    #登录状态
    #账号状态

