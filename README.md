# wildsearch
A little search tool for your knowledge library

### Step 1 - Install Docker in Windows
https://github.com/docker/toolbox/releases

Note:
Enable VT-d in the bios for the virual toolbox installation in windows. 
http://www.netinstructions.com/how-to-install-docker-on-windows-behind-a-proxy/

### Step 2 - Install elastic search in Docker
> docker run -e ES_JAVA_OPTS="-Dfile.encoding=UTF-8 -Xms128m -Xmx1024m -XX:PermSize=64m -XX:MaxPermSize=256m"  -p 9200:9200 -d elasticsearch

### Step 3 - Install wildsearch-bottle in Docker
> docker pull gyanlon/wildsearch-bottle

or

> docker build -t gyanlon/wildsearch-bottle:latest git@github.com:gyanlon/wildsearch.git

### Step 4 - Create shared folder in window and copy your data files (xls or xlsx files) here
c:/Users/wildsearch/todo

### Step 5 - Run wildsearch in Docker with shared folder
> docker run -p 8080:8080 -v //c/Users/wildsearch:/data -d gyanlon/wildsearch-bottle

or

> docker run -e "ES_IP=192.168.99.100" -e "ES_PORT=9200" -p 8080:8080 -v //c/Users/wildsearch:/data -d gyanlon/wildsearch-bottle

### Step 6 - Load data
http://localhost:8080/load

### Step 7 - Search it
http://localhost:8080
