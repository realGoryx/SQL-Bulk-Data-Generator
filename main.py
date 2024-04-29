from faker import Faker
from faker.providers import BaseProvider
import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta
import calendar

f = Faker('pl_PL')

teacherID = []
teacherName = []
teacherSurname = []
teacherTitle = []
teacherBeginningDate = []
teacherCity = []
teacherDistrict = []
teacherGender = []
teacherDateBirth = []

studentID = []
studentName = []
studentSurname = []
studentGender = []
studentDateBirth = []
studentPhone = []
studentEmail = []
studentCity = []
studentDistrict = []
studentClass = []

classNumber = []
classFloor = []
classBuilding = []
classSize = []

className = []
classSpecialization = []
classLevel = []

examID = []
examType = []
examDate = []
examSupervisor = []
examClass = []
examDuration = []

gradeID = []
gradeValue = []
gradeDate = []
gradeStudent = []
gradeTeacher = []
gradeExam = []
gradePlagiarism = []
gradeSatis = []
gradeWritingTime = []

studentGenerator = 45000
teacherGenerator = 45000
gradeGenerator = 842000
classroomGenerator = 980

classTotalNumber = 260

T1Start = 2019
T2Start = 2022


class CustomProvider(BaseProvider):
    @staticmethod
    def random_city_and_district():
        city = random.choice(miasta)
        if city == 'Gdansk':
            district = random.choice(dzielnica_gdansk)
        elif city == 'Gdynia':
            district = random.choice(dzielnica_gdynia)
        elif city == 'Sopot':
            district = random.choice(dzielnica_sopot)
        return city, district


for i in range(0, 10):
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        className.append(f"{i}{letter}")


def random_date_time_exam(year, month):
    num_days = calendar.monthrange(year, month)[1]
    random_day = random.randint(1, num_days)
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    return datetime(year, month, random_day, random_hour, random_minute, random_second)


def generate_first_name(is_male):
    if is_male:
        return f.first_name_male()
    else:
        return f.first_name_female()


def generate_last_name(is_male):
    if is_male:
        return f.last_name_male()
    else:
        return f.last_name_female()


def return_gender(gender):
    if gender:
        return 'M'
    else:
        return 'F'


def get_floor(class_number):
    return class_number // 100 if len(str(class_number)) == 3 else 0


f.add_provider(CustomProvider)

miasta = ['Gdansk', 'Gdynia', 'Sopot']

dzielnica_gdansk = ['Aniolki', 'Bretowo', 'Brzezno',
                    'Chelm', 'Jasien', 'Kokoszki',
                    'Letnica', 'Matarnia', 'Mlyniska',
                    'Nowy Port', 'Oliwa', 'Olszynka',
                    'Orunia Górna', 'Osowa', 'Piecki-Migowo',
                    'Przerobka', 'Przymorze Małe', 'Przymorze Wielkie',
                    'Rudniki', 'Siedlce', 'Stogi', 'Strzyza', 'Suchanino',
                    'Srodmiescie', 'Ujescisko-Lostowice', 'Wrzeszcz Dolny',
                    'Wrzeszcz Gorny', 'Wyspa Sobieszewska', 'Wzgorze Mickiewicza',
                    'Zaspa Mlyniec', 'Zaspa Rozstaje']
dzielnica_gdynia = ['Babie Doly', 'Chwarzno-Wilczlino', 'Chylonia',
                    'Cisowa', 'Dzialki Lesne', 'Dabrowa', 'Grabowek',
                    'Kamienna Gora', 'Karwiny', 'Leszczynki', 'Maly Kack',
                    'Obluze', 'Oksywie', 'Orlowo', 'Pogorze', 'Redlowo',
                    'Srodmiescie', 'Wielki Kack', 'Witomino', 'Wzgorze sw. Maksymiliana']
dzielnica_sopot = ['Brodwino', 'Dolny Sopot', 'Gorny sopot',
                   'Kammieny Potok', 'Karlikowo', 'Swiemirowo']

title = ['Primary', 'Secondary', 'BSc', 'MSc', 'Phd', 'Engineer']

examTypes = ['H', 'S', 'L']

classSpecs = ['Mathematics', 'Linguistics', 'Biology-Chemistry', 'Humanistic', 'Computer Science', 'Geographic',
              'General']
classLevels = ['Basic', 'Intermediate', 'Advanced', 'College Preparatory', 'Specialized', 'Mixed']

