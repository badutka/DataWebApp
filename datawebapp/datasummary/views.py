from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def data_summary(request):
    context = {'title': 'Data Summary', 'nbar': 'data_summary'}
    return render(request, 'datasummary/data_summary.html', context=context)
