# Fintwin – Cash-Flow Digital Twin

Fintwin is an AI-powered financial planning platform designed for micro and small enterprises. It creates a **Cash-Flow Digital Twin** using consented invoices, receivables, recurring expenses, and payment history.

The platform helps businesses understand their current financial position, forecast future liquidity, identify payment and concentration risks, simulate financial shocks, and compare suitable financing options.

> **Important:** Fintwin provides transparent financial insights and recommendations. It does **not** make automatic lending or credit decisions.

---

## 🚀 Key Features

* 📊 **Cash-Flow Digital Twin**

  * Centralized view of business cash inflows and outflows
  * Tracks invoices, receivables, expenses, and payments

* 🔮 **Cash-Flow Forecasting**

  * Predict future cash position
  * Identify potential liquidity gaps
  * Estimate upcoming inflows and expenses

* ⚠️ **Risk Detection**

  * Delayed-payment risk
  * Customer concentration risk
  * Cash-flow shortage alerts

* 🧪 **What-If Simulation**

  * Simulate delayed customer payments
  * Test expense increases
  * Model revenue drops and other financial shocks

* 💰 **Financing Comparison**

  * Compare non-debt options
  * Invoice-financing options
  * Working-capital options
  * Display costs and implications clearly

* 🤖 **AI-Assisted Insights**

  * Explain financial patterns
  * Generate understandable recommendations
  * Support decision-making without making lending decisions

* ✏️ **User Data Correction**

  * Users can review imported data
  * Correct inaccurate information
  * Maintain transparency and control

---

## 🏗️ Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap / Custom CSS
* Chart.js

### Backend

* Python
* Django
* Django REST Framework

### Database

* PostgreSQL
* SQLite for local development

### AI / Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Machine Learning forecasting models
* AI API integration where required

### Development Tools

* Git
* GitHub
* VS Code
* Postman

---

## 📁 Project Structure

```text
Fintwin/
│
├── backend/
│   │
│   ├── manage.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── accounts/
│   ├── dashboard/
│   ├── transactions/
│   ├── forecasting/
│   ├── risk/
│   ├── financing/
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   │
│   ├── index.html
│   ├── dashboard.html
│   │
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       ├── api.js
│       ├── dashboard.js
│       ├── charts.js
│       └── auth.js
│
├── .gitignore
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/faizkhan013/Fintwin.git
```

Move into the project:

```bash
cd Fintwin
```

---

## 2. Open the Backend

```bash
cd backend
```

---

## 3. Create a Virtual Environment

### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not exist yet:

```bash
pip install django djangorestframework django-cors-headers pandas numpy scikit-learn
```

Then:

```bash
pip freeze > requirements.txt
```

---

# 🗄️ Database Setup

For local development, Fintwin can use SQLite.

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your administrator account.

---

# ▶️ Running the Backend

From the `backend` directory:

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

---

# 🌐 Running the Frontend

The frontend is located inside:

```text
frontend/
```

You can use VS Code Live Server during development or serve the frontend through Django depending on the deployment architecture.

The JavaScript frontend communicates with Django through REST APIs.

Example:

```text
Frontend
   ↓
JavaScript Fetch / API Client
   ↓
Django REST Framework
   ↓
Business Logic
   ↓
Database / AI Models
```

---

# 🔌 API Architecture

The backend exposes REST APIs for different modules.

Example endpoints:

```text
/api/auth/
/api/business/
/api/invoices/
/api/expenses/
/api/payments/
/api/cashflow/
/api/forecast/
/api/risk/
/api/financing/
/api/scenarios/
```

Example:

```http
GET /api/cashflow/
```

```http
POST /api/invoices/
```

```http
GET /api/forecast/
```

```http
POST /api/scenarios/
```

---

# 🤖 AI & Forecasting

Fintwin uses historical financial information to create a digital representation of the business's cash-flow position.

Example input:

```text
Invoices
Receivables
Expenses
Payments
Payment History
Recurring Expenses
```

The forecasting system processes this information and estimates:

```text
Expected Cash Inflow
Expected Cash Outflow
Future Cash Balance
Liquidity Gaps
Payment Delays
Risk Indicators
```

The AI layer is designed to provide **explainable insights** rather than opaque financial decisions.

---

# 🧪 What-If Scenarios

Users can simulate different financial situations.

Example:

```text
Scenario:
30% of receivables are delayed by 30 days
```

Fintwin calculates the potential effect on:

```text
Cash Balance
Liquidity
Upcoming Expenses
Cash Shortage
Risk Level
```

Other possible scenarios include:

* Revenue decrease
* Expense increase
* Customer payment delay
* Major unexpected expense
* Loss of a major customer

---

# 🔐 Security & Privacy

Fintwin is designed around user consent and transparency.

Key principles:

* User-controlled financial data
* Authentication and authorization
* Secure API communication
* Environment variables for secrets
* No hardcoded API keys
* User ability to correct imported data
* Explainable recommendations
* No automatic lending decisions

Sensitive configuration should be stored in `.env`.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=your-database-url
AI_API_KEY=your-api-key
```

Never commit `.env` to GitHub.

---


# 🧑‍💻 Development Workflow

```text
Issue / Feature
      ↓
Create Git Branch
      ↓
Develop
      ↓
Test
      ↓
Commit
      ↓
Push Branch
      ↓
Pull Request
      ↓
Code Review
      ↓
Merge into Main
```

---

# 🧪 Testing

Run Django tests using:

```bash
python manage.py test
```

API testing can be performed using Postman or similar API testing tools.

Before creating a Pull Request, verify:

* Authentication works
* APIs return correct responses
* Database migrations work
* Forecasting produces valid results
* Scenario simulations work
* Frontend API integration works
* No API keys or `.env` files are committed

---

# 📌 Project Goals

Fintwin aims to help small businesses:

1. Understand their cash position
2. Predict upcoming liquidity problems
3. Identify financial risks early
4. Test possible financial shocks
5. Compare financing alternatives
6. Make better financial decisions
7. Maintain control over their own financial data

---

# 🌱 Social Impact

Small and micro businesses often struggle with unpredictable cash flows, delayed customer payments, and limited access to financial planning tools.

Fintwin aims to provide an accessible and transparent financial planning system that helps businesses make informed decisions and improve financial resilience.

The platform supports the broader vision of **Atmanirbhar Bharat** by helping small businesses become more financially informed, resilient, and self-reliant.

---

# 📄 License

This project is developed for educational, innovation, and hackathon purposes.

---

## 👨‍💻 Contributors

**Fintwin Development Team**

GitHub:

```text
https://github.com/faizkhan013/Fintwin
```
