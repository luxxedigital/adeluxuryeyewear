from django.db import models
from products.models import Product
import json

# this Cart class is used to handle cart data
# to prepate it for both the view and the session var
class Cart:
    def __init__(self, load=None):
        if load is not None:
            self.__reload(load)
        else:
            self.items = None
            self.__subtotal = 0.00
            self.__num_items = 0

    # this will get the stuff in the cart ready for the view (not done)
    def populate(self):
        new_list = {}

        for item in self.items:
            product_info = Product.objects.values(
                        'eyewear_id',
                        'name',
                        'image',
                        'promotional_price'
                      ).get(eyewear_id=item['id'])

            new_list += { item['id']: {
                    'name': product_info.name,
                    'img': product_info.image,
                    'price': product_info.promotional_price,
                    'quantity': item['quantity']
                }
            }

    def get(self):
        return json.dumps(self.__dict__)

    def __reload(self, instance):
        self.__dict__ = json.loads(instance)

    def addToCart(self, item):
        _id = item['id']
        num_added = item['quantity']

        if self.items is not None:
            if self.items[_id]:
                self.items[_id]['quantity'] += num_added

        self.items[_id] = item

    def deleteFromCart(self, item):
        _id = item['product_id']
        quantity_deleted = self.items[_id]['quantity']

        self.__num_items -= quantity_deleted
        self.__subtotal -= item['price'] * quantity_deleted

        del self.items[_id]

    def changeQuantity(self, product, new_quantity):
        _id = product['id']

        old_quantity = self.items[_id]['quantity']
        old_items_price = old_quantity * self.items[_id]['price']
        self.items[_id]['quantity'] = new_quantity

        pre_num_items = self.__num_items - old_quantity
        self.__num_items = pre_num_items + new_quantity
        pre_price = self.__subtotal - old_items_price
        self.__subtotal = pre_price + (self.items[_id]['price'] * new_quantity)

    def calculateSubTotal(self):
        running_total = 0
        for item in self.items:
            product_price = Product.objects.only('promotional_price').get(eyewear_id=item['id'])
            if product_price.promotional_price is None:
                product_price = Product.objects.only('price').get(eyewear_id=item['id'])

            running_total += product_price * item['quantity']
        return running_total



