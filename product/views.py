

from django.http import JsonResponse
from django.shortcuts import render
from .models import Product1,DataModel

def ShowAllProduct(request):
    products = Product1.objects.all()
    for product in products:
        rating_percent = (product.ratings / 5) * 100
        product.rating_class = f"width-{round(rating_percent / 20) * 20}"
    context = {
        'products': products,
        'cart_count': request.session.get('cart_count', 0),  # Get cart count from session
    }
    return render(request, 'showallproduct.html', context)


def ProductDetails(request, pk):
    eachproduct = Product1.objects.get(id=pk)
    context = {
        'eachproduct': eachproduct,
        'cart_count': request.session.get('cart_count', 0),  # Get cart count from session
    }
    return render(request, 'productdetails.html', context)



def reset_cart(request):
    if request.method == 'POST':
        # Clear the cart and cart count from the session
        request.session['cart'] = []
        request.session['cart_count'] = 0

        # Save the session to persist changes
        request.session.modified = True

        # Return the updated cart count (which will be 0)
        return JsonResponse({'cart_count': 0})
    
    
from django.shortcuts import render
from django.http import Http404
from .models import Product1

from django.shortcuts import redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product1

def add_to_cart(request):
    if request.method == 'POST':
        # Get product_id and quantity from the POST data
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        # Validate product ID and quantity
        if not product_id or not quantity:
            return JsonResponse({'error': 'Product ID and quantity are required.'}, status=400)

        try:
            product = get_object_or_404(Product1, id=product_id)
        except Product1.DoesNotExist:
            return JsonResponse({'error': 'Product not found.'}, status=404)

        try:
            quantity = int(quantity)
            if quantity < 1:
                return JsonResponse({'error': 'Quantity must be greater than 0.'}, status=400)
        except ValueError:
            return JsonResponse({'error': 'Invalid quantity.'}, status=400)

        # Initialize cart if not already present in the session
        if 'cart' not in request.session:
            request.session['cart'] = []

        cart = request.session['cart']

        # Check if product is already in the cart
        existing_product = next((item for item in cart if item[0] == product_id), None)
        if existing_product:
            existing_product[1] += quantity
        else:
            cart.append([product_id, quantity])

        # Save the updated cart and cart count
        request.session['cart'] = cart
        request.session['cart_count'] = len(cart)
        request.session.modified = True

        # Return the updated cart count in the JSON response
        return JsonResponse({'cart_count': len(cart)})

    return JsonResponse({'error': 'Invalid request method.'}, status=405)


from django.shortcuts import render
from .models import Product1

def CartView(request):
    # Get the cart data from the session
    cart = request.session.get('cart', [])
    
    if not cart:
        # If the cart is empty, show an empty cart page
        return render(request, 'empty_cart.html')  # You can create this template for an empty cart

    total_price = 0
    cart_items = []

    # Loop through the cart items to calculate the total price and display product details
    for product_id, quantity in cart:
        try:
            product = Product1.objects.get(id=product_id)  # Get the product by ID
            item_total = product.price * quantity  # Calculate the total for this product
            total_price += item_total  # Add to the grand total

            cart_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total,
            })
        except Product1.DoesNotExist:
            # If a product is missing, skip (or log this error)
            continue

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'cart.html', context)


def order_success(request):
    return render(request, 'checkout.html')


from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import DataModel


def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        door_number = request.POST.get('door_number')
        street_name = request.POST.get('street_name')
        town_name = request.POST.get('town_name')
        city_name = request.POST.get('city_name')
        district_name = request.POST.get('district_name')
        district_pincode = request.POST.get('district_pincode')
        state_name = request.POST.get('city_name')
        message = request.POST.get('message')
        
        # # Save form data to the database
        your_model_instance = DataModel(name=name, phone_number=phone_number,door_number=door_number, street_name= street_name,town_name=town_name,city_name=city_name,district_name=district_name,district_pincode=district_pincode, state_name= state_name, message=message)
        your_model_instance.save()
        
        # # Send email notification
        subject = 'New Form Submission'
        message = f'Name: {name}\nPhone Number: {phone_number}\nMessage: {message}\ndoor_number: {door_number}\nstreet_name: {street_name}\ntown_name: {town_name}\ncity_name: {city_name}\ndistrict_name: {district_name}\ndistrict_pincode: {district_pincode}\nstate_name: {state_name}'
        sender = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_RECEIVER]  # Add the recipient's email address here
        send_mail(subject, message, sender, recipient_list)
      
        return render(request, 'success.html')  # Render a success page after submission
        #return HttpResponse("success")
    
    #return render(request, 'your_form_template.html')  # Render your form template
    return HttpResponse("fail")



