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

### Step 3 - Create shared folder in window and copy your data files (xls or xlsx files) here
c:/Users/wildsearch

### Step 4 - Run wildsearch in Docker with shared folder
> docker run -p 8080:8080 -v //c/Users/wildsearch:/data -d gyanlon/wildsearch-bottle

### Step 5 - Load data
http://localhost:8080/load

### Step 6 - Use search
http://localhost:8080
