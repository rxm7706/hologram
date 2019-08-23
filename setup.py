from setuptools import setup

requires = [
    "python-dateutil",
    "jsonschema",
    'dataclasses;python_version<"3.7"',
]

package_version = "0.0.2a1"


def read(f):
    return open(f, encoding="utf-8").read()


setup(
    name="hologram",
    description="JSON schema generation from dataclasses",
    long_description=read("README.md"),
    packages=["hologram"],
    package_data={"hologram": ["py.typed"]},
    version=package_version,
    author="Connor McArthur, Jacob Beck, Simon Knibbs",
    author_email="info@fishtowanalytics.com, simon.knibbs@gmail.com",
    url="https://github.com/fishtown-analytics/hologram",
    install_requires=requires,
    setup_requires=["pytest-runner", "setuptools_scm"],
    tests_require=["pytest", "flake8", "mypy"],
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
    ],
)
