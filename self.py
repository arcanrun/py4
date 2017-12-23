class Students():

    students = []
    disciplinesOf = {}



    def showMenu(self):
        print("\n---------- Главное меню -----------")
        print("1. Показать курсантов уч. группы \n2. Добавить курсанта \n3. Найти курсанта\n4. Удалить курсанта\n5. Дисциплина\n6. Сортировка\n")
        keyForDict = input()
        dictionary = {
                        '1': self.showStudents,
                        '2': self.addStudent,
                        '3': self.showKursant,
                        '4': self.deleteStudent,
                        '5': self.showDiscipline,
                        '6': self.showSortOptions
                     }.get(keyForDict, self.showMenu)()


    def showStudents(self):

        if len(self.students) == 0:
            print('Курсантов нет')

            return self.showMenu()

        for i in range(len(self.students)):
            print(i+1, '.', self.students[i])

        return self.showMenu()


    def addStudent(self):
        dictionary = {
            1: self.addStudent,
            2: self.showMenu
        }

        print('Введите имя курсанта в формате "Имя Фамилия +999999999 dd.mm.yyyy" : \n\n')
        newStudent = input()

        self.students.append(newStudent)
        self.disciplinesOf.update({newStudent : {}})


        print('Продолжить? - 1 \nГлавное меню - 2\n')
        nextStep = int(input())

        return dictionary[nextStep]()


    def findKursant(self):


        print('Введите данные курасанта, которого надо найти:\n')

        enteredInfo = input()

        finded = 0

        for i in range(len(self.students)):
            if enteredInfo in self.students[i]:
                print(self.students[i])
                finded += 1
        if finded > 0:
            print('\nНикого не нашли\n')
            self.showKursant()
        else:
            self.showKursant()




    def showKursant(self):
        print('\n1. Поиск\n2. Главное меню\n')
        choose = input()
        dictionary = {
            '1': self.findKursant,
            '2': self.showMenu
        }.get(choose, self.showKursant)()



    def deleteStudent(self):
            print("\nВведите данные курсанта, которого нужно удалить:\n")
            infoKursDelete = input()
            if len(self.students) != 0:
                for i in range(len(self.students)):
                    if infoKursDelete in self.students[i]:
                        deleted = self.students[i]
                        self.students.pop(i)
                        print('\nКурсант ', deleted, 'удален\n')
                        self.showStudents()
                        break
                print("\nКурсант не найден\n")
                return self.showStudents()
            else:
                print("\nКурсант не найден\n")
                return self.showStudents()
    def showDiscipline(self):

        print('\n1.Показать дисцип\n2.Добавить дисциплину\n3.Удалить дисциплину\n4.Главное меню\n')
        choose = input()
        dictionary = {
            '1': self.letsSeeDiscipline,
            '2': self.addDiscipline,
            '3': self.showRemoveDisciplineOptions,
            '4': self.showMenu
        }.get(choose, self.showMenu)()

    def addDiscipline(self):
        print('\nДанные курсанта:\n')
        kursant = input()

        finded = 0
        findedKurs = ''
        for i in range(len(self.students)):
            if kursant in self.students[i]:

                finded += 1
                findedKurs = self.students[i]
                print(findedKurs)
                break
        if finded == 0:
            print('Никого не нашли')
            self.showDiscipline()
        print('\nВведите название дисциплины\n')
        discip = input()


        self.disciplinesOf[findedKurs][discip] = ''

        print(self.disciplinesOf)
        print('\n1.Добавить оценки:\n2.Назад\n')

        choose = input()
        dictionary = {
                    '1': self.addMarks,
                    '2': self.showDiscipline
                    }.get(choose, self.showDiscipline)(findedKurs, discip)
        if finded < 0:
            print('\nНикого не нашли\n')
            self.showDiscipline()


    def addMarks(self, who, dis):
        print('\nВведите оценки через пробел:\n')
        marks = input()

        self.disciplinesOf[who][dis] = marks
        print(self.disciplinesOf)
        self.showDiscipline()

    def showRemoveDisciplineOptions(self):
        print('\n1.Удалить все дисциплины у курсанта\n2.Удалить конкретную дисциплину\n3.Назад\n')
        choose = input()
        dicttionary = {
                '1': self.removAllDisciplines,
                '2': self.removeDiscipline,
                '3': self.showDiscipline
        }.get(choose, self.showDiscipline)()

    def removeDiscipline(self):
        print('\nУ кого удаляем?\n')
        who = self.findKursantCustom()
        print('\nКакую дисциплину?\n')
        self.letsSeeDisciplineDefenited(who)
        dis = input()

        which = self.disciplinesOf[who][dis]
        self.disciplinesOf[who][dis] = {}
        print('У курсанта ', who, 'удалены оценки по дисциплине', dis)
        self.showMenu()

    def removAllDisciplines(self):
        print('У кого удаляем?')

        who = self.findKursantCustom()
        self.disciplinesOf[who] = {}
        print('У курсанта ', who, 'все дисциплины удалены')
        self.showDiscipline()

    def letsSeeDiscipline(self):
        for i in self.disciplinesOf:
            print(i)
            for j in self.disciplinesOf[i]:
                print('\t', j,':', self.disciplinesOf[i][j])
        self.showDiscipline()

    def letsSeeDisciplineDefenited(self, who):
        i = self.disciplinesOf[who]
        for i in self.disciplinesOf:
            print(i)
            for j in self.disciplinesOf[i]:
                print('\t', j,':', self.disciplinesOf[i][j])

    def findKursantCustom(self):
        print('\nДанные курсанта:\n')
        kursant = input()

        finded = 0
        findedKurs = ''
        for i in range(len(self.students)):
            if kursant in self.students[i]:
                finded += 1
                findedKurs = self.students[i]

                return findedKurs

        if finded == 0:
            findedKurs = 0
            return findedKurs

    def showSortOptions(self):
        print('\n1.Сортировка по имени\n2.Сортировка по фамилии\n3.Главное меню\n')
        choose = input()
        dictionary = {
            '1': self.sortByName,
            '2': self.sortBySecName,
            '3': self.showMenu
        }.get(choose, self.showSortOptions)()

    def sortByName(self):

        sorted = self.students[:]
        sorted.sort()

        for i in range(len(sorted)):
            print(i+1, '.', sorted[i])

        self.showMenu()

    def sortBySecName(self):
        sorted = []
        for i in range(len(self.students)):

            sorted.append(self.students[i].split(' ')[1].strip().replace(' ', ''))


        middleSort = []

        for k in range(len(self.students)):
            middleSort.append(sorted[k] + ',' + self.students[k])

        middleSort.sort()

        final = []
        for g in range(len(middleSort)):
            final.append(middleSort[g].split(',', maxsplit=1)[1])

        for j in range(len(final)):
            print(j + 1, '.', final[j])



        self.showMenu()

# =================================== Main ===================================

Students = Students()
Students.showMenu()
