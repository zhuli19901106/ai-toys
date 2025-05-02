from setuptools import setup, find_packages

with open("requirements.txt", encoding="utf-8") as f:
    required = f.read().splitlines()

try:
    with open("README.md", encoding="utf-8") as f:
        long_description = f.read()
except Exception:
    long_description = ""

setup(
    name="talk-to-me",
    version="0.1.0",
    packages=find_packages(),
    install_requires=required,
    author="Zhu Li",
    author_email="zhuli19901106@gmail.com",
    description="A FastAPI web service with Swagger UI support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhuli19901106/ai-toys",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "talk-to-me=talk_to_me.cli:main",
        ],
    },
)
