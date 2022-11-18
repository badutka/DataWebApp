from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'webapp/home.html', {'nbar': 'home'})


def about(request):
    context = {'title': 'about', 'nbar': 'about'}
    # data view, edit and automation tool DVEAT
    return render(request, 'webapp/about.html', context=context)


@login_required
def data_summary(request):
    context = {'title': 'Data Summary', 'nbar': 'data_summary'}
    return render(request, 'webapp/data_summary.html', context=context)
