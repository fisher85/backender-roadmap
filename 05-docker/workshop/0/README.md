```bash
docker run -d -p 5000:5000 --restart=always --name registry registry:2
docker tag gcc localhost:5000/test_my_gcc
docker push localhost:5000/test_my_gcc
```