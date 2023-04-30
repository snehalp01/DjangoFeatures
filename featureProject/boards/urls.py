from django.urls import path
from . import views, classBasedViews
urlpatterns = [
    path('home/', views.home, name='home'),
    path('board/<pk>/', views.board_topics, name='board'),
    path('board/<pk>/new/', views.new_topic,name='new_topic'),

    path('boardData/', classBasedViews.BoardDetails.as_view(), name='boardData'),
    path('deleteBoard/<pk>/', classBasedViews.deleteBoard.as_view(), name='deleteBoard'),
    

]