import os
from dotenv import load_dotenv
from string import Template
from pathlib import Path

def absolute_path(filename):
    project_root = Path(__file__).resolve().parent.parent
    path_body = project_root / '.circleci' / filename
    return path_body


with open(f"{absolute_path('config_template.yml')}") as f:
    template = Template(f.read())

rendered = template.substitute(os.environ)

with open(f"{absolute_path('config.yml')}", "w") as f:
    f.write(rendered)