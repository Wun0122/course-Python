class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class OrderItem:
    def __init__(self, drink, sweetness, ice_level):
        self.drink = drink
        self.sweetness = sweetness
        self.ice_level = ice_level
        self.total_price = self.drink.price

    def calculate_total(self):
        return self.total_price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = sum(item.total_price for item in self.items)
        return total

class BubbleTeaShop:
    def __init__(self):
        self.menu = [
            Drink("蜜春茶后", 40),
            Drink("經典五桐茶", 35),
            Drink("老實人紅茶", 30),
            Drink("桂花烏龍凍飲", 50),
            Drink("綠茶凍奶茶", 60)
        ]
        self.sweetness_levels = ["全糖", "半糖", "微糖", "無糖"]
        self.ice_levels = ["正常冰", "少冰", "去冰", "熱飲"]
        self.promotions = ["折價卷", "點數", "會員折扣"]
        self.invoice_methods = ["紙本發票", "手機載具", "愛心捐贈"]
        self.payment_methods = ["現金支付", "Line Pay"]

    def display_menu(self):
        print("歡迎光臨！本店菜單如下：")
        for idx, drink in enumerate(self.menu):
            print(f"{idx + 1}. {drink.name} - ${drink.price}")

    def get_user_input(self):
        order = Order()

        while True:
            choice = input("請選擇您要的飲料編號（輸入0結束點餐）：")
            if choice == "0":
                break

            try:
                choice = int(choice)
                if choice < 1 or choice > len(self.menu):
                    raise ValueError
            except ValueError:
                print("輸入有誤，請重新輸入。")
                continue

            drink = self.menu[choice - 1]

            print("甜度選項：")
            for idx, sweetness in enumerate(self.sweetness_levels):
                print(f"{idx + 1}. {sweetness}")
            sweetness_choice = input("請選擇甜度編號：")
            try:
                sweetness_choice = int(sweetness_choice)
                if sweetness_choice < 1 or sweetness_choice > len(self.sweetness_levels):
                    raise ValueError
            except ValueError:
                print("輸入有誤，請重新輸入。")
                continue
            sweetness = self.sweetness_levels[sweetness_choice - 1]

            print("冰塊選項：")
            for idx, ice_level in enumerate(self.ice_levels):
                print(f"{idx + 1}. {ice_level}")
            ice_choice = input("請選擇冰塊編號：")
            try:
                ice_choice = int(ice_choice)
                if ice_choice < 1 or ice_choice > len(self.ice_levels):
                    raise ValueError
            except ValueError:
                print("輸入有誤，請重新輸入。")
                continue
            ice_level = self.ice_levels[ice_choice - 1]

            order_item = OrderItem(drink, sweetness, ice_level)
            order.add_item(order_item)

        return order

    def process_order(self, order):
        print("您的訂單如下：")
        total_price = 0
        for idx, item in enumerate(order.items, start=1):
            print(f"飲料 {idx}: {item.drink.name} - {item.sweetness} - {item.ice_level} - ${item.total_price}")
            total_price += item.total_price

        print(f"總金額：${total_price}")

        # 選擇優惠方案
        print("請選擇優惠方案：")
        for idx, promotion in enumerate(self.promotions):
            print(f"{idx + 1}. {promotion}")
        promotion_choice = input("請選擇優惠方案編號：")
        try:
            promotion_choice = int(promotion_choice)
            if promotion_choice < 1 or promotion_choice > len(self.promotions):
                raise ValueError
        except ValueError:
            print("輸入有誤，請重新輸入。")
            return
        promotion = self.promotions[promotion_choice - 1]

        # 選擇付款方式
        print("請選擇付款方式：")
        for idx, payment_method in enumerate(self.payment_methods):
            print(f"{idx + 1}. {payment_method}")
        payment_choice = input("請選擇付款方式編號：")
        try:
            payment_choice = int(payment_choice)
            if payment_choice < 1 or payment_choice > len(self.payment_methods):
                raise ValueError
        except ValueError:
            print("輸入有誤，請重新輸入。")
            return
        payment_method = self.payment_methods[payment_choice - 1]

        if payment_method == "Line Pay":
            print("已成功使用 Line Pay 付款。")
        else:
            print("請準備現金，將在取餐時結帳。")

        # 選擇開立發票方式
        print("請選擇開立發票方式：")
        for idx, invoice_method in enumerate(self.invoice_methods):
            print(f"{idx + 1}. {invoice_method}")
        invoice_choice = input("請選擇開立發票方式編號：")
        try:
            invoice_choice = int(invoice_choice)
            if invoice_choice < 1 or invoice_choice > len(self.invoice_methods):
                raise ValueError
        except ValueError:
            print("輸入有誤，請重新輸入。")
            return
        invoice_method = self.invoice_methods[invoice_choice - 1]

        if invoice_method == "手機載具":
            vehicle_number = input("請輸入手機載具號碼：")
            print(f"已成功開立發票，手機載具號碼為：{vehicle_number}")
        elif invoice_method == "紙本發票":
            print("已成功開立發票，將提供紙本發票。")
        else:
            print("已成功愛心捐贈，感謝您的支持！")

        print("訂單已完成！謝謝光臨！")

    def run(self):
        self.display_menu()
        order = self.get_user_input()
        self.process_order(order)

# 主程式
if __name__ == "__main__":
    shop = BubbleTeaShop()
    shop.run()

