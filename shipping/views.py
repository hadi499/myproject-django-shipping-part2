from django.shortcuts import render, get_object_or_404, redirect

from .forms import ShippingForm, GantiTarifForm

from .models import Shipping, Category, TarifPerKilo


def home(request):
    shipping = Shipping.objects.all().order_by('-id')
    return render(request, 'shipping/home.html', {'shipping': shipping})


def create(request):
    shipping_form = ShippingForm(request.POST)
    kategori = Category.objects.all()
    tarif_per_kilo = TarifPerKilo.objects.all().last()
    tarif = tarif_per_kilo.harga
    tarif_final = int(tarif)
    print(type(tarif_final))

    if request.method == 'POST':
        if shipping_form.is_valid():
            shipping_form.save()

        return redirect('home')

    context = {
        'page_title': 'Tambah shipping',
        'shipping_form': shipping_form,
        'kategori': kategori,
        'tarif': tarif_final

    }

    return render(request, 'shipping/create.html', context)


def tarifperkilo(request):
    tarif = TarifPerKilo.objects.all().order_by('-id')

    return render(request, 'shipping/tarif.html', {'tarif': tarif})


def ganti_tarif(request):
    form = GantiTarifForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

        return redirect('tarif')

    context = {
        'form': form,

    }

    return render(request, 'shipping/ganti_tarif.html', context)
