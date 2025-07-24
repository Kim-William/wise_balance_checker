# config.py

from dotenv import load_dotenv
import os

load_dotenv()

WISE_API_KEY = 'caffa7c9-1bdd-4912-a235-e93cb68da804' # os.getenv("WISE_API_KEY")
WISE_PROFILE_ID = '40364566' # os.getenv("WISE_PROFILE_ID")
WISE_BALANCE_ID = '59136018' # os.getenv("WISE_BALANCE_ID")

WISE_API_BASE = "https://api.wise.com/v4"