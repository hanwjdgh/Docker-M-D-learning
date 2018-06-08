# Docker Machine&Deep learning
Docker hub : https://hub.docker.com/r/hanwjdgh/mlearn/
docker pull hanwjdgh/mlearn
## Search image
```bash
docker search <image>
```

## Pull image
```bash
docker pull <image>
```

## Run image
```bash
docker run -it <image> /bin/bash
```

## Print container list
```bash
docker ps -a
```

## Delete All container 
```bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

## Commit container
```bash
docker commit <container ID> <tag>
```

## Mount folder 
```bash
docker run -it -v <window folder>:<container folder> <image>:<tag>
```
