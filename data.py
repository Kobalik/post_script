# Все отделения, где ключ это почтовый индекс, а значение это текстовое название

name_opc = {
    '231891': 'Волковыск-1',
    '231892': 'Волковыск-2',
    '231895': 'Волковыск-5',
    '231896': 'Волковыск-6',
    '231905': 'Верейки',
    '231916': 'Ендриховцы',
    '231921': 'Войтковичи',
    '231908': 'Волпа',
    '231901': 'Гнезно',
    '231913': 'Дубовцы',
    '231918': 'Дулевцы',
    '231922': 'Изабелин',
    '231911': 'Красносельский',
    '231926': 'Лапеница',
    '231924': 'Матвеевцы',
    '231902': 'Мстибово',
    '231920': 'Юбилейный',
    '231917': 'Мочулино',
    '231923': 'Подороск',
    '231912': 'Россь',
    '231915': 'Репля',
    '231909': 'Родники',
    '231927': 'Рупейки',
    '231907': 'Субочи',
    '231904': 'Шиловичи',
    '231894': 'ПОПС',
    '230415': 'Отдел_доставки',
    '230414': 'Бизнес_Почта',
    '231778': 'Берестовица-1',
    '231785': 'Большие_Эйсмонты',
    '231775': 'Кваторы',
    '231782': 'Конюхи',
    '231781': 'Макаровцы',
    '231780': 'Малая_Берестовица',
    '231788': 'Массоляны',
    '231784': 'Олекцищы',
    '231771': 'Пархимовцы',
    '231773': 'Пограничный',
    '231772': 'Поплавцы',
    '231776': 'Старый_Дворец',
    '231779': 'Берестовица_ПОПС',
    '231961': 'ПОПС–1_Свислочь',
    '231962': 'Гринки',
    '231963': 'Доброволя',
    '231964': 'Тиховоля',
    '231965': 'Незбодичи',
    '231967': 'Пацуи ',
    '231969': 'Свислочь-1',
    '231970': 'Ханчицы',
    '231971': 'Великое_Село',
    '231972': 'Вердомичи',
    '231980': 'Сокольники ',
    '231982': 'Порозово',
    '231983': 'Новый_Двор',
    '231985': 'Хоневичи',
    '231988': 'Корнадь',
    '231591': 'Мосты-1',
    '231592': 'Мосты-2',
    '231593': 'Мосты-3',
    '231594': 'Мосты-4',
    '231601': 'Мосты_ПОПС-1',
    '231602': 'Дубно',
    '231604': 'Мосты_ПОПС-3',
    '231605': 'Хартица',
    '231606': 'Лунна',
    '231607': 'Глядовичи',
    '231608': 'Стрельцы',
    '231609': 'Мосты_ПОПС-2',
    '231611': 'Микелевщина',
    '231613': 'Голубы',
    '231614': 'Куриловичи',
    '231615': 'Милевичи',
    '231616': 'Большие_Озерки',
    '231619': 'Правые_Мосты',
    '231621': 'Пески',
    '231622': 'Пацевичи',
    '231623': 'Большая_Рогозница',
    '231626': 'Гудевичи',
    '231630': 'Струбница',
    '230481': 'Торговая_секция'
}
# номер тиража
edition_number = input('Введите тираж (например "013", без пробелов и лишних символов):')

# Все билеты, где ключ это почтовый индекс, а значение номера билетов в списке
tickets = {}
all_tickets = []
for index in name_opc.keys():
    # try потому что существуют отделения без билетов
    try:
        # идём по всем файлам
        with open(f'loto\\{edition_number}-{index}.tos', 'r', encoding='utf-8') as file_tickets:
            # надо пропускать первую строчку, так как в ней не номер билета
            skipper = True
            # читаем построчно
            for ticket in file_tickets:
                # пропускаем
                if skipper:
                    skipper = False
                    continue
                # за ненадобностью убираем перенос строки
                ticket = ticket.replace('\n','')
                # есть пустые строчки, пропускаем их
                if ticket != '':
                    tickets.setdefault(index, []).append(ticket)
                    all_tickets.append(ticket)
    # если файла нет, т.е. билетов для этого отделения, просто пропускаем это отделение
    except:
        pass