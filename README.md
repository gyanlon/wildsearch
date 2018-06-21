# wildsearch


### Step 1 - Install Docker in Windows
https://github.com/docker/toolbox/releases

Note:
Enable VT-d in the bios for the virual toolbox installation in windows. 
http://www.netinstructions.com/how-to-install-docker-on-windows-behind-a-proxy/


### Step 2 - Install wildsearch in Docker
> docker pull gyanlon/wildsearch-bottle

or

> docker build -t gyanlon/wildsearch-bottle:latest git@github.com:gyanlon/wildsearch.git

### Step 3 - Run wildsearch in Docker
> docker run -p 8080:8080 -d gyanlon/wildsearch-bottle
