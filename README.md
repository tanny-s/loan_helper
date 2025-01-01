# Loan Helper 💸

![Python](https://img.shields.io/badge/Python-3.12.3-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

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

## Features ✨
- **Eligibility Evaluation**: Quick loan eligibility checks.
- **History Tracking**: Keeps records of all eligibility checks.
- **API Endpoints**: Seamless integration into other applications.

---

## Requirements 🛠️
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

## Setup and Running 🏃‍♂️
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

4. Open your browser and navigate to `http://127.0.0.1:8080`.

---

## API Endpoints 🌐
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

## Testing the Application 🧪
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

## Contribution 🤝
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

---

## License 📜
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact 📧
For inquiries, contact the team:
- **Tanmay Bhupendra Sonawane**: [tanmaysonawane007@gmail.com](mailto:tanmaysonawane007@gmail.com)
- **Mayur Ramchandra Ranode**: [mayurranode7@gmail.com](mailto:mayurranode7@gmail.com)
- **Prathmesh Ravindra Dhekane**: [prathmesh2003dhekane@gmail.com](mailto:prathmesh2003dhekane@gmail.com)
- **Tanishka Amit Pansare**: [tanishkapansare5555@gmail.com](mailto:tanishkapansare5555@gmail.com)

