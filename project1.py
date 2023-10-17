file_employees = open('employees.txt', encoding='utf-8', mode='r').read().replace(',', '').split('\n')
file_tasks = open('tasks.txt', encoding='utf-8', mode='r').read().replace(',', '').split('\n')
file_plans = open('plans.txt', encoding='utf-8', mode='w+')


# разделение работников по уровням
junior_employees = []
middle_employees = []
senior_employees = []

employees_without_levels = []

for i in range(len(file_employees)-1):                  #перебор всех строковых элементов в файле с работниками
    employee = ' '.join(file_employees[i].split(' '))          #разделение отдельно каждого элемента на строки по словам

    if 'junior' in file_employees[i]:
        junior_employees.append(file_employees[i])      #добавление в список по уровню
        employee = employee.replace('junior ', '')
        employees_without_levels.append(employee)       #удаление уровня из списка работника

    elif 'middle' in file_employees[i]:
        middle_employees.append(file_employees[i])
        employee = employee.replace('middle ', '')
        employees_without_levels.append(employee) 

    elif 'senior' in file_employees[i]:
        senior_employees.append(file_employees[i])
        employee = employee.replace('senior ', '')
        employees_without_levels.append(employee)
     

#разделение работников по скилам
java_employees = []
python_employees = []
proger_employees = []
analist_employees = []
tester_employees = []
r_employees = []
statistic_employees = []
html_employees = []

for i in range(len(file_employees)-1):
    
    if 'тестирование' in employees_without_levels[i]:
        tester_employees.append(file_employees[i])
        employees_without_levels[i] = employees_without_levels[i].replace('тестирование', '')                
    
    if 'java' in employees_without_levels[i]:
        java_employees.append(file_employees[i])
        employees_without_levels[i] = employees_without_levels[i].replace('java', '')

    if 'python' in employees_without_levels[i]:
        python_employees.append(file_employees[i])
        employees_without_levels[i] = employees_without_levels[i].replace('python', '')

    if 'программирование' in employees_without_levels[i]:
        proger_employees.append(file_employees[i])
        employees_without_levels[i] = employees_without_levels[i].replace('программирование', '')
                    
    if 'html' in employees_without_levels[i]:
        html_employees.append(file_employees[i])
        employees_without_levels[i] = employees_without_levels[i].replace('html', '')
                            
    if 'анализ' in employees_without_levels[i]:
        analist_employees.append(file_employees[i])
        employees_without_levels[i] = employees_without_levels[i].replace('анализ', '')
    
    if 'данных' in employees_without_levels[i]:
        employees_without_levels[i] = employees_without_levels[i].replace('данных', '')
    
    if 'R' in employees_without_levels[i]:
        r_employees.append(file_employees[i])
        employees_without_levels[i] = employees_without_levels[i].replace('R', '')
    
    if 'статистика' in employees_without_levels[i]:
        statistic_employees.append(file_employees[i])
        employees_without_levels[i] = employees_without_levels[i].replace('статистика', '')


names = sorted(employees_without_levels)


#разделение задач по уровням
junior_tasks = []
middle_tasks = []
senior_tasks = []

tasks_without_levels = []

for i in range(len(file_tasks)):
    task = ' '.join(file_tasks[i].split(' '))

    if 'junior' in file_tasks[i]:
        junior_tasks.append(file_tasks[i])    
        task = task.replace('junior ', '')
        tasks_without_levels.append(task)     

    elif 'middle' in file_tasks[i]:
        middle_tasks.append(file_tasks[i])
        task = task.replace('middle ', '')
        tasks_without_levels.append(task) 

    elif 'senior' in file_tasks[i]:
        senior_tasks.append(file_tasks[i])
        task = task.replace('senior ', '')
        tasks_without_levels.append(task)


#разделение задач по скилам
java_tasks = []
python_tasks = []
proger_tasks = []
analist_tasks = []
tester_tasks = []
r_tasks = []
statistic_tasks = []
html_tasks = []

for i in range(len(file_tasks)):
    
    if 'тестирование' in tasks_without_levels[i]:
        tester_tasks.append(file_tasks[i])
        tasks_without_levels[i] = tasks_without_levels[i].replace('тестирование', '')                
    
    if 'java' in tasks_without_levels[i]:
        java_tasks.append(file_tasks[i])
        tasks_without_levels[i] = tasks_without_levels[i].replace('java', '')

    if 'python' in tasks_without_levels[i]:
        python_tasks.append(file_tasks[i])
        tasks_without_levels[i] = tasks_without_levels[i].replace('python', '')

    if 'программирование' in tasks_without_levels[i]:
        proger_tasks.append(file_tasks[i])
        tasks_without_levels[i] = tasks_without_levels[i].replace('программирование', '')
                    
    if 'html' in tasks_without_levels[i]:
        html_tasks.append(file_tasks[i])
        tasks_without_levels[i] = tasks_without_levels[i].replace('html', '')
                            
    if 'анализ' in tasks_without_levels[i]:
        analist_tasks.append(file_tasks[i])
        tasks_without_levels[i] = tasks_without_levels[i].replace('анализ', '')
    
    if 'данных' in tasks_without_levels[i]:
        tasks_without_levels[i] = tasks_without_levels[i].replace('данных', '')
    
    if 'R' in tasks_without_levels[i]:
        r_tasks.append(file_tasks[i])
        tasks_without_levels[i] = tasks_without_levels[i].replace('R', '')
    
    if 'статистика' in tasks_without_levels[i]:
        statistic_tasks.append(file_tasks[i])
        tasks_without_levels[i] = tasks_without_levels[i].replace('статистика', '')


#проверка кто какую задачу может выполнить
for i in range(len(file_tasks)):
    for j in range(len(tester_employees)):
        if 'senior' in file_tasks[i] and 'тестирование' in file_tasks[i] and 'senior' in tester_employees[j]:
            print(file_tasks[i], ':', tester_employees[j])
        elif 'middle' in file_tasks[i] and 'тестирование' in file_tasks[i] and ('middle' in tester_employees[j] or 'senior' in tester_employees[j]):
            print(file_tasks[i], ':', tester_employees[j])
        elif 'junior' in file_tasks[i] and 'тестирование' in file_tasks[i] and ('junior' in tester_employees[j] or 'middle' in tester_employees[j] or 'senior' in tester_employees[j]):
            print(file_tasks[i], ':', tester_employees[j])

    for k in range(len(python_employees)):
        if 'senior' in file_tasks[i] and 'python' in file_tasks[i] and 'senior' in python_employees[k]:
            print(file_tasks[i], ':', python_employees[k])
        elif 'middle' in file_tasks[i] and 'python' in file_tasks[i] and ('middle' in python_employees[k] or 'senior' in python_employees[k]):
            print(file_tasks[i], ':', python_employees[k])
        elif 'junior' in file_tasks[i] and 'python' in file_tasks[i] and ('junior' in python_employees[k] or 'middle' in python_employees[k] or 'senior' in python_employees[k]):
            print(file_tasks[i], ':', python_employees[k])

    for l in range(len(java_employees)):
        if 'senior' in file_tasks[i] and 'python' in file_tasks[i] and 'senior' in java_employees[l]:
            print(file_tasks[i], ':', java_employees[l])
        elif 'middle' in file_tasks[i] and 'python' in file_tasks[i] and ('middle' in java_employees[l] or 'senior' in java_employees[l]):
            print(file_tasks[i], ':', java_employees[l])
        elif 'junior' in file_tasks[i] and 'python' in file_tasks[i] and ('junior' in java_employees[l] or 'middle' in java_employees[l] or 'senior' in java_employees[l]):
            print(file_tasks[i], ':', java_employees[l])
            