class Bank:
    def __init__(self, balance: List[int]):
        # initialize balances
        self.balances = balance

    def is_account_valid(self, account: int):
        """
        Check if account number is valid.
        """
        # account number must be between 1 and n inclusive
        return account > 0 and account <= len(self.balances)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        """
        Transfer money between accounts.
        """
        # check if account numbers are valid
        if not self.is_account_valid(account1):
            return False

        if not self.is_account_valid(account2):
            return False

        # withdraw from account 1
        # if it fails, then there is not sufficient funds for the transfer
        if not self.withdraw(account1, money):
            return False

        # transfer the money to account 2
        return self.deposit(account2, money)

    def deposit(self, account: int, money: int) -> bool:
        """
        Deposit money to an account.
        """
        # check if account number is valid
        if not self.is_account_valid(account):
            return False

        # deposit money to account
        self.balances[account - 1] += money

        return True

    def withdraw(self, account: int, money: int) -> bool:
        """
        Withdraw money from an account.
        """
        # check if account number is valid
        if not self.is_account_valid(account):
            return False

        # check if account has sufficient balance
        if self.balances[account - 1] < money:
            return False

        # withdraw money from account
        self.balances[account - 1] -= money

        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
