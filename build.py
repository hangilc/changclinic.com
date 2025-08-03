from jinja2 import Environment, FileSystemLoader
import glob
import frontmatter
import os

env = Environment(loader=FileSystemLoader('templates'))
site = env.get_template('site.html')

page_files = glob.glob("templates/pages/*.html")
for page_file in page_files:
    page_content = frontmatter.load(page_file)
    home = "./" if page_content["title"] == "index" else "../"
    page = site.render(
        title=page_content["title"], 
        home=home,
        content=page_content
        )
    page_name = os.path.basename(page_file)
    with open(f"docs/{page_name}", "w", encoding="utf-8") as f:
        f.write(page)
