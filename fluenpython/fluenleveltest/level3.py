#  字典和集合详细讲解

# 创造字典的多种方法
# a1 = {"key":1,'ui':3,'po':0,4:0}
#
# a2 = dict(one=1,two=2,three=3)
#
# a3 = dict(zip(['one','er','op'],[1,2,3]))
#
# print(a1,a1[4],a2,a3)
#
# # 字典推导式 把装满元组的列表运用 语法  {表达式 for 迭代变量 in 可迭代对象[if 表达式]}
# country_code = [(51,'china'),(66,'usa'),(98,'sig'),(77,'opi'),(89,'yuo')]
# a4 = {test1:test2 for test1,test2 in country_code}
# print(len(a4))
# i=0
# for i in range(4):
#     for j in range(4):
#         print(j)
from collections import defaultdict
#
# strings = ('puppy', 'kitten', 'puppy', 'puppy',
#            'weasel', 'puppy', 'kitten', 'puppy')

# counts = {}
#
# for kw in strings:
#     if kw not in counts:
#         counts[kw] = 1
#     else:
#         counts[kw] += 1
# print(counts)
# defaultdict 可以字典设置默认值
# counts = defaultdict(lambda:0)
# for s in strings:
#     counts[s]+=1
#
# print(counts)
#
# print(lambda: 0)

# 创建一个映射类型, userdict 的使用
# import collections
#
#
# class StrKeyDict(collections.UserDict):
#        def __missing__(self, key):
#         if isinstance(key, str):
#             raise KeyError
#         return self[str[key]]  # 如果找不到键的本身就是字符串
#
#     def __contains__(self, key):  #
#         return str(key) in self.data # 使用data 方法可以直接返回字符串key
#
#     def __setitem__(self, key, value):
#         self.data[str[key]] = value # 把具体实现委托给了data
#  让字典只有只读的性质 ,只能修改原来的d ，如果修改d_pro 不可以
# from types import MappingProxyType
# d = {1:'a'}
# d_pro = MappingProxyType(d)
# print(d_pro,d_pro[1])
# print(d_pro[2])





