pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                git url : 'https://github.com/DELTA-swe/devops-setup.git', branch: 'main'
            }
        }
    }
}
