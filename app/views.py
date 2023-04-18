from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect

from app.forms import PostForm # , ReceiptForm
from .models import Post

# Create your views here.


def index(request):
    context = {'receipts': Post.objects.all()}
    return render(request, 'index.html', context=context)


# def add_new_element(request):
#     if request.method == 'POST':
#         form = ReceiptForm(request.POST)
#         if form.is_valid():
#             form.save(commit=False)
#             form.save()
#     else:
#         form = ReceiptForm()
#     return render(request, 'receipt_form.html', {'form': form})


# def add_receipt(request):
#     if request.method == 'POST':
#         form = ReceiptForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('receipts')
#     else:
#         form = ReceiptForm()
#     return render(request, 'add_receipt.html', {'form': form})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receipts')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})