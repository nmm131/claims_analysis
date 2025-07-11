import json
from typing import List, Dict, Any

def load_claims(filepath: str) -> List[Dict[str, Any]]:
    try:
        with open(filepath, "r") as file:
            claims = json.load(file)
            return claims
    except FileNotFoundError:
        print(f"Error: '{filepath}' file not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{filepath}'.")
    return []

def summarize_status(claims: List[Dict]) -> Dict[str, int]:
    counts = {}
    for claim in claims:
        status = claim.get('status')
        if status in counts:
            counts[status] += 1
        else:
            counts[status] = 1
    return counts

def map_users_to_claims(claims: List[Dict]) -> Dict[str, List[str]]:
    users = {}
    for claim in claims:
        user_id = claim.get('user_id')
        claim_id = claim.get('claim_id')
        if user_id not in users:
            users[user_id] = []
        users[user_id].append(claim_id)
    return users


def get_all_actions_sorted(claims: List[Dict]):
    actions = []
    for claim in claims:
        claim_actions = claim.get('actions', [])
        actions.extend(claim_actions)
    sorted_actions = sorted(actions, key=lambda x: x['timestamp'])
    return sorted_actions

def main():
    filepath = "claims.json"
    claims = load_claims(filepath)

    if not claims:
        print("No valid claims data to process.")
        return
    
    counts = summarize_status(claims)
    print(f"Counts: {counts}")

    users = map_users_to_claims(claims)
    print(f"Users: {users}")

    actions = get_all_actions_sorted(claims)
    print(f"Actions: {actions}")

if __name__ == "__main__":
    main()