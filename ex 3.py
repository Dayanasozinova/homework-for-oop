class Student:
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}
    self.courses_attached = {}

  def grade_for_a_lectur(self, lecturer, course, grade):
    if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
      if course in lecturer.grades:
        lecturer.grades[course] += [grade]
      else:
       lecturer.grades[course] = [grade] 
    else: 'Ошибка'

  def medium_grades_for_hw(self):    
    sum = 0
    quantity = 0
    if len(self.grades) != 0:
      for val in self.grades.values():
        for grade in val:
          sum += grade
          quantity += 1
          average = sum / quantity
        return average
    else:
      return 0

  def __str__(self):
    return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнии задания: {self.medium_grades_for_hw()} \nКурсы в процессе обучения: {self.courses_in_progress} \nЗавершённые курсы: {self.finished_courses}'

  def __lt__(self, other):
    if not isinstance(other, Student):
      print('Не можем сравнить!')
      return 
    return self.medium_grades_for_hw() < other.medium_grades_for_hw()
  
        
class Mentor:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
  
     

class Lecturer(Mentor):
  def __init__(self,name, surname):
    super().__init__(name, surname)
    self.courses_attached = []
    self.grades = {}

  def medium_grades(self):    
    sum = 0
    quantity = 0
    if len(self.grades) != 0:
      for val in self.grades.values():
        for grade in val:
          sum += grade
          quantity += 1
          average = sum / quantity
        return average
    else:
      return 0

  def __lt__(self, other):
    if not isinstance(other, Lecturer):
      print('Не можем сравнить!')
      return
    return self.medium_grades() < other.medium_grades() 

  def __str__(self):
    return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.medium_grades()}'

  

class Reviewer(Mentor):
  def __init__(self,name, surname):
    super().__init__(name, surname)
    self.courses_attached = []
  def rate_hw(self, student, course, grade):
    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
      if course in student.grades:
          student.grades[course] += [grade]
      else:
          student.grades[course] = [grade]
    else:
      return 'Ошибка'
  def __str__(self):
    return f'Имя:{self.name} \nФамилия:{self.surname}'



best_student = Student('Ruoy', 'Eman', 'boy')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

second_student = Student('Bob', 'Grenn', 'girl')
second_student.courses_in_progress += ['Geology']


nice_reviewer = Reviewer('Dayana', 'Sozinova')
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(second_student, 'Geology', 8)
# print(best_student.grades)

interesting_lecturer = Lecturer('Artur', 'Red')
cool_lecturer = Lecturer('Sam', 'Smith')
cool_lecturer.courses_attached += ['Geology']
second_student.grade_for_a_lectur(cool_lecturer, 'Geology', 9)
# print(cool_lecturer.grades)


print(nice_reviewer)
print('\n')
print(cool_lecturer)
print('\n')
print(best_student)
print('\n')
print(best_student < second_student)
print(interesting_lecturer < cool_lecturer)