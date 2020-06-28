SRC = 'resume-liam-beckman.tex'
OUT = 'build/resume-liam-beckman.pdf'
PROD = '/var/www/pkgs/resume'

node {
    stage('Update') {
        git url: 'https://git.liambeckman.com/liam/resume/'
    }
    stage('Build') {
        sh "make"
    }
    stage('Sign') {
        sh "> sha256sums.txt"
            sh "sha256sum ${SRC} ${OUT} >> sha256sums.txt"
            withCredentials([string(credentialsId: 'gpgpass', variable: 'gpgpass')]) {
                sh "gpg --pinentry-mode=loopback --passphrase=${gpgpass} --yes --detach-sign -a sha256sums.txt"
            }
    }
    stage('Copy') {
        echo "Master branch received. Copying to production."
            sh "mkdir -p ${PROD}"
            files = ["${SRC}", "${OUT}"]
            files.each { item ->
                sh "cp ${item}* ${PROD}"
            }
    }
}

