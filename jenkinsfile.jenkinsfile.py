pipeline {
  agent any
  stages {
    stage('Installing required libraries') {
      steps {
        echo 'Installing required pyhon libraries'
        sh 'pip3 install robotframework'
        sh 'pip3 install robotframework-databaselibrary'
        sh 'pip3 install pyodbc'
        sh 'pip3 install pytest'
      }
    }
    stage('PyTest') {
      steps {
        sh 'python3 -m pytest dq.py'
      }
    }  
  }
}
