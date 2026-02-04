from supabase import create_client
 
 
PROJECT_URL='https://xskmowjtfufmqdhhtrgk.supabase.co'
API_KEY='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inhza21vd2p0ZnVmbXFkaGh0cmdrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ4NTUxOTIsImV4cCI6MjA4MDQzMTE5Mn0.ugaIRMa5hwu7wTQbX9oi0Q-rrG0hokhQihqPHPqlWlY'
db = create_client(PROJECT_URL, API_KEY)
 
import os
import json
import hashlib
 
# Simple local user store (fallback) — stores users in data/users.json
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
 
def _ensure_store():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f)
 
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
 
def save_user(email: str, password: str) -> None:
    _ensure_store()
    with open(USERS_FILE, 'r', encoding='utf-8') as f:
        users = json.load(f)
    users[email] = hash_password(password)
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f)
 
def get_user_hash(email: str):
    _ensure_store()
    with open(USERS_FILE, 'r', encoding='utf-8') as f:
        users = json.load(f)
    return users.get(email)
 