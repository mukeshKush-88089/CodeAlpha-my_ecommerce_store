# store/views.py
from django.shortcuts import render, get_object_or_404 # get_object_or_404 add kiya
from .models import Product

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)

# Naya view Product Details ke liye
def product_detail(request, pk):
    # Agar ID (pk) waala product mila toh theek, nahi toh 404 Error page dikha dega
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

# store/views.py ke aakhiri mein add karein

def cart_view(request):
    # Yeh sirf html page render karega, baaki ka saara data frontend JavaScript handle karegi
    return render(request, 'store/cart.html')

# store/views.py ke end mein add karein
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages

# 1. Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) # Register hote hi user login ho jayega
            messages.success(request, "Registration successful! Welcome to Mera Shop.")
            return redirect('store')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})

# 2. Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('store')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

# 3. Logout View
def logout_view(request):
    auth_logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('store')

# store/views.py ke bilkul end mein copy-paste karein
import json
from django.http import JsonResponse
from .models import Order, OrderItem, Product

def process_order(request):
    # Agar user login nahi hai toh order nahi lene denge
    if not request.user.is_authenticated:
        return JsonResponse({'status': 'login_required'}, status=401)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cart_data = data.get('cart', {})

            if not cart_data:
                return JsonResponse({'status': 'empty_cart'}, status=400)

            # 1. Naya Order create karein database mein
            order = Order.objects.create(
                user=request.user,
                complete=True,
                transaction_id=f"TXN-{request.user.id}-{Order.objects.count() + 1}"
            )

            # 2. Cart ke har item ko OrderItem table mein save karein
            for product_id, item_info in cart_data.items():
                product = Product.objects.get(id=int(product_id))
                OrderItem.objects.create(
                    product=product,
                    order=order,
                    quantity=item_info['quantity']
                )
                
                # Optionals: Stock kam karna
                if product.stock >= item_info['quantity']:
                    product.stock -= item_info['quantity']
                    product.save()

            return JsonResponse({'status': 'success', 'transaction': order.transaction_id})
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'invalid_method'}, status=405)