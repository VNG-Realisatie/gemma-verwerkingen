# Stage 1 - Compile needed python dependencies
FROM alpine:3.7 AS build
RUN apk --no-cache add \
    gcc \
    musl-dev \
    pcre-dev \
    linux-headers \
    postgresql-dev \
    python3 \
    python3-dev \
    zlib-dev && \
  pip3 install virtualenv && \
  virtualenv /app/env

WORKDIR /app
COPY requirements.txt /app
RUN /app/env/bin/pip install -r requirements.txt

# Stage 2 - Build docker image suitable for execution and deployment
FROM alpine:3.7
RUN apk --no-cache add \
      ca-certificates \
      mailcap \
      musl \
      pcre \
      postgresql \
      python3 \
      zlib

COPY ./src /app
COPY ./docker/start.sh /start.sh

COPY --from=build /app/env /app/env

ENV PATH="/app/env/bin:${PATH}"
WORKDIR /app
EXPOSE 8000
CMD ["/start.sh"]