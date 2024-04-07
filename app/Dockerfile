# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.10-slim 
# AS builder

WORKDIR /app

# Install OpenGL libraries
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libx11-6 \
    libxext6 \
    mesa-utils \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    freeglut3-dev \
    libnss3 \
    libgconf-2-4

COPY requirements.txt /app

# RUN --mount=type=cache,target=/root/.cache/pip \
#   pip3 install -r requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]
CMD ["app.py"]
