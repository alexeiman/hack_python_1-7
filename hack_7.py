"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = [5, 4, 3, 2, 1, 0]
    x = 0
    while (x <= len(result)):
        print(result)
        x += 1
    return result