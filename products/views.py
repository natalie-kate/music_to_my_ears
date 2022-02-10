""" Imports required by products app """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Vinyl, Genre, Image
from .forms import ProductForm


def genres():
    """ Gets those genres that currently have products """
    all_genres = Genre.objects.all()
    current_genres = []
    for genre in all_genres:
        filtered_products = Vinyl.objects.filter(genre=genre.pk)
        if filtered_products:
            current_genres.append(genre)
    return current_genres


def default_images():
    """ Contingency plan in case superuser make 2 images default=True """
    products = Vinyl.objects.all()
    image_list = []
    for vinyl in products:
        image = Image.objects.filter(default=True, vinyl=vinyl.id)
        image_list.append(image[0])
    return image_list


def open_shop(request):
    """ A view to return the shopping page """

    products = Vinyl.objects.all()
    search = None

    if request.GET:
        if 'search' in request.GET:
            search = request.GET['search']
            searches = Q(title__icontains=search) | Q(
                artist__icontains=search) | Q(track_list__icontains=search)
            products = products.filter(searches)
            if not products:
                messages.error(
                    request, (
                        "Sorry your query didn't match any of our products"))
                return redirect(reverse('shop'))

        if not search:
            messages.error(
                request, "Oops you need to enter a search keyword first")
            return redirect(reverse('shop'))

    context = {
        'products': products,
        'genres': genres(),
        'images': default_images(),
        'search': search,
    }

    return render(request, 'products/shop.html', context)


def view_all_products(request):
    """ View to return all products rather than in genre sorting """
    products = Vinyl.objects.all()

    context = {
        'products': products,
        'genres': genres(),
        'images': default_images(),
        'search': True,
    }

    return render(request, 'products/shop.html', context)


def browse_genre(request, genre_id):
    """ View all products in a genre """
    products = Vinyl.objects.filter(genre=genre_id)

    context = {
        'products': products,
        'images': default_images(),
        'search': True,
    }

    return render(request, 'products/shop.html', context)


def product(request, product_id):
    """ Get product details """
    quantity_in_basket = 0
    product_info = get_object_or_404(Vinyl, pk=product_id)
    images = Image.objects.filter(vinyl=product_id)
    tracklist = product_info.track_list.split(",")
    basket = request.session.get('basket', {})
    basket_product = product_id in list(basket.keys())
    if basket_product:
        quantity_in_basket = basket[product_id]

    context = {
        'product': product_info,
        'images': images,
        'tracklist': tracklist,
        'basket_product': basket_product,
        'quantity': quantity_in_basket,
    }

    return render(request, 'products/product.html', context)


@login_required
def add_vinyl(request):
    """ Add new product view """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('shop'))

    if request.method == 'POST':
        # If post method, check form is valid and if product
        # already exists in database
        form = ProductForm(request.POST)
        if form.is_valid():
            check_product = Vinyl.objects.filter(title=form['title'].value())
            if not check_product:
                # If product not already in database add it
                new_vinyl = form.save()
                # Get default image and add to database
                default_image = request.FILES.get('default_image')
                vinyl_id = Vinyl.objects.get(pk=new_vinyl.id)
                image_name = str(default_image).split('.', maxsplit=1)[0]
                Image.objects.create(
                    vinyl=vinyl_id,
                    image=default_image,
                    image_name=image_name,
                    default=True,
                )
                # If additional images add them to database
                files = request.FILES.getlist('additional_images')
                if files:
                    for file in files:
                        image_name = str(file).split('.', maxsplit=1)[0]
                        Image.objects.create(
                            vinyl=vinyl_id,
                            image=file,
                            image_name=image_name,
                            default=False,
                        )
                messages.success(request, 'Successfully added product!')
                return redirect(reverse('product', args=[new_vinyl.id]))
            else:
                messages.error(request, (
                    'Product already exists in database.'))
                return redirect(reverse('shop'))
        else:
            messages.error(
                request, (
                    'Failed to add product. '
                    'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_vinyl.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_vinyl(request, product_id):
    """ Edit product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('shop'))

    edit_product = get_object_or_404(Vinyl, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=edit_product)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, (
                'Failed to update product. '
                'Please ensure the form is valid.'))

        files = request.FILES.getlist('additional_images')
        if files:
            for file in files:
                image_name = str(file).split('.', maxsplit=1)[0]
                Image.objects.create(
                    vinyl=edit_product,
                    image=file,
                    image_name=image_name,
                    default=False,
                )
        messages.success(request, 'Thats updated!')
        return redirect(reverse('product', args=[edit_product.id]))
    else:
        form = ProductForm(instance=edit_product)

    template = 'products/edit_vinyl.html'
    context = {
        'form': form,
        'product': edit_product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ delete product from database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('shop'))

    del_product = get_object_or_404(Vinyl, pk=product_id)
    del_product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('shop'))
