from django import forms

from course.models import Course, CoruseConnectionStudent,Tag


class SerachForm(forms.Form):
    tag = forms.ModelChoiceField(label=u'类目', queryset=Tag.objects.all())
    # lever = forms.ModelChoiceField(label=u'难度', queryset=Tag.objects.all())
    # start_date = forms.DateTimeField(label=u'时间')

