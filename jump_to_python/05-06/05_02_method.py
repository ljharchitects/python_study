class Student:
    id = 0

    def __init__(self, name):
        # type: (str) -> None
        self.name = name

    def study_method(self):
        print(f"study_method : {self.name}")

    # Student 내 함수는 비어있는 인자로 생성하지 못함
    # 인스턴스로 호출시 예외 발생
    def study_func():
        print(f"study_func {Student.id}")

    @staticmethod
    def study_static():
        print(f"study_static {Student.id}")

    @classmethod
    def study_classmethod(cls):
        print(f"study_classmethod {cls.id}")


student = Student("학생이름")

# student.study_method()  # O
# Student.study_method()  # 예외 발생

# student.study_func()  # 예외 발생
# Student.study_func()

# def study_func():
#     pass

# study_func()

# student.study_static()
# Student.study_static()

# student.study_classmethod()
# Student.study_classmethod()


# 상속에서 차이 발생


class Person:
    default = "아빠"

    def __init__(self):
        self.data = self.default

    @classmethod
    def class_person(cls):
        return cls()

    @staticmethod
    def static_person():
        return Person()


# def person():
#     return "아빠"


class WhatPerson(Person):
    default = "엄마"


person1 = WhatPerson.class_person()  # return 엄마
print(f"person1 : {person1.default}")
person2 = WhatPerson.static_person()  # return 아빠
print(f"person2 : {person2.default}")


"""
전문가를 위한 파이썬을 지은 파이썬구루인 루시아누 하말류는 이렇게 말합니다.

@classmethod 는 쓰임새가 많은 게 확실하지만, @staticmethod 는 사용해야하는 이유를 잘 모르겠다.클래스와 함께 작동하지 않는 함수를 정의하려면, 단지 함수를 모듈에 정의하면 된다. 아마 함수가 클래스를 건드리지는 않지만, 그 클래스와 밀접히 연관되어 있어서 클래스 코드 가까운 곳에 두고 싶을 수는 있을 것이다. 그런 경우에는 클래스의 바로 앞이나 뒤에서 함수를 정의하면 된다.
"""
