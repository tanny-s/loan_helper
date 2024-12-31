import json
from http.server import BaseHTTPRequestHandler, HTTPServer
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

checker = LoanEligibilityChecker()

class LoanAPIHandler(BaseHTTPRequestHandler):
    def _send_response(self, status, data):
        """Helper function to send HTTP responses."""
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        """Handle POST requests."""
        if self.path == "/check_eligibility":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data)
                name = data.get('name')
                annual_income = data.get('annual_income')
                cibil_score = data.get('cibil_score')
                previous_loan = data.get('previous_loan')

                if not all([name, annual_income, cibil_score, previous_loan]):
                    self._send_response(400, {"error": "Missing required fields"})
                    return

                # Determine eligibility
                eligibility = checker.check_eligibility(
                    name, float(annual_income), int(cibil_score), previous_loan.lower() == "yes"
                )
                self._send_response(200, {"eligibility": eligibility})
            except Exception as e:
                self._send_response(500, {"error": f"Internal Server Error: {str(e)}"})
        else:
            self._send_response(404, {"error": "Endpoint not found"})

    def do_GET(self):
        """Handle GET requests."""
        if self.path.startswith("/get_history"):
            name = self.path.split("/")[-1]
            history = checker.get_history(name)

            if not history:
                self._send_response(404, {"error": "No history found for client"})
                return

            self._send_response(200, {"history": history})
        else:
            self._send_response(404, {"error": "Endpoint not found"})

def run_server():
    """Run the HTTP server."""
    server_address = ("", 8080)  # Run on localhost and port 8080
    httpd = HTTPServer(server_address, LoanAPIHandler)
    print("Server running on http://127.0.0.1:8080")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
