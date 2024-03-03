# Introduction to Hands-on Security
We will expand on this during our discussions.

## How to Make it Run
You will need [docker](https://www.docker.com/products/docker-desktop/) if you don't already have it and docker-compose.
```
docker build -f Dockerfile_bad_app . -t bad-app
docker build -f Dockerfile_evil_box . -t evil-box
docker-compose up
```

