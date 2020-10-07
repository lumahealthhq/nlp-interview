# Base stage
FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install --yes \
    python3-pip
    
RUN pip3 install Flask==1.1.2 \
    scikit-learn==0.23.2 \
    googletrans==3.0.0 

COPY . /luma-health/ 

WORKDIR /luma-health/

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]
