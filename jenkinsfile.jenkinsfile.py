pipeline {
  agent any
  stages {
    stage('Installing required libraries') {
      steps {
        echo 'Installing required pyhon libraries'
        sh 'pip3 install robotframework'
        sh 'pip3 install robotframework-databaselibrary'
        sh 'pip3 install pyodbc'
        sh 'pip3 install pypyodbc'
        sh 'pip3 install pytest'
      }
    }
    stage('Install') {
        steps {
            sh'''
uname -a
'''
        }

      }  
    stage('PyTest') {
      steps {
        sh 'python3 -m pytest dq.py'
      }
    }  
  }
}
