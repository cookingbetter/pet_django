from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect

from app.forms import ReceiptForm # , ReceiptForm
from .models import Receipt

# Create your views here.


def index(request):
    context = {'receipts': Receipt.objects.all()}
    return render(request, 'index.html', context=context)


def add_post(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('receipts')
    else:
        form = ReceiptForm()
    return render(request, 'add_post.html', {'form': form})


def favorites(request):
    context = {'favorites_receipts': Receipt.objects.all().filter(favorite=True)}
    return render(request, 'favorites.html', context=context)


def checkout(request, receipt_id):
    if request.method == 'POST':
        obj = Receipt.objects.get(id=receipt_id)
        obj.purchased = True
        obj.save()
        return redirect('receipts')
    else:
        receiptDetail = Receipt.objects.get(id=receipt_id)
        return render(request, 'checkout.html', {'receipt': receiptDetail})
    

def purchases(request):
    context = {'purchased_receipts': Receipt.objects.all().filter(purchased=True)}
    return render(request, 'purchases.html', context=context)


# если зайти на index, purchases, favorites, и выбрать отдельный товар, мы переходим на item и там должен быть выбор
# если покупка совершена, то показывается рецепт, если нет, кнопка перехода на checkout

def item(request, receipt_id):
    if request.method == 'POST':
        obj = Receipt.objects.get(id=receipt_id)
        obj.purchased = True
        obj.save()
        return redirect('receipts')
    else:
        receiptDetail = Receipt.objects.get(id=receipt_id)
        return render(request, 'item.html', {'receipt': receiptDetail})