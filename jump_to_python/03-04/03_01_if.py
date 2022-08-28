

'''
0, False, None, [] 인지 확인할때
'''


number = 0
# (X)
if number == 0:
    print("number", number)

# (O)
if not number:
    print("number", number)


is_somthing = False
# (X)
if is_somthing is False:
    print("is_somthing", is_somthing)

# (X)
if is_somthing == False:
    print("is_somthing", is_somthing)

# (O)
if not is_somthing:
    print("is_somthing", is_somthing)


is_somthing = None
# (X)
if is_somthing is None:
    print("is_somthing", is_somthing)

# (X)
if is_somthing == None:
    print("is_somthing", is_somthing)

# (O)
if not is_somthing:
    print("is_somthing", is_somthing)



something_list = []
# (X)
if something_list is []:  # 실행 안됨 (False)
    print("something_list in if", something_list)
print("check!! something_list is []", something_list is [])
print(id(something_list), id([]))

# (X)
if something_list == []:
    print("something_list", something_list)

# (O)
if not something_list:
    print("something_list", something_list)




'''
코드의 가독성을 고려해서 들여쓰기(indent)는 최소화하는게 좋다
'''



# (X)
def func1(condition1, condition2, condition3):
    result = []

    if condition1:
        result.append(condition1)

        if condition2:
            result.append(condition2)

            if condition3:
                result.append(condition3)
                return result
    return result

# (O)
def func2(condition1, condition2, condition3):
    result = []

    if not condition1 or not condition2 or not condition3:
        return result

    for c in (condition1, condition2, condition3):
        result.append(c)
    return c


condition1 = True
condition2 = True
condition3 = True

func1(condition1, condition2, condition3)
func2(condition1, condition2, condition3)
