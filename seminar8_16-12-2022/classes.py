class Person(object):
    def __init__(self, name: str = 'nobody', age: int = 0, gender: str = 'male', department: str = None, status: str = None):
        self.name = name
        self.age = age
        self.status = status
        self.gender = gender
        self.department = department

    def show_info(self):
        print(f'Имя: {self.name}\nВозраст: {self.age}\nПол: {self.gender}\nОтдел: {self.department}\nДолжность: {self.status}\n')

    def remove_person(self):
        with open('people.csv', encoding='utf-8') as f:
            f = f.readlines()
            for i in range(len(f)):
                if f[i] == f'{self.name};{self.age};{self.gender};{self.status};{self.department};{self.status}\n':
                    f.remove(f[i])
        with open('people.csv', mode='w', encoding='utf-8') as f_new:
            for i in range(len(f)):
                f_new.write(f[i])
        del self

    def __eq__(self, other):
        return self.name == other.name and self.status == other.status and self.age == other.age and self.gender == other.gender and self.department == other.department

if __name__ == "__main__":
    pass