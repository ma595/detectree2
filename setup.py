from setuptools import find_packages, setup

setup(
    name="detectree2",
    version="0.0.1",
    author="James G. C. Ball",
    author_email="ball.jgc@gmail.com.com",
    description="Detectree packaging",
    url="https://github.com/PatBall1/detectree2",
    package_dir={"": "src"},
    packages=find_packages(),
    test_suite="src.tests.test_all.suite",
    install_requires=[
        "pyyaml==5.1",
        "GDAL>=1.11",
        "proj",
        "geos",
        "pygeos",
        "geopandas",
        "rasterio==1.2.10",
        "fiona",
        "pycrs",
        "descartes",
        "detectron2@git+https://github.com/facebookresearch/detectron2.git",
    ],
)
