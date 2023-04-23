import os

from dotenv import load_dotenv
from pyrogram import Client
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "8934899"))
API_HASH = os.getenv("API_HASH", "bf3e98d2c351e4ad06946b4897374a1e")
SESSION = os.getenv("SESSION", "AQABDwOIUb-LJfIxRp6MZRaxyRwni3HpfCnVfMhH1yz2j9ZH01qLdZ28yEb6SJGuuvsZeA4W6LwQz-cC48iZuiCQezn8d28DUdIndATt7wSuTc2hNw1qlcX3WLZ2dr2L_HMY2zp0NSG6JPffr_H2iKEk81NoS1j6UVjmki-R4e_dX5Rfh5Xz368zWSIwgGLuNZiLO2zi4p5jECQtuTXpi--SmAEy-xwezYYmn71ml7VOogWxYNoz94FwNgeR1LCB59y8IB1wyTTu5R8XMEyiSJAKnEcotTraYYJOOxUzIrHSj9kVEHsGciuPkm7Ca4wR5YjKlkvQeRyJSBxgBhXp9_DfdXuJZwA")
HNDLR = os.getenv("HNDLR", "!")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "1854384004").split()))

# Cellmusic
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicAndVideo"))
call_py = PyTgCalls(bot)
