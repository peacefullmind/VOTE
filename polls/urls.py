from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/vote/', views.VoteFormView.as_view(), name='vote-form'),

    path('Manage/',views.ManageView.as_view(),name='manage'),
    path('all_choice/', views.ChoiceView.as_view(), name='listchoice'),
    path('all_question/', views.QuestionView.as_view(), name='list_question'),

    # path('new_question/', views.new_question, name='new_question'),
    #NewQuesFormView
    # path('new_question/', views.NewQuesFormView.as_view(), name='new_question'),
    path('new_question/', views.NewQuesFormView.as_view(), name='new_question_form'),
    # path('new_question/', views.QuesCreateView.as_view(), name='new_question_form'),
    path('new_choice/', views.NewChoiceFormView.as_view(), name='new_choice_form'),


    path('edit_question/<int:pk>/', views.EditQuesFormView.as_view(), name='edit_question_form'),
    path('edit_choice/<int:pk>/', views.EditChoiceView.as_view(), name='edit_choice_form'),



]