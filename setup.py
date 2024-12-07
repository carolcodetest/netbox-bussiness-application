from setuptools import find_packages, setup

setup(
    name="netbox-business-application",
    version="0.0.1",
    description="A NetBox plugin to manage business applications and their relationships to virtual machines.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/your-repo/netbox-business-application",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)