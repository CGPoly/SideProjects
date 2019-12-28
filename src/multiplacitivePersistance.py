# import time
import random


def max_steps(num: int, n: int = 0) -> int:
    if len(str(num)) == 1:
        return n
    res = 1
    for i in str(num):
        res *= int(i)
    return max_steps(res, n + 1)


def shorten(num: int) -> int:
    tmp = list(str(num))
    tmp.sort()
    tmp = "".join(tmp)
    return int(str(tmp).replace("1", ""))


def search(_in: int = 1):
    _max_s = 0
    _max = _in
    while _max_s < 9:
        tmp = max_steps(_in)
        if _max_s < tmp:
            _max_s = tmp
            _max = _in
            print(_max, _max_s)
        _in += 1
        # while any([i == "0" or i == "5" for i in str(_in)]):
        #     _in += 1
        

def search_random(_in: int = 1):
    _max_s = 0
    _max = _in
    while _max_s < 10:
        tmp = max_steps(_in)
        if _max_s < tmp:
            _max_s = tmp
            _max = shorten(_in)
            print(_max, _max_s)
        _in = int(random.random()*1e16)
        _in = int(str(_in).replace("0", "1").replace("5", "6"))
        # while any([i == "0" or i == "5" for i in str(_in)]):
        #     _in += 1


# print(max_steps(277777788888899))
# start = time.time()
search_random()
# end = time.time()
# print(end - start)
