from setuptools import setup, find_packages


install_requires = []
dev_requires = ["black", "flake8"]
tests_requires = []

setup(
    classifiers=[
        # "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
    ],
    python_requires=">3.5",
    packages=find_packages(exclude=["ioknife.tests"]),
    install_requires=install_requires,
    extras_require={"testing": tests_requires, "dev": dev_requires},
    tests_require=tests_requires,
    test_suite="ioknife.tests",
    entry_points="""
      [console_scripts]
      ioknife = ioknife.cli:main
""",
)
