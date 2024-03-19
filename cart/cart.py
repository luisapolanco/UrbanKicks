from product.models import Product
from user.models import User
class Cart():
    def __init__(self, request):
        self.session = request.session
        self.request = request

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart
    
    def db_add(self, product, quantity):
        product_id = str(product)
        product_quantity = str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]= int(product_quantity)
        
        self.session.modified = True

        if self.request.user.is_authenticated:

            current_user = User.objects.filter(id = self.request.user.id)

            carty = str(self.cart)
            carty = carty.replace("\'", "\"")

            current_user.update(old_cart=str(carty))

    def add(self, product, quantity):
        product_id = str(product.product_id)
        product_quantity = str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]= int(product_quantity)
        
        self.session.modified = True

        if self.request.user.is_authenticated:

            current_user = User.objects.filter(id = self.request.user.id)

            carty = str(self.cart)
            carty = carty.replace("\'", "\"")

            current_user.update(old_cart=str(carty))
    
    def cart_total(self):
        product_ids = self.cart.keys()

        products= Product.objects.filter(product_id__in=product_ids)

        quantites = self.cart
        
        total = 0
        for key, value in quantites.items():
            key = int(key)
            for product in products:
                if product.product_id == key:
                    total = total + (product.price*value)
        
        return total

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(product_id__in=product_ids)

        return products
    
    def get_quantities(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_quantity = int(quantity)

        current_cart = self.cart
        
        current_cart[product_id] = product_quantity

        self.session.modified = True
        if self.request.user.is_authenticated:

            current_user = User.objects.filter(id = self.request.user.id)

            carty = str(self.cart)
            carty = carty.replace("\'", "\"")

            current_user.update(old_cart=str(carty))
        
        new_cart = self.cart
        return new_cart
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True

        if self.request.user.is_authenticated:

            current_user = User.objects.filter(id = self.request.user.id)

            carty = str(self.cart)
            carty = carty.replace("\'", "\"")

            current_user.update(old_cart=str(carty))