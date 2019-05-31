#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    products = []
    # TODO - your code! Generate and add random products.
    for _ in range(0,num_products):
        name = (ADJECTIVES[randint(0,(len(ADJECTIVES)-1))] + ' ' + NOUNS[randint(0,(len(ADJECTIVES)-1))])

        price=randint(5,100)
        weight=randint(5,100)
        flamibility=round(uniform(0.0,2.5),1)

        products.append(Product(name,price,weight,flamibility))
    return products


def inventory_report(products):
    unique_names = []
    count_unique = {}

    for prod in products:
        if prod.name not in unique_names:
            unique_names.append(prod)
            count_unique.update({prod.name:1})
        else:
            count_unique.update({prod.name: count_unique.get(prod.name)+1})


    price_mean = sum([p.price for p in products])
    weight_mean = sum([p.weight for p in products])
    flamibility_mean = sum([p.flamibility for p in products])

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names ', len(count_unique))
    print('Average price ', price_mean)
    print('Average weight ', weight_mean)
    print('Average flamibility ', round(flamibility_mean,1))


if __name__ == '__main__':
    inventory_report(generate_products())
