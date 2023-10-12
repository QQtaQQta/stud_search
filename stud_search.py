file_name = 'students_new.txt'
students = []
student_full_names = []

with open(file_name, 'r') as file:
    for line in file:
        q = number, student_full_name, var, group, qwertqeyqre = line.split(';')
        last_name, first_name, patronymic = student_full_name.split()
    
        student = {
            'number': number,
            'var': var,
            'group': group,
            'last_name': last_name,
            'first_name': first_name,
            'patronymic': patronymic,
        }
        students.append(student)
        
search_last_name = input('Введите фамилию студента: ')


for student in students:
    if student['last_name'] == search_last_name:
        poi = ''
        print('Найден студент:')
        print (f'Номер: {student["number"]}\nФамилия: {student["last_name"]}\nИмя: {student["first_name"]}\nОтчество: {student["patronymic"]}\nГруппа: {student["group"]}\nВариант: {student["var"]}\n')
        
        break
    else:
        poi= 'не '

print(f'Студент {poi}найден.')