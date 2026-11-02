#37 用组合起来的类来实现多层结构，不要用嵌套内置类型
from gc import garbage


class SimpleGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)


    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)

    def __str__(self):
        return str(self._grades)


book = SimpleGradebook()
book.add_student('Isaac Newton')
book.report_grade('Isaac Newton', 90)
book.report_grade('Isaac Newton', 95)
book.report_grade('Isaac Newton', 85)

print(book)
print(book.average_grade('Isaac Newton'))


from collections import defaultdict

class BySubjectGradebook:

    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


book = BySubjectGradebook()
book.add_student('Al')
book.report_grade('Al', 'math', 75)
book.report_grade('Al', 'math', 65)
book.report_grade('Al', 'gym', 90)
book.report_grade('Al', 'gym', 95)
print(book.average_grade('Al'))

#需要添加科目以及权重

class WeightedGradebook:
    def __init__(self):
        self._grades = {}
    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, grade, weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((grade, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for subject, score in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in score:
                subject_avg += score * weight
                total_weight += weight
            score_sum += subject_avg / total_weight
            score_count += 1
        return score_sum / score_count

book = WeightedGradebook()
book.add_student('Al')
book.report_grade('Al', 'math', 75, 0.05)
book.report_grade('Al', 'math', 65, 0.15)
book.report_grade('Al', 'math', 70, 0.80)
book.report_grade('Al', 'gym', 100, 0.40)
book.report_grade('Al', 'gym', 85, 0.60)
print(book.average_grade('Al'))



grades = []
grades.append((95, 0.45))
grades.append((85, 0.55))
total = sum(score * weight for score, weight in grades)
total_weight = sum(weight for _, weight in grades)
average = total / total_weight
print(average)

grades = []
grades.append((95, 0.45, 'Greate job'))
grades.append((85, 0.55, 'Better next Time'))
total = sum(score * weight for score, weight, _  in grades)
total_weight = sum(weight for _, weight, _ in grades)
average = total / total_weight
print(average)
#元祖拖得太长，就跟字典套太深一样，都不好维护，所以只要发现元祖的元素超过两个，就应该考虑其他方法了


#python 内置的collections模块具名元祖（namedtuple类型），
from collections import namedtuple

Grade = namedtuple('Grade', ('score' , 'weight'))

class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0

        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight

class Student:
    def __init__(self):
        self._subject = defaultdict(Subject)

    def get_subject(self, name):
        return self._subject[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subject.values():
            total += subject.average_grade()
            count += 1
        return total / count

class Gradebook:
    def  __init__(self):
        self._students = defaultdict(Student)

    def get_student(self, name):
        return self._students[name]

book = Gradebook()
albert = book.get_student('Al')
math = albert.get_subject('math')
math.report_grade(75, 0.05)
math.report_grade(65, 0.15)
math.report_grade(70, 0.80)

gym = albert.get_subject('gym')
gym.report_grade(100, 0.40)
gym.report_grade(85, 0.60)
print(albert.average_grade())

#总结
#不要在字典里嵌套字典、长元祖以及用其他内置类型构造的复杂结构
#nametuple能够实现出轻量级容器，以存放不可变的数据，而且将来可以灵活地转换为普通类
#如果发现字典用来维护内部状态的那些代码已经越写越复杂了，那么就应该考虑用多个类来实现。