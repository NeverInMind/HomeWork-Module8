from datetime import datetime


test = [{'name': 'Христина Зінчук', 'birthday': datetime(2020, 6, 6)},
        {'name': 'Нестор Авраменко',
            'birthday': datetime(1954, 7, 25)},
        {'name': 'Валентин Копитко',
            'birthday': datetime(1989, 11, 21)},
        {'name': 'Мирон Філіпенко',
            'birthday': datetime(1936, 6, 15)},
        {'name': 'Мартин Засенко',
            'birthday': datetime(1923, 2, 16)},
        {'name': 'пані Вікторія Каденюк',
            'birthday': datetime(1985, 8, 19)},
        {'name': 'Веніямин Ґалаґан',
            'birthday': datetime(1981, 2, 22)},
        {'name': 'Святослав Єфименко',
            'birthday': datetime(1965, 7, 18)},
        {'name': 'Ірина Дерегус',
            'birthday': datetime(1946, 2, 14)},
        {'name': 'Лариса Лупій', 'birthday': datetime(2020, 10, 30)}]


for item in test:
    brthday = item['birthday'].strftime('%A')
    print(brthday)
