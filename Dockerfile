FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y python3
COPY roll /tmp/ 
ENTRYPOINT ["python3", "/tmp/roll"]
CMD ["--help"]