classPossibleBuildings = ['Main Building', 'North Wing', 'South Wing', 'Science Building']

class_teacher_relationships = []


def generate_class_teacher_relationships(class_names, teacher_ids, a, b, existing_relationships=None):
    if existing_relationships is None:
        existing_relationships = {}

    class_teacher_relationships = []

    for class_name in class_names:
        num_teachers = random.randint(a, b)

        available_teachers = [teacher_id for teacher_id in teacher_ids if
                              teacher_id not in existing_relationships.get(class_name, set())]

        num_teachers = min(num_teachers, len(available_teachers))

        teachers_for_class = random.sample(available_teachers, num_teachers)

        existing_relationships[class_name] = existing_relationships.get(class_name, set()).union(teachers_for_class)

        class_teacher_relationships.extend([(class_name, teacher_id) for teacher_id in teachers_for_class])

    return class_teacher_relationships, existing_relationships


def random_date_within_range(base_date, range_days):
    range_seconds = range_days * 24 * 60 * 60
    random_seconds = random.randint(0, range_seconds)
    return base_date + timedelta(seconds=random_seconds)


for _ in range(teacherGenerator):
    gender = random.choice([True, False])
    tCity, tDistrict = f.random_city_and_district()
    teacherID.append(f.unique.random_int(min=100000, max=199999))
    teacherName.append(generate_first_name(gender))
    teacherSurname.append(generate_last_name(gender))
    teacherTitle.append(random.choice(title))
    teacherBeginningDate.append(f.date_of_birth(minimum_age=6, maximum_age=12))
    teacherCity.append(tCity)
    teacherDistrict.append(tDistrict)
    teacherGender.append(return_gender(gender))
    teacherDateBirth.append(f.date_of_birth(minimum_age=32, maximum_age=65))

for _ in range(studentGenerator):
    gender = random.choice([True, False])
    studentID.append(f.unique.random_int(min=200000, max=999999))
    studentName.append(generate_first_name(gender))
    studentSurname.append(generate_last_name(gender))
    studentGender.append(return_gender(gender))
    studentBirth = f.date_of_birth(minimum_age=14, maximum_age=20)
    studentDateBirth.append(studentBirth)
    studentClass.append(random.choice(className))
    studentPhone.append(f.phone_number())
    studentEmail.append(f.email())
    sCity, sDistrict = f.random_city_and_district()
    studentCity.append(sCity)
    studentDistrict.append(sDistrict)

used_teacher_ids = set(teacherID)
used_student_ids = set(studentID)


def random_grade_set(number):
    grade_set1 = [1.0, 1.5, 1.5, 2.0, 2.0, 2.0, 2.0, 2.5, 3.0, 3.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.0]
    grade_set2 = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.0, 4.0, 4.0, 4.5, 4.5, 4.5, 5.0, 5.0, 5.5, 6.0]
    grade_set3 = [1.0, 1.5, 2.0, 2.5, 2.5, 2.5, 2.5, 3.0, 3.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.0]
    grade_set4 = [1.0, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.0, 5.5, 6.0, 6.0, 6.0, 6.0]
    grade_set5 = [1.0, 1.0, 1.0, 1.5, 2.0, 2.0, 2.0, 2.5, 3.0, 3.0, 3.5, 3.5, 4.0, 4.5, 5.0, 5.5, 5.5, 6.0]
    grade_set6 = [1.0, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 3.5, 4.0, 4.5, 4.5, 4.5, 5.0, 5.0, 5.0, 5.5, 6.0]

    if number == 1:
        return random.choice(grade_set1)
    elif number == 2:
        return random.choice(grade_set2)
    elif number == 3:
        return random.choice(grade_set3)
    elif number == 4:
        return random.choice(grade_set4)
    elif number == 5:
        return random.choice(grade_set5)
    elif number == 6:
        return random.choice(grade_set6)


for _ in range(classroomGenerator):
    class_number = f.unique.random_int(min=1, max=999)
    classNumber.append(class_number)
    classFloor.append(get_floor(class_number))
    classBuilding.append(random.choice(classPossibleBuildings))
    classSize.append(random.randint(20, 81))

for i in className:
    classSpecialization.append((random.choice(classSpecs)))
    classLevel.append(random.choice(classLevels))

isTeachingRelationship1, existing_relationships = generate_class_teacher_relationships(className, teacherID, 230, 270)

