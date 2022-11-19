from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from django.contrib import messages
import pandas as pd


@login_required
def data_summary(request):
    context = {'title': 'Data Summary', 'nbar': 'data_summary'}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES['file'])
            df, df_head= handle_file(request.FILES['file'], request)
            context.update({'df': df, 'df_head': df_head})
    else:
        form = UploadFileForm()
    context.update({'form': form})
    return render(request, 'datasummary/data_summary.html', context=context)


def handle_file(file, request):
    if not file.name.endswith('.csv'):
        messages.error(request, 'File is not CSV type')
        # if file is too large, return
    if file.multiple_chunks():
        messages.error(request, "Uploaded file is too big (%.2f MB)." % (file.size / (1000 * 1000),))
    # data = file.read().decode("utf-8")
    data = pd.read_csv(file)
    return data, data.head()
