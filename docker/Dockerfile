FROM python:3.11-slim

# ARG used during build (sometimes accidentally logged or left behind)
ARG BUILD_API_KEY=BUILDKEY_FAKE_0001

LABEL maintainer="dev@example.com"
LABEL hidden_secret="LABELKEY_FAKE_ABC123"

COPY . /app
WORKDIR /app

RUN echo "Build arg was: $BUILD_API_KEY" || true

CMD ["python", "app.py"]
