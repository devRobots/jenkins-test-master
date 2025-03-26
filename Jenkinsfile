#!groovy

pipeline {
    agent any

    stages {
        stage('Run local script') {
            steps {
                script {
                    git(url:'https://github.com/devRobots/jenkins-test-master', branch: 'main')
                    sh 'echo "Actually $(cat README.md)"'
                    sh 'echo "Hola mundo desde $(cat README.md)" > output.txt'
                    sh 'mv output.txt /tmp/'
                }
            }
        }
        stage('Run remote script') {
            steps {
                script {
                    git(url:'https://github.com/devRobots/jenkins-test-slave', branch: 'main')
                    sh 'echo "Actually $(cat README.md)"'
                    sh 'echo "Got this from /tmp $(cat /tmp/output.txt)"'
                }
            }
        }
    }
}
