# auth/telegram_auth_setup.py
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()  # Assumes .env is in the project root or specify path

# Retrieve and validate Telegram API credentials
def fetch_api_credentials():
    """
    Fetches API credentials from environment variables and validates their presence.
    Returns a tuple of (api_id, api_hash) or raises an error if missing.
    """
    api_id_str = os.getenv("TELEGRAM_API_ID")
    api_hash = os.getenv("TELEGRAM_API_HASH")
    
    if not api_id_str or not api_hash:
        raise ValueError("Telegram API credentials (TELEGRAM_API_ID or TELEGRAM_API_HASH) are not set in .env file.")
    
    try:
        api_id = int(api_id_str)  # Ensure API_ID is an integer
        return api_id, api_hash
    except ValueError:
        raise ValueError("TELEGRAM_API_ID must be a valid integer.")

if __name__ == "__main__":
    try:
        api_id, api_hash = fetch_api_credentials()
        print("API credentials successfully loaded.")
    except ValueError as err:
        print(f"Error: {err}")