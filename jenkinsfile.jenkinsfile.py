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
            if ! [[ "18.04 20.04 22.04" == *"$(lsb_release -rs)"* ]];
then
    echo "Ubuntu $(lsb_release -rs) is not currently supported.";
    exit;
fi

sudo su
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list

exit
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18
echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
source ~/.bashrc
# optional: for unixODBC development headers
sudo apt-get install -y unixodbc-dev
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
