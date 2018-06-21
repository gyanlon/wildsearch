# wildsearch


### Step 1 - Install Docker in Windows
https://github.com/docker/toolbox/releases

### Step 2 - Install wildsearch in Docker
> docker pull gyanlon/wildsearch-bottle

or

> docker build -t gyanlon/wildsearch-bottle:latest git@github.com:gyanlon/wildsearch.git

### Step 3 - Run wildsearch in Docker
> docker run -p 8080:8080 -d gyanlon/wildsearch-bottle
