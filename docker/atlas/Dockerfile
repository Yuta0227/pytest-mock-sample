# docker/atlas/Dockerfile
FROM debian:bullseye-slim

# Install necessary tools
RUN apt-get update && apt-get install -y \
    bash \
    coreutils \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Atlas CLI
RUN curl -sSf https://atlasgo.sh | sh

# Set the default command to keep the container running
CMD ["tail", "-f", "/dev/null"]