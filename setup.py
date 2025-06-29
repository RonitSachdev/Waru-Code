from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="waru-code-roast",
    version="1.0.0",
    author="WaruCodeRoast",
    description="A brutally honest CLI tool that roasts your code reviews using GPT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RonitSachdev/Waru-Code",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "waru-roast=waru_roast:cli",
        ],
    },
    keywords="code-review, cli, gpt, openai, humor, development",
    project_urls={
        "Bug Reports": "https://github.com/RonitSachdev/Waru-Code/issues",
        "Source": "https://github.com/RonitSachdev/Waru-Code",
    },
) 