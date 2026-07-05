// store/static/store/js/cart.js

// 1. LocalStorage se cart ka purana data nikalna, ya fir ek khali object {} banana
let cart = JSON.parse(localStorage.getItem('cart')) || {};

// Page load hote hi cart ka count update karna
updateCartCount();

// 2. "Add to Cart" buttons par click event lagana
document.addEventListener('DOMContentLoaded', () => {
    const actionButtons = document.querySelectorAll('.add-btn');
    
    actionButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.dataset.product;
            const productName = this.dataset.name;
            
            // Agar product pehle se cart mein hai toh quantity badhao, nahi toh 1 set karo
            if (cart[productId]) {
                cart[productId].quantity += 1;
            } else {
                cart[productId] = {
                    name: productName,
                    quantity: 1
                };
            }
            
            // Updated cart ko browser memory (LocalStorage) mein save karein
            localStorage.setItem('cart', JSON.stringify(cart));
            
            // Navbar ka counter badhayein
            updateCartCount();
            
            alert(`${productName} successfully cart mein add ho gaya!`);
        });
    });
});

// 3. Navbar mein total items ka count dikhane ka function
function updateCartCount() {
    let totalItems = 0;
    for (let item in cart) {
        totalItems += cart[item].quantity;
    }
    
    const cartCountElement = document.getElementById('cart-count');
    if (cartCountElement) {
        cartCountElement.innerText = totalItems;
    }
}