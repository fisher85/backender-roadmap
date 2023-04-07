# Run app in docker container

## Prerequisites

* Docker: 20.10.7

## Usage
Run service in container, need to run this command in folder with Dockerfile
```bash
docker build --rm --tag app .
docker run -d -p 8080:80 --rm -it -v $(pwd):/app app
```

Build image for CI
```bash
docker build --platform linux/amd64 --rm --tag likesimba9/backender_roadmap:4.0 Dockerfile_for_backender_image
docker push likesimba9/backender_roadmap:4.0
```