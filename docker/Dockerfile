# Dockerfile describing development builds of Detectree2
#
# Authors:
# Matt Archer <ma595@cam.ac.uk>

FROM ubuntu:20.04 as dev-env
LABEL maintainer="ma595 <ma595@cam.ac.uk>"
LABEL description="Detectree2 testing and development environment"

# Install GDAL headers:

RUN apt update -y && apt install -y software-properties-common

# Clone Detectree2 
RUN add-apt-repository -y ppa:ubuntugis/ppa && apt -y update && \
  apt install -y \
  libgdal-dev \
  gdal-bin \
  python3-pip \ 
  git \
  python3-opencv 

RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal && \
  export C_INCLUDE_PATH=/usr/include/gdal

RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

RUN pip3 install opencv-python wandb numpy sphinx 

RUN python3 -m pip install 'git+https://github.com/facebookresearch/detectron2.git'

RUN git clone https://github.com/ma595/detectree2.git && cd detectree2 && \
  git fetch -a && \
  git checkout -b documentation origin/documentation && \
  sphinx-apidoc -o ./docs/source/ detectree2/ && \
  sphinx-build -b html docs/source/ docs/build/html
