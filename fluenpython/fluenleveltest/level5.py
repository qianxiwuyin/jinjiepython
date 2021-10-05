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

# def tag(name, cls=None, *content, **attrs):
#     """生成一个或者多个HTML 标签"""
#     if cls is not None:
#         attrs['class'] = cls
#     if attrs:
#         attr_str = ''.join(' %s="%s"' % (attr,value)
#                            for attr,value
#                            in sorted(attrs.items()))
#     else:
#         attr_str = ''
#     if content:
#         return '\n'.join('<%s%s>%s</%s>' %
#                          (name,attr_str,c,name) for c in content)
#     else:
#         return '<%s%s />' % (name,attr_str)
#
# if __name__ == '__main__':
#     a = {'name':'img','io':'09'}
#     b=('img',9,45)
#     print(tag(*b))

# def clip(text:str,max_len:'int > 0 ' = 80) -> str:
#     """在 max——len 前面或者后面的第一个空格处截断文本,注解 的妙用
#     :param text:
#     :param max_len: 最长值
#     :return:
#     """
#     end = None
#     if len(text) > max_len:
#         space_before = text.find(' ',0,max_len)# 指定检索空格
#         print('3',space_before)
#         if space_before >= 0:
#             end = space_before
#         else:
#             space_after = text.find(' ',max_len)
#             print(space_after)
#             if space_after >= 0:
#                 end = space_after
#     if end is None: # 没有找到空格
#         end = len(text)
#     return text[:end].rstrip()

# 函数声明的例子
# """把tag签名绑在一个参数字段上"""
# import inspect
# def tag(name, cls=None, *content, **attrs):
#     """生成一个或者多个HTML 标签"""
#     if cls is not None:
#         attrs['class'] = cls
#     if attrs:
#         attr_str = ''.join(' %s="%s"' % (attr,value)
#                            for attr,value
#                            in sorted(attrs.items()))
#     else:
#         attr_str = ''
#     if content:
#         return '\n'.join('<%s%s>%s</%s>' %
#                          (name,attr_str,c,name) for c in content)
#     else:
#         return '<%s%s />' % (name,attr_str)
#
# sig = inspect.signature(tag)
# my_tag = {'name':'img','title':'Sunset Boulevard',
#           'src':'sunset.jpg','cls':'framd'}
# bound_args = sig.bind(**my_tag)
# for name,values in bound_args.arguments.items():
#     print(name,'=',values)

# 5.10 介绍函数式编程的包 主要式两个模块 operator 和

# from functools import reduce
# from operator import mul
# from operator import itemgetter
#
#
# def fact(n: int):
#     return reduce(mul, range(1, n + 1))
#
#
# metro_data = [('tokyo', 'jp', 36.44, (35.4, 12.4)), ('delhi ncr', 'in', 36.45, (35.5, 121.4)),
#               ('moxige', 'mo', 37.44, (37.4, 13.4))]
#
# for city in sorted(metro_data,key=itemgetter(2)):
#     # itemgetter(1) 类似与lamda a:a[1] 一样 返回索引1的位置，按照国家代码第二个
#     print(city)
#
# cc_name = itemgetter(1,0) # 按照多元参数传给itemgetter 他会构建函数返回提取的值构成元素
# for city in metro_data:
#     print(cc_name(city))

#
# from collections import namedtuple
#
#
# metro_data = [('tokyo', 'jp', 36.44, (35.4, 12.4)), ('delhi ncr', 'in', 36.45, (35.5, 121.4)),
#               ('moxige', 'mo', 37.44, (37.4, 13.4))]
#
# LatLong = namedtuple('LatLong','lat long')
# Metropolis = namedtuple('Metropolis','name cc pop coord')
#
# metro_areas = [Metropolis(name,cc,pop,LatLong(lat,long))
#                for name,cc,pop,(lat,long) in metro_data]
#
# print(metro_areas[0])

# 这是用nametuple 展示

# 使用methodcaller 使用实例 第二个测试展示绑定额外参数方式

# from operator import methodcaller
# s = 'this is time'
# upcase = methodcaller('upper') # 传参以字符串的形式调用
# print(upcase(s))
# hiphenate = methodcaller('replace',' ','-')
# print(hiphenate(s))

# 使用赴南昌tools。partial冻结参数 使用这个函数可以把接受一个或多个参数的函数改编成需要回调的api
# from operator import mul
# from functools import partial
#
# triple = partial(mul,3)
# print(triple(7)) # 把其中一个参数定为3  然后需要传成7
# a = list(map(triple,range(1,10)))
# print(a)

# 常用于多国编写脚本
# import unicodedata,functools
#
# nfc = functools.partial(unicodedata.normalize,'NFC')
# s1 = 'café'
# S2 = 'cafe\u0301'
# print(s1,S2)
# print(s1==S2)
# print(nfc(s1) == nfc(S2))



import inspect
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

sig = inspect.signature(tag)
my_tag = {'name':'img','title':'Sunset Boulevard',
          'src':'sunset.jpg','cls':'framd'}

