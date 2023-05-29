from jinja2 import Environment, FileSystemLoader
from engine import Path, eel
from pathlib import Path


root = Path(__file__).parent
templates_dir = Path(root, 'desktop_ui')
env = Environment(loader=FileSystemLoader(templates_dir))
template = env.get_template('base.jinja')

# Save the compiled html to a file
filename = Path(root, 'desktop_ui', 'index.html')
with open(filename, 'w') as fh:
    fh.write(template.render())


eel.start("index.html", mode="chrome", jinja_templates='/')
