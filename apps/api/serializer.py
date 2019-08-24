from rest_framework.serializers import ModelSerializer
from apps.catalogs.models import Category, Product

class CategorySerializer(ModelSerializer):
    class Meta: 
        model = Category
        fields = ('name', 'description')

class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class ProductDetailSerializer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'