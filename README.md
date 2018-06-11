# wildsearch


### Step 1 - Install Docker in Windows
https://github.com/docker/toolbox/releases

### Step 2 - Install wildsearch in Docker
docker pull gyanlon/wildsearch:0.1.0
or 
docker build -t gyanlon/wildsearch:0.1.0 git@github.com:gyanlon/wildsearch.git

### Step 3 - Run wildsearch in Docker
docker run -p 8080:8080 -d gyanlon/wildsearch:0.1.0
