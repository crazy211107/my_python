from typing import Type


class Student:
    name = None
    age = None
    tel = None
    __Private_var = None  # 私有变量

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        self.__Private_var = "私有变量"
        print("构造函数")

    def __say_hi1(self):
        print(f"{self.name}hello world")

    def say_hi(self, msg):
        print(f"hello我是{self.name} 大家好 {msg}")

    def __str__(self):
        return f"Student类对象,name= {self.name}, age={self.age}, tel= {self.tel}"

    def __lt__(self, other):  # 小于
        return self.age < other.age

    def __gt__(self, other):  # 大于
        return self.age > other.age

    def __le__(self, other):  # 小于等于
        return self.age <= other.age

    def __ge__(self, other):  # 大于 等于
        return self.age >= other.age

    def __eq__(self, other):  # 等于
        return self.age == other.age


stu1 = Student("源宝", 18, 17892102)
stu2 = Student("版本", 19, 19292102)

stu1.say_hi("我是大宝贝")

print(stu1)
print(stu1 < stu2)


class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


clock = Clock()
clock.ring()


# 单继承
class Phone:
    IMEI = None
    producer = "华为"

    def call_by_4G(self):
        print("4G通话")

    def read_card(self):
        print("读取phone")

    def call(self):
        print("父类的通话")


class phone222(Phone):
    face_id = True

    def call_by_5G(self):
        print("5G通话")

    def call(self):
        print("子类的通话")
        # 调用父类的成员
        print(f"方式一父类的品牌是{Phone.producer}")
        print(f"方式二父类的品牌是{super().producer}")


# 多态
phone = phone222()
phone.call()


# 多继承
class NFC:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("读取NFC")

    def write_card(self):
        print("写进NFC")


class MyPhone(Phone, NFC):
    pass  # 假若子类不想添加内容 但它内部不可以空着 使用pass代替


myphone = MyPhone()
myphone.call_by_4G()
myphone.read_card()

var_1: int = 10
var_2: float = 3.1415
stu: Student = Student("密码", 10, 219130)

my_list: list = [1, 2, 5]
my_tuple: tuple = (1, 3, 6)
my_set: set[int] = {1, 5, 8}
my_dict: dict[str, int] = {"ithe", 218}

import random

var_7 = random.randint(1, 10)  # type: int

from typing import Union


def add(x: int, y: int) -> Union[int, str]:
    """

    :param x:
    :param y:
    :return:
    """
    return x + y


print(add(10, 89))


# 多态
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):

    def speak(self):
        print("喵喵喵")


def make_noice(animal: Animal):
    animal.speak()


cat = Cat()
dog = Dog()
make_noice(cat)
make_noice(dog)