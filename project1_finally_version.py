#читаем файл работников 
file_employees = open('employees.txt', encoding='utf-8', mode='r')
f = file_employees.read()
employees = ' '.join([x for x in f.split(" ") if x]).split('\n')


#читаем файл задач
file_tasks = open('tasks.txt', encoding='utf-8', mode='r')
tasks = file_tasks.read().split('\n')


#задаем список с уровнями
levels = ['junior', 'middle', 'senior']


#проверка файла работников и задач на пустоту
if len(employees) > 1 and len(tasks) > 1:

    #сортировка работников по уровню
    for i in range(len(employees)):
        if 'junior' in employees[i]:
            employees[i] = '1 ' + employees[i]
        elif 'middle' in employees[i]:
            employees[i] = '2 ' + employees[i]
        elif 'senior' in employees[i]:
            employees[i] = '3 ' + employees[i]
    employees.sort()


    #разбиение работников на слова
    words_employees = []
    for i in range(len(employees)):
        words_employees.append(employees[i].split(' '))


    #удаление запятых из скилов работников
    for i in range(len(words_employees)):
        for j in range(len(words_employees[i])):
            if ',' in words_employees[i][j]:
                words_employees[i][j] = words_employees[i][j].rstrip(',')


    #разбиение задач на слова
    words_tasks = []
    for i in range(len(tasks)):
        words_tasks.append(tasks[i].split(' '))


    #удаление запятых из скилов задач
    for i in range(len(words_tasks)):
        for j in range(len(words_tasks[i])):
            if ',' in words_tasks[i][j]:
                words_tasks[i][j] = words_tasks[i][j].rstrip(',')


    #скилы задач и время на их выполнение
    skills_tasks = []
    hours = [] #для вывода в конце
    hour = [] #для подсчета суммы часов
    for i in range(len(words_tasks)):
        for j in range(len(words_tasks[i])):
            if words_tasks[i][j] in levels:
                skills_tasks.append(' '.join(words_tasks[i][j + 1:-1]))
                hours.append(int(tasks[i].split()[-1]))
                hour.append(int(tasks[i].split()[-1]))


    #имя работника и скилы работника
    names_employees = []
    skills_employees = []
    for i in range(len(employees)):
        if words_employees[i][4] in levels:
            names_employees.append(words_employees[i][1] + ' ' + words_employees[i][2] + ' ' + words_employees[i][3])
            skills_employees.append(' '.join(words_employees[i][5:]))
        elif words_employees[i][3] in levels:
            names_employees.append(words_employees[i][1] + ' ' + words_employees[i][2])
            skills_employees.append(' '.join(words_employees[i][4:]))


    #уровень работника
    level_employees = []
    for i in range(len(employees)):
        if 'junior' in employees[i]:
            level_employees.append(1)
        elif 'middle' in employees[i]:
            level_employees.append(2)
        elif 'senior' in employees[i]:
            level_employees.append(3)


    #уровень задач
    level_tasks = []
    for i in tasks:
        if 'junior' in i:
            level_tasks.append(1)
        elif 'middle' in i:
            level_tasks.append(2)
        elif 'senior' in i:
            level_tasks.append(3)


    #выделение названия задачи
    names_tasks = []
    for i in range(len(tasks)):
        if 'junior' in tasks[i]:
            names_tasks.append(tasks[i].split('junior')[0])
        elif 'middle' in tasks[i]:
            names_tasks.append(tasks[i].split('middle')[0])
        elif 'senior' in tasks[i]:
            names_tasks.append(tasks[i].split('senior')[0])


    #функция для проверки соответствия скилов задач и работника
    def contain(a, b):
        c = 0
        for i in a:
            if i not in b:
                c = 1
        if c == 1:
            return 0
        return 1


    #сумма часов
    sum_hours = [0] * len(employees)
    sum_hour = 0
    for i in range(len(employees)):
        for j in range(len(tasks)):
            if level_employees[i] >= level_tasks[j] and contain(skills_tasks[j].split(), skills_employees[i].split()) == 1:

                sum_hour += hour[j]
                hour[j] = 0

                if sum_hour == 0:
                    sum_hours[i] = 0 
                else:
                    sum_hours[i] = sum_hour
        sum_hour = 0
        

    #проверка на соответсвие уровня и скилов работника и задачи, запись списка задач в файл
    can = []
    cannot = [] 
    plans = open('plans.txt', encoding='utf-8', mode='w+')       
    for i in range(len(employees)):
        plans.write(f'{names_employees[i]} - {sum_hours[i]}\n')
        if sum_hours[i] == 0:
            plans.write('>>> Пока на расслабоне, на чиле\n')
        k = 0
        for j in range(len(tasks)):  
            if level_employees[i] >= level_tasks[j] and contain(skills_tasks[j].split(), skills_employees[i].split()) == 1:
                can.append(names_tasks[j])
                k += 1
                plans.write(f'{k}. {names_tasks[j]}- {hours[j]}\n')
                skills_tasks[j] = 'Распределено'     
        plans.write('\n')

                    
    #задачи, которые никто не может выполнить     
    for i in range(len(names_tasks)):
        if names_tasks[i] not in can:
            cannot.append(names_tasks[i] + '- ' + str(hours[i]))  


    #работники без задач
    plans.write('Работники без задач:\n')
    x = 0
    for i in range(len(sum_hours)):
        if sum_hours[i] == 0:
            x += 1
            plans.write(f'{x}. {names_employees[i]}\n')  
    plans.write('\n')  


    #запись задач, которые никто не может решить в файл
    plans.write('Задачи, которые никто не может решить:\n')
    if len(cannot) > 0:
        for i in range(len(cannot)):
            plans.write(f'{i + 1}. {cannot[i]} \n')
    else:
        plans.write('>>> Таких задач нет\n')
    plans.write('\n')


    #полезная информация
    plans.write('>>> Полезная информация <<<\n')
    plans.write(f'Количество задач, которые можно выполнить: {len(can)}\n')
    plans.write(f'Количество задач, которые нельзя выполнить: {len(cannot)}\n')
    plans.write(f'Общее время на выполнение всех задач: {sum(sum_hours)}\n')

    
    #закрытие всех файлов
    file_employees.close()
    file_tasks.close()
    plans.close()


elif len(employees) <= 1 and len(tasks) <= 1:
    plans = open('plans.txt', encoding='utf-8', mode='w+') 
    plans.write('>>> ОШИБКА\n')   
    plans.write('Файл работников и файл задач являются пустыми')
    plans.close()
elif len(employees) <= 1:
    plans = open('plans.txt', encoding='utf-8', mode='w+') 
    plans.write('>>> ОШИБКА\n')    
    plans.write('Файл работников является пустым')
    plans.close()
elif len(tasks) <= 1:
    plans = open('plans.txt', encoding='utf-8', mode='w+') 
    plans.write('>>> ОШИБКА\n')    
    plans.write('Файл задач является пустым')
    plans.close()
