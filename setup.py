from setuptools import setup, find_packages


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name="marshmallow-jsonapi-webargs",
    version="0.0.1",
    description="Schemas for JSON API request parameters",
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
    author="Michael Milton",
    author_email="michael.r.milton@gmail.com",
    url="https://github.com/TMiguelT/marshmallow-jsonapi-webargs",
    packages=find_packages(exclude=("test*",)),
    install_requires=[
        "marshmallow>=2.15.2",
        "webargs>=5.5.1",
        "querystring-parser>=1.2.4",
    ],
    extras_require={
        "tests": ["pytest"],
    },
    python_requires=">=3.5",
    license="LGPLv3",
    keywords=(
        "marshmallow-jsonapi marshmallow marshalling serialization "
        "jsonapi deserialization validation"
    ),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    test_suite="tests",
    project_urls={
        "Bug Reports": "https://github.com/TMiguelT/marshmallow-jsonapi-webargs/issues"
    },
)
