import hashlib
from datetime import datetime

def hash_query(query):
    return hashlib.sha256(query.encode()).hexdigest()

def log_query(query):
    query_hash = hash_query(query)
    timestamp = datetime.now()

    print("Query:", query)
    print("Hash:", query_hash)
    print("Timestamp:", timestamp)

    # Future: push this hash to Algorand blockchain

if __name__ == "__main__":
    sample_query = "SELECT * FROM users WHERE id = 1;"
    log_query(sample_query)