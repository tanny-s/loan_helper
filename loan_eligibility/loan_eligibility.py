from datetime import datetime

class LoanEligibility:
    def __init__(self):
        self.clients = {}

    def check_eligibility(self, client):
        eligible = client.annual_income >= 300000 and client.civil_score >= 700 and not client.previous_loan
        eligibility_message = "Client is eligible for the loan." if eligible else "Client is not eligible for the loan."
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        client.add_history(eligibility_message, timestamp)
        self.clients[client.name] = client
        return eligibility_message

    def get_history(self, name):
        client = self.clients.get(name)
        if not client:
            return None
        return client.history
