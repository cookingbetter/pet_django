from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.shortcuts import redirect

from app.forms import ReceiptForm # , ReceiptForm
from .models import Favorite, Purchased, Receipt, Subscription
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('receipts')


class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    success_url = reverse_lazy('receipts')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receipts')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            # return redirect('receipts')
        return redirect('receipts')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})


def index(request):
    purchaseds = Purchased.objects.filter(user=request.user)
    purchased = [purchased.receipt for purchased in purchaseds]
    context = {'receipts': Receipt.objects.all(), 'user': request.user, 'purchased': purchased}

    return render(request, 'index.html', context=context)


@login_required
def add_post(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST, request.FILES)

        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.user = request.user
            receipt.save()
            if form.cleaned_data['is_favorite']:
                favorite = Favorite(user=request.user, receipt=receipt)
                favorite.save()
            return redirect('receipts')
    else:
        form = ReceiptForm()
    return render(request, 'add_post.html', {'form': form})


@login_required
def favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    favorite = [favorite.receipt for favorite in favorites]

    purchaseds = Purchased.objects.filter(user=request.user)
    purchased = [purchased.receipt for purchased in purchaseds]

    context = {'favorites_receipts': favorite, 'purchased': purchased}
    return render(request, 'favorites.html', context=context)


@login_required
def checkout(request, receipt_id):
    if request.method == 'POST':
        receipt = Receipt.objects.get(id=receipt_id)
        purchased = Purchased(user=request.user, receipt=receipt)
        purchased.save()
        return redirect('receipts')
    else:
        receipt = Receipt.objects.get(id=receipt_id)
        return render(request, 'checkout.html', {'receipt': receipt})
    

@login_required
def purchases(request):
    purchases = Purchased.objects.filter(user=request.user)
    purchased = [purchased.receipt for purchased in purchases]
    context = {'purchaseds': purchased}

    return render(request, 'purchases.html', context=context)


def item(request, receipt_id):
    if request.method == 'POST':
        form_id = request.POST.get('form_id')
        if form_id == 'form1' or form_id == 'form2':
            receipt = get_object_or_404(Receipt, pk=receipt_id)
            # если такой рецепт существует в избранных, то надо удалить его
            # если нет, то создать 
            try:
                favorite = Favorite.objects.get(user=request.user, receipt=receipt)
                favorite.delete()
            except Favorite.DoesNotExist:
                favorite = Favorite(user=request.user, receipt=receipt)
                favorite.save()
            # return redirect('receipts')

            return redirect(f'/item/{receipt_id}')

        obj = Receipt.objects.get(id=receipt_id)
        obj.purchased = True
        obj.save()
        return redirect('receipts')
    else:

        receipt = Receipt.objects.get(id=receipt_id)
        is_favorite = Favorite.objects.filter(user=request.user, receipt=receipt).exists()
        purchases = Purchased.objects.filter(user=request.user)
        purchased = [purchased.receipt for purchased in purchases]
        context = {
            'receipt': receipt,
            'is_favorite': is_favorite,
            'purchased': purchased,
        }

        return render(request, 'item.html', context)
    

def subscribe(request, receipt_id):
    # Сделать кнопки подписаться и отписаться как это сделано с избранными
    context = {'receipt': Receipt.objects.get(id=receipt_id)}

    return render(request, 'subscribe.html', context)
    
