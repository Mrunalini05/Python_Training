'''def fun(x):
    if x==6:
        return
    print(x)
    fun(x+1)
    print(x)
fun(1)
print('hi')
'''


def fun(x):
    if x==6:
      return 500
    print(x)
    t=fun(x+1)
    print(x)
    return t
print(fun(1))


'''def fun(x):
    return
fun(5)
'''

'''def fun(x):
    return
print(fun(5))
'''

'''def fun(x):
    return 500
print(fun(5))
'''