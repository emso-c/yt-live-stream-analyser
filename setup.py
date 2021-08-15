from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_desc = fh.read()

with open('requirements.txt') as f:
    requirements = [rq.replace("==", ">=") for rq in f.read().splitlines()]

setup(
    name="stream-analyser",
    version="v0.2.0",
    author="emso-c",
    author_email="emsoc192@gmail.com",
    description=("A tool that analyses live streams"),
    keywords=["youtube", "live", "stream", "chat", "highlight", "analyser"],
    url="https://github.com/emso-c/stream-analyser",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Environment :: Console",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    packages=find_packages("streamanalyser"),
    package_dir={"": "streamanalyser"},
    python_requires=">=3.9",
    include_package_data=True,
    install_requires=requirements,
)
