from django.shortcuts import render


def home(request):
    return render(request, 'webapp/home.html', {'nbar': 'home'})


def about(request):
    context = {'title': 'about', 'nbar': 'about'}
    # data view, edit and automation tool DVEAT
    return render(request, 'webapp/about.html', context=context)
