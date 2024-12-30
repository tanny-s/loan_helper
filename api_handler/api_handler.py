from flask import Flask, request, jsonify
from client import Client
from loan_eligibility import LoanEligibility

app = Flask(__name__)
loan_eligibility = LoanEligibility()

@app.route("/check_eligibility", methods=["POST"])
def check_eligibility():
    data = request.json

    try:
        name = data["name"]
        annual_income = data["annual_income"]
        civil_score = data["civil_score"]
        previous_loan = data["previous_loan"]

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Invalid name.")
        if not isinstance(annual_income, (int, float)) or annual_income < 0:
            raise ValueError("Invalid annual income.")
        if not isinstance(civil_score, int) or not (300 <= civil_score <= 900):
            raise ValueError("Invalid civil score.")
        if not isinstance(previous_loan, bool):
            raise ValueError("Invalid previous loan value.")
    except (KeyError, ValueError) as e:
        return jsonify({"message": "Invalid input: " + str(e)}), 400

    client = Client(name, annual_income, civil_score, previous_loan)
    eligibility_message = loan_eligibility.check_eligibility(client)
    return jsonify({"message": eligibility_message}), 200

@app.route("/history/<name>", methods=["GET"])
def get_history(name):
    history = loan_eligibility.get_history(name)
    if not history:
        return jsonify({"message": f"No history found for client: {name}"}), 404
    return jsonify(history), 200

if __name__ == "__main__":
    app.run(debug=True)
