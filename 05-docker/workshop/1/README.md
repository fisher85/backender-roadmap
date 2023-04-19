```bash
docker pull ubuntu:22.04
docker run -it ubuntu:22.04
docker run  ubuntu:22.04 echo "hello w
orld"
docker run ubuntu:22.04 --entrypoint  sleep infinity
docker run  ubuntu:22.04 while true; do sleep 1; done
docker container ps -a
docker cp requirements.txt <hash>:/
```