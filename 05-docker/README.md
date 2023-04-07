# Run app in docker container

## Prerequisites

* Docker: 20.10.7

## Usage

```bash
docker build --rm --tag app .
docker run -d -p 8080:80 --rm -it -v $(pwd):/app app
```
