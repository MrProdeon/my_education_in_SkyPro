def say_hello_to_user(name):
    """Получение имени и вывод приветствия"""
    return f'Привет, {name}, начинаем тренировку!'


def get_questions():
    """Просто возвращение словаря с уже известными данными"""
    return {
        'My name ___ Vova.' : 'is',
        'I ___ a coder.' : 'am',
        'I live ___ Moscow.' : 'in'
    }

def main():
    """Сборка всей программы"""
    score = 0
    correct_answer = 0

    name = input('Как тебя зовут? ---> ')
    # Проверяю, что имя записано букваи, а не цифрами и спец.символами
    while not name.isalpha():
        name = input('Как тебя зовут? Для ввода допускаются только буквы! ---> ')
    # Здороваюсь с пользователем
    print(say_hello_to_user(name))

    print('''Правила игры:
тебе поступает предложение и твоя задача - ввести недостающее слово.
За каждый правильный ответ - будет начисляться 10 баллов.''')
    # В переменную questions помещаю результат выполнения функции get_questions(), а именно словарь с вопросами и ответами
    questions = get_questions()
    #Для корректного подсчета номера вопроса - использую счетчик.
    question_number = 1

    # Прохожу по каждому вопросу и проверяю верный ли ответ дал пользователь.
    for i in questions:
        print(f'Вопрос № {question_number}. Чего здесь не хватает? {i}')
        question_number += 1
        answer = input().lower()
        while not answer.isalpha():
            answer = input('В предложении нехватает СЛОВА! Так чего же не хватает ---> ').lower()
        # Если да - увеличиваю счет и корректные ответы.
        if answer == questions.get(i):
            print('Правильно, молодец! Ты получаешь 10 баллов!')
            score += 10
            correct_answer += 1
        # Если нет - просто вывожу, что ответ неверный и выдаю верный ответ.
        else:
            print(f'К сожалению, неверно. Правильный ответ - {questions.get(i)}')

    #Кол-во вопросов = длина словаря с вопросами. 1 вопрос = 1 элемент словаря
    percentage_of_correct_answers = int(correct_answer / len(questions) * 100)
    # Прощаюсь и даю подсчёты.
    print(f'Вот и всё, {name}.\n'
          f'Количество верных ответов : {correct_answer}.\n'
          f'Ваш счет : {score}.\n'
          f'Процент правильных ответов : {percentage_of_correct_answers}.')

# Вызываю main(), чтобы всё заработало.
main()
