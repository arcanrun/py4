class Students():

    students = []
    disciplines = []
    # names = []
    # telNumbers = []
    # birthdayDates =[]
    # secondNames = []

    def showMenu(self):
        print("\n---------- Главное меню -----------")
        print("1. Показать курсантов уч. группы \n2. Добавить курсанта \n3. Найти курсанта\n4. Удалить курсанта\n5. Дисциплина\n")
        keyForDict = input()
        dictionary = {
                        '1': self.showStudents,
                        '2': self.addStudent,
                        '3': self.showKursant,
                        '4': self.deleteStudent,
                        '5': self.showDiscipline
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

        # self.names.append(self.students[len(self.students)-1].split(' ')[0].strip().replace(' ',''))
        # self.secondNames.append(self.students[len(self.students)-1].split(' ')[1].strip().replace(' ',''))
        # self.telNumbers.append(self.students[len(self.students) - 1].split(' ')[2].strip().replace(' ', ''))
        # self.birthdayDates.append(self.students[len(self.students) - 1].split(' ')[3].strip().replace(' ', ''))
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



    #     if name != 0:
    #         clearName = name.replace(' ', '').strip()
    #         for j in range(len(self.names)):
    #
    #             if self.names[j] == clearName:
    #                 print('\nТакой курсант есть: \n', self.students[j])
    #                 return self.showMenu()
    #
    #         print('не найдено')
    #         return self.showMenu()
    #
    #
    #     elif secName !=0:
    #         clearsecName = secName.replace(' ', '').strip()
    #         for j in range(len(self.names)):
    #
    #             if self.secondNames[j] == clearsecName:
    #                 print('\nТакой курсант есть: \n', self.students[j])
    #                 return self.showMenu()
    #
    #         print('не найдено')
    #         return self.showMenu()
    #
    #     elif tel != 0:
    #         clearTel = tel.replace(' ', '').strip()
    #         for j in range(len(self.telNumbers)):
    #
    #             if self.telNumbers[j] == clearTel:
    #                 print('\nТакой курсант есть: \n', self.students[j])
    #                 return self.showMenu()
    #
    #         print('не найдено')
    #         return self.showMenu()
    #
    #     elif bDate != 0:
    #         clearBDate = bDate.replace(' ', '').strip()
    #         for j in range(len(self.birthdayDates)):
    #
    #             if self.birthdayDates[j] == clearBDate:
    #                 print('\nТакой курсант есть: \n', self.students[j])
    #                 return self.showMenu()
    #
    #         print('не найдено')
    #         return self.showMenu()

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

        print('\n1.Добавить дисциплину\n2.Удалить дисциплину\n3.Главное меню\n')
        choose = input()
        dictionary = {
            '1': self.addDiscipline,
            '2': self.removeDiscipline,
            '3': self.showMenu
        }.get(choose, self.showMenu)()

    def addDiscipline(self):
        pass
    def removeDiscipline(self):
        pass

    # def testName(self):
    # return print(self.names, "  ", self.secondNames)s

# ======================================================================

Students = Students()

Students.showMenu()
