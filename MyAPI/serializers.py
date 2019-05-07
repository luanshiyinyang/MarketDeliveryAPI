from rest_framework import serializers
from MyAPI.models import User, Order, Merchant, Good


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone', 'name', 'email', 'icon', 'password', 'address')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'userID', 'name', 'state', 'price',  'timePlaced', 'timeExpected', 'timeArrived',
                  'address', 'wayOfPay', 'goodsNumber', 'goodsIDs', 'goodNames')


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ('id', 'name', 'icon', 'sales', 'rating', 'priceSend', 'distance')


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ('id', 'name', 'kind', 'icon', 'allowance', 'price', 'sales', 'merchantID')
