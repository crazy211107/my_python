
class Record:

    def __init__(self, data, order_id, money, province) :
        # 成员变量直接在下面定义
        self.data = data
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        # 这里是return
        return f"{self.data}, {self.order_id}, {self.money}, {self.province}"



