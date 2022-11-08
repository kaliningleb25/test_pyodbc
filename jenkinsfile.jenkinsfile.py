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
#Download the desired package(s)
curl -O https://download.microsoft.com/download/b/9/f/b9f3cce4-3925-46d4-9f46-da08869c6486/msodbcsql18_18.1.2.1-1_amd64.apk
curl -O https://download.microsoft.com/download/b/9/f/b9f3cce4-3925-46d4-9f46-da08869c6486/mssql-tools18_18.1.2.1-1_amd64.apk


#(Optional) Verify signature, if 'gpg' is missing install it using 'apk add gnupg':
#curl -O https://download.microsoft.com/download/b/9/f/b9f3cce4-3925-46d4-9f46-da08869c6486/msodbcsql18_18.1.2.1-1_amd64.sig
#curl -O https://download.microsoft.com/download/b/9/f/b9f3cce4-3925-46d4-9f46-da08869c6486/mssql-tools18_18.1.2.1-1_amd64.sig

#curl https://packages.microsoft.com/keys/microsoft.asc  | gpg --import -
#gpg --verify msodbcsql18_18.1.2.1-1_amd64.sig msodbcsql18_18.1.2.1-1_amd64.apk
#gpg --verify mssql-tools18_18.1.2.1-1_amd64.sig mssql-tools18_18.1.2.1-1_amd64.apk


#Install the package(s)
sudo apk add --allow-untrusted msodbcsql18_18.1.2.1-1_amd64.apk
sudo apk add --allow-untrusted mssql-tools18_18.1.2.1-1_amd64.apk
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
