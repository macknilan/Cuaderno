# 1
#FROM debian
#RUN apt-get -q update
#RUN apt-get install -y curl
#RUN apt-get install -y vim
# 2
#FROM debian
#CMD ping -c 10 www.google.com
# 3
#FROM debian
#CMD ["ping", "-c", "10", "www.google.com"]
# 4
FROM debian
CMD ["-c", "10", "www.google.com"]
ENTRYPOINT["ping"]

