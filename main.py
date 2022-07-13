# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

pc_v = list(map(float, per_cent.values()))

money = input("Введите сумму вклада:")
money = float(money)

deposit = list(map(lambda x: x*money/100, pc_v))

print("Максимальная сумма, которую вы можете заработать —", round(max(deposit), 2))