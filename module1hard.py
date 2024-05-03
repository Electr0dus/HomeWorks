grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sort_students = sorted((students))  # Отсортированный в алфавитном порядке список
new_students = {}
new_grades = []  # Для хранения среднего бала
lenght_ = len(grades)  # Для хранения длины всего списка
count = 0  # Счётчик списка
while count < lenght_:
    new_grades.append(sum(grades[count]) / len(grades[count]))
    count += 1
for i in range(5):
    new_students[sort_students[i]] = new_grades[i]
print(new_students)
