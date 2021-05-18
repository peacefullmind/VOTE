from django.shortcuts import render, resolve_url, redirect
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



# def new_question(request):
#     if request.method !='POST':
#         form=forms.QuestionFormPure()
#     else:
#         form=forms.QuestionFormPure(data=request.POST)
#         if form.is_valid():
#             form.save()
#             print("=======保存成功！================")
#             return redirect(resolve_url('polls:index'))
#
#     context={'form':form}
#     return render(request,'polls/new_question.html',context)

class NewQuesView(generic.ListView):
    model = models.Question
    template_name = 'polls/new_question.html'

    # def get_context_data(self, **kwargs):
    #     kwargs.setdefault('form',
    #         forms.QuestionForm(instance=self.object)
    #     )
    #     return super().get_context_data(**kwargs)




class NewQuesFormView(generic.FormView):
    http_method_names = ['post']
    form_class = forms.QuestionFormPure
    template_name = 'polls/new_question.html'

    # def get_form_kwargs(self):
    #     self.object = models.Question.objects.get(id=self.kwargs['pk'])
    #     kwargs = super().get_form_kwargs()
    #     kwargs['instance'] = self.object
    #     kwargs['user'] = self.request.user
    #     return kwargs

    def form_valid(self, form):
        form.save()
        return redirect(resolve_url('polls:index'))

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                object=self.object),
        )


