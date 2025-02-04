FROM python:3.10
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR /app

# Install dependencies

RUN apt-get update && apt-get install -y \
  libxml2-dev
COPY requirements.txt /app
RUN pip install -r requirements.txt


RUN curl -o datasets 'https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/v2/linux-amd64/datasets'
RUN chmod +x datasets

RUN mkdir /assemblies
COPY ./ /app

CMD ["/app/download_assemblies"]
