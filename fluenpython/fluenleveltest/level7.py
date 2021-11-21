# 基础了解

# registry = []
#
#
# def register(func):
#     print('running register(%s)' % func)
#     registry.append(func)
#     return func
#
#
# @register
# def f1():
#     print('running f1()')
#
#
# @register
# def f2():
#     print('running f2()')
#
# #f3 没有装饰器
# def f3():
#     print('running f3()')
#
#
# def main():
#     print('running main()')
#     print('registry ->', registry)
#     f1()
#     f2()
#     f3()
#
#
# if __name__ == '__main__':
#     main()

# 7.4 变量作用域规则

class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_values):
        self.series.append(new_values)
        total = sum(self.series)
        return total / len(self.series)


# 闭包的高阶思想

# def make_Averager():
#     series = []   # 这里虽然不会被初始化 因为返回函数会存储数据 ，自由变量才会有这个存储功能
#
#     def averager(new_values):
#
#         series.append(new_values)
#         total = sum(series)
#         return total / len(series)
#
#     return averager

# 7.6 noncal 声名

# def make_Averager():
#     count = 0
#     total = 0
#
#     def averager(new_value):
#         """
#         这里加声明是因为 字符串 元组数字 不可变类型，只能读取不能更新
#         列表是可变的可引用， 所以声明使用于不可变变量
#         """
#         nonlocal count, total
#         count += 1
#         total += new_value
#         return total/count
#     return averager

# 实现简单的装饰器
