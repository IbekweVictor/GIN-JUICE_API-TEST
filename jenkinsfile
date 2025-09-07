pipeline {
    agent any
    
    environment {
        PYTHON = 'python'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(
                    branches: [[name: '*/main']], 
                    extensions: [], 
                    userRemoteConfigs: [[url: 'https://github.com/IbekweVictor/GIN-JUICE_API-TEST.git']]
                )
            }
        }

        stage('Build') {
            steps {
                // Install dependencies if there's a requirements.txt
                bat "${env.PYTHON} -m pip install --upgrade pip"
                bat "${env.PYTHON} -m pip install -r requirement.txt"
            }
        }

        stage('Test') {
            steps {
                bat "${env.PYTHON} -m pytest -v -s --junitxml=results.xml --html=report.html"
            }
            post {
                always {
                    junit 'results.xml'
                    archiveArtifacts artifacts: 'report.html', fingerprint: true
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Build and tests passed successfully!'
        }
        failure {
            echo 'Pipeline failed - check logs and reports.'
        }
    }
}

