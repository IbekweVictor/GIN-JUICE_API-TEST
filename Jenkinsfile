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
            emailext(
                subject: "✅ SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                mimeType: 'text/html',
                body: """
                    <html>
                      <body>
                        <h2 style="font-family: Arial, sans-serif; color: #2e7d32;">Build Successful ✅</h2>
                        <p><strong>Project:</strong> ${env.JOB_NAME}</p>
                        <p><strong>Build Number:</strong> ${env.BUILD_NUMBER}</p>
                        <p><strong>Status:</strong> SUCCESS</p>
                        <p>View the build details: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                        <hr>
                        <p style="font-size: 0.9em; color: #666;">This is an automated message from Jenkins.</p>
                      </body>
                    </html>
                """,
                to: 'victoruriel306@gmail.com'
            )
        }

        failure {
            emailext(
                subject: "❌ FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                mimeType: 'text/html',
                body: """
                    <html>
                      <body>
                        <h2 style="font-family: Arial, sans-serif; color: #c62828;">Build Failed 🚨</h2>
                        <p><strong>Project:</strong> ${env.JOB_NAME}</p>
                        <p><strong>Build Number:</strong> ${env.BUILD_NUMBER}</p>
                        <p><strong>Status:</strong> FAILURE</p>
                        <p>Please check the console output for details:</p>
                        <p><a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                        <h3>Quick diagnostics</h3>
                        <ul>
                          <li>Started by: ${env.BUILD_USER ?: 'unknown'}</li>
                          <li>Result: ${currentBuild.currentResult}</li>
                        </ul>
                        <hr>
                        <p style="font-size: 0.9em; color: #666;">You can reply to this email to contact the build owner.</p>
                      </body>
                    </html>
                """,
                to: 'victoruriel306@gmail.com'
            )
        }

        changed {
            emailext(
                subject: "⚙️ STATUS CHANGED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                mimeType: 'text/html',
                body: """
                    <html>
                      <body>
                        <h2 style="font-family: Arial, sans-serif; color: #0277bd;">Build Status Changed</h2>
                        <p><strong>Project:</strong> ${env.JOB_NAME}</p>
                        <p><strong>Build Number:</strong> ${env.BUILD_NUMBER}</p>
                        <p><strong>New Status:</strong> ${currentBuild.currentResult}</p>
                        <p>Details: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                        <hr>
                        <p style="font-size: 0.9em; color: #666;">If you want different recipients, update the <code>to:</code> field.</p>
                      </body>
                    </html>
                """,
                to: 'victoruriel306@gmail.com'
            )
        }
    }
}
