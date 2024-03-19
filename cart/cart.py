from product.models import Product
class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart
    
    def add(self, product, quantity):
        product_id = str(product.product_id)
        product_quantity = str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]= int(product_quantity)
        
        self.session.modified = True
    
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
        new_cart = self.cart
        return new_cart
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True
