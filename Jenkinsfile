pipeline {
  agent {
    dockerfile {
      dir 'multples_of_y_and_x'
      args '-it --rm --name multiples -v "$PWD/results":/usr/src/app/results'
    }
  }
  stages {
    stage('test') {
      steps {
        sh 'multiples robot'
      }
    }

  }
}
