students = [
    {"name": "김일성", "kr": 86.3, "math": 23.4, "eng": 35, "sci": 87},
    {"name": "김이성", "kr": 90, "math": 87.6, "eng": 94, "sci": 100},
    {"name": "김삼성", "kr": 87, "math": 94, "eng": 100, "sci": 100},
    {"name": "김사성", "kr": 96, "math": 87.3, "eng": 90, "sci": 84},
    {"name": "김오성", "kr": 100, "math": 80, "eng": 100, "sci": 50},
    {"name": "김육성", "kr": 15, "math": 25, "eng": 37, "sci": 21}
]


class Student:
    def __init__(self, name, kr, math, eng, sci):
        self.name = name
        self.kr = kr
        self.math = math
        self.eng = eng
        self.sci = sci


def score(self):
    return self.kr + self.math + self.eng + self.sci


def avg(self):
    return self.score() / 4


def print_(self):
    print(self.name, self.score(), self.avg(), sep="\t")


print("이름", "   총점", "  평균", sep="\t")
for student in students:
    print_()
