FROM styl3r/vanilla:latest

LABEL version="1.0"
LABEL description="Install any package using SDKMan"



RUN ["mkdir", "-p", "/apps/home"] 
RUN ["mkdir", "-p", "/model"]
RUN ls -la /apps/home
COPY . /apps/home
WORKDIR /apps/home
RUN apt-get update && apt install -y python3 python3-pip
RUN pip3 install -r requirements.txt
RUN python3 -m spacy download en_core_web_sm

EXPOSE 8080
ENTRYPOINT ["./docker-entry.sh"]


