import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spw",
    version="0.0.1",
    author="ileler",
    author_email="kerwin612@qq.com",
    description="A wrap for sshpass",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ileler/spw",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    scripts=['src/spw'],
)
