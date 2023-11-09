#читаем файл работников 
employees = open('employees.txt', encoding='utf-8', mode='r').read().split('\n')


#читаем файл задач
tasks = open('tasks.txt', encoding='utf-8', mode='r').read().split('\n')


levels = ['junior', 'middle', 'senior']


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
hours = []
hour = []
for i in range(len(words_tasks)):
    for j in range(len(words_tasks[i])):
        if words_tasks[i][j] in levels:
            skills_tasks.append(' '.join(words_tasks[i][j + 1:-1]))
            hours.append(int(tasks[i][-1]))
            hour.append(int(tasks[i][-1]))


#имя работника и скилы работника
names_employees = []
skills_employees = []
for i in range(len(employees)):
    if words_employees[i][3] in levels:
        names_employees.append(words_employees[i][0] + ' ' + words_employees[i][1] + ' ' + words_employees[i][2])
        skills_employees.append(' '.join(words_employees[i][4:]))
    elif words_employees[i][2] in levels:
        names_employees.append(words_employees[i][0] + ' ' + words_employees[i][1])
        skills_employees.append(' '.join(words_employees[i][3:]))


#уровень работника
level_employees = []
for i in employees:
    if 'junior' in i:
        level_employees.append(1)
    elif 'middle' in i:
        level_employees.append(2)
    elif 'senior' in i:
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


#сумма часов
sum_hours = [0] * len(employees)
sum_hour = 0
for i in range(len(employees)):
    for j in range(len(tasks)):
        if level_employees[i] >= level_tasks[j] and skills_tasks[j] in skills_employees[i]:
            sum_hour += hour[j]
            hour[j] = 0
            
            if sum_hour != 0:
                sum_hours[i] = sum_hour
            else:
                sum_hours[i] = 0    

        elif level_employees[i] <= level_tasks[j] and skills_tasks[j] not in skills_employees[i]:
                sum_hour = 0


#проверка на соответсвие уровня и скилов работника и задачи, запись списка задач в файл
can = []
cannot = [] 
plans = open('plans.txt', encoding='utf-8', mode='w+')
for i in range(len(employees)):
    if sum_hours[i] > 0:
        plans.write(f'{names_employees[i]} - {sum_hours[i]}\n')
    k = 0
    for j in range(len(tasks)):  
        
        if level_employees[i] >= level_tasks[j] and skills_tasks[j] in skills_employees[i]:
            
            can.append(names_tasks[j])                                  
            k += 1
            plans.write(f'{k}. {names_tasks[j]}- {hours[j]}\n')
            skills_tasks[j] = '    '

            
        elif level_employees[i] <= level_tasks[j] and skills_tasks[j] not in skills_employees[i]:
            c = 0
    plans.write('в\n')
        

                
#задачи, которые никто не может выполнить     
for i in range(len(names_tasks)):
    if names_tasks[i] not in can:
        cannot.append(names_tasks[i] + '- ' + str(hours[i]))      


#запись задач, которые никто не может решить в файл
plans.write('Задачи, которые никто не может решить:\n')
for i in range(len(cannot)):
    plans.write(f'{i + 1}. {cannot[i]} \n')




                
                



        





