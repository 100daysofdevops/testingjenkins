pipeline {
    agent any
    parameters {
        string(name: 'username', defaultValue: '', description: 'GitHub username')
    }
    environment {
        PAT_TOKEN = credentials('personal_access_token')
    }
    stages {
        stage('Build') {
            steps {
                sh 'export PAT_TOKEN=${env.PAT_TOKEN} && python ghe_org.py --username ${params.username}'
            }
        }
    }
}
