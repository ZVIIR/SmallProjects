#! python3
# randomQuizGenerator - создаёт билеты с вопросами и ответами,
# расположенными в случайном порядке, вместе с ключами ответов

import random
# Данные билетов: ключи - названия штатов, а значения - столицы
capitals = {'Айдахо': 'Бойсе', 'Айова': 'Де-Мойн', 'Алабама': 'Монтгомери',
            'Аляска': 'Джуно', 'Аризона': 'Финикс', 'Арканзас': 'Литл-Рок',
            'Вайоминг': 'Шайенн', 'Вашингтон': 'Олимпия', 'Вермонт': 'Монтпилиер',
            'Виргиния': 'Ричмонд', 'Висонсин': 'Мадисон', 'Гавайи': 'Гонолулу',
            'Делавэр': 'Довер', 'Джорджия': 'Атланта', 'Западная Виргиния': 'Чарлстон',
            'Иллинойс': 'Спрингфилд', 'Индиана': 'Индианаполис', 'Калифорния': 'Сакраменто',
            'Канзас': 'Топика', 'Кентукки': 'Франкфорт', 'Колорадо': 'Денвер', 'Коннектикут': 'Хартфорд',
            'Луизиана': 'Батон-Руж', 'Массачусетс': 'Бостон', 'Миннесота': 'Сент-Пол', 'Миссисипи': 'Джэксон',
            'Миссури': 'Джефферсон-Сити', 'Мичиган': 'Лансинг', 'Монтана': 'Хелена', 'Мэн': 'Огаста',
            'Мэриленд': 'Аннаполис', 'Небраска': 'Линкольн', 'Невада': 'Карсон-Сити', 'Нью-Джерси': 'Трентон',
            'Нью-Йорк': 'Олбани', 'Нью-Мексико': 'Санта-Фе', 'Нью-Гемпшир': 'Конкорд', 'Огайо': 'Колумбус',
            'Оклахома': 'Оклахома-Сити', 'Орегон': 'Сейлем', 'Пенсильвания': 'Гаррисберг', 'Род-Айленд': 'Провиденс',
            'Северная Дакота': 'Бисмарк', 'Северная Каролина': 'Роли', 'Теннесси': 'Нашвилл', 'Техас': 'Остин',
            'Флорида': 'Таллахасси', 'Южная Дакота': 'Пирр', 'Южная Каролина': 'Колумбия', 'Юта': 'Солт-Лейк-Сити'}

#Генерирование 35 файлов билетов
for quizNum in range(35):
    #Создание файлов и ключей ответов
    quizFile = open(f'capitalquiz{quizNum + 1}.txt','w')
    answerKeyFile = open(f'capitalquiz_answers{quizNum + 1}.txt', 'w')

    #Запись заголовка билета
    quizFile.write('Имя:\n\nДата:\n\nГруппа:\n\n')
    quizFile.write((' ' * 20) + f'Столицы штатов (билет {quizNum + 1})')
    quizFile.write('\n\n')

    #Перемешевание порядка следования штатов
    states = list(capitals.keys())
    random.shuffle(states)

    # Организация цикла по всем 50 штатам
    # и создание вопроса для каждого из них
    for questionNum in range(50):
        # Получение правильных и неправильных ответов
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Запись вариантов вопросов и ответов в файл билета
        quizFile.write(f'{questionNum + 1}. Выберете столицу штата {states[questionNum]}.\n\n')
        for i in range(4):
            quizFile.write(f"   {'АБВГ'[i]}. {answerOptions[i]}\n")
            quizFile.write('\n')

            # Запись ключа ответа в файл
            answerKeyFile.write(f"{questionNum + 1}. {'АБВГ'[answerOptions.index(correctAnswer)]}\n")
    quizFile.close()
    answerKeyFile.close()