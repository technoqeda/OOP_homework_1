def _calculate_average_grade(grades): # Вычисление средней оценки
    total_grades = sum(sum(grades) for grades in grades.values())
    total_count = sum(len(grades) for grades in grades.values())
    return round(total_grades / total_count, 1) if total_count > 0 else 0

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade): # Оценка лекторов
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _calculate_average_grade(self): # Расчет средней оценки студента
        return _calculate_average_grade(self.grades)

    def __str__(self): # Вывод информации о студенте
        in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self._calculate_average_grade()}\n' \
               f'Курсы в процессе изучения: {in_progress}\n' \
               f'Завершенные курсы: {finished}'

    def __lt__(self, other):
        return self._calculate_average_grade() < other._calculate_average_grade()

    def __le__(self, other):
        return self._calculate_average_grade() <= other._calculate_average_grade()

    def __gt__(self, other):
        return self._calculate_average_grade() > other._calculate_average_grade()

    def __ge__(self, other):
        return self._calculate_average_grade() >= other._calculate_average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _calculate_average_grade(self): # расчет средней оценки лектора
        return _calculate_average_grade(self.grades)

    def __str__(self): # Вывод информации о лекторе
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self._calculate_average_grade()}'

    def __lt__(self, other):
        return self._calculate_average_grade() < other._calculate_average_grade()

    def __le__(self, other):
        return self._calculate_average_grade() <= other._calculate_average_grade()

    def __gt__(self, other):
        return self._calculate_average_grade() > other._calculate_average_grade()

    def __ge__(self, other):
        return self._calculate_average_grade() >= other._calculate_average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade): # Оценка домашних заданий студентов
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

some_reviewer1 = Reviewer("Роман", "Полански")
some_reviewer2 = Reviewer("Ричард", "Фейнман")
some_lecturer1 = Lecturer("Елена", "Блиновская")
some_lecturer2 = Lecturer("Аяз", "Шабутдинов")
some_student1 = Student("Игорь", "Николваев", "Male")
some_student2 = Student("Лариса", "Долина", "Feale")

some_student1.courses_in_progress += ['Python']
some_student1.courses_in_progress += ['Git']
some_student1.finished_courses += ['Введение в программирование']
some_student2.courses_in_progress += ['Python']
some_student2.courses_in_progress += ['Git']
some_student2.finished_courses += ['Введение в программирование']

some_reviewer1.rate_student(some_student1, 'Python', 10)
some_reviewer2.rate_student(some_student1, 'Python', 9)
some_reviewer1.rate_student(some_student2, 'Python', 8)
some_reviewer2.rate_student(some_student2, 'Python', 7)
some_student1.rate_lecturer(some_lecturer1, 'Python', 6)
some_student2.rate_lecturer(some_lecturer1, 'Python', 5)
some_student1.rate_lecturer(some_lecturer2, 'Python', 4)
some_student2.rate_lecturer(some_lecturer2, 'Python', 3)

print(some_reviewer2) # проверка вывода информации о проверяющих из задания №3
print(some_lecturer2) # проверка вывода информации о лекторах из задания №3
print(some_student1) # проверка вывода информации о студентах из задания №3

def calculate_average_grade_for_course(students, course):
    total_grades = 0
    total_count = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_count += len(student.grades[course])
    return round(total_grades / total_count, 1) if total_count > 0 else 0

def calculate_average_grade_for_lecturers(lecturers, course):
    total_grades = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            total_count += len(lecturer.grades[course])
    return round(total_grades / total_count, 1) if total_count > 0 else 0

students = [some_student1, some_student2]
lecturers = [some_lecturer1, some_lecturer2]

average_grade_for_homework = calculate_average_grade_for_course(students, 'Python')
print(f"Средняя оценка за домашние задания по курсу Python: {average_grade_for_homework}")

average_grade_for_lectures = calculate_average_grade_for_lecturers(lecturers, 'Python')
print(f"Средняя оценка за лекции по курсу Python: {average_grade_for_lectures}")