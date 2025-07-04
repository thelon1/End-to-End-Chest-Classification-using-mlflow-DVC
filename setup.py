import setuptools

with open('README.MD', 'r', encoding= 'utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-to-End-Chest-Classification-using-mlflow-DVC"
AUTHOR_USERNAME = "rohit"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "rohitwamanr19@gmail.com"

setuptools.setup(

    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USERNAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for Chest X-ray Classification",
    long_description = long_description,
    url = f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src")
)

