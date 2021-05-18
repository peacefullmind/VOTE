from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/vote/', views.VoteFormView.as_view(), name='vote-form'),

    # path('new_question/', views.new_question, name='new_question'),
    #NewQuesFormView
    path('new_question/', views.NewQuesView.as_view(), name='new_question'),
    path('new_question/add', views.NewQuesFormView.as_view(), name='new_question_form'),


]