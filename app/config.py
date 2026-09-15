import tomllib 
from pathlib import Path
 
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config.toml"
 
 

def get_user_settings(): 
    with open(CONFIG_PATH, "rb") as file:
        data = tomllib.load(file) 
    return data 
