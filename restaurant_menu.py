#/usr/bin/env python
# -*- coding: utf-8 -*-

print '***RESTAURANT MENU***'

menu = {}

while True:
    daily_menu = raw_input('Enter a daily menu food: ')
    price = float(raw_input('Please enter the price for %s: ' % daily_menu))
    menu[daily_menu] = [price]

    new = raw_input('Would you like to add new food? y/n ')
    if new != 'y':
        break



print 'Your daily menu is: %s' % menu

with open("menu.txt", "w+") as menu_file:
    for food in menu:
        menu_file.write("%s, %s €\n" % (food, menu[food]))
