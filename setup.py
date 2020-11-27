import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygisty",
    version="0.0.1",
    author="BlyatManGopnik",
    author_email="emailforsurveys420@gmail.com",
    description="Bad GitHub Gist client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BlyatManGopnik/pygisty",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'pygisty=pygisty:main.main'
        ],
    },
)