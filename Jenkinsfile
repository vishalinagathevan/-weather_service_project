node {
   echo 'Docker CI Pipeline Started'
   withCredentials([usernamePassword(credentialsId: 'DOCKERHUB_USER', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
        stage('checkout') {
            checkout scm
        }
        stage('docker login') {
            powershell getLogInCmd(DOCKERHUB_USERNAME, DOCKERHUB_PASSWORD)
        }
        String imageName = DOCKERHUB_USERNAME + '/' + 'weather-service'
        stage('docker build') {
            powershell getBuildCmd('Dockerfile', imageName, ['v1', 'latest'])
        }
        stage('docker publish') {
            powershell getPushCmd(imageName)
            // powershell getRmCmd(imageName)
        }
    }
}

String getLogInCmd(username, password) {
    def cmd = 'docker login'
    cmd <<= ' --username ' + username
    cmd <<= ' --password ' + password
    return cmd.toString()
}

String getBuildCmd(dockerFile, imageName, tags) {
    def cmd = 'docker build'
    cmd <<= ' -f ' + dockerFile
    for (tag in tags) {
        cmd <<= ' -t ' + imageName + ':' + tag
    }
    cmd <<= ' .'
    return cmd.toString()
}

String getPushCmd(imageName) {
    def cmd = 'docker push'
    cmd <<= ' ' + imageName
    cmd <<= ' --all-tags'
    return cmd.toString()
}

// String getRmCmd(imageName) {
//     def cmd = 'docker images --format' + "\"{{.Repository}}:{{.Tag}}\"" + '|findstr ' + imageName
//     return 'docker rmi $()'
// }