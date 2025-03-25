#!groovy

def outputres = '1'

pipeline {
    agent any

    stages {
        stage('Run local script') {
            steps {
                script {
                    sh 'app.py 2 4'
                }
            }
        }
        stage('Run remote script') {
            steps {
                script {
                    git clone 'https://github.com/devRobots/jenkins-test-slave'
                    sh 'jenkins-test-slave/app.py 1'
                }
            }
        }
    }
}
