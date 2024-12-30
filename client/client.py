class Client:
    def __init__(self, name, annual_income, civil_score, previous_loan):
        self.name = name
        self.annual_income = annual_income
        self.civil_score = civil_score
        self.previous_loan = previous_loan
        self.history = []

    def add_history(self, eligibility, timestamp):
        self.history.append({
            "annual_income": self.annual_income,
            "civil_score": self.civil_score,
            "previous_loan": self.previous_loan,
            "eligibility": eligibility,
            "timestamp": timestamp
        })
