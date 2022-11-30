from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from django.contrib import messages

import pandas as pd
from collections import namedtuple

from mlengine.data_manager.file_reader import get_df_details


@login_required
def data_summary(request):
    context = {'title': 'Data Summary', 'nbar': 'data_summary'}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df, df_head = handle_file(file, request)
            df_details = namedtuple('df_details',
                                    'col_count, dtypes, non_null_counts, dtype_counts, memory_usage_string')
            (col_count, dtypes, non_null_counts, dtype_counts, memory_usage_string) = get_df_details(df)
            # noinspection PyTypeChecker,PyUnresolvedReferences
            # df_details = df_details(col_count, zip(dtypes.index, dtypes.values, non_null_counts.values), zip(non_null_counts.index, non_null_counts.values), dtype_counts, memory_usage_string)
            df_details = {'index': dtypes.index, 'dtypes': dtypes.values, 'non_nulls': non_null_counts.values}
            # df_details = zip(dtypes.index, dtypes.values, non_null_counts.values)
            # noinspection PyTypeChecker,PyUnresolvedReferences
            column_details = {'col_count': col_count, 'dtype_counts': zip(dtype_counts.index, dtype_counts.values), 'memuse':  memory_usage_string}
            context.update({'df': df, 'df_head': df_head, 'df_details': df_details, 'column_details': column_details})
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
