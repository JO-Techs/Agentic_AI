from github import Github
import jwt
import time

from config import GITHUB_APP_ID, GITHUB_PRIVATE_KEY

def generate_jwt():
    payload = {
        "iat": int(time.time()),
        "exp": int(time.time()) + (10 * 60),
        "iss": GITHUB_APP_ID
    }
    return jwt.encode(payload, GITHUB_PRIVATE_KEY, algorithm="RS256")

def get_github_client():
    token = generate_jwt()
    return Github(token)
