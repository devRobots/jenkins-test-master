#!groovy

def OUTPUTRES = '1'

pipeline {
    agent { docker { image 'python:3.13.2-alpine3.21' } }

    stages {
        stage('Run local script') {
            steps {
                script {
                    sh 'python app.py 2 4'
                }
            }
        }
        stage('Run remote script') {
            steps {
                script {
                    git clone 'https://github.com/devRobots/jenkins-test-slave'
                }
            }
        }
    }
}
