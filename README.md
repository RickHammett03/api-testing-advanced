# API Testing Advanced Framework (Python)

## Description

This project is an advanced API testing framework built using Python, Pytest, and Requests.

It demonstrates best practices in API automation, including data-driven testing, schema validation, logging, and CI/CD integration.

---

## Features

- Automated API testing using Pytest
- Reusable HTTP client (Requests)
- Data-driven testing with external data
- JSON schema validation
- Logging of requests and responses
- HTML test reports
- CI/CD integration with GitHub Actions

---

## Project Structure
api-testing-advanced/
│
├── tests/ # Test cases
├── utils/ # API client, auth, logger
├── data/ # Test data
├── schemas/ # JSON schemas
├── conftest.py # Fixtures
├── requirements.txt # Dependencies

---

## Installation

```bash
git clone https://github.com/RickHammett03/api-testing-advanced.git
cd api-testing-advanced
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run Tests
pytest

## Generate Report
pytest --html=report.html --self-contained-html


