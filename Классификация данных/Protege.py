from abc import ABC


class TechnicalService(ABC):
    birth = ''
    check = ''
    name = ''
    overdraft = ''
    probation = ''
    salary = 0.0
    telephone = ''

    def __init__(self, birth, check, name, overdraft, probation, salary, telephone):
        self.birth = birth
        self.check = check
        self.name = name
        self.overdraft = overdraft
        self.probation = probation
        self.salary = salary
        self.telephone = telephone


class TechnologicalService(ABC):
    birth = ''
    check = ''
    name = ''
    overdraft = ''
    probation = ''
    salary = 0.0
    telephone = ''

    def __init__(self, birth, check, name, overdraft, probation, salary, telephone):
        self.birth = birth
        self.check = check
        self.name = name
        self.overdraft = overdraft
        self.probation = probation
        self.salary = salary
        self.telephone = telephone


class Guide:
    birth = ''
    check = ''
    name = ''
    overdraft = ''
    probation = ''
    salary = 0.0
    telephone = ''

    def __init__(self, birth, check, name, overdraft, probation, salary, telephone):
        self.birth = birth
        self.check = check
        self.name = name
        self.overdraft = overdraft
        self.probation = probation
        self.salary = salary
        self.telephone = telephone


class Mechanic(TechnicalService, Guide):
    responsible_for = 0

    def __init__(self, birth, check, name, overdraft, probation, salary, telephone, responsible_for):
        TechnicalService.__init__(self, birth, check, name, overdraft, probation, salary, telephone)
        self.responsible_for = responsible_for


class Fitter(TechnicalService):
    rank = 0

    def __init__(self, birth, check, name, overdraft, probation, salary, telephone, rank):
        TechnicalService.__init__(self, birth, check, name, overdraft, probation, salary, telephone)
        self.rank = rank


class Electric(TechnicalService):
    rank = 0

    def __init__(self, birth, check, name, overdraft, probation, salary, telephone, rank):
        TechnicalService.__init__(self, birth, check, name, overdraft, probation, salary, telephone)
        self.rank = rank


class Foreman(TechnicalService, TechnologicalService, Guide):
    responsible_for = 0

    def __init__(self, birth, check, name, overdraft, probation, salary, telephone, responsible_for):
        TechnicalService.__init__(self, birth, check, name, overdraft, probation, salary, telephone)
        self.responsible_for = responsible_for


class Technologist(TechnologicalService, Guide):
    responsible_for = 0

    def __init__(self, birth, check, name, overdraft, probation, salary, telephone, responsible_for):
        TechnologicalService.__init__(self, birth, check, name, overdraft, probation, salary, telephone)
        self.responsible_for = responsible_for


class Packer(TechnologicalService):
    def __init__(self, birth, check, name, overdraft, probation, salary, telephone):
        TechnologicalService.__init__(self, birth, check, name, overdraft, probation, salary, telephone)


class Confectioner(TechnologicalService):
    rank = 0

    def __init__(self, birth, check, name, overdraft, probation, salary, telephone, rank):
        TechnologicalService.__init__(self, birth, check, name, overdraft, probation, salary, telephone)
        self.rank = rank


class Master(TechnologicalService):
    responsible_for = 0

    def __init__(self, birth, check, name, overdraft, probation, salary, telephone, responsible_for):
        TechnologicalService.__init__(self, birth, check, name, overdraft, probation, salary, telephone)
        self.responsible_for = responsible_for


class Glazier(TechnologicalService):
    def __init__(self, birth, check, name, overdraft, probation, salary, telephone):
        TechnologicalService.__init__(self, birth, check, name, overdraft, probation, salary, telephone)


Lukin = Fitter('06.11.1971', '0', "Lukin", '0', '1 year', 30000.0, '359-00-66', '4')
Putin = Fitter('20.10.1967', '0', 'Putin', "8 hour", '5 year', 40000.0, '222-22-22', '6')
Zimin = Electric('16.12.1964', '1 hour', 'Zimin', "0", '3 year', 30000.0, '442-95-99', '4')
list1 = [Lukin, Putin, Zimin]
Smirnov = Mechanic('15.02.1972', '0', 'Smirnov', '8 hour', '4 year', 50000.0, '321-21-12', list1)
Portnova = Packer('01.04.1990', '0', 'Portnova', '8 hour', '1 year', 20000.0, '555-65-56')
Krotova = Confectioner('17.04.1970', '0', 'Krotova', '8 hour', '5 year', 35000.0, '693-15-17', '5')
Tomina = Glazier('22.05.1979', '0', 'Tomina', '8 hour', '3 year', 35000.0, '845-71-00')
list2 = [Portnova, Krotova, Tomina]
Fedina = Master('11.05.1965', '0', 'Fedina', '8 hour', '3 year', 40000.0, '723-22-33', list2)
list3 = [Smirnov, Fedina]
Ivanov = Foreman('01.01.1980', '0', 'Ivanov', '0', '10 year', 70000.0, '123-12-23', list3)

list4 = [Lukin, Putin, Zimin, Smirnov, Portnova, Krotova, Tomina, Fedina, Ivanov]
for i in list4:
    if i.salary > 30000.0:
        print(i.name, i.salary)
