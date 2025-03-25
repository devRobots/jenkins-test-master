#!groovy

def outputres = '1'

pipeline {
    agent any

    stages {
        stage('Run local script') {
            steps {
                outputres = sh(
                    script: 'ls -l',
                    returnStdout: true
                ).trim()
            }
        }
        stage('Run remote script') {
            steps {
                script {
                    git clone 'https://github.com/devRobots/jenkins-test-slave'
                    echo "Previous result: ${outputres}"
                }
            }
        }
    }
}
