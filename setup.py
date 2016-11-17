from setuptools import setup


def readme():
    encoding = "utf-8"
    with open("README.rst", "rb") as readme_file:
        data = readme_file.read()
    return data.decode(encoding)


setup(
    name="unisearch_django",
    version="0.0.0",
    description="Django wrapper providing the Unisearch frontend",
    long_description=readme(),
    url="http://github.com/harts-boundless/unisearch_django",
    maintainer="Sasha Hart",
    maintainer_email="harts@boundlessgeo.com",
    license="",
    packages=[
        "unisearch_django"
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Framework :: Django",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
    ],
)
