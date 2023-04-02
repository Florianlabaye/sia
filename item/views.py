from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Category, Item


def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        owner = "tz1PZY3agTGshV48bcYVbuz88G3mfL8wgm1p"
        sc_adresse = "KT1MArMCMVWohqsuksyAtCCi2TGshDpp4G5F"
        link_img = "http://partsofthesun.com/wp-content/uploads/2018/05/3L4A1592.jpg"
        name = "vfds"
        description = "fds"
        coordinates = "fdsf"

        smart_contract_mint_request(owner, sc_adresse, name, description, link_img, coordinates)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')




import os

def string_to_hexa(string):
    hexa = "0x"
    for i in range(len(string)):
        hexa += hex(ord(string[i]))[2:]
    return hexa

def hexa_to_string(hexa):
    string = ""
    for i in range(2, len(hexa), 2):
        string += chr(int(hexa[i:i+2], 16))
    return string


def smart_contract_mint_request(owner : str, sc_adresse : str,  titre : str, description : str, photo_link : str, localisation : str):
    
    titre = string_to_hexa(titre)
    description = string_to_hexa(description)
    photo_link = string_to_hexa(photo_link)
    localisation = string_to_hexa(localisation)

    request =  "octez-client -l --endpoint https://ghostnet.smartpy.io transfer 0 \
    from " + owner + " to " + sc_adresse + " \
    --entrypoint mint --arg '(Pair \"" + owner + "\" {Elt \"description\" " + description + " ; Elt \"localisation\" "+ localisation +"; Elt \"photo_link\" "+ localisation +" ; Elt \"titre\" " + titre +" })' \
    --fee 0.01 \
    --gas-limit 10000 \
    --storage-limit 800"


    os.system(request) # executer la commande pour interagir avec le smart contract

    return request