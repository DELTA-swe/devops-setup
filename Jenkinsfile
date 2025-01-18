pipeline {
    agent any

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

        stage('SonarQube Code Analysis') {
            steps {
                dir("${WORKSPACE}"){
                // Run SonarQube analysis for Python
                script {
                    def scannerHome = tool name: 'scanner-name', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
                    withSonarQubeEnv('SonarqubeScanner') {
                        sh "echo $pwd"
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
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
