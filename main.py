import warnings

import universal
import db

warnings.filterwarnings("ignore")


def check_any_sumb_in_str():
    string = input('Строка: ')
    if len(string) != 0:
        print('Симовлы есть')
        db.save_result('Наличие символов', '+')
    else:
        print('Символов нет', '-')
    return

def ch_nch_min_nch():
    n = int(input('n: '))
    ch = []
    nch = []
    for i in range(n):
        a = int(input(str(i) + ': '))
        if a % 2 == 0:
            ch.append(a)
        else:
            nch.append(a)
    print(ch, nch, min(nch), sep='\n')
    db.save_result('min(nechet)', min(nch))
    return

def dictionary_month():
    month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    dict_month = dict(zip(month, range(1, 13)))
    print(dict_month)
    db.save_result('month', dict_month)
    return

def main():
    run = True
    commands = """==========================================================================
1. Создать таблицу в MySQL.
2. Проверка символа в строке с клавиатуры, сохранение и вывод из MySQL.
3. Поиск наименьшего нечетного числа, сохранение и вывод из MySQL.
4. Создание словаря, сохранение и вывод из MySQL.
5. Сохранить данные из MySQL в Excel и вывести на экран.
6. Завершить"""
    while run:
        run = universal.uni(commands, 
                      db.check_db, check_any_sumb_in_str, ch_nch_min_nch,
                      dictionary_month, db.save_db_to_xlxs)
    return

if __name__ == '__main__':
    main()