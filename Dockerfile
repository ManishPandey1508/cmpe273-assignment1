FROM python:2.7.12
MAINTAINER Your Name "manish.123kumarpandey@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt && \
	pip install PyGithub 
ENTRYPOINT ["python", "app.py"]
CMD [$1]
