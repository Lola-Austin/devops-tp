# Start from the official Jenkins LTS image
FROM jenkins/jenkins:lts

# Switch to root user to install software
USER root

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Switch back to Jenkins user
USER jenkins
