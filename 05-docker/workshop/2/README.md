```bash
docker run -it -v $(pwd)/root_dir:/dir --workdir="/dir" ubuntu:22.04 
docker build --tag user .
docker run  -v $(pwd)/user_dir:/dir user
```