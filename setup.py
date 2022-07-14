import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qapi",
    version="0.0.1",
    description="A simple wrapper for querying the private Quotient API",
    long_description=long_description,
    author="deadshot",
    long_description_content_type="text/markdown",
    url="https://github.com/quotientbot/qapi",
    packages=["qapi"],
)
