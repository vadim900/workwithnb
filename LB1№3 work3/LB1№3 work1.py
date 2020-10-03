
koloda = [6,7,8,9,10,2,3,4,11] * 4

import random
random.shuffle(koloda)

print('Пограємо в очко?')
count = 0

while True:
    choice = input('Будете брати карту? y/n\n')
    if choice == 'y':
        current = koloda.pop()
        print('Вам попалася карта гідністю %d' %current)
        count += current
        if count > 21:
            print('Вибачте, але ви програли')
            break
        elif count == 21:
            print('Вітаю, ви набрали 21!')
            break
        else:
            print('У вас %d балів.' %count)
    elif choice == 'n':
        print('У вас %d балів і ви закінчили гру.' %count)
        break

print('До нових зустрічей!')