sqlClasses = pd.DataFrame(zip(className, classSpecialization, classLevel),
                          columns=['Name', 'Class Specialization', 'Class Level'])

sqlTeachers = pd.DataFrame(zip(teacherID, teacherName, teacherSurname), columns=['Teacher_ID', 'TName', 'TSurname'])

sqlClassrooms = pd.DataFrame(zip(classNumber, classFloor, classBuilding, classSize),
                             columns=['Room_number', 'School_floor', 'Building', 'Size'])

sqlStudents = pd.DataFrame(zip(studentID, studentName, studentSurname, studentClass),
                           columns=['StudentID', 'SName', 'SSurname', 'Class_Name'])
sqlIsTeaching = pd.DataFrame(isTeachingRelationship1, columns=['Class Name', 'Teacher ID'])


sqlTeachers.to_csv('Teachers.csv', sep=',', index=False, encoding='utf-8', header=False)
sqlClassrooms.to_csv('Classrooms.csv', sep=',', index=False, encoding='utf-8', header=False)
sqlStudents.to_csv('Students.csv', sep=',', index=False, encoding='utf-8', header=False)
sqlClasses.to_csv('Classes.csv', sep=',', index=False, encoding='utf-8', header=False)
sqlIsTeaching.to_csv('IsTeaching.csv', sep=',', index=False, encoding='utf-8', header=False)

examCounter = 0
for year in range(T1Start, T2Start):
    for month in range(1, 13):
        examCounter += 1
        examID.append(examCounter)
        examType.append(random.choice(examTypes))
        examDate.append(random_date_time_exam(year, month))
        examDuration.append(f.random_int(min=60, max=120))
        examSupervisor.append(teacherID[f.random_int(min=0, max=len(teacherID) - 1)])
        examClass.append(classNumber[f.random_int(min=0, max=len(classNumber) - 1)])

assigned_grades = set()
gradeCounter = 0
for _ in range(gradeGenerator):
    gradeCounter += 1
    plagiarism = 0
    satis = 0
    writing = 0

    studentID_grade = studentID[f.random_int(min=0, max=len(studentID) - 1)]
    examID_grade = examID[f.random_int(min=0, max=len(examID) - 1)]

    while (studentID_grade, examID_grade) in assigned_grades:
        studentID_grade = studentID[f.random_int(min=0, max=len(studentID) - 1)]
        examID_grade = examID[f.random_int(min=0, max=len(examID) - 1)]

    assigned_grades.add((studentID_grade, examID_grade))

    exam_index = examID.index(examID_grade)
    exam_date = examDate[exam_index]

    grade_date = random_date_within_range(exam_date, 14)

    gradeID.append(gradeCounter)
    gradeRand = random_grade_set(random.randint(1, 6))
    gradeValue.append(gradeRand)

    if gradeRand == 1 and random.random() < 0.1:
        plagiarism = 1

    if gradeRand == 1 or gradeRand == 1.5:
        satis = random.randint(1, 2)
    elif gradeRand == 6:
        satis = random.randint(5, 6)
    else:
        satis = random.randint(1, 6)

    writing = random.randint(examDuration[exam_index] - 35, examDuration[exam_index])

    gradePlagiarism.append(plagiarism)
    gradeDate.append(grade_date)
    gradeStudent.append(studentID_grade)
    gradeExam.append(examID_grade)
    gradeTeacher.append(teacherID[f.random_int(min=0, max=len(teacherID) - 1)])
    gradeSatis.append(satis)
    gradeWritingTime.append(writing)

sqlGrade = pd.DataFrame(
    zip(gradeID, gradeValue, gradeDate, gradePlagiarism, gradeStudent, gradeExam, gradeTeacher, gradeSatis,
        gradeWritingTime),
    columns=['GradeID', 'GradeValue', 'GradeDate', 'GradePlagiarism', 'StudentID', 'ExamID', 'TeacherID',
             'GradeSatisfaction', 'WritingTime'])

sqlGrade.to_csv('Grades_Comp.csv', sep=',', index=False, encoding='utf-8', header=False)

sqlExams = pd.DataFrame(zip(examID, examType, examDate, examDuration, examSupervisor, examClass),
                        columns=['examID', 'examType',
                                 'examDate', 'examDuration', 'examSupervisor', 'examClassroom'])

sqlExams.to_csv('Exams.csv', sep=',', index=False, encoding='utf-8', header=False)
