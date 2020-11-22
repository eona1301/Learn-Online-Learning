class Stock:
    def __init__(self, name, code, PER, PBR, revenue):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.revenue = revenue

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def set_per(self, PER):
        self.PER = PER

    def set_PBR(self, PBR):
        self.PBR = PBR

    def set_dividend(self, revenue):
        self.revenue = revenue

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code


samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
hyundea = Stock("현대차", "005380", 8.70, 0.35, 4.27)
lg = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

stock_list = [samsung, hyundea, lg]

for data in stock_list:
    print(data.code, data.PER)
