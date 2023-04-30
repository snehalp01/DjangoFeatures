from rest_framework.viewsets import ViewSet, ModelViewSet
from .models import Board
from .serializers import BoardSerializer
class BoardsModelViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer