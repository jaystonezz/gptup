
# Dockerfile for Python-based development environment
FROM mcr.microsoft.com/devcontainers/python:3.9

# Install additional dependencies
RUN apt-get update && apt-get install -y     curl     git     && apt-get clean
