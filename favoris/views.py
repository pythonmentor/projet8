from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from products.models import Products
from favoris.models import Favorite
from products.forms import ProductSearch

@login_required
def saving_search(request, id_searched, id_substitue):
    """views to save the user's search"""
    product = Products.objects.get(id_code=id_searched)
    sub = Products.objects.get(id_code=id_substitue)
    Favorite.objects.get_or_create(user_link=request.user,
                                   product_searched=product,
                                   product_substitute=sub)
    return redirect('home')


@login_required
def display_account(request):
    """views that display searched details"""
    form = ProductSearch(request.POST or None)
    favoris = Favorite.objects.filter(
        user_link=request.user).order_by('product_searched')
    paginator = Paginator(favoris, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'display_account.html', {'page_obj': page_obj, 'form': form})
