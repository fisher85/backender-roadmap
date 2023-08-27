```bash
docker volume create secret_data
docker run -it --workdir="/data" -v secret_data:/data --name first_cont ubuntu:22.04
docker run -it --workdir="/data" -v secret_data:/data --name second_cont  ubuntu:22.04
```