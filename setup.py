from setuptools import setup, find_packages

setup(
    name="common-utils",
    version="0.1.0",
    description="A reusable Python package",
    author="kiennt9696",
    author_email="kiennt9696@gmail.com",
    url="https://github.com/kiennt9696/common-utils",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pyjwt==2.4.0",
        "PyYAML==6.0.2",
        "flask==3.1.0"
    ],
)