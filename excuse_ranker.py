def rank_excuse(excuse, urgency):
    score = 50
    if len(excuse.split()) > 12:
        score += 10
    if urgency.lower() == "high":
        score += 15
    if "unexpected" in excuse.lower():
        score += 10
    return min(score, 100)