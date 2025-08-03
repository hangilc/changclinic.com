from jinja2 import Environment, FileSystemLoader
import glob
import frontmatter
import os

env = Environment(loader=FileSystemLoader('templates'))
site = env.get_template('site.html')

page_files = glob.glob("templates/pages/*.html")
for page_file in page_files:
    page_content = frontmatter.load(page_file)
    page = site.render(title=page_content["title"], content=page_content)
    page_name = os.path.basename(page_file)
    with open(f"dist/{page_name}", "w", encoding="utf-8") as f:
        f.write(page)
# output = index.render()
# with open("dist/index.html", "w", encoding="utf-8") as f:
#     f.write(output)
