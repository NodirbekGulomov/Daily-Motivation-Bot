import os

import dotenv

dotenv.load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
__admin_id = os.getenv("ADMIN_ID")

if __admin_id:
    ADMIN_ID = int(__admin_id)
