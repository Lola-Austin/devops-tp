pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "https://github.com/Lola-Austin/devops-tp.git"
    }

    stages {
        stage('Build Docker') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE} .'
            }
        }

        stage('Push Docker') {
            steps {
                // Simulate Docker Hub push
                sh 'echo "docker push ${DOCKER_IMAGE}"'
            }
        }
    }
}
