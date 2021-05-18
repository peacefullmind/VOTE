import datetime

from django import forms
from django.forms import fields

from . import models
from django.utils import timezone




class QuestionForm(forms.ModelForm):
    choice = forms.ModelChoiceField(
        label='',
        queryset=models.Choice.objects.all(),
        widget=forms.RadioSelect)

    class Meta:
        model = models.Question
        fields = []

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = self.instance.choice_set.all()

    def save_selected_choice(self):
        self.cleaned_data['choice'].voted_users.add(self.user)
        self.cleaned_data['choice'].votes += 1
        self.cleaned_data['choice'].save(update_fields=['votes'])

    def clean(self):
        if self.user is None:
            raise forms.ValidationError('User is None')

        question_choice_pks = list(self.instance.choice_set.all().values_list('pk', flat=True))
        user_voted_choice_pks = self.user.uservote_set.all().values_list('choice__pk', flat=True)
        for pk in user_voted_choice_pks:
            if pk in question_choice_pks:
                raise forms.ValidationError('已经投过票了')
        return self.cleaned_data

class QuestionFormPure(forms.ModelForm):
    question_text = fields.CharField()
    pub_date = fields.DateTimeField()
    class meta:
        model=models.Question
        fields=['question_text','pub_date']

# class ChoiceInline(forms.ModelForm):
#     model = models.Choice
#     extra = 0
#     show_change_link = True
#
# class QuestionUser(forms.ModelForm):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['question_text']
#
#     def was_published_recently(self, obj):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= obj.pub_date <= now
#     was_published_recently.admin_order_field = 'pub_date'
#     was_published_recently.boolean = True
#     was_published_recently.short_description = 'Published recently?'
