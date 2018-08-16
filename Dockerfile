FROM alpine:3.8
RUN apk add python3
COPY roll.py /tmp/ 
ENTRYPOINT ["python3", "/tmp/roll.py"]
CMD ["--help"]
