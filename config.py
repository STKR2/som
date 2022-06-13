import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars

load_dotenv()
admins = {}
API_ID = int(os.getenv("API_ID", "8186557"))
API_HASH = os.getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
SESSION = os.getenv("SESSION", "AQC2O__E3DkkDBmp07B54NV86MGNCUq4NPUXHaaoZ86eTjQ1mir8cGAre6EUrdPWZfuwaURlyQwHJ3nfvrQlhs4fUogeK9dlIzTPTbs0tBEv3KJo5B2hbV--OXWTche8H6LDbyv_3QAcLxUhIVKcdGPl2ecpBGrfx4fR_0UXmUIw7yM58WxyzPlzDVorHyvAEpqln4tlnL-6dGZdgVjuDXm5r77IXFd_ridOfp4f9WDnlcRpvnC_60W6WqlC_g8SbAs_XYrGEbaxX0j-iIfW-IOl4RfQLhn0cS-E6p_tvtrsSCyUTNgdAlt2klDah61P9jnAAO2QzkfrXBKHCuOtlUkhdXuJZwA")
HNDLR = os.getenv("HNDLR", "/")


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicAndVideo"))
call_py = PyTgCalls(bot)
