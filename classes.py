class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating    
    
    def __str__(self):
        res = f'print(some_student)\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_rating()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res
    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Сравнение невозможно!")
            return
        return self.av_rating() < other.av_rating()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        
    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating
    def __str__(self):
        res = f"print(some_lecturer)\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_rating()}"
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Сравнение невозможно!")
            return
        return self.av_rating() < other.av_rating()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'print(some_reviewer)\nИмя: {self.name} \nФамилия: {self.surname}'
        return res
      
# Создаем по 2 экземпляра каждого класса:

# Студенты
student_1 = Student('A', 'A', 'Муж')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ["Git"]

student_2 = Student('B', 'B', 'Жен')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ["Git"]

# Лекторы
lecturer_1 = Lecturer('C', 'C')
lecturer_1.courses_attached += ['Python']
 
lecturer_2 = Lecturer('D', 'D')
lecturer_2.courses_attached += ['Python']

# Проверяющие

reviewer_1 = Reviewer('E', 'E')
reviewer_1.courses_attached += ['Python']
 
reviewer_2 = Reviewer('F', 'F')
reviewer_2.courses_attached += ['Python']

# Создаем общие списки студентов/лекторов/проверяющих (на лекции сказали таким способом)

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]
reviewer_list = [reviewer_1, reviewer_2]


# Оценки студентов за домашнее задание

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)


reviewer_2.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 9)

# Оценки лекторов за лекции

student_1.rate_lecturer(lecturer_1, 'Python', 1)
student_1.rate_lecturer(lecturer_2, 'Python', 10)


student_2.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'Python', 10)


# Выводим результыты метода __str__

all_users_list = student_list + lecturer_list + reviewer_list
for i in all_users_list:
    print(f'\n{i}\n')

    
def rating_for_course(course, list_1):
    sum_rating = 0
    len_rating = 0
    for stud in list_1:
        for lesson in stud.grades.keys():
            if lesson == course:
                sum_rating += sum(stud.grades[course])
                len_rating += len(stud.grades[course])
    average_rating = round(sum_rating / len_rating, 2)
    return average_rating    

# Выводим средние значения по заданию № 4

print(f"Средняя оценка за домашние задания по всем студентам в рамках конкретного курса: {rating_for_course('Python', student_list)}\n")
print(f"Средняя оценка за лекции всех лекторов в рамках курса: {rating_for_course('Python', lecturer_list)}\n")