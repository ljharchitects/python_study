class Student:
    def __init__(self, name, score):
        # type: (str, int) -> None
        self.name = name
        self.score = score

    def __len__(self):
        return self.score


student_1 = Student("학생1", 85)
student_2 = Student("학생2", 90)
student_3 = Student("학생3", 80)

print(f"len(student_1) : {len(student_1)}")
print(f"len(student_2) : {len(student_2)}")

sorted_result = sorted((student_1, student_2, student_3), key=len)
for sorted_student in sorted_result:
    print(
        f"sorted_student name : {sorted_student.name}, score : {sorted_student.score}"
    )
