```bash
docker build . --tag cpp_env
docker run --name cpp_debug -v $(pwd)/dev:/developer -it cpp_env /bin/bash
```