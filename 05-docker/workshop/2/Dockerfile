FROM ubuntu:22.04
WORKDIR /dir
RUN useradd simba9 -u 1000 -g 100 -m -s /bin/bash
USER simba9
ENTRYPOINT echo "test" > file.txt