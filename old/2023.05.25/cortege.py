marks_club = [
    # ИСПОЛЬЗОВАТЬ: удобный для чтения способ записи вложенных структур данных
    {
        'user_id': 1,
        'name': 'Василий',
        'marks_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 12, 15, 15, 22, 124, 23, 23, 22, 28]
    },
    {
        'user_id': 2,
        'name': 'Петр',
        'marks_id': [1, 2, 3, 4, 8, 6, 7, 18, 9, 9, 12, 15, 13, 22, 122, 23, 23, 22, 28]
    },
    {
        'user_id': 3,
        'name': 'Мария',
        'marks_id': [1, 12, 3, 7, 5, 6, 7, 8, 9, 9, 12, 15, 15, 22, 126, 23, 23, 22, 128]
    },
    {
        'user_id': 4,
        'name': 'Дарья',
        'marks_id': [1, 2, 13, 4, 15, 6, 7, 8, 9, 6, 12, 15, 15, 22, 124, 23, 23, 122, 28]
    },
    {
        'user_id': 5,
        'name': 'Алексей',
        'marks_id': [1, 2, 13, 4, 5, 126, 7, 8, 29, 92, 132, 15, 165, 22, 124, 23, 223, 22, 28]
    },
]
# ИСПОЛЬЗОВАТЬ: создание такой длинной строки лучше выполнить отдельной инструкцией
prompt = '''1. Посмотреть список уникальных марок, которые есть в нашем клубе'
2. Посмотреть список уникальных марок, которые есть у конкретного пользователя по его ID
3. Получить два ID пользователей и вывести список марок, которые есть у каждого из них, но при этом нет у другого

Введите номер запроса: '''
# ИСПОЛЬЗОВАТЬ: PEP 8 рекомендует размещать комментарии над комментируемой строчкой кода
# Пользовательский ввод
user_input = int(input(prompt))


# 1. Посмотреть список уникальных марок которые есть в нашем клубе
def full_list():
    all_marks = []
    for member_club in marks_club:
        for marks_id in member_club['marks_id']:
            if marks_id not in all_marks:
                all_marks += [marks_id]
    print(all_marks)


# 2. Посмотреть список уникальных марок которые есть у конкретного пользователя(по его ID)
def stamp_collection():
    input_user = int(input('введите id участника клуба: '))
    for member_club in marks_club:
        if input_user == member_club['user_id']:
            print(member_club['marks_id'])


#  3. Получить два ID пользователей и вывести список марок которые есть у каждого из них, но при этом нет у другого;
def compare_two_collections():
    input_id_1 = input("Введите ID первого пользователя: ")
    input_id_2 = input("Введите ID второго пользователя: ")
    
    marks_id_1 = set()
    marks_id_2 = set()
    
    for member in marks_club:
        if member['user_id'] == int(input_id_1):
            marks_id_1.update(member['marks_id'])
        elif member['user_id'] == int(input_id_2):
            marks_id_2.update(member['marks_id'])
    
    unique_marks_1 = marks_id_1 - marks_id_2
    unique_marks_2 = marks_id_2 - marks_id_1
    
    print(f"Уникальные марки у пользователя с ID {input_id_1}: {list(unique_marks_1)}")
    print(f"Уникальные марки у пользователя с ID {input_id_2}: {list(unique_marks_2)}")


match user_input:
    # если введено 1 работает первая функция
    case 1:
        full_list()
    # если введено 2 работает вторая функция
    case 2:
        stamp_collection() 
    # если введено 3 работает третья функция
    case 3:
        compare_two_collections() 
    case _:
        print('введено что-то другое')


# КОММЕНТАРИЙ: PEP 8 — сборник рекомендаций по стилистическому оформлению Python кода — их стоит использовать для большего удобства чтения своего и чужого кода: https://peps.python.org/pep-0008/

