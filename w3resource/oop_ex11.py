class Bank:
    def __init__(self) -> None:
        self.customers = {}

    def create_account(self, id_account: int, balance: float) -> None:
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным!")
        if id_account in self.customers:
            raise ValueError("Аккаунт с таким id уже существует!")
        self.customers[id_account] = balance
        print(f"Аккаунт с id:{id_account} и балансом:{balance} успешно создан")

    def deposite(self, id_account: int, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сумма зачисления не может быть меньше или равной нулю!")
        if id_account not in self.customers:
            raise ValueError("Аккаунт с таким id не существует!")
        self.customers[id_account] += amount
        print(
            f"Аккаунт с id:{id_account} успешно пополнен на сумму:{amount}. Итогоый баланс: {self.customers[id_account]}"
        )

    def withdrawal(self, id_account: int, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сумма снятия не может быть меньше или равной нулю!")
        if amount > self.customers[id_account]:
            raise ValueError("Сумма снятия не может быть больше чем ваш баланс!")
        if id_account not in self.customers:
            raise ValueError("Аккаунт с таким id не существует!")
        self.customers[id_account] -= amount
        print(
            f"С аккаунта с id:{id_account} успешно произведено снятие на сумму:{amount}. Итогоый баланс: {self.customers[id_account]}"
        )

    def check_balance(self, id_account: int) -> str:
        if id_account not in self.customers:
            raise ValueError("Аккаунт с таким id не существует!")
        return f"Баланс аккаунта с id: {id_account} равен: {self.customers[id_account]}"


bank = Bank()
bank.create_account(1, 100)
bank.create_account(2, 200)
bank.create_account(3, 300)
print(bank.customers)

bank.deposite(3, 100)
print(bank.customers)

bank.withdrawal(2, 200)
print(bank.customers)

print(bank.check_balance(1))
