FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    && curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

RUN npm install -g @asyncapi/generator@1.15.0
RUN npm install -g @asyncapi/cli@1.15.0
RUN npm install -g  @asyncapi/markdown-template@1.6.0

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

VOLUME /docs
VOLUME /site

EXPOSE 8000

CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
