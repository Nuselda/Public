import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
Список команд:
1. Добавить / удалить / редактировать оценки ученика по выбранному предмету      
2. Вывести средний балл по всем предметам по каждому ученику
3. Вывести все оценки по всем ученикам
4. Вывести все оценки ученика и средний балл по каждому предмету
5. Вывести оценки и средний балл всех учеников по выбранному предмету
6. Добавить / удалить ученика
7. Добавить / удалить предмет
8. Выход из программы
''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить / удалить / редактировать оценки ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            print(f''''
            1. Добавить оценки ученика {student} по предмету {class_}
            2. Удалить оценки ученика {student} по предмету {class_}
            3. Редактирвать оценки ученика {student} по предмету {class_}
            ''''')
            command_1 = int(input('Введите команду изменения оценок: '))
            if command_1 == 1:
                mark = int(input('Введите оценку: '))
                students_marks[student][class_].append(mark)
                print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
                print()
            elif command_1 == 2:
                for value in students_marks[student][class_]:
                    print(f'{students_marks[student][class_].index(value)} - {value}')
                index = int(input('Выберите индекс оценки для удадения: '))
                del_mark = students_marks[student][class_].pop(index)
                print(f'Для студента {student} по предмету {class_} удалены оценки {del_mark} Новые оценки {students_marks[student][class_]}')
                print()
            elif command_1 == 3:
                print(f'Редактирвать оценки ученика {student} по предмету {class_}')
                for value in students_marks[student][class_]:
                    print(f'{students_marks[student][class_].index(value)} - {value}')
                index = int(input('Выберите индекс оценки для редактирования: '))
                if index in range(2):
                    new_mark = int(input('Введите новое значение'))
                    students_marks[student][class_] = students_marks[student][class_][:index] + [new_mark] + \
                                                          students_marks[student][class_][index + 1:]
                    print(f'Для студента {student} по предмету {class_} отредактрованы оценки {students_marks[student][class_]}')
                    print()
                else:
                    print('ОШИБКА: неверный индекс оценки')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
        print()
    elif command == 4:
        print('Вывести все оценки ученика и средний балл по каждому предмету')
        student = input('Введите имя: ')
        for class_ in classes:
            marks_sum = sum(students_marks[student][class_])
            marks_count = len(students_marks[student][class_])
            print(f'{class_} - {students_marks[student][class_]} - {marks_sum // marks_count}')
            print()
    elif command == 5:
        print('5. Вывести оценки и средний балл всех учеников по выбранному предмету')
        class_ = input('Введите предмет: ')
        if class_ in students_marks[student].keys():
            avg_sum = 0
            avg_count = 0
            for student in students:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{student} - {students_marks[student][class_]} - {marks_sum // marks_count}')
                avg_sum += marks_sum
                avg_count += marks_count
            print()
            print(f'Общий средний балл: {avg_sum // avg_count}')
            print()
        else:
            print('ОШИБКА: неверное название предмета')
    elif command == 6:
        print('Добавить / удалить ученика:')
        student = input('Введите имя ученика: ')
        if student in students and student in students_marks.keys():
            students.remove(student)
            del students_marks[student]
            print(f'Ученик {student} был удален из журнала')
        else:
            students.append(student)
            students_marks.setdefault(student)
            students_marks[student] = {}
            for class_ in classes:
                students_marks[student][class_] = []
            print(f'Ученик {student} Добавлен в журнал')
            print(f'''{student}
{students_marks[student]}''')
            print()
    elif command == 7:
        print('Добавить / удалить предмет:')
        class_ = input('Введите предмет: ')
        if class_ in students_marks[student].keys():
            classes.remove(class_)
            print(f'Предмет {class_} удален из журнала')
        else:
            classes.append(class_)
            for student in students:  # 1 итерация: student = 'Александра'
                students_marks[student][class_] = []
            print(f'Предмет {class_} добавлен в журнал')
            print(f'Список предметов {classes}')
    elif command == 8:
        print('7. Выход из программы')
        break