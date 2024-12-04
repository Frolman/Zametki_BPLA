file_name = "bpla_notes.txt" # Имя файла для сохранения

def sozdanie_zametki(): # Создание заметками
    Zametka_Model=input ('Введите модель БПЛА')
    Zametka_Motors = int (input('Введите количество двигателей БПЛА'))
    Zametka_Ves = int(input('Введите вес БПЛА'))
    Zametka_Skorost = int (input('Введите максимальную скорость БПЛА'))
    Zametka_Primechaniya = input ('Введите примечание')
    Zametka_str = f'{Zametka_Model} | {Zametka_Motors} | {Zametka_Ves} | {Zametka_Skorost} | {Zametka_Primechaniya} |' #Разделитель |
    try:
       with open (file_name, 'a') as bpla_file: # Добавляем заметку в текстовый файл
           bpla_file.write(Zametka_str+'\n')
    except:
        print ('Произошла ошибка!') # Это чтобы знать об ошибках
     
 
# чтение заметок
def chtenie_zametki():
    try:
        with open (file_name, 'r') as bpla_file:
            Zametka_str = bpla_file.readlines() # Построчное считывание
            if not Zametka_str: # Если заметок нет
                print ('В файле пусто!')
            else:
                print("Список заметок о БПЛА")
                for nomer in range (1, len(Zametka_str)+1):
                    Zametka = Zametka_str[nomer-1].strip()
                    print(f'{nomer}.{Zametka}')
    except FileNotFoundError:# Если не нашли файл с заметками
        print ("файл с заметками не найден")            

def glavnoe_menu():#Главное меню
    while True:
        print ('====Меню программы====')
        print ('0 Создать заметку о БПЛА')
        print ('1 Посмотреть заметку о БПЛА')
        print ('2 Закончить работу с заметками о БПЛА')
        Vibor = input('Выберите 0 - 2)')
        if Vibor == '0': 
            sozdanie_zametki()
        elif Vibor == '1':
            chtenie_zametki()
        elif Vibor == '2':
            break #прерывание цикла
        else:
            print ('Некорректный выбор.')
            
glavnoe_menu()