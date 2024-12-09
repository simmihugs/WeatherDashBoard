from setuptools import setup, find_packages

setup(
    name="WeatherDashBoard",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "reflex",
    ],
    author="Simon Graetz",
    author_email="simon.graetz@gmx.de",
    description="A little weather dashboard",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/simmihugs/WeatherDashBoard",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD2 License",
        "Operating System :: Ubuntu24.04",
    ],
)
