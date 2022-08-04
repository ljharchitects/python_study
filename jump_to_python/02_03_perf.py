import time


# 파이썬은 모든 것이 객체(object, class의 instance)이다

# 함수도 다른 함수의 인자로 넘길 수 있다
def outer_func(origin_func):
    print(f"origin_func : {type(origin_func)}")
    return origin_func


# def elapsed_time(origin_func):
#     """docstring : 함수에 대한 설명 또는 사용법을 적는다
#     연산 시간을 계산하는 함수
#     """

#     def wrapper_func(*args, **kwargs):
#         start_time = time.time()
#         result = origin_func(*args, **kwargs)
#         end_time = time.time()
#         print(
#             "WorkingTime[{}]: {} sec".format(
#                 origin_func.__name__, end_time - start_time
#             )
#         )
#         return result

#     return wrapper_func


def add_num_for_count1(num, count):
    # type: (int, int) -> int
    """
    num을 count 횟수만큼 더한다.
    """

    # type 은 에디터를 위한 것일뿐 타입을 강제하지 않는다
    result = 0
    for _ in range(count):  # _는 사용하지 않는 변수임을 의미한다
        result += num
    return result


# python 3.6 이후 가능
def add_num_for_count2(num: int, count: int):
    """
    num을 count 횟수만큼 더한다.
    """
    result = 0
    for _ in range(count):  # _는 사용하지 않는 변수임을 의미한다
        result += num
    return result


# result = add_num_for_count1(1, 100)
# result = add_num_for_count2(1, 100)
# result = outer_func(add_num_for_count1)(1, 100)


# decorator
# result = elapsed_time(add_num_for_count1)(100, 1000)


# print(result)


##################################################################
from datetime import datetime

# print("datetime : ", datetime.now())


# def logger(logging_message, dt=datetime.now()):
#     print(f"{dt} : {logging_message}")


# logger("test message1")
# time.sleep(1)
# logger("test message2")
# time.sleep(1)
# logger("test message3")
