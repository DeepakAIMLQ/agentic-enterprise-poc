# backend/core/governance.py

FORBIDDEN_WORDS = ["ssn", "credit card", "password", "private key"]

def safety_check(text: str):
    text_lower = text.lower()
    violations = [w for w in FORBIDDEN_WORDS if w in text_lower]

    if violations:
        return {
            "approved": False,
            "reason": f"Sensitive data detected: {violations}"
        }

    if len(text) < 200:
        return {
            "approved": False,
            "reason": "Output too short — likely hallucinated"
        }

    return {"approved": True, "reason": "Passed"}
