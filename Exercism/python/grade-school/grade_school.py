from collections import defaultdict


class School:
    def __init__(self):
        self.students = defaultdict(list)
        self.is_sorted = defaultdict(bool)

    def add_student(self, name, grade):
        self.students[grade].append(name)
        self.is_sorted[grade] = False

    def roster(self):
        return [name for grade in sorted(self.students.keys()) for name in self.grade(grade)]

    def grade(self, grade_number):
        if not self.is_sorted[grade_number]:
            self.students[grade_number] = sorted(self.students[grade_number])
            self.is_sorted[grade_number] = True
        return self.students[grade_number]
