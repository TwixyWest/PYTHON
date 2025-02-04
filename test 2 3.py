import random

class Account:
    def __init__(self, name, address, login, password):
        self.id = random.randint(1000, 9999)
        self.name = name
        self.address = address
        self.login = login
        self.password = password
        self.balance = 0
        self.debt = 0

    def display_info(self):
        print(f"\nІнформація про акаунт:")
        print(f"ID: {self.id}")
        print(f"Ім'я: {self.name}")
        print(f"Адреса: {self.address}")
        print(f"Баланс: {self.balance} грн")
        print(f"Борг: {self.debt} грн\n")


accounts = []
current_account = None


def login():
    global current_account
    login_input = input("Введіть логін: ")
    password_input = input("Введіть пароль: ")

    for acc in accounts:
        if acc.login == login_input and acc.password == password_input:
            print(f"Вхід успішний! Вітаємо, {acc.name}.")
            current_account = acc
            return
    print("Неправильний логін або пароль.")


def create_account():
    name = input("ім'я: ")
    address = input("адреса: ")
    login = input("логін створ швидка: ")
    password = input("пароль: ")
    new_acc = Account(name, address, login, password)
    accounts.append(new_acc)
    print(f"акаунт створено. Ваш ID: {new_acc.id}")

def change_password():
    if current_account:
        new_password = input("новий пароль: ")
        current_account.password = new_password
        print("Пароль змінено")
    else:
        print("спочатку увійшов в акаунт")


def deposit_money():
    if current_account:
        try:
            amount = int(input("Сума для поповнення: "))
            if amount > 0:
                current_account.balance += amount
                print(f"Баланс поповнено на {amount} грн. Поточний баланс: {current_account.balance} грн.")
            else:
                print("Сума повинна бути більше 0")
        except ValueError:
            print("Введіть правильну суму")
    else:
        print("Спочатку увійди в акаунт")


def withdraw_money():
    if current_account:
        try:
            amount = int(input("Сума для зняття: "))
            if 0 < amount <= current_account.balance:
                current_account.balance -= amount
                print(f"Ви зняли {amount} грн. Поточний баланс: {current_account.balance} грн.")
            else:
                print("Недостатньо коштів або неправильна сумаю")
        except ValueError:
            print("Введіть правильну сумму.")
    else:
        print("Спочатку увійдіть в акаунт.")


def transfer_money():
    if current_account:
        try:
            recipient_id = int(input("Введіть ID отримувача: "))
            amount = int(input("Сума переказу: "))

            if amount <= 0:
                print("Сума повинна бути більше нуля!!!!!!!!!!!!!!!!!!!")
                return

            recipient = next((acc for acc in accounts if acc.id == recipient_id), None)
            if recipient is None:
                print("акаунт отримувача не знайдено.LOOOSER")
                return

            if current_account.balance >= amount:
                current_account.balance -= amount
                recipient.balance += amount
                print(f"Переказ успішний! Ваш баланс: {current_account.balance} грн.")
            else:
                print("Недостатньо коштів для переказу.")
        except ValueError:
            print("ID та сума повинні бути числами!")
    else:
        print("Спочатку увійдіть в акаунт.")

def take_loan():
    if current_account:
        try:
            loan_amount = int(input("Сума кредиту: "))
            if loan_amount > 0:
                current_account.balance += loan_amount
                current_account.debt += loan_amount
                print(f"Ви взяли кредит на {loan_amount} грн. Борг: {current_account.debt} грн.")
            else:
                print("Сума повинна бути більше нуля!!!!!!!!!!")
        except ValueError:
            print("Введіть коректну суму!!!!!!!!")
        else:
            print("Спочатку увійдіть в акаунт!!!!!!!!!!!!")

        def rob_bank():
            if current_account:
                success = random.choice([True, False])
                if success:
                    reward = random.randint(500, 2000)
                    current_account.balance += reward
                    print(f"Вам пощастило!ВАС НЕ СПІЙМАЛИ МУСОРА{reward} грн.")
                else:
                    print("Вас зловили! Штраф 1000000 грн і тюряга на 25 років.")
                    current_account.balance = max(0, current_account.balance - 1000)
            else:
                print("Спочатку увійдіть в акаунт!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        def logout():
            global current_account
            if current_account:
                print(f"До побачення, {current_account.name}!")
                current_account = None
            else:
                print("Ви не ввійшли в акаунт.")

        def main():
            while True:
                print("\nДоступні команди:")
                print("1. Створити акаунт")
                print("2. Увійти в акаунт")
                print("3. Змінити пароль")
                print("4. Поповнити баланс")
                print("5. Зняти гроші")
                print("6. Переказати гроші")
                print("7. Взяти кредит")
                print("8. Пограбувати банк")
                print("9. Інформація про акаунт")
                print("10. Вийти з акаунту")
                print("11. Вихід з програми")

                choice = input("номер команди: ")

                if choice == "1":
                    create_account()
                elif choice == "2":
                    login()
                elif choice == "3":
                    change_password()
                elif choice == "4":
                    deposit_money()
                elif choice == "5":
                    withdraw_money()
                elif choice == "6":
                    transfer_money()
                elif choice == "7":
                    take_loan()
                elif choice == "8":
                    rob_bank()
                elif choice == "9":
                    if current_account:
                        current_account.display_info()
                    else:
                        print("Спочатку увійдіть в акаунт!!!!!!!!!!!!!!!!!!!")
                elif choice == "10":
                    logout()
                elif choice == "11":
                    print("Програма завершена. БАЙ БАЙ!")
                    break
                else:
                    print("ХЗ ЩО ЗА КОМАНДА.")
                if __name__ == "__main__":
                    main()
