# -*- coding:utf-8 -*-
""" Created by FizLin on 2017/07/31/-下午2:54
    mail: https://github.com/Fiz1994
"""
from django.forms import forms


class FileUploadForm(forms.Form):
    my_file = forms.FileField()