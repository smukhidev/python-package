import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shurjopay-pkg-tareq",  # Replace with your own username
    version="0.0.4",
    author="TAREQ ANAM",
    author_email="trex0069@gmail.com",
    description="shurjopay integration package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tareqanam/shurjopay",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
