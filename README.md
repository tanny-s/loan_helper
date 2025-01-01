# Loan Helper

## Project Description
Loan Helper is a Python-based application that helps users determine their loan eligibility based on the following criteria:
- **Annual Income**: Must be ₹300,000 or higher.
- **CIBIL Score**: Must be 700 or above.
- **Previous Loan Status**: Users must not have any previous loans.

The application provides:
- Loan eligibility checks.
- History of eligibility checks with timestamps.
- API-based interaction for programmatic access.

---

## Features
- Eligibility evaluation based on user inputs.
- History tracking for previous checks.
- API endpoints to integrate with other applications.

---

## Requirements
To run the Loan Helper application locally, ensure you have:
- Python 3.x installed on your system.
- Required libraries:
  - `json`: For JSON data parsing.
  - `http.server`: To host the HTTP server.
  - `datetime`: For handling timestamps.

Install required libraries using:
```bash
pip install json
```

---

## Setup and Running
### Steps to Run Locally
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-repository>/loan-helper.git
   ```

2. **Navigate to the Directory**:
   ```bash
   cd loan-helper
   ```

3. **Run the Server**:
   ```bash
   python loan_helper.py
   ```

4. The server will start running at `http://127.0.0.1:8080`.

---

## API Endpoints
### 1. Check Loan Eligibility
**Endpoint**: `POST /check_eligibility`

**Request Body (JSON)**:
```json
{
  "name": "John Doe",
  "annual_income": 500000,
  "cibil_score": 750,
  "previous_loan": "no"
}
```

**Response**:
- Eligible:
  ```json
  {
    "eligibility": "Client is eligible for the loan."
  }
  ```
- Not Eligible:
  ```json
  {
    "eligibility": "Client is not eligible for the loan."
  }
  ```

### 2. Retrieve Eligibility History
**Endpoint**: `GET /get_history/{name}`

**Response**:
- With history:
  ```json
  {
    "history": [
      {
        "annual_income": 500000,
        "cibil_score": 750,
        "previous_loan": "no",
        "eligibility": "Client is eligible for the loan.",
        "timestamp": "2024-12-31 12:34:56"
      }
    ]
  }
  ```
- No history:
  ```json
  {
    "error": "No history found for client."
  }
  ```

---

## Testing the Application
### Using Postman
#### Test Eligibility Check
- **URL**: `http://127.0.0.1:8080/check_eligibility`
- **Method**: POST
- **Headers**:
  ```json
  {
    "Content-Type": "application/json"
  }
  ```
- **Body**:
  ```json
  {
    "name": "John Doe",
    "annual_income": 500000,
    "cibil_score": 750,
    "previous_loan": "no"
  }
  ```

#### Test Loan History
- **URL**: `http://127.0.0.1:8080/get_history/John Doe`
- **Method**: GET

---

## Contribution
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact
For inquiries, contact the team:
- **Project Leader**: Tanmay Bhupendra Sonawane
- **Group Member 1**: Mayur Ramchandra Ranode
- **Group Member 2**: Prathmesh Ravindra Dhekane
- **Group Member 3**: Tanishka Amit Pansare

