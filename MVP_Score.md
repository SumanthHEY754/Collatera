
# 📄 MVP Scope – Collatera

This document outlines the minimum viable product (MVP) feature set, logic, and flow for Collatera's initial prototype build.

---

## 🧠 AI Credit Scoring (Rule-Based + ML-Ready)

### 📌 Objective:
Create an initial credit scoring mechanism that classifies borrowers based on their risk, using business rules. This system should be structured in a way that it can be easily upgraded to include a machine learning model.

### ✅ What to Include:
- Rule-Based Logic Example:
  - If income > 3x monthly loan repayment → good
  - If existing debts < 40% of income → good
  - If collateral ≥ 30% of loan amount → great
  - If credit score (mock) ≥ 700 → preferred borrower
- Output: Risk Tier → Low, Medium, High
- Score Range: 300–850 scale (simulated)
- Use mock data (CSV/JSON) to simulate behavior

### 🛠 Future ML Integration:
- Placeholder pipeline to plug in a scikit-learn model
- Create sample features: income, assets, age, credit history, etc.
- Train/test on synthetic 100k-record dataset

---

## 📝 Loan Application UI

### 📌 Objective:
Design a simple, intuitive form where users apply for a loan by entering basic details and choosing collateral.

### ✅ Fields to Capture:
- Name, Email, Phone
- Employment status
- Income (monthly or yearly)
- Loan amount & purpose
- Loan term (in months)
- Collateral selection (multi-select)
- Optional: Upload income proof (mock)

### 🎯 Goals:
- Minimum input to start the application
- Clear CTA: “Submit Application”
- Display outcome on next screen: “Approved / Needs Review / Rejected”

---

## 💰 Collateral Options

### 📌 Objective:
Support different types of collateral from day 1 using mock input fields.

### ✅ Collateral Types:
- Stocks: Ticker, number of shares, estimated value
- Mutual Funds: Fund name, estimated value
- Crypto: Token (e.g., BTC, ETH), amount, estimated USD value
- Savings: Input amount held in account

### 🧠 Backend Logic (Mocked):
- Store each type of asset linked to the user
- Compute collateral coverage percentage
- Use it to drive loan tier eligibility

---

## 🎯 Tiered Loan Structure

### 📌 Objective:
Use the collateral and credit score to categorize borrowers into risk tiers that determine their loan terms.

### ✅ Suggested Structure:

| Tier   | Criteria                          | Loan Type | Interest | Max Loan Amount     |
|--------|-----------------------------------|-----------|----------|----------------------|
| Tier 1 | High credit + solid collateral    | Secured   | 4–5%     | 80% of collateral    |
| Tier 2 | Decent credit + some collateral   | Secured   | 6–9%     | 60% of collateral    |
| Tier 3 | No/low collateral, low credit     | Unsecured | 10–15%   | ≤ $5K                |

These are flexible and should be documented in a config file or JSON.

---

## 🛠 Admin Dashboard (Internal Tool)

### 📌 Objective:
Provide an internal interface to view, approve, reject, or flag loan applications.

### ✅ Features:
- Login screen (admin only access)
- View all applications
- Filters: by loan type, amount, status, credit tier
- Manual action: Approve, Reject, Request Docs (no real action for MVP)
- Stats: Number of applications, approval rate, average score

---

## 🧪 Test Data Only – No Live APIs or Payments

### 📌 Objective:
Keep development lightweight and fast by avoiding third-party integrations.

### ✅ Mock Elements:
- Use static files for:
  - Stock prices
  - Crypto rates
  - User data
- Loan approval logic is all offline
- No Plaid, Stripe, or crypto wallets at this stage

---

## 📄 Deliverable: MVP_Scope.md

Include:
- Final list of MVP features (as above)
- Diagram of user flow (apply → score → admin review)
- Summary of rule-based logic for scoring and tiering
- Sample JSON structure of a loan application and a collateral entry
- Mention of future ML and API plans

---

## 📂 Suggested Folder Structure

```bash
collatera/
├── backend/
│   ├── api/
│   ├── models/
│   ├── credit_scoring/
│   └── mock_data/
├── frontend/
│   ├── components/
│   └── pages/
├── docs/
│   └── MVP_Scope.md
├── README.md
```
