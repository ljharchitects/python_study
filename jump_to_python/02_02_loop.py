import time
import dis


def while_func(count):
    i = 0
    result_list = []
    while i < count:
        i += 1
        result_list.append(i)
    return result_list


def for_func(count):
    result_list = []
    for i in range(count):
        result_list.append(i)
        pass
    return result_list


def for_com_func(count):
    return [i for i in range(count)]


COUNT = 10_000_000

while_start = time.time()
while_result = while_func(COUNT)
print("while time : ", time.time() - while_start)


for_start = time.time()
for_func(COUNT)
print("for time : ", time.time() - for_start)

for_com_start = time.time()
for_com_func(COUNT)
print("for_com_start time : ", time.time() - for_com_start)


dis.dis(while_func)
print("*" * 50)
dis.dis(for_func)
print("*" * 50)
dis.dis(for_com_func)
