from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CustomDatasetForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages


@login_required
def add_model_page(request):
    if request.method == 'POST':
        form = CustomDatasetForm(request.POST, request.FILES)
        if form.is_valid():
            dataset = form.save(commit=False)
            dataset.user = request.user
            dataset.save()
            messages.success(request, '✅ Dataset succesfulyy uploaded!')
            return redirect('add-model')  
        else:
            messages.error(request, '❌ There is a mistake in form, please check')
    else:
        form = CustomDatasetForm()

    return render(request, 'customdash/add_model.html', {'form': form})



@login_required
def upload_dataset(request):
    if request.method == 'POST': #wwhen post request is made, chechk the coming datas, and validation of form
        form = CustomDatasetForm(request.POST, request.FILES)
        if form.is_valid():
            dataset = form.save(commit=False)
            dataset.user = request.user
            dataset.save()
            return JsonResponse({'success': True})
        else:
            error_msg = form.errors.get('file', ['Geçersiz dosya'])[0]
            return JsonResponse({'success': False, 'error': error_msg}, status=400)
    else:
        form = CustomDatasetForm()
        return render(request, 'customdash/add_model.html', {'form': form})


