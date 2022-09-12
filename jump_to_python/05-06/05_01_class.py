"""클래스 사용 이유

데이터와 해당 데이터와 관련된 함수들을 묶어서 한 덩어리로 만든다

의미 있는 단위로 구분지어서 생각한다 -> 사람이 현실을 바라보는 모습과 유사하게 표현
    동물 -> 애완동물 -> 강아지  -> 매리, 해피...
                     -> 고양이  -> 쫑이, 깡이...
"""

# SAMPLE
"""
학생들에 대한 데이터를 관리하는 프로그램을 만든다고 가정

자료구조 (리스트, 딕셔너러리 등)를 이용해서 만들때
vs
클래스를 이용해서 만들때
    * 참고 : 클래스를 이용한다고해서 자료구조를 사용하지 않는 것은 아니다
"""

# LIST
student_id = [0, 1, 2, 3, 4]
student_name = ["강정훈", "강지수", "김재욱", "심명훈", "이진환"]
student_grade = [2, 2, 1, 2, 2]
student_address = ["판교", "판교", "서울", "성남", "서울"]
student_phone_number = [
    "010-1234-1234",
    "010-5678-5678",
    "010-9012-9012",
    "010-3456-3456",
    "010-7890-7890",
]


# DICT
student_dict = {
    0: {"name": "강정훈", "grade": 2, "address": "판교", "phone_number": "010-1234-1234"},
    1: {"name": "강지수", "grade": 2, "address": "판교", "phone_number": "010-5678-5678"},
    2: {"name": "김재욱", "grade": 1, "address": "서울", "phone_number": "010-9012-9012"},
    3: {"name": "심명훈", "grade": 2, "address": "성남", "phone_number": "010-3456-3456"},
    4: {"name": "이진환", "grade": 2, "address": "서울", "phone_number": "010-7890-7890"},
}

###################################################################

# CLASS
# 클래스 = 데이터(property) + 해당 데이터와 관련된 함수(method)
class Student:
    id = 0

    def __init__(self, name):
        # type: (str) -> None
        self.name = name

        self.__id = 0
        self._id = Student.id
        Student.id += 1

        self._grade = 0
        self._address = None  # type: str
        self._phone_number = None  # type: str

    @property
    def grade(self):
        # type: () -> int
        if not self._grade:
            raise Exception("학년이 정의되지 않았습니다")
        return self._grade

    @grade.setter
    def grade(self, grade):
        # type: (int) -> None
        if not isinstance(grade, int):
            raise Exception("학년은 정수만 입력 가능합니다")
        if grade <= 0 or grade > 3:
            raise Exception("학년은 1, 2, 3 만 입력할 수 있습니다")
        self._grade = grade

    def set_grade(self, grade):
        # type: (int) -> None
        if not isinstance(grade, int):
            raise Exception("학년은 정수만 입력 가능합니다")
        if grade <= 0 or grade > 3:
            raise Exception("학년은 1, 2, 3 만 입력할 수 있습니다")
        self._grade = grade

    def get_grade(self):
        # type: () -> int
        if not self._grade:
            raise Exception("학년이 정의되지 않았습니다")
        return self._grade

    def get_id(self):
        return self._id

    @property
    def address(self):
        # type: () -> str
        if not self._address:
            raise Exception("주소가 정의되 않았습니다")
        return self._address

    @address.setter
    def address(self, input_address):
        # type: (str) -> None
        if not isinstance(input_address, str):
            raise Exception("주소는 문자열로 입력해야합니다")
        self._address = input_address


###################################################################

from typing import List

students = []  # type: List[Student]
for name in ("강정훈", "강지수", "김재욱", "심명훈", "이진환"):
    student = Student(name)

    grade = 2
    if name == "김재욱":
        grade = 1
    # student.set_grade(grade)
    student.grade = grade
    students.append(student)
    assert student.grade < 4

for student in students:
    # print(student._id)  # X
    print(dir(student))
    print(
        f"\
        번호 : {student.get_id()}\
        이름 : {student.name}\
        학년 : {student.grade}\
        "
    )
