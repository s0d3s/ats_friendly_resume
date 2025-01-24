import os
from setuptools import setup, find_packages

import src.constants as const


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

with (
    open(os.path.join(CURRENT_DIR, "README.md"), encoding="UTF-8") as readme,
    open(os.path.join(CURRENT_DIR, "requirements.txt"), encoding="UTF-8") as requirements
):
    setup(
        name=const.package,
        version=const.version,
        author=const.author,
        description=const.description,
        long_description=readme.read(),
        long_description_content_type="text/markdown",
        url=const.repo_url,
        packages=find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3.9",
        include_package_data=True,
        install_requires=requirements.read().splitlines(),
        entry_points={
            "console_scripts": [
                "ats_friendly_resume=src.main:main",  # Указываем консольную команду
            ],
        },
    )
