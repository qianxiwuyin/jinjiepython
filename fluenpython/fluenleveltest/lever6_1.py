# 基于lever 6的优化项  用于对比

# 1.策略模式

from abc import ABC, abstractmethod
from collections import namedtuple
from inspect import getmembers

# 定义
Customer = namedtuple('Customer', 'name fidelity')


class LineItem:  # 定义参数

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # 上下文

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):  # 定义优惠力度
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
            print('op', discount)
        return self.total() - discount

    def __repr__(self):  # 给函数命名 自我介绍
        fmt = '<Order total:{:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


# class Promotion(ABC):  # 策略：抽象基类 作为一个中转 为了使用装饰器abs
# #     @abstractmethod
# #     def discount(self, order):
# #         """返回折扣金额 正值 父类 的 discount"""  新的优化这里删除掉
promos = []


def promotion(promo_func):  # 把函数添加到列表 然后原封不动的
    promos.append(promo_func)
    return promo_func


@promotion
def Fidelity_Promo(order):  # 第一个具体策略 继承Order 以前继承prontion
    """为积分为1000或以上的顾客提供5%折扣"""

    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
def BulkItem_Promo(order):  # 第二个策略
    "单个商品为20个或以上时提供10%折扣"
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


@promotion
def Large_Order_Promo(order):
    """订单中的不同商品达到10个或以上时提供7%的折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


def bes_promo(order):
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)


if __name__ == '__main__':
    joe = Customer('John', 0)
    ann = Customer('Ann SMITH', 1100)
    cart = [LineItem('banana', 4, 0.5), LineItem('apple', 10, 1.5), LineItem('watermelon', 5, 5.0)]
    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    a = Order(joe, cart, bes_promo)
    print(a)
