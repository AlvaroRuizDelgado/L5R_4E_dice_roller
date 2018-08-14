FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y python3
RUN cp $(which python3) /usr/local/bin/
COPY roll /tmp/ 
RUN chmod +x /tmp/roll
ENTRYPOINT ["./tmp/roll"]
CMD ["--help"]
