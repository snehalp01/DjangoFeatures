from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Board,Topic,Post
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    boards = Board.objects.all()
    board_names = []
    for board in boards:
        board_names.append(board.name)
    context={'board_names':boards}
    template_name = 'boards_app\home.html'
    return render(request, template_name,context)

def board_topics(request, pk):
    try:
        board = Board.objects.get(id=pk)
        template_name = 'boards_app\\topics.html'
        return render(request, template_name, {'board': board})
    except Board.DoesNotExist as msg:
        raise Http404

def new_topic(request, pk):
    board = Board.objects.get(pk=pk)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()  # TODO: get the currently logged in user

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )

        return redirect('board', pk=board.pk)  # TODO: redirect to the created topic page

    return render(request, 'boards_app\\new_topic.html', {'board': board})