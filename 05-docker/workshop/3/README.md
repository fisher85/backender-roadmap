```bash
docker build --rm --tag app .
docker run  -p 8080:80  -v $(pwd):/app app
```

```
--rm
-it
-d
docker exec --it <hash> /bin/bash
docker ps -a
docker image ls -q
```