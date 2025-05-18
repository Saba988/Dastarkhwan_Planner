import json
import os

DB_PATH = "data/db.json"

def initialize_db():
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(DB_PATH):
        with open(DB_PATH, "w") as f:
            json.dump({"users": [], "donations": []}, f)

def read_db():
    with open(DB_PATH, "r") as f:
        return json.load(f)

def write_db(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=4)

def get_user(username):
    db = read_db()
    for user in db["users"]:
        if user["username"] == username:
            return user
    return None

def add_user(username, role):
    db = read_db()
    db["users"].append({"username": username, "role": role})
    write_db(db)

def add_donation(donation_dict):
    db = read_db()
    db["donations"].append(donation_dict)
    write_db(db)

def get_all_donations():
    db = read_db()
    return db["donations"]