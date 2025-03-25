#!groovy

def OUTPUTRES = '1'

pipeline {
    agent any

    stages {
        stage('Run local script') {
            steps {
                script {
                    sh 'ls -l'
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
