"""Setup script for the markdown to PDF converter package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="md-to-pdf-converter",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A professional markdown to PDF converter with customizable themes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/md-to-pdf-converter",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Office/Business :: Office Suites",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=[
        "markdown2>=2.4.0",
        "weasyprint>=52.5",
        "Pillow>=8.0.0",
        "click>=8.0.0",
        "colorama>=0.4.4",
    ],
    entry_points={
        "console_scripts": [
            "md2pdf=cli.main:cli",
        ],
    },
    include_package_data=True,
    keywords="markdown, pdf, converter, document, report, theme",
)