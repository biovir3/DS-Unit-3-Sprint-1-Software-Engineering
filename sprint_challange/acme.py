#!/usr/bin/env python

import random

class Product:

    def __init__(self,
                 name = '',
                 price = 10,
                 weight = 20,
                 flamibility = 0.5,
                 identifier = 0):

        self.name = name
        self.price = price
        self.weight = weight
        self.flamibility = flamibility
        self.identifier = random.randint(1000000,9999999)

    def stealability(self):

        stealable = self.price/self.weight

        if(stealable < 0.5):
            return('Not so stealable...')
        elif((stealable >= 0.5) and (stealable < 1.0)):
            return('Kinda stealable.')
        else:
            return('Very stealable!')

    def explode(self):
        flame = self.flamibility * self.weight

        if(flame < 10):
            return('...fizzle.')
        elif((flame >= 10) and (flame < 50)):
            return('...boom!')
        else:
            return('...BABOOM!!')

class BoxingGlove(Product):

    def __init__(self,
                name = '',
                price = 0,
                weight = 0,
                flamibility = 0,
                identifier = 0):

        super().__init__(name,price,weight,flamibility,identifier)
        self.weight = 10

    def explode(self):
        return '...it\'s a glove.'

    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif (self.weight >= 5) and (self.weight < 15):
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
