pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "lola/hello-devops"
    }

    stages {
        stage('Build Docker') {
            steps {
                sh 'sudo docker build -t ${DOCKER_IMAGE} .'
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


