from django.db import models


# 用户表
class User(models.Model):
    id = models.AutoField(null=False, verbose_name="用户ID号", primary_key=True)
    phone = models.CharField(max_length=11, null=False, verbose_name="手机号")
    name = models.CharField(max_length=10, null=False, verbose_name="昵称")
    address = models.CharField(max_length=100, null=False, verbose_name="地址", default="空地址")
    password = models.CharField(max_length=32, null=False, verbose_name="密码")
    email = models.EmailField(null=False, verbose_name="邮箱")
    icon = models.CharField(max_length=30, null=False, verbose_name="头像")

    def __str__(self):
        return self.id

    class Meta:
        # 自定义表名，不指定django自动生成
        db_table = 'User'
        # 可读的名字
        verbose_name = "用户表"
        # 可读名字的复数形式
        verbose_name_plural = verbose_name


class Order(models.Model):
        id = models.AutoField(null=False, verbose_name="订单ID号", primary_key=True)
        # 其实就是商家图标
        # icon = models.CharField(max_length=30, null=False, verbose_name="图标")
        userID = models.BigIntegerField(null=False, verbose_name="所属用户ID")
        name = models.CharField(max_length=20, null=False, verbose_name="名称")
        # True表示已完成， False表示配送中
        state = models.BooleanField(null=False, verbose_name="状态")
        price = models.FloatField(null=False, verbose_name="总价")
        phone = models.CharField(max_length=11, null=False, verbose_name="商家联系电话")
        timePlaced = models.DateTimeField(null=False, verbose_name="下单时间")
        timeExpected = models.CharField(max_length=20, null=False, verbose_name="期待送达时间")
        timeArrived = models.DateTimeField(null=True, verbose_name="送达时间")
        address = models.CharField(max_length=100, null=False, verbose_name="地址")
        # 只有平台在线支付和货到付款
        wayOfPay = models.CharField(max_length=20, null=False, verbose_name="支付方式")
        goodsNumber = models.IntegerField(null=False, verbose_name="商品数目")
        goodsIDs = models.CharField(max_length=200, null=False, verbose_name="商品id串");goodNames = models.CharField(max_length=200, null=False, verbose_name="商品串")

        def __str__(self):
            return self.id

        class Meta:
            # 自定义表名，不指定django自动生成
            db_table = 'Order'
            # 可读的名字
            verbose_name = "订单表"
            # 可读名字的复数形式
            verbose_name_plural = verbose_name


class Merchant(models.Model):
    id = models.AutoField(null=False, verbose_name="商家ID号", primary_key=True)
    name = models.CharField(max_length=30, null=False, verbose_name="名称")
    icon = models.CharField(max_length=30, null=False, verbose_name="图标")
    sales = models.IntegerField(null=False, verbose_name="销量")
    rating = models.FloatField(null=False, verbose_name="评分")
    priceSend = models.FloatField(null=False, verbose_name="起送价格")
    distance = models.FloatField(null=False, verbose_name="距离", default=2.0)
    def __str__(self):
        self.id

    class Meta:
        # 自定义表名，不指定django自动生成
        db_table = 'Merchant'
        # 可读的名字
        verbose_name = "商家表"
        # 可读名字的复数形式
        verbose_name_plural = verbose_name


class Good(models.Model):
    id = models.AutoField(null=False, verbose_name="商品ID号", primary_key=True)
    name = models.CharField(max_length=20, null=False, verbose_name="名称")
    kind = models.CharField(max_length=20, null=False, verbose_name="类型")
    icon = models.CharField(max_length=30, null=False, verbose_name="图标")
    allowance = models.IntegerField(null=False, verbose_name="余量")
    price = models.FloatField(null=False, verbose_name="价格")
    sales = models.IntegerField(null=False, verbose_name="销量")
    merchantID = models.BigIntegerField(null=False, verbose_name="商家ID")

    def __str__(self):
        return self.id

    class Meta:
        # 自定义表名，不指定django自动生成
        db_table = 'Good'
        # 可读的名字
        verbose_name = "商品表"
        # 可读名字的复数形式
        verbose_name_plural = verbose_name


