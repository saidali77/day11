# -*- coding: utf-8 -*-
guests = ['Saidali', 'Abdulla', 'Imran']
a = guests.pop()
print(a)

guests.insert(2, 'Emir')


guests.insert(0, 'Bekjan')
guests.insert(2, 'Astan')
guests.insert(5, 'Anton')

print('Я приглашаю на обед ' + guests[0])
print('Я приглашаю на обед ' + guests[1])
print('Я приглашаю на обед ' + guests[2])
print('Я приглашаю на обед ' + guests[3])
print('Я приглашаю на обед ' + guests[4])
print('Я приглашаю на обед ' + guests[5])

print("Список моих гостей разширяется")