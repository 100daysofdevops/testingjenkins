pipeline {
    agent any
    parameters {
        string(name: 'username', defaultValue: '', description: 'GitHub username')
    }
    environment {
        PAT_TOKEN = credentials('personal_access_token')
        PAT_TOKEN = mask(PAT_TOKEN)
    }
    stages {
        stage('Build') {
            steps {
                sh 'export PAT_TOKEN=${env.PAT_TOKEN} && python script.py --username ${params.username}'
            }
        }
    }
}
