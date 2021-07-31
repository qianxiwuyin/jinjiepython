# import collections
# from random import choice
#
# Card = collections.namedtuple('Card', ['rank', 'suit'])
#
# """扑克牌式练习"""
# class FrenchDeck:
#     """这个库可以创作"""
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = 'spades diamonds clubs hearts'.split()
#
#     def __init__(self):
#         self._cards = [Card(rank, suit) for suit in self.suits
#                        for rank in self.ranks]
#
#     def __len__(self):
#         return len(self._cards)
#
#     def __getitem__(self, position):
#         return self._cards[position]
#
#
# # 定义花色等级的字典
#
# suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
#
#
# def spades_high(card):
#     rank_value = FrenchDeck.ranks.index(card.rank)
#     return rank_value * len(suit_values) + suit_values[card.suit]
#
#
# deck = FrenchDeck()
#
#
# for card in sorted(deck,key=spades_high):
#     print(card)
#

# 模拟数值类型
import array

# symbols = '$%*#'
# beyond_ascii = [ord(s) for s in symbols if ord(s) > 17]
# print(beyond_ascii)
# a = list(filter(lambda c: c > 17, map(ord, symbols)))
# print(a)
#
# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
# for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
#     print(tshirt)
#
# # 元组的记录功能
#
# lax_coordinates = (33.9425, -118.408056)
# city, year, pop, chg, area = ('TOKYO', 2003, 32450, 0.66, 8014)
# traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ERP', 'XDA851478')]
# for passport in sorted(traveler_ids):
#     print('%s/%s' % passport)
#
# for _, country in traveler_ids:
#     print(country)
#
# import os
#
# _, filename = os.path.split('/home/lucianl/.sh/idrd.sd')
# print(filename)

# metro_ares = [('tokyo','jp',36.33,(35,-88)),('as','as',44,(12,33)),('b','bb',44,(12,33))]
# print('{:12} | {:^9} | {:9}'.format('','lat.','long.'))
# fmt = '{:12} | {:9.4f} | {:9.4f}'
# for name,cc,pp,(lan,long) in metro_ares:
#     if long <= 0:
#         print(fmt.format(name,lan,long))

# from collections import namedtuple
#
# city = namedtuple('city','name country population coordinates')
# tokyo = city('tokyo','jp',38.33,(12,33))
# latlong = namedtuple('latlong','lat long')
# delhi_data = ('delhi dcr','in',21.935,latlong(28,77))
# delhi = city._make(delhi_data)
# print(delhi._asdict())
# for key,value in delhi._asdict().items():
#     print(key + ':', value)

# import sys
# import bisect
#
# """对于索引判断位置"""
# haystack = [1, 2, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
# needles = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
#
# row_fmt = '{0:2d} @ {1:3d}   {2}{0:<3d}'
#
#
# def demo(bisect_fn):
#     for needle in reversed(needles):
#         position = bisect_fn(haystack, needle)
#         offset = position * '  |'
#         print(row_fmt.format(needle, position, offset))
#
#
# if __name__ == '__main__':
#     if sys.argv[-1] == 'left':
#         bisect_fn = bisect.bisect_left()
#     else:
#         bisect_fn = bisect.bisect
#     print('demo:', bisect_fn.__name__)
#     print('haystack -', ''.join('%3d' % n for n in haystack))
#     demo(bisect_fn)
#
#
# # 先用bisect 去标准分数，然后再转化成英文成绩
# def grade(score, breakpoints=[60, 70, 80, 90], greades='FDCBA'):
#     i = bisect.bisect(breakpoints, score)
#     print(i)
#     return greades[i]
#
#
# a = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
# print(a)

'''bisect.insort 有序队列使用的方法'''
# import bisect
# import random
# '''
# 对列表和元组有效 可以使用数组 array ，array 是数字的机器翻译，
# '''
# SIZE = 7
# random.seed(1729) # 固定随机数
# my_list = []
# for i in range(SIZE):
#     # 从0-14 取随机数
#     new_item = random.randrange(SIZE*2)
#     bisect.insort(my_list,new_item)
#     print('%2d -' % new_item,my_list)

"""数组 只包含数字的列表 比list高效"""

from array import array
from random import random
#
# floats = array('d', (random() for i in range(10 ** 7)))  # d 表示dobble
# print(floats[-1])
# fp = open('floats.bin', 'wb')
# floats.tofile(fp)  # 把数组存到二进制文件里面
# fp.close()
# floats2 = array('d')  # 新键一个双精度浮点数组
# fp = open('floats.bin', 'rb')  # 以二进制格式打开一个文件用于只读
# floats2.fromfile(fp, 10 ** 7)  # fromfile 只能读
# fp.close()
# print(floats2[-1])  # 查看新数组元素
# if floats == floats2:
#     print(True)
#
# # 总结 floats.tofile(fp)写入，floats2.fromfile(fp,10**7)读取

# 内存视图 作为字节替换
# numbers = array('h',[-2,-1,0,1,2])
# memv = memoryview(numbers)
# print(len(memv))
# memv_oct = memv.cast('B')
# print(memv_oct.tolist())
# memv_oct[5] = 4
# print(memv_oct)
# print(numbers)

# numpy 库的了解
# import numpy
# a = numpy.arange(12)
# a.shape = 3,4 # 改成二维数组 三行四列
# a[:,1] # 只打印列 array([1, 5, 9])
# a.transpose() # 把行和列交换

# import numpy
# floats = numpy.loadtxt('floats-10m-lines.txt')
# floats[-3:]


# 队列
from collections import deque
dq = deque(range(10),maxlen=10)#maxlen 限制队列的长度
dq.rotate(3)# 当数字大于零的时候 n个 元素会被移到左边，小于0时会被移到右边
dq.appendleft(-1) # 在左边添加一位数，但是队列已满就会把末尾的数字删除
dq.extend([11,22,33]) # 在尾部添加的话，前面的都会被删掉，挤掉-1，1，2
dq.extendleft([10,20,30,40]) # 会逆序添加到左边 40，30，20，10，3，4

