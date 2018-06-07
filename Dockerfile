# A super-simple "search" server that exposes port 8080
# from https://github.com/joshuaconner/hello-world-docker-bottle
#
# VERSION               0.1.0
FROM joshuaconner/hello-world-docker-bottle
MAINTAINER Yan Long Gao <gyanlon@hotmail.com>

COPY src /home/bottle

USER root
RUN apt-get install python3
RUN apt-get install python3-pip

#RUN rm /usr/bin/python
#RUN ln -s /usr/bin/python3 /usr/bin/python

#RUN pip --version
#RUN pip install --upgrade pip
#RUN pip install bottle
#RUN pip install elasticsearch-dsl
#RUN pip install xlsd

# in case you'd prefer to use links, expose the port
EXPOSE 8080
ENTRYPOINT ["/usr/bin/python", "/home/bottle/server.py"]
#USER bottle
