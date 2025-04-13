def score_loan_application(app):
    '''
    Rule-based scoring system
    Input: app (dict) with keys: income, loan_amount, term_months, credit_score, collateral_value, employment_status
    Output: dict with score, tier, and decision
    '''

    score = 0
    app["income"] = float(app["income"])
    app["loan_amount"] = float(app["loan_amount"])
    app["term_months"] = int(app["term_months"])
    app["credit_score"] = int(app["credit_score"])
    app["collateral_value"] = float(app["collateral_value"])

    # Rule 1: Credit score
    if app["credit_score"] >= 750:
        score += 30
    elif app["credit_score"] >= 700:
        score += 20
    elif app["credit_score"] >= 650:
        score += 10

    # Rule 2: Income vs monthly repayment
    monthly_payment = app["loan_amount"] / app["term_months"]
    if app["income"] >= monthly_payment * 3:
        score += 25
    elif app["income"] >= monthly_payment * 2:
        score += 15

    # Rule 3: Collateral coverage
    if app["collateral_value"] >= app["loan_amount"]:
        score += 30
    elif app["collateral_value"] >= app["loan_amount"] * 0.5:
        score += 15

    # Rule 4: Employment status
    if app["employment_status"].lower() == "full-time":
        score += 10
    elif app["employment_status"].lower() == "part-time":
        score += 5

    # Determine decision
    if score >= 75:
        tier = "Tier 1"
        decision = "Approved"
    elif score >= 50:
        tier = "Tier 2"
        decision = "Needs Review"
    else:
        tier = "Tier 3"
        decision = "Rejected"

    return {
        "score": score,
        "tier": tier,
        "decision": decision
    }