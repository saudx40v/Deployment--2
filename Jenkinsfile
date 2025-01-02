pipeline {
    agent any

    environment {
        DOCKER_USERNAME = 'saudx40v' // اسم المستخدم في Docker Hub
        DOCKER_PASSWORD = 'Qqwer2008*' // كلمة المرور في Docker Hub
        DOCKER_IMAGE_NAME = 'saudx40v/py3' // اسم الصورة
    }

    stages {
        stage('Checkout') {
            steps {
                // سحب الملفات من مستودع GitHub
                git 'https://github.com/saudx40v/Deployment--2.git' 
            }
        }

        stage('Build Docker Image') {
            steps {
                // بناء صورة Docker باستخدام Dockerfile
                sh 'docker build -t ${py3} .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                // تسجيل الدخول إلى Docker Hub
                sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
            }
        }

        stage('Push Docker Image') {
            steps {
                // رفع صورة Docker إلى Docker Hub
                sh 'docker push ${py3}'
            }
        }
    }

    post {
        always {
            // تسجيل الخروج من Docker Hub
            sh 'docker logout'
        }
    }
}
