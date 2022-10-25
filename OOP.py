Object_list = []

class Car():
    door = 'Двери_закрыты'
    light = "Фары_выключены"
    Name = None
    Maker = None
    Year = None
    Colour = None
    Price = None
    Condition = None
    KP = None
    def __init__(self, all_char):
        self.Name = all_char[0]
        self.Maker = all_char[1]
        self.Year = all_char[2]
        self.Colour = all_char[3]
        self.Price = all_char[4]
        self.Condition = all_char[5]
        self.KP = all_char[6]
        if(len(all_char)==8):
            self.door=all_char[7]
        if(len(all_char)==9):
            self.door = all_char[7]
            self.light=all_char[8]

    def save(self):
        save = str(self.Name) + ' ' + str(self.Maker) + ' ' + str(self.Year) + ' ' + str(self.Colour) + ' ' + str(
            self.Price) + ' ' + str(
            self.Condition) + ' ' + str(self.KP) + ' ' + self.door + ' ' + self.light
        self.view = save


class Menu():
    @staticmethod
    def read():
        f=open("data.txt")
        for s in f:
            print(s.split())
            Object_list.append(Car(s.split()))
        f.close()

    @staticmethod
    def Save():
        f = open("data.txt",'w')
        for s in Object_list:
            s.save()
            f.write(s.view+'\n')
        f.close()
    @staticmethod
    def start():
        inp = input("Команды: добавить смотреть стоп" + '\n')
        if (inp == "добавить"):
            Menu.Add()
        elif (inp == "смотреть"):
            Menu.See()
        elif (inp == "стоп"):
            return 0
        else:
            Menu.start()

    @staticmethod
    def Add():
        inp = input("Введите по порядку через пробел:Название Производитель Год Цвет Цена Состояние КП" + '\n')
        if (len(inp.split())==7):
            Object_list.append(Car(inp.split()))
            Menu.start()
        else:
            print("Заполните правильно!!!"+'\n')
            Menu.Add()

    @staticmethod
    def See():
        if len(Object_list) > 0:
            i = 1
            for s in Object_list:
                s.save()
                print(str(i) + ')' + s.view)
                i += 1
            i = int(input())
            if(i==0):Menu.start()
            if (i > 0 and i <= len(Object_list)):
                Object_list[i - 1].save()
                print(Object_list[i - 1].view)
                inp = input('\n' + "Выберите опцию:" + '\n' + "изменить" + '\n' + "удалить" + '\n')
                if (inp == 'изменить'):
                    Menu.Change(i - 1)
                elif (inp == 'удалить'):
                    Menu.Delete(i - 1)

        else:
            print('Машин нет'+'\n')
            Menu.start()

    @staticmethod
    def Change(i):
        inp=input("Наберите название параметра"+'\n')
        if(inp=="название"):
            Object_list[i].Name=input('Введите замену'+'\n')
            Menu.start()
        elif (inp == "производитель"):
            Object_list[i].Maker = input('Введите замену' + '\n')
            Menu.start()
        elif (inp == "год"):
            Object_list[i].Year = input('Введите замену' + '\n')
            Menu.start()
        elif (inp == "цвет"):
            Object_list[i].Colour = input('Введите замену' + '\n')
            Menu.start()
        elif (inp == "цена"):
            Object_list[i].Price = input('Введите замену' + '\n')
            Menu.start()
        elif (inp == "состояние"):
            Object_list[i].Condition = input('Введите замену' + '\n')
            Menu.start()
        elif (inp == "кп"):
            Object_list[i].KP = input('Введите замену' + '\n')
            Menu.start()
        elif (inp == "двери"):
            Object_list[i].door = ("Двери_"+input('Введите замену' + '\n'))
            Menu.start()
        elif (inp == "фары"):
            Object_list[i].light = ("Фары_"+input('Введите замену' + '\n'))
            Menu.start()
        else:
            print("Такого параметра нет")
            Menu.Change(i)

    @staticmethod
    def Delete(i):
        Object_list.pop(i)
        Menu.start()
Menu.read()
Menu.start()
Menu.Save()
