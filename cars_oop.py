avtlist = open('avtlist.txt', 'r+', encoding='utf-8').read().splitlines()
#hello
class Menu():
    @staticmethod
    def start():
        print('Введите желаемое действие: "добавить", "изменить", "удалить", "посмотреть список", "конец работы"')
        vvod = input()
        if vvod == 'добавить':
            Menu.add()
        if vvod == 'изменить':
            Menu.change()
        if vvod == 'удалить':
            Menu.delete()
        if vvod == 'посмотреть список':
            Menu.see()
        if vvod == 'конец работы':
            file = open('avtlist.txt', 'w', encoding='utf-8')
            for i in avtlist:
                if type(i) is str:
                    st = i
                if type(i) is list:
                    st = ' '.join(i)
                file.write('%s\n' % st)
            return 0

    @staticmethod
    def add():
        print('Введите марку, цвет, тип кузова и состояние фар (фары=вкл, фары=выкл) через пробел')
        avt = input().split()
        if len(avt) == 4 and (avt[3] == 'фары=вкл' or avt[3] == 'фары=выкл'):
            print('Данные добавлены')
            avtlist.append(avt)
            file = open('avtlist.txt', 'w', encoding='utf-8')
            for i in avtlist:
                if type(i) is str:
                    st = i
                if type(i) is list:
                    st = ' '.join(i)
                file.write('%s\n' % st)
            Menu.start()
        if len(avt) != 4 or (avt[3] != 'фары=вкл' and avt[3] != 'фары=выкл'):
            print('Введите корректные данные')
            Menu.start()

    @staticmethod
    def change():
        n = len(avtlist)
        if n != 0:
            print('Для изменения параметров автомобиля выберите номер автомобиля от 1 до', n)
            for i in range(len(avtlist)):
                if type(avtlist[i]) is str:
                    print(i + 1, avtlist[i])
                if type(avtlist[i]) is list:
                    print(i + 1, ' '.join(avtlist[i]))
            avtnum = int(input())
            if avtnum > n:
                print('Введите корректный номер')
                Menu.start()

            print('Выберите параметр для изменения (марка, цвет, тип кузова, фары)')
            vvod = input()
            if vvod == 'марка':
                print('Введите замену марки')
                zam = input()
                s = avtlist[int(avtnum) - 1]
                s1 = str(s).split()
                s1[0] = zam
                (avtlist[int(avtnum) - 1]) = s1
                print('Данные изменены')
                Menu.start()

            elif vvod == 'цвет':
                print('Введите замену цвета')
                zam = input()
                s = str(avtlist[int(avtnum) - 1])
                s1 = s.split()
                s1[1] = zam
                (avtlist[int(avtnum) - 1]) = s1
                print('Данные изменены')
                Menu.start()

            elif vvod == 'тип кузова':
                print('Введите замену типа кузова')
                zam = input()
                s = str(avtlist[int(avtnum) - 1])
                s1 = s.split()
                s1[2] = zam
                (avtlist[int(avtnum) - 1]) = s1
                print('Данные изменены')
                Menu.start()

            if vvod == 'фары':
                print('Введите 1, чтобы включить фары и 0, чтобы выключить')
                zam = ''
                ch = int(input())
                if ch == 1:
                    zam = 'фары=вкл'
                if ch == 0:
                    zam = 'фары=выкл'
                if ch != 1 and ch != 0:
                    Menu.start()
                if zam == 'фары=вкл':
                    s = str(avtlist[int(avtnum) - 1])
                    s1 = s.split()
                    s1[3] = zam
                    (avtlist[int(avtnum) - 1]) = s1
                    print('Фары включены')
                    Menu.start()
                if zam == 'фары=выкл':
                    s = str(avtlist[int(avtnum) - 1])
                    s1 = s.split()
                    s1[3] = zam
                    (avtlist[int(avtnum) - 1]) = s1
                    print('Фары выключены')
                    Menu.start()

            elif vvod == 'назад':
                Menu.start()
        if n == 0:
            print('Машин нет')
            Menu.start()
        file = open('avtlist.txt', 'w', encoding='utf-8')
        for i in avtlist:
            if type(i) is str:
                st = i
            if type(i) is list:
                st = ' '.join(i)
            file.write('%s\n' % st)

    @staticmethod
    def delete():
        n = len(avtlist)
        if n != 0:
            print('Для удаления введите номер автомобиля от 1 до ', n, ', для отмены введите "0"')
            for i in range(len(avtlist)):
                if type(avtlist[i]) is str:
                    print(i + 1, avtlist[i])
                if type(avtlist[i]) is list:
                    print(i + 1, ' '.join(avtlist[i]))
            avtnum = int(input())
            if avtnum > n:
                print('Введите корректный номер')
                Menu.delete()
            if avtnum != 0:
                avtlist.remove(avtlist[int(avtnum) - 1])
                print('Машина удалена')
                Menu.delete()
            if avtnum == 0:
                Menu.start()
        if n == 0:
            print('Машин нет')
            Menu.start()
        file = open('avtlist.txt', 'w', encoding='utf-8')
        for i in avtlist:
            if type(i) is str:
                st = i
            if type(i) is list:
                st = ' '.join(i)
            file.write('%s\n' % st)

    @staticmethod
    def see():
        if avtlist != []:
            for i in range(len(avtlist)):
                if type(avtlist[i]) is str:
                    print(i + 1, avtlist[i])
                if type(avtlist[i]) is list:
                    print(i + 1, ' '.join(avtlist[i]))
        elif avtlist == []:
            print('Список пуст')
        Menu.start()
        file = open('avtlist.txt', 'w', encoding='utf-8')
        for i in avtlist:
            if type(i) is str:
                st = i
            if type(i) is list:
                st = ' '.join(i)
            file.write('%s\n' % st)

Menu.start()