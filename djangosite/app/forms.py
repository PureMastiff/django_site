# coding=utf-8

from django.forms import ModelForm
from .models import Moment

class MomentForm(Moment):
    class Meta:
        model = Moment
        fields = '__all__'