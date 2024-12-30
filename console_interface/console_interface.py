import requests

class ConsoleInterface:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_client_details(self):
        print("Enter Client Details for Loan Eligibility Check:")
        name = input("Name: ").strip()
        annual_income = float(input("Annual Income: "))
        civil_score = int(input("Civil Score (300-900): "))
        previous_loan = input("Has Previous Loan (yes/no): ").strip().lower()

        if previous_loan not in ["yes", "no"]:
            print("Invalid input for previous loan. Please enter 'yes' or 'no'.")
            return None
        
        return {
            "name": name,
            "annual_income": annual_income,
            "civil_score": civil_score,
            "previous_loan": previous_loan == "yes"
        }

    def check_loan_eligibility(self, client_details):
        try:
            response = requests.post(f"{self.api_url}/check_eligibility", json=client_details)
            if response.status_code == 200:
                print("\nLoan Eligibility Result:")
                print(response.json().get("message"))
            else:
                print("Error:", response.text)
        except Exception as e:
            print("Failed to connect to the API:", str(e))

    def view_client_history(self):
        name = input("Enter Client Name to View History: ").strip()
        try:
            response = requests.get(f"{self.api_url}/history/{name}")
            if response.status_code == 200:
                history = response.json()
                print(f"\nHistory for {name}:")
                for record in history:
                    print(
                        f"Date: {record['timestamp']}, Annual Income: {record['annual_income']}, "
                        f"Civil Score: {record['civil_score']}, Previous Loan: {record['previous_loan']}, "
                        f"Eligibility: {record['eligibility']}"
                    )
            else:
                print("Error:", response.json().get("message"))
        except Exception as e:
            print("Failed to connect to the API:", str(e))

    def run(self):
        while True:
            print("\n--- Loan Eligibility Checker ---")
            print("1. Check Loan Eligibility")
            print("2. View Client History")
            print("3. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                client_details = self.get_client_details()
                if client_details:
                    self.check_loan_eligibility(client_details)
            elif choice == "2":
                self.view_client_history()
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
