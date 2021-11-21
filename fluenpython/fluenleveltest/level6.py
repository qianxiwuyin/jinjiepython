"""
第6章  一等函数实现设计模式
"""

# 1.策略模式

from abc import ABC, abstractmethod
from collections import namedtuple

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
            print('erer', self.__total)
        return self.__total

    def due(self): #定义优惠力度
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
            print('op', discount)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total:{:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):  # 策略：抽象基类 作为一个中转 为了使用装饰器abs
    @abstractmethod
    def discount(self, order):
        """返回折扣金额 正值 父类 的 discount"""


class FidelityPromo(Promotion):  # 第一个具体策略
    """为积分为1000或以上的顾客提供5%折扣"""

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):  # 第二个策略
    "单个商品为20个或以上时提供10%折扣"

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):
    """订单中的不同商品达到10个或以上时提供7%的折扣"""

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        # print(distinct_items)
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0


if __name__ == '__main__':
    joe = Customer('John', 0)
    ann = Customer('Ann SMITH', 1100)
    cart = [LineItem('banana', 4, 0.5), LineItem('apple', 10, 1.5), LineItem('watermelon', 5, 5.0)]
    a = Order(joe, cart, FidelityPromo())
    b = Order(ann, cart, FidelityPromo())  # m没有达到10哥以上
    # 产品20个的时候
    banana_cart = [LineItem('banana',30,.5),LineItem('apple',10,1.5)]
    c = Order(joe,banana_cart,BulkItemPromo())
    # long 多个产品
    long_order = [LineItem(str(item_code),1,1.0) for item_code in range(10)]
    d = Order(joe,long_order,LargeOrderPromo())
    print(d)
