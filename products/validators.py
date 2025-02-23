from rest_framework.validators import UniqueValidator

from products.models import Product

unique_title_validator = UniqueValidator(
    queryset=Product.objects.all(), lookup="iexact"
)
