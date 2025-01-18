pipeline {
    agent {
        docker {
            image 'maven:3.8.4-jdk-11' // This uses Maven with JDK 11
            args '-v /tmp:/tmp' // Optional: mount any required volume
        }
    }

    environment {
        FRONTEND_IMAGE = "calcFrontend:latest"
        BACKEND_IMAGE = "calcBackend:latest"
        SONAR_HOST_URL = "http://localhost:9000"
        ARTIFACTORY_URL = "http://localhost:8082/artifactory/calcacr/"
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout code using credentials stored in Jenkins
                git credentialsId: 'github_pat', url: 'https://github.com/DELTA-swe/devops-setup.git', branch: 'main'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'sonar-id', variable: 'SONARQUBE_TOKEN')]) {
                        sh """
                        mvn clean verify sonar:sonar \
                        -Dsonar.projectKey=calc-dev \
                        -Dsonar.host.url=${SONAR_HOST_URL} \
                        -Dsonar.login=${SONARQUBE_TOKEN}
                        """
                    }
                }
            }
        }
        stage('Build Backend Docker Image') {
            steps {
                script {
                    // Build the backend Docker image
                    sh "docker build -t ${BACKEND_IMAGE} ."
                }
            }
        }

        stage('Build Frontend Docker Image') {
            steps {
                script {
                    // Build the frontend Docker image
                    sh "docker build -t ${FRONTEND_IMAGE} ./frontend"
                }
            }
        }
        stage('Push Docker Images to JFrog Artifactory') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'jfrog-credentials', passwordVariable: 'JFROG_PASSWORD', usernameVariable: 'JFROG_USERNAME')]) {
                        // Login to JFrog Artifactory
                        sh """
                        echo "${JFROG_PASSWORD}" | docker login ${ARTIFACTORY_URL} -u ${JFROG_USERNAME} --password-stdin
                        """
                        // Push images to JFrog Artifactory
                        sh "docker tag ${FRONTEND_IMAGE} ${ARTIFACTORY_URL}/myrepo/${FRONTEND_IMAGE}"
                        sh "docker tag ${BACKEND_IMAGE} ${ARTIFACTORY_URL}/myrepo/${BACKEND_IMAGE}"
                        sh "docker push ${ARTIFACTORY_URL}/myrepo/${FRONTEND_IMAGE}"
                        sh "docker push ${ARTIFACTORY_URL}/myrepo/${BACKEND_IMAGE}"
                    }
                }
            }
        }
    }
}
