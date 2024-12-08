from setuptools import find_packages, setup

setup(
    name="netbox-business-application",
    version="1.0.1",
    description="A NetBox plugin to manage business applications and their relationships to virtual machines.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ivan Mitruk",
    author_email="imitruk@gmail.com",
    url="https://github.com/Shock3udt/netbox-bussiness-application",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)