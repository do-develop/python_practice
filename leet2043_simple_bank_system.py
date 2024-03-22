from threading import RLock

class Bank:
    class Account:
        def __init__(self, balance: int):
            self.balance = balance
            self.lock = RLock()

        def deposit(self, amount: int):
            self.lock.acquire()
            try:
                self.balance += amount
            finally:
                self.lock.release()
        
        def withdraw(self, amount: int):
            self.lock.acquire()
            try:
                if self.balance < amount:
                    return False
                self.balance -= amount
            finally:
                self.lock.release()
            return True

    def __init__(self, balance: List[int]):
        self.lock: RLock = RLock()
        self.accounts: List[self.Account] = []
        for b in balance:
            self.accounts.append(self.Account(b))

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        acc1: self.Account = self.get_account(account1)
        acc2: self.Account = self.get_account(account2)

        if not acc1 or not acc2 or money < 0:
            return False
        
        try:
            acc1.lock.acquire()
            acc2.lock.acquire()
            if acc1.withdraw(money):
                acc2.deposit(money)
            else:
                return False
        finally:
            acc1.lock.release()
            acc2.lock.release()
        return True

    def deposit(self, account: int, money: int) -> bool:
        if self.check_is_valid_account(account):
            self.get_account(account).deposit(money)
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.check_is_valid_account(account):
            return self.get_account(account).withdraw(money)
        return False

    def check_is_valid_account(self, account:int) -> Account:
        return account > 0 and account <= len(self.accounts)

    def get_account(self, account: int) -> Account:
        if not self.check_is_valid_account(account):
            return None
        return self.accounts[account - 1]


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
