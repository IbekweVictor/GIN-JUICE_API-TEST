# GinAndJuice API Test Suite

## 📌 Overview

This repository contains an **automated API test framework** for the [`ginandjuice.shop`](https://ginandjuice.shop) application.
It is built using **Pytest**, **Requests**, and **Allure**, following **modular best practices** suitable for CI/CD pipelines and maintainable long-term testing.

---

## ✅ Key Features

* **Class-based Test Organization** → Each module groups related test cases logically.
* **Modular Utilities** → Common configs, session management, and logging are reusable.
* **CSRF Handling** → Automatically extracts CSRF tokens for form submissions.
* **Checkout & Authentication Flow Tests** → Validates redirects (302/303) and login behavior.
* **Allure Integration** → Generates rich, interactive test reports (HTML-based).
* **Structured Logging** → Each test logs key steps, making debugging easier.
* **Scalable Design** → Easy to add new test files or extend to new endpoints.

---

## 📂 Project Structure

```
ginandjuice_api_tests/
├── tests/
│   ├── test_homepage.py          # Homepage tests
│   ├── test_login.py             # Authentication tests
│   ├── test_products.py          # Product listing/search tests
│   ├── test_cart_checkout.py     # Cart & checkout flow tests
│
├── utils/
│   ├── config.py                 # Stores BASE_URL and shared configs
│   ├── logger.py                 # Logger setup for all tests
│
├── conftest.py                   # Pytest fixtures (sessions, base_url)
├── pytest.ini                    # Pytest configuration (Allure, verbosity)
├── requirements.txt              # Dependencies
└── README.md                     # Documentation
```

---

## ⚙️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/ginandjuice-api-tests.git
   cd ginandjuice-api-tests
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Running Tests

To run all tests:

```bash
pytest
```

To run a specific test file:

```bash
pytest tests/test_cart_checkout.py
```

To run with detailed logs:

```bash
pytest -v -s
```

---

## 📊 Generating Allure Reports

1. Run tests with Allure enabled:

   ```bash
   pytest
   ```

2. Serve the Allure report:

   ```bash
   allure serve reports/allure-results
   ```

This will launch an interactive HTML report in your browser showing:

* Test history
* Execution timeline
* Step-by-step logs
* Attachments (if added later)

---

## 🔧 Configuration

* **Base URL** is defined in `utils/config.py`.
  Example:

  ```python
  BASE_URL = "https://ginandjuice.shop"
  ```
* **Logger** settings are defined in `utils/logger.py`.

---

## 🛠 Future Enhancements

* [ ] Add authentication token support.
* [ ] Parallel test execution (`pytest-xdist`).
* [ ] Dockerized test runner.
* [ ] CI/CD pipeline integration (GitHub Actions, GitLab CI, Jenkins).

---


