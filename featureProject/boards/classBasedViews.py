from rest_framework.response import Response
from rest_framework.views import APIView   
from .models import Board 
from .serializers import BoardSerializer
class BoardDetails(APIView):
    def get(self, request):
        board_data = Board.objects.all()
        serializer = BoardSerializer(board_data, many=True)
        return Response({"msg":"Board View", "data":serializer.data})
    def post(self,request):
        data = request.data
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"new board created"})
        return Response({"msg":"Error in creating new board"})
    def put(self,request):
        data = request.data
        board = Board.objects.get(id=data['id'])
        serializer = BoardSerializer(instance=board,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"board updated successfully"})
        return Response({"msg":"Error in updating board"})
    

class deleteBoard(APIView):
    def delete(self,request, pk):
        # data = request.POST
        board = Board.objects.get(id=pk)
        board.delete()
        return Response({"msg":"board deleted successfully"})

