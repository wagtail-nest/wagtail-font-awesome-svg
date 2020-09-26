import os

from bs4 import BeautifulSoup

import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


for directory in [
    "brands",
    "regular",
    "solid",
]:
    for src_filename in glob.glob(f"fontawesome-free-5.14.0-web/svgs/{directory}/*.svg"):
        with open(src_filename, "r") as src_file:
            soup = BeautifulSoup(src_file.read(), "html.parser")
            tag = soup.find("svg")
            tag.name = "symbol"
            del tag['xmlns']

            filename = os.path.basename(src_filename)
            tag['id'] = f"icon-{filename[:-4]}"

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
