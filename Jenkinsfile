pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                
                git url : 'https://github.com/DELTA-swe/devops-setup.git', branch: 'main'
            }
        }
    }
}
