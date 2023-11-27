from rest_framework.generics import *

from .models import Item
from .serializers import ItemSerializer


class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
