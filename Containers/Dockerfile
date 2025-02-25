# Use Alpine Linux as the base image
FROM alpine:latest

# Install necessary dependencies
RUN apk add --no-cache git bash curl sqlite

# Create a non-root user and group for Gitea
RUN addgroup -S gitea && adduser -S -G gitea gitea

# Create necessary directories and set correct permissions
RUN mkdir -p /data /app && chown -R gitea:gitea /data /app

# Copy Gitea binary and set permissions
COPY ./gitea-1.23.1-linux-amd64 /app/gitea
RUN chmod +x /app/gitea && chown gitea:gitea /app/gitea

# Switch to the non-root user
USER gitea

# Set the working directory
WORKDIR /app

# Expose the default Gitea web port
EXPOSE 3000

# Run Gitea in web mode
CMD ["/app/gitea", "web"]


# to Build: docker build . -t gitea
# to Run: docker run -d -p 3000:3000 gitea 
# another clean option to run: docker run -d -p 3000:3000 --name gitea gitea/gitea:latest