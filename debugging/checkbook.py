class Checkbook:
    """
    Classe représentant un carnet de chèques avec des opérations de dépôt, retrait et vérification du solde.

    Attributes:
        balance (float): Le solde courant du compte.
    """

    def __init__(self):
        """
        Initialise un nouveau carnet de chèques avec un solde de 0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Dépose une somme d'argent sur le compte.

        Parameters:
            amount (float): La somme à déposer.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Retire une somme d'argent du compte, si le solde est suffisant.

        Parameters:
            amount (float): La somme à retirer.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Affiche le solde courant du compte.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Fonction principale qui gère les opérations du carnet de chèques en fonction des entrées utilisateur.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
