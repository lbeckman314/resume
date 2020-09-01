SRC='resume-liam-beckman.tex'
RESUME='resume-liam-beckman.pdf'
PROD='/var/www/pkgs/resume'

node {
    stage('Update') {
        git url: 'https://git.liambeckman.com/liam/resume/'
    }
    stage('Build') {
        sh "make"
    }
    stage('Sign') {
        sh "> sha256sums.txt"
            sh "sha256sum ${SRC} ${RESUME} >> sha256sums.txt"
            withCredentials([string(credentialsId: 'gpgpass', variable: 'gpgpass')]) {
                sh "gpg --pinentry-mode=loopback --passphrase=${gpgpass} --yes --detach-sign -a sha256sums.txt"
            }
    }
    stage('Copy') {
        sh "mkdir -p ${PROD}"
            files = ["${SRC}", "${RESUME}"]
            files.each { item ->
                sh "cp ${item}* ${PROD}"
            }
    }
}

