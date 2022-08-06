import time

COUNT = 50_000

# list
t0 = time.time()
target_list = list(range(COUNT))
for i in range(COUNT):
    if i in target_list:
        pass
print("list : ", time.time() - t0)

# set
t1 = time.time()
target_set = set(range(COUNT))
for i in range(COUNT):
    if i in target_set:
        pass
print("set : ", time.time() - t1)
