# Docker Machine&Deep learning

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

## Commit container
```bash
docker commit <container ID> <tag>
```

## Mount folder 
```bash
docker run -it -v <window folder>:<container folder> <image>:<tag>
```