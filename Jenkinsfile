pipeline {
    agent any

    environment {
        FRONTEND_IMAGE = "calcFrontend:latest"
        BACKEND_IMAGE = "calcBackend:latest"
        SONARQUBE_SERVER = 'MySonarServer' // Name of your SonarQube server in Jenkins
        SCANNER_HOME = tool 'SonarScanner' // Name of your SonarQube Scanner tool in Jenkins
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
                    withSonarQubeEnv('MySonarServer') { // Matches the name in SonarQube Servers configuration
                        sh """
                        ${SCANNER_HOME}/bin/sonar-scanner \
                            -Dsonar.projectKey=calc-dev \
                            -Dsonar.sources=. \
                            -Dsonar.language=py \
                            -Dsonar.python.version=3.13 \
                            -Dsonar.host.url=http://sonarqube-cont:9000 \
                            -Dsonar.login=sqp_328bbeb4d27f8ef97b9864e9aed339f33c9aeca4 \
                            -Dsonar.python.coverage.reportPaths=./coverage.xml \
                            -Dsonar.exclusions=**/tests/**,coverage.xml
                        """
                    }
                }
            }
        }       
    }
}
