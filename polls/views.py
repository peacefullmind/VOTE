from django.http import Http404
from django.shortcuts import render, resolve_url, redirect
from django.urls import reverse_lazy
from django.views import generic

from . import models, forms



class IndexView(generic.ListView):
    model = models.Question
    template_name = 'polls/index.html'


class DetailView(generic.DetailView):
    model = models.Question
    template_name = 'polls/detail.html'

    def get_context_data(self, **kwargs):
        kwargs.setdefault('form',
            forms.QuestionForm(instance=self.object)
        )
        return super().get_context_data(**kwargs)


class VoteFormView(generic.FormView):
    http_method_names = ['post']
    form_class = forms.QuestionForm
    template_name = 'polls/detail.html'

    def get_form_kwargs(self):
        self.object = models.Question.objects.get(id=self.kwargs['pk'])
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save_selected_choice()
        return redirect(resolve_url('polls:results', self.kwargs['pk']))

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                object=self.object),
        )

class ResultsView(generic.DetailView):
    model = models.Question
    template_name = 'polls/results.html'



# class NewQuesFormView(generic.FormView):
#     # http_method_names = ['post']
#     form_class = forms.QuestionFormPure
#     template_name = 'polls/new_question.html'
#
#     def form_valid(self, form):
#         form.save()
#         return redirect(resolve_url('polls:index'))
#
#     def form_invalid(self, form):
#         return self.render_to_response(
#             self.get_context_data(
#                 form=form,
#                 object=self.object),
#         )

class NewQuesFormView(generic.CreateView):
    # http_method_names = ['post']

    model=models.Question
    template_name = 'polls/new_question.html'
    form_class = forms.QuestionFormPure
    success_url = ''

    # def form_valid(self, form):
    #     form.save()
    #     return redirect(resolve_url('polls:index'))
    #
    # def form_invalid(self, form):
    #     return self.render_to_response(
    #         self.get_context_data(
    #             form=form,
    #             object=self.object),
    #     )


class NewChoiceFormView(generic.FormView):
    # http_method_names = ['post']
    form_class = forms.ChoiceForm
    template_name = 'polls/new_choice.html'

    def form_valid(self, form):
        form.save()
        return redirect(resolve_url('polls:index'))

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                object=self.object),
        )


class EditQuesFormView(generic.UpdateView):
    # http_method_names = ['post']、
    model = models.Question
    fields = ['id', 'question_text', 'pub_date']
    # fields = '__all__'
    # form_class = forms.QuestionForm2
    template_name = 'polls/edit_question.html'

    # context_object_name =
    # success_url = 'polls/index.html'
    #
    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset=queryset)
    #     if obj.author != self.request.user:
    #         raise Http404()
    #     return obj


class EditChoiceView(generic.UpdateView):
    model = models.Choice
    fields = ['question', 'choice_text']
    template_name = 'polls/edit_choice.html'
    success_url = ''


# class QuesCreateView(generic.CreateView):
#     model = models.Question
#     fields = '__all__'

# class QuesUpdateView(generic.UpdateView):
#     model = models.Question
#     fields = '__all__'

# class QuesDeleteView(generic.DeleteView):
#     model = models.Question
#     fields = '__all__'

class ManageView(generic.ListView):
    model = models.Question
    template_name = 'polls/manage.html'

class ChoiceView(generic.ListView):
    model = models.Choice
    template_name = 'polls/all_choice.html'
class QuestionView(generic.ListView):
    model = models.Question
    template_name = 'polls/all_question.html'