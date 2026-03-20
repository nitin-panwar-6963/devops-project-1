pipeline{
    agent any
    stages{
        stage("clone"){
            steps{
                echo "cloning the code from github......"
                sh "sleep 2s"
                git branch: 'main' , url: 'https://github.com/nitin-panwar-6963/devops-project-1.git'
                echo "clone is succesfully done ....."
            }
        }
        stage("build"){
            steps{
                echo "build the base image ....."
                sh "docker build -t expense_tracker ."
                echo "base is created succesfully"
            }
        }
                   
        stage("deploy"){
            steps{
                echo "your website is hosted......"
                sh "docker-compose up -d"
                sh "sleep 10s"
                echo "your webiste is hosted succesfully..."
            }
        }
    }
}
