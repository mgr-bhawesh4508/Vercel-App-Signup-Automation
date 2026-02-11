import requests
import time
import re

BASE_URL = "https://api.mail.tm"
OTP_REGEX = r"\b\d{4,6}\b"   # supports 4-6 digit OTP

# Create Temporary Email
def create_temp_email():
    # Get available domains
    domain_response = requests.get(f"{BASE_URL}/domains").json()
    domain = domain_response["hydra:member"][0]["domain"]

    # Generate random email
    email = f"user{int(time.time())}@{domain}"
    password = "Test@12345"

    # Create account
    requests.post(f"{BASE_URL}/accounts", json={
        "address": email,
        "password": password
    })

    return email, password

# Get Auth Token
def get_token(email, password):
    response = requests.post(f"{BASE_URL}/token", json={
        "address": email,
        "password": password
    })

    return response.json()["token"]

# Read OTP From Email
def get_otp(token, timeout=90):
    headers = {"Authorization": f"Bearer {token}"}
    start_time = time.time()

    while time.time() - start_time < timeout:
        messages = requests.get(f"{BASE_URL}/messages", headers=headers).json()

        if messages["hydra:member"]:
            message_id = messages["hydra:member"][0]["id"]

            message = requests.get(
                f"{BASE_URL}/messages/{message_id}",
                headers=headers
            ).json()

            body = message.get("text", "")

            match = re.search(OTP_REGEX, body)
            if match:
                return match.group()

        time.sleep(5)

    raise Exception("OTP not received within timeout")

