# @author: Berke Altıparmak
# You may use, distribute and modify this code under the
# terms of the Beerware license, which unfortunately won't be
# written for another century.
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <berkealtiparmak@outlook.com> wrote this file.  As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return.   Berke Altıparmak
# ----------------------------------------------------------------------------
#


import random
import math

class Phone:
    def __init__(self, price, point):
        self.price = price
        self.point = point


def decide():
    phonearr = [Phone(random.randint(300, 2000), random.randint(2, 10))
                for x in range(100)]
    phoneprice = []
    phonepoint = []

    for x in range(100):
        phoneprice.append(phonearr[x].price)
        phonepoint.append(phonearr[x].point)

    for x in range(100):
        if phoneprice[x] < 1000 and phonepoint[x] > 7:
            print(
                f'Buy this phone; Price:{phoneprice[x]}, Point:{phonepoint[x]}')


if __name__ == '__main__':
    decide()
