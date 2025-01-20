pipeline {
    agent any

    environment {
        FRONTEND_IMAGE = "calcFrontend:latest"
        BACKEND_IMAGE = "calcBackend:latest"
        SONARQUBE_SERVER = 'MySonarServer' // Name of your SonarQube server in Jenkins
        SCANNER_HOME = tool 'SonarScanner' // Name of your SonarQube Scanner tool in Jenkins
        DOCKER_REGISTRY = 'localhost:8082/artifactory/calcacr'
        ARTIFACTORY_USERNAME = credentials('jfrog-id')
        ARTIFACTORY_PASSWORD = credentials('jfrog-id')
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout code using credentials stored in Jenkins
                git credentialsId: 'github_pat', url: 'https://github.com/DELTA-swe/devops-setup.git', branch: 'main'
            }
        }
        stage('Install Node.js') {
            steps {
                sh '''
                curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
                sudo apt-get install -y nodejs
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv('MySonarServer') { // Matches the name in SonarQube Servers configuration
                        sh """
                        ${SCANNER_HOME}/bin/sonar-scanner
                        """
                    }
                }
            }
        }       
        stage('Install Docker'){
            steps{
                sh 'sudo apt-get install -y docker.io'
            }
        }
        stage('Build Frontend Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_REGISTRY}/${FRONTEND_IMAGE} ./frontend'
            }
        }
        stage('Build Backend Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_REGISTRY}/${BACKEND_IMAGE} .'
            }
        }
        stage('Push Docker Images to JFrog') {
            steps {
                script {
                    
                    // Authenticate Docker with JFrog Artifactory
                    sh """
                    echo "${ARTIFACTORY_PASSWORD}" | docker login ${DOCKER_REGISTRY} -u "${ARTIFACTORY_USERNAME}" --password-stdin
                    """

                    // Push frontend image to JFrog Artifactory
                    sh """
                    docker push ${DOCKER_REGISTRY}/${FRONTEND_IMAGE}
                    """

                    // Push backend image to JFrog Artifactory
                    sh """
                    docker push ${DOCKER_REGISTRY}/${BACKEND_IMAGE}
                    """
                }
            }
        }
    }
}
