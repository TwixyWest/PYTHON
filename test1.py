import random

Money = 600
password = "1234"
login_attempts = 0
fake_money_attempts = 0


def login():
    global login_attempts
    print("\nВведіть ваш пароль:")
    entered_pass = input()
    if entered_pass == password:
        print("Ласкаво просимо!")
        return True
    else:
        login_attempts += 1
        print("Невірний пароль!")
        if login_attempts >= 3:
            print("Ви заблоковані через 3 невірні спроби.")
            return False
        return False


def ChangePass():
    global password
    print("\nВведіть новий пароль:")
    password = input()
    print("Пароль змінено!")


def Fakemoney():
    global Money, fake_money_attempts
    fake_money_attempts += 1

    if fake_money_attempts > 5 and random.random() < 0.3:
        print("\nВас спіймали поліція! Ви втратили всі фейкові гроші!")
        Money = 0
        fake_money_attempts = 0
    else:
        fake_money = random.randint(100, 1000)
        Money += fake_money
        print(f"Ви отримали {fake_money}$ фейкових грошей!")


def Work():
    global Money
    Money += 100
    print("Ви працювали і заробили 100$!")


def BankRob():
    global Money
    success = random.choice([True, False])
    if success:
        Money += 100000
        print("Ви успішно пограбували банк і отримали 100000$!")
    else:
        print("Вас спіймали! Ви втратили гроші і вас заарештовано.")
        Money = 0


def Log():
    print(f"\nВаш баланс: {Money}$")
    print(f"Кількість спроб входу: {login_attempts}")


def ATM():
    global Money
    print("\nВведіть суму для зняття з банкомату:")
    withdrawal = int(input())
    if withdrawal > Money:
        print("У вас недостатньо грошей для зняття!")
    else:
        Money -= withdrawal
        print(f"Ви зняли {withdrawal}$, залишок на рахунку: {Money}$")
def main():
    global Money, login_attempts, fake_money_attempts
    logged_in = False
    while not logged_in:
        logged_in = login()

    while True:
        print("\nОберіть дію:")
        print("1 - Змінити пароль")
        print("2 - Отримати фейкові гроші")
        print("3 - Працювати (+100$)")
        print("4 - Пограбувати банк (+100000$)")
        print("5 - Переглянути журнал (баланс та спроби входу)")
        print("6 - Зняти гроші з банкомату")
        print("7 - Перевірити баланс")
        print("8 - Вийти")

        choice = input()

        if choice == "1":
            ChangePass()
        elif choice == "2":
            Fakemoney()
        elif choice == "3":
            Work()
        elif choice == "4":
            BankRob()
        elif choice == "5":
            Log()
        elif choice == "6":
            ATM()
        elif choice == "8":
            print("Вихід з гри...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")



main()
