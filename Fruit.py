def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: Введите целое число.")


def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка: Введите число с плавающей точкой.")


class Fruit:
    def __init__(self, index, is_import):
        self.id = index
        self.title = input("Введите наименование товара\t")
        self.is_import = is_import
        self.orders = None
        self.nick_localized_data = {}
        print(f"\t*весовой*\n\tТовар № {self.id}") if is_import == 0 else print(f"*импортный*\n\tТовар № {self.id}")
        if self.title != 'импорт' and self.title != 'стоп':
        # if self.title.lower() in ['импорт', 'стоп']:
            self.purchase_price = get_valid_int("Введите закупочную цену\t")
            self.owner = input(f"Введите хоязина {self.title}\t")
            self.price = get_valid_int(f"Введите отправочную цену {self.title}\t")
            if self.is_import == 0:
                self.tare = get_valid_float(f"Введите тару для {self.title}\t")
            else:
                self.imp_weight = get_valid_int("Введи вес за 1 у.е.\t")
            self.nick_localized_data = self.get_clients_data()

    def get_nicks_counts_weights(self):
        while True:
            if self.is_import == 0:
                orders = list(map(str, input(f"{self.title}\n\tчерез запятую запишите НИК-КОЛЛИЧЕСТВО-ВЕС,"
                                             f"\nв следущем формате АА-5-105.4,Ж-7-243.2,Р-3-200.3\n").upper().strip().split(
                    ',')))[:]
                fields = ['nick', 'quantity', 'weight']
                if all(len(order.split('-')) == len(fields) for order in orders):
                    return orders
            else:
                orders = list(map(str, input(f"{self.title}\n\tчерез запятую запишите НИК-КОЛЛИЧЕСТВО,"
                                             f"\nв следущем формате АА-5,Ж-10,Р-3\n").upper().strip().split(',')))[:]
                fields = ['nick', 'quantity']
                if all(len(order.split('-')) == len(fields) for order in orders):
                    return orders
            print("Некорректный ввод. Пожалуйста, введите данные в правильном формате.")

    def get_general_data(self):
        general_data = {}
        nicks = []
        counts = []
        weights = []
        total_weight = 0
        total_count = 0
        field_title = 'тара'
        net_weight_field = 'чистый вес'
        avg_weight_field = ''
        net_weight = 0
        avg_weight=0
        for order in self.orders:
            fields = order.split('-')
            counts.append(int(fields[1]))
            total_count += int(fields[1])
            nicks.append(fields[0])
            if self.is_import == 0:
                weights.append(float(fields[2].strip()))
                total_weight += float(fields[2].strip())
                weight = ["{:.1f}".format(total_weight), weights]
                tare_weight = self.tare
                amount = int((total_weight - (total_count * self.tare)) * self.purchase_price)
                margin = int((total_weight - (total_count * self.tare)) * (self.price - self.purchase_price))
                avg_weight = [total_weight / total_count, total_weight - (total_count * self.tare)]
                net_weight = total_weight - (total_count * self.tare)
            else:
                weight = total_count * self.imp_weight
                field_title = 'вес'
                tare_weight = self.imp_weight
                amount = int(total_count * self.purchase_price)
                margin = int(total_count * (self.price - self.purchase_price))
                avg_weight_field = None
                net_weight_field = None
            general_data[self.title] = {
                'наименование': [self.title, nicks],
                'кол-во': [total_count, counts],
                'ВЕС': weight,
                field_title: tare_weight,
                'отпр': self.price,
                'закуп': self.purchase_price,
                'хозяин': self.owner,
                'сумма': amount,
                'маржа': margin,
                avg_weight_field: avg_weight,
                net_weight_field: net_weight
            }
        return general_data

    def get_clients_data(self):
        localized_data = {}
        self.orders = self.get_nicks_counts_weights()
        for order in self.orders:
            fields = order.split('-')
            if self.is_import == 0:
                weight = float(fields[2].strip())
                net = float(fields[2].strip()) - (int(fields[1].strip()) * self.tare)
                tare = self.tare
                amount = round(self.price * (float(fields[2].strip()) - (int(fields[1].strip()) * self.tare)))
            else:
                tare = None
                net = None
                weight = int(fields[1]) * self.imp_weight
                amount = int(fields[1]) * self.price
            localized_data[fields[0].strip()] = {
                'quantity': fields[1],
                'weight': weight,
                'net': net,
                'tare': tare,
                'amount': amount
            }
        return localized_data
