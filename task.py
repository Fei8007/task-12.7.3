money = int(input('Введите сумму депозита: '))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

percent_arr = list(per_cent.values())

deposit = []

for value in percent_arr:
    deposit.append(int(value * money / 100))

print('Максимальная сумма, которую вы можете заработать — %d' % max(deposit))
