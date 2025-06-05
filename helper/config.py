import os
from dotenv import load_dotenv
from string import Template

load_dotenv()
env = os.getenv("ENVIRONMENT")

API_URL = os.getenv(f"{env}_API_URL")
TOKEN = os.getenv(f"{env}_TOKEN")
TEAM_ID = os.getenv(f"{env}_TEAM_ID")
FOLDER_ID = os.getenv(f"{env}_FOLDER_ID")

with open("config_template.yml") as f:
    template = Template(f.read())

rendered = template.substitute(os.environ)

with open("config.yml", "w") as f:
    f.write(rendered)

print("✅ config.yml generated successfully.")