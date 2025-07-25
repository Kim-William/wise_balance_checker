# config.py

from dotenv import load_dotenv
import os

load_dotenv()

WISE_API_KEY = os.getenv("WISE_API_KEY")
WISE_PROFILE_ID = os.getenv("WISE_PROFILE_ID")
WISE_BALANCE_ID = os.getenv("WISE_BALANCE_ID")

WISE_API_BASE = "https://api.wise.com/v4"