"""
Напишите программу банкомат. 
Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму денег

Разбейть её на отдельные операции — функции. 
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""

class ATM:
    def __init__(self):
        self.balance = 0
        self.operations_count = 0
        self.history = []

    def deposit(self, amount):
        if amount % 50 != 0:
            print("Сумма пополнения должна быть кратна 50 у.е.")
            return
        self.balance += amount
        self.operations_count += 1
        self.history.append(('deposit', amount))
        self.check_tax()
        self.check_interest()
        print(f"Вы пополнили счёт на {amount} у.е. Текущий баланс: {self.balance} у.е.")

    def withdraw(self, amount):
        if amount % 50 != 0:
            print("Сумма снятия должна быть кратна 50 у.е.")
            return
        fee = max(30, min(amount * 0.015, 600))
        if self.balance < amount + fee:
            print("Недостаточно средств на счете.")
            return
        self.balance -= amount + fee
        self.operations_count += 1
        self.history.append(('withdraw', amount))
        self.check_tax()
        self.check_interest()
        print(f"Вы сняли со счёта {amount} у.е. с комиссией {fee} у.е. Текущий баланс: {self.balance} у.е.")

    def check_interest(self):
        if self.operations_count % 3 == 0:
            interest = self.balance * 0.03
            self.balance += interest
            print(f"Начислено процентное вознаграждение в размере {interest} у.е.")

    def check_tax(self):
        if self.balance > 5000000:
            tax = self.balance * 0.1
            self.balance -= tax
            print(f"Списан налог на богатство в размере {tax} у.е.")

    def exit(self):
        print("Вы вышли из системы.")

def main():
    atm = ATM()
    while True:
        print("\nДоступные действия:")
        print("1. Пополнить")
        print("2. Снять")
        print("3. Выйти")
        choice = input("Выберите действие: ")
        if choice == '1':
            amount = int(input("Введите сумму для пополнения (кратную 50 у.е.): "))
            atm.deposit(amount)
        elif choice == '2':
            amount = int(input("Введите сумму для снятия (кратную 50 у.е.): "))
            atm.withdraw(amount)
        elif choice == '3':
            atm.exit()
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()