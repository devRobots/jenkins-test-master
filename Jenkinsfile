#!groovy

def outputres = '1'

pipeline {
    agent any

    stages {
        stage('Run local script') {
            steps {
                ansiColor('xterm') {
                    print '\u001B[34m[B2B] - Running first script\u001B[0m: Starting Python script... }'
                }
                script {
                    outputres = (sh 'app.py' 2 4)
                }
            }
        }
        stage('Run remote script') {
            steps {
                ansiColor('xterm') {
                    print '\u001B[34m[B2B] - Running first script\u001B[0m: Starting Python script... }'
                }
                script {
                    git clone "https://github.com/devRobots/jenkins-test-slave"
                    sh 'jenkins-test-slave/app.py' outputres
                }
            }
        }
    }

    post {
        success {
            script {
                ansiColor('xterm') { print '\u001B[32m[SUCCESS]\u001B[0m' }
                cleanWs()
            }
        }
        failure {
            script {
                ansiColor('xterm') { print '\u001B[31m[FAILURE]\u001B[0m' }
                cleanWs()
            }
        }
        aborted {
            script {
                ansiColor('xterm') { print '\u001B[31m[ABORTED]\u001B[0m' }
                cleanWs()
            }
        }
        always { script { env.build_url = env.BUILD_URL } }
    }
}
