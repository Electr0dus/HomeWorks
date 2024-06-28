'''
---------------------
В данном проекте буду использовать
библиотеку для визуализации данных matplotlib
---------------------
Данная библиотека нужна для задач представления данных в удобочитаемой форме
в виде таблиц, графиком, диаграмм и прочее
'''

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fruits = ['Яблоки', 'Голубика', 'Вишня',  'Апельсин']
counts_fruits = []

for i in range(4):
    counts_fruits.append(int(input(f'Введите колличество {fruits[i]}: ')))

bar_labels = ['Яблоки', 'Голубика', 'Вишня', 'Апельсин']
bar_colors = ['tab:green', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(fruits, counts_fruits, label=bar_labels, color=bar_colors)

ax.set_ylabel('Кол-во фруктов')
ax.set_title('Пример визуализации кол-во фруктов')
ax.legend(title='Фрукты с соответсвием их цветов')
plt.show()
# Данная библиотека очень просто позволяет визуализировать данные любого рода