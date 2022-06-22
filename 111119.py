import json



class Student:
    def __init__(self, id, name, subject, score):
        self.id = id
        self.name = name
        self.score = score
        self.advanced_in = None
        self.advanced_score = None
        self.average_score = None

    def calculate_score(self, score, subject):



def solution(students):
    js_obj = json.loads(students)
    list_of_sudents = []
    for student in js_obj:
         list_of_sudents.append(Student(student["id"], student["name"]))

    for student in list_of_sudents:



    return 0


students_json = """[{"id":"123","name":"John Smith","subject":"Maths","score":6.1},{"id":"123","name":"John Smith","subject":"Science","score":1.2},{"id":"123","name":"John Smith","subject":"Geography","score":8.7},{"id":"456","name":"Walter Burry","subject":"Maths","score":3.4},{"id":"8bcd","name":"Sandra Koch","subject":"Maths","score":7.3},{"id":"8bcd","name":"Sandra Koch","subject":"Sports","score":2.8}]"""


solution(students_json)