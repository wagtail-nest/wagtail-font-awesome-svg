import os

from bs4 import BeautifulSoup, Comment

import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


for directory in [
    "brands",
    "regular",
    "solid",
]:
    for src_filename in glob.glob(f"fontawesome-free-6.5.2-web/svgs/{directory}/*.svg"):
        with open(src_filename, "r") as src_file:
            soup = BeautifulSoup(src_file.read(), "html.parser")
            tag = soup.find("svg")

            filename = os.path.basename(src_filename)
            id = filename[:-4]
            tag['id'] = f"icon-{id}"

            # Remove existing licensing comment.
            for comment in tag.find_all(string=lambda text: isinstance(text, Comment)):
                comment.extract()

            # Add back our shorter, human-readable comment.
            tag.insert(0, Comment(f" {id} ({directory}): Font Awesome Free 6.4.0 CC BY 4.0"))

            target_filename = os.path.join(
                BASE_DIR,
                "wagtailfontawesomesvg",
                "templates",
                "wagtailfontawesomesvg",
                directory,
                filename,
            )

            target_dir = os.path.dirname(target_filename)
            if not os.path.exists(target_dir):
                os.mkdir(target_dir)

            with open(target_filename, "w") as target_file:
                target_file.write(str(tag))
