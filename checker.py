from data import edition_number, tickets, name_opc, all_tickets

file = f'{edition_number}_unfinded_tickets.txt'
unchecked_file = f'{edition_number}_unchecked.txt'
unfinded_tickets = []
try:
    with open(file, 'r') as f:
        for line in f:
            unfinded_tickets.append(line.replace('\n',''))
except: pass

def unfinded(input_ticket):
    if input_ticket not in unfinded_tickets:
        unfinded_tickets.append(input_ticket)
        print('Не найдено!')
        return
    print('Такой уже есть в не найденых!')

def find_ticket(input_ticket):
    for index in name_opc:
        try:
            for ticket in tickets[index]:
                if input_ticket == ticket:
                    print(f'Есть такой! На отделении "{name_opc[index]}"')
                    all_tickets.remove(input_ticket)
                    return
        except: continue
    unfinded(input_ticket)

def run():
    while True:
        input_value = input('Введите номер билета(например "0130123039") или 0 для выхода:').replace(' ', '')
        if not input_value.isnumeric():
            print("Вы ввели не число. Попробуйте снова!")
            continue
        if input_value == '0':
            return
        if len(input_value) == 10:
            find_ticket(input_value)
            continue
        print('Неверный номер билета!')

def write_in_file(value_list, file):
    with open(file, 'w') as f:
        for value in value_list:
            f.write(f'{value}\n')

def write_unchecked(value_list, file):
    if all_tickets:
        print('Не проверенные билеты:')
        with open(file, 'w', encoding='utf-8') as f:
            for index in tickets:
                try:
                    for value in value_list:
                        if value in tickets[index]:
                            for ticket in tickets[index]:
                                if value == ticket:
                                    f.write(f'{name_opc[index]} - {value}\n')
                                    print(f'{name_opc[index]} - {value}')
                except: pass
    else:
        print("Все билеты проверены!")


run()
write_in_file(unfinded_tickets, file)
write_unchecked(all_tickets,unchecked_file)
input('Для завершения работы нажмите Enter.')