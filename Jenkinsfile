#!groovy

def OUTPUTRES = '1'

pipeline {
    agent any

    stages {
        stage('Run local script') {
            steps {
                script {
                    OUTPUTRES = sh (
                        script: 'ls -l',
                        returnStdout: true
                    ).trim()
                }
            }
        }
        stage('Run remote script') {
            steps {
                script {
                    git clone 'https://github.com/devRobots/jenkins-test-slave'
                    echo "Previous result: ${OUTPUTRES}"
                }
            }
        }
    }
}
