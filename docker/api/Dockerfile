FROM python:3.9-slim

WORKDIR /workspace

# Install build tools and dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

    
# RUN pip install -U pip \
#     && pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install pipreqs
CMD ["./run.sh"]