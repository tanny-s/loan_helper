from datetime import datetime

class Client:
    def __init__(self, name, annual_income, cibil_score, previous_loan):
        self.name = name
        self.annual_income = annual_income
        self.cibil_score = cibil_score
        self.previous_loan = previous_loan
        self.history = []

    def add_history(self, eligibility, timestamp):
        self.history.append({
            "annual_income": self.annual_income,
            "cibil_score": self.cibil_score,
            "previous_loan": self.previous_loan,
            "eligibility": eligibility,
            "timestamp": timestamp
        })

class LoanEligibilityChecker:
    def __init__(self):
        self.clients = {}

    def check_eligibility(self, name, annual_income, cibil_score, previous_loan):
        if name in self.clients:
            client = self.clients[name]
        else:
            client = Client(name, annual_income, cibil_score, previous_loan)
            self.clients[name] = client

        eligible = annual_income >= 300000 and cibil_score >= 700 and not previous_loan
        message = "Client is eligible for the loan." if eligible else "Client is not eligible for the loan."

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        client.add_history(message, timestamp)
        return message

    def get_history(self, name):
        if name not in self.clients:
            return None
        return self.clients[name].history

def display_menu():
    print("\nLoan Eligibility Checker")
    print("1. Check Loan Eligibility")
    print("2. View Client History")
    print("3. Exit")

if __name__ == "__main__":
    checker = LoanEligibilityChecker()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter client's name: ")
            annual_income = float(input("Enter annual income: "))
            cibil_score = int(input("Enter CIBIL score: "))
            previous_loan = input("Does the client have a previous loan? (yes/no): ").strip().lower() == "yes"

            result = checker.check_eligibility(name, annual_income, cibil_score, previous_loan)
            print(f"\n{name}: {result}")

        elif choice == "2":
            name = input("Enter client's name to view history: ")
            history = checker.get_history(name)

            if history is None:
                print(f"\nNo history found for client: {name}")
            else:
                print(f"\nHistory for {name}:")
                for record in history:
                    print(f"- On {record['timestamp']}, Annual Income: {record['annual_income']}, "
                          f"CIBIL Score: {record['cibil_score']}, Previous Loan: {record['previous_loan']}, "
                          f"Eligibility: {record['eligibility']}")

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
