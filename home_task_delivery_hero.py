"""
You are provided with JSON string, where each element is referred to a student and a subject, having the following fields: id, name, subject and score.

You have to write a solution what receives that JSON string and returns a string as follows:

Each student will be represented by their id
Right afterwards, between parenthesis, you need to include the average of their scores (2 decimals maximum)
If the student is the best in a subject, you need to append “#subject” to the average score. If more than one subject meets the condition, concatenate with ‘+’
Students have to be sorted by their total average score, starting from the one with higher average
Example:

students_json = ‘[ {“id”:”123”,”name”:”John Smith”,”subject”:”Maths”,”score”:6.1}, {“id”:”123”,”name”:”John Smith”,”subject”:”Science”,”score”:1.2}, {“id”:”123”,”name”:”John Smith”,”subject”:”Geography”,”score”:8.7}, {“id”:”456”,”name”:”Walter Burry”,”subject”:”Maths”,”score”:3.4}, {“id”:”8bcd”,”name”:”Sandra Koch”,”subject”:”Maths”,”score”:7.3}, {“id”:”8bcd”,”name”:”Sandra Koch”,”subject”:”Sports”,”score”:2.8} ]’

Expected result:

“123(5.33#Geography),8bcd(5.05#Maths+Sports),456(3.4)”
"""

import json

ID = "id"
NAME = "name"
SUBJECT = "subject"
SCORE = "score"

class Subject:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.average_score = 0
        self.count_of_disciplines = 0

class University:
    def __init__(self):
        self.students = {}
        self.subjects = {}
        self.rating = {}

    def add_student(self, student, id):
        if id not in self.students:
            self.students[id] = student

    def add_subject(self, subject):
        if subject.name not in self.subjects:
            self.subjects[subject.name] = {}

    def _get_student_by_id(self, id):
        return self.students[id]

    def _get_subject_by_name(self, subject_name):
        return self.subjects[subject_name]

    def students_performance_updater(self, subject_name, student_id, score):
        subject = self._get_subject_by_name(subject_name)
        if subject.get("the_best_score", 0) < score:
            subject["the_best_student_id"] = student_id
            subject["the_best_score"] = score

        student = self._get_student_by_id(student_id)
        student.count_of_disciplines += 1
        student.total_score += score
        student.average_score = round(((student.total_score) / student.count_of_disciplines), 2)

        self.rating[student_id] = student.average_score

    def _get_rating(self):
         return {k: v for k, v in sorted(self.rating.items(), key=lambda item: item[1], reverse=True)}

    def _get_leadership_in_subjects(self, student_id):
        result = []
        for subject_name in self.subjects:
            if self.subjects[subject_name]["the_best_student_id"] == student_id:
                result.append(subject_name)
        return result

    def report(self):
        result_string = ""
        rating = self._get_rating()
        for id in rating:
            leadership = "+".join(self._get_leadership_in_subjects(id))
            average_score = self._get_student_by_id(id).average_score
            student_performance = "({average_score}{delimiter}{leadership})".format(average_score=average_score,
                                                                                    delimiter="#" if leadership!= '' else '',
                                                                                    leadership=leadership )
            result_string += id + student_performance + ","
        return result_string[:-1]


def solution(students):
    js_obj = json.loads(students)
    university = University()
    for item in js_obj:
        student = Student(item[NAME])
        subject = Subject(item[SUBJECT])
        university.add_student(student, item[ID])
        university.add_subject(subject)
        university.students_performance_updater(item[SUBJECT], item[ID], item[SCORE])
    print(university.report())

students_json = """[{"id":"123","name":"John Smith","subject":"Maths","score":6.1},{"id":"123","name":"John Smith","subject":"Science","score":1.2},{"id":"123","name":"John Smith","subject":"Geography","score":8.7},{"id":"456","name":"Walter Burry","subject":"Maths","score":3.4},{"id":"8bcd","name":"Sandra Koch","subject":"Maths","score":7.3},{"id":"8bcd","name":"Sandra Koch","subject":"Sports","score":2.8}]"""

solution(students_json)