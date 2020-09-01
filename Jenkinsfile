SRC='resume-liam-beckman.tex'
RESUME='resume-liam-beckman.pdf'
PROD='/var/www/pkgs/resume'

node {
    stage('Update') {
        git url: 'https://git.liambeckman.com/liam/resume/'
    }
    stage('Build') {
        sh "make resume"
    }
    stage('Sign') {
        sh "> sha256sums.txt"
            sh "sha256sum ${SRC} ${RESUME} >> sha256sums.txt"
            withCredentials([string(credentialsId: 'gpgpass', variable: 'gpgpass')]) {
                sh "gpg --pinentry-mode=loopback --passphrase=${gpgpass} --yes --detach-sign -a sha256sums.txt"
            }
    }
    if (env.BRANCH_NAME == 'master') {
        stage('Copy') {
            echo "Master branch received. Copying to production."
                sh "mkdir -p ${PROD}"
                files = ["${SRC}", "${RESUME}"]
                files.each { item ->
                    sh "cp ${item}* ${PROD}"
                }
        }
    } else {
        echo "Non-master branch received. Not copying to production."
    }
}

