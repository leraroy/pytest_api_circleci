import os
from dotenv import load_dotenv
from string import Template
from pathlib import Path
from config import *

def absolute_path(filename):
    project_root = Path(__file__).resolve().parent.parent
    path_body = project_root / '.circleci' / filename
    return path_body

env = dict(os.environ)
env.setdefault("QA_API_URL", API_URL)
env.setdefault("QA_TOKEN", TOKEN)
env.setdefault("QA_TEAM_ID", TEAM_ID)

with open(f"{absolute_path('config_template.yml')}") as f:
    template = Template(f.read())
    rendered = template.substitute(env)


with open(f"{absolute_path('config.yml')}", "w") as f:
    f.write(rendered)