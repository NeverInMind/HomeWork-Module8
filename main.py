from datetime import datetime, timedelta


test = [{'name': 'Христина Зінчук', 'birthday': datetime(2020, 6, 6)},
        {'name': 'Нестор Авраменко',
            'birthday': datetime(1954, 6, 21)},
        {'name': 'Валентин Копитко',
            'birthday': datetime(1989, 11, 21)},
        {'name': 'Мирон Філіпенко',
            'birthday': datetime(1936, 6, 25)},
        {'name': 'Мартин Засенко',
            'birthday': datetime(1923, 2, 16)},
        {'name': 'пані Вікторія Каденюк',
            'birthday': datetime(1985, 6, 25)},
        {'name': 'Веніямин Ґалаґан',
            'birthday': datetime(1981, 2, 22)},
        {'name': 'Святослав Єфименко',
            'birthday': datetime(1965, 7, 18)},
        {'name': 'Ірина Дерегус',
            'birthday': datetime(1946, 2, 14)},
        {'name': 'Лариса Лупій', 'birthday': datetime(2020, 10, 30)}]


days_of_week = {
    'Monday': [],
    'Tuesday': [],
    'Wednesday': [],
    'Thursday': [],
    'Friday': [],
    'Saturday': [],
    'Sunday': [],

}


def get_birthdays_per_week():
    for item in test:
        brthday = item['birthday'].strftime('%A')
        today = datetime.now()
        timedel = timedelta(days=7)
        if today.month == item['birthday'].month:
            if item['birthday'].day >= today.day and item['birthday'].day <= \
                    (today + timedel).day:
                brthday = datetime(
                    today.year, item['birthday'].month, item['birthday'].day).strftime('%A')
                find = days_of_week[brthday]
                find.append(item['name'])

    for keys, value in days_of_week.items():
        if value != []:
            res = ', '.join(value)
            print(f'{keys}: {res}')


get_birthdays_per_week()
