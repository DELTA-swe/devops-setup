pipeline {
    agent any

    environment {
        FRONTEND_IMAGE = "calcfrontend:latest"
        BACKEND_IMAGE = "calcbackend:latest"
        SONARQUBE_SERVER = 'MySonarServer' // Name of your SonarQube server in Jenkins
        SCANNER_HOME = tool 'SonarScanner' // Name of your SonarQube Scanner tool in Jenkins
        DOCKER_REGISTRY = 'localhost:8082/artifactory/calcacr'
        ARTIFACTORY_USERNAME = credentials('jfrog-id')
        ARTIFACTORY_PASSWORD = credentials('jfrog-id')
    }
    stages {
        stage('Checkout') {
            steps {
                sh ' echo "Checking out code from GitHub"'
                // Checkout code using credentials stored in Jenkins
                git credentialsId: 'github_pat', url: 'https://github.com/DELTA-swe/devops-setup.git', branch: 'main'
                sh 'echo "Code checked out successfully"'
            }
        }
        stage('Install Node.js') {
            steps {
                sh '''
                echo "Installing Node.js"
                curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
                sudo apt-get install -y nodejs
                echo "Node.js installed successfully"
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    sh 'echo "Running SonarQube analysis"'
                    withSonarQubeEnv('MySonarServer') { // Matches the name in SonarQube Servers configuration
                        sh """
                        ${SCANNER_HOME}/bin/sonar-scanner
                        """
                    }
                    sh 'echo "SonarQube analysis completed"'
                }
            }
        }       
        stage('Install Docker'){
            steps{
                sh 'echo "Installing Docker"'
                sh 'sudo apt-get install -y docker.io'
                sh 'echo "Docker Installed successfully"'
            }
        }
        stage('Build Frontend Docker Image') {
            steps {
                sh 'echo "Building Frontend Docker Image"'
                sh 'docker build -t ${DOCKER_REGISTRY}/${FRONTEND_IMAGE} ./frontend'
                sh 'echo "Frontend Docker Image built successfully"'
            }
        }
        stage('Build Backend Docker Image') {
            steps {
                sh 'echo "Building Backend Docker Image"'
                sh 'docker build -t ${DOCKER_REGISTRY}/${BACKEND_IMAGE} .'
                sh 'echo "Backend Docker Image built successfully"'
            }
        }
        stage('Push Docker Images to JFrog') {
            steps {
                script {
                    
                    sh 'echo "Pushing Docker Images to JFrog"'
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
                    sh 'echo "Docker Images pushed to JFrog successfully"'
                }
            }
        }
    }
}
