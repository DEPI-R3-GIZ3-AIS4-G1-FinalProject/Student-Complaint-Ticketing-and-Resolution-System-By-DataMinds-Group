import json
import requests

# Path to SLA policies file
POLICIES_FILE = "sla_policies.json"

# Load SLA policies
with open(POLICIES_FILE, "r") as f:
    policies = json.load(f)["policies"]

# Ollama endpoint (running locally in WSL)
OLLAMA_API = "http://localhost:11434/api/generate"
MODEL = "llama3-chatqa:8b"


def query_llm(prompt: str) -> str:
    """
    Send prompt to local Ollama model and return the response.
    """
    response = requests.post(
        OLLAMA_API,
        json={"model": MODEL, "prompt": prompt, "stream": False, "options": {"temperature": 0}}
    )
    if response.status_code == 200:
        return response.json().get("response", "").strip()
    else:
        return f"Error: LLM request failed ({response.status_code})"


def classify_issue(issue: str) -> dict:
    """
    Use LLM to match issue to SLA policy.
    Returns a dict with SLA details or 'Unknown'.
    """
    # Build the policy summary for LLM
    policy_summary = "\n".join(
        [f"- {p['category']}: {', '.join(p['examples'])}" for p in policies]
    )

    prompt = f"""
    A student reported the following issue:
    "{issue}"

    Here are the only valid categories:
    {policy_summary}

    If the issue clearly matches one of these categories, respond with EXACTLY the category name.

    If the issue is unrelated (for example: transportation, housing, cafeteria, library, or anything not listed), respond ONLY with:
    Unknown

    Never guess. Your answer must be either one of the category names above or "Unknown".
    """

    category = query_llm(prompt)

    # Force category to be valid
    valid_categories = [p["category"].lower() for p in policies] + ["unknown"]
    if category.lower().strip() not in valid_categories:
        category = "Unknown"

    # Exact match only
    for policy in policies:
        if policy["category"].lower() == category.lower().strip():
            return policy

    return {"category": "Unknown", "priority": "N/A", "response_time": "N/A", "resolution_time": "N/A"}


def main():
    print("🎓 Student SLA Assistant (Local LLM Demo)")
    print("Type 'exit' to quit.\n")

    while True:
        issue = input("Enter student issue: ")
        if issue.lower() in ["exit", "quit"]:
            print("Goodbye 👋")
            break

        policy = classify_issue(issue)

        print("\n📌 Matched Category:", policy["category"])
        print("⭐ Priority:", policy["priority"])
        print("⏱️ Response Time:", policy["response_time"])
        print("🛠️ Resolution Time:", policy["resolution_time"])
        print("-" * 50)


if __name__ == "__main__":
    main()
