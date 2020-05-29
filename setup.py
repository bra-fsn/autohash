import io
import re
import setuptools

with io.open("README.md", "rt", encoding="utf8") as f:
    long_description = f.read()

with io.open("autohash/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \'(.*?)\'", f.read()).group(1)

setuptools.setup(
    name="autohash",
    version=version,
    author="NAGY, Attila",
    author_email="nagy.attila@gmail.com",
    description="Hashes nonhashable / mutable objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bra-fsn/autohash",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
