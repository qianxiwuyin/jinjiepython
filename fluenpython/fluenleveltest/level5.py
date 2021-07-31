""" 关于函数的进阶 第五章"""

from functools import reduce
from operator import add
import random

# def fact(n):
#     """return n"""
#     return 1 if n < 2 else n * fact(n - 1)

# 给一个单词长度列表排序

# l = ['strawberry','fig','apple','cherry','raspberry','banana']
# sorted(l,key=len)
# sorted(l,reverse=True)
#
# # 推导map和filter 和列表推导比较 结果 列表清晰容易替代他们
# a = list(map(fact, filter(lambda n: n % 2, range(6))))
# b= [fact(n) for n in range(6) if n % 2]
# print(a,b)

# reduce and add 比较 连续累加之和 sum 更方便因为不需要导包
# a = reduce(add,range(100))
# b = sum(range(100))
# print(a,b)

# 7种可调用对象
"""
7种
内置函数： len，time
内置方法：c语言 dict.get
方法 ： 在类的定义中定义函数
类： 调用类运行类的——new————方法，然后运行--init--
类的实例： 如果定义类的实例__call__ 的方法，他的实例可以作为函数调用
生成器函数： yield 函数和方法
"""


# class BingoCage:  # call 方法的用法
#
#     def __init__(self, items):  # 接受可迭代对象
#         self._items = list(items)  # 控制列表传入
#         random.shuffle(self._items)
#
#     def pick(self): # 如果pick 为空 抛出异常
#         try:
#             return self._items.pop()
#         except IndexError:
#             raise LookupError('pick from empty BingoCage')
#
#     def __call__(self):
#         return self.pick() # bingo.pick() 的快捷方式式bingo（）

# def uppper_case_name(obj):
#     return ("%s %s" % (obj.first_name, obj.last_name)).upper()
#
# uppper_case_name.short_description = 'adasdfsdf'

def tag(name, cls=None, *content, **attrs):
    """生成一个或者多个HTML 标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr,value)
                           for attr,value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name,attr_str,c,name) for c in content)
    else:
        return '<%s%s />' % (name,attr_str)

if __name__ == '__main__':
    a = {'name':'img','io':'09'}
    b=('img',9,45)
    print(tag(*b))