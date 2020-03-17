SOURCE = 'resume-liam-beckman.tex'
RESUME = 'resume-liam-beckman.pdf'
PRODUCTION = 'pi@liambeckman.com:/var/www/pkgs/resume'

node {
    stage('Update') {
        git url: 'https://git.liambeckman.com/liam/resume/'
    }
    stage('Build') {
        sh "pdflatex $SOURCE"
    }
    stage('Sign') {
        sh "sha256 ${SOURCE} ${RESUME} > sha256sums.txt"
            withCredentials([string(credentialsId: 'gpgpass', variable: 'gpgpass')]) {
                sh "gpg --pinentry-mode loopback --passphrase ${gpgpass} --yes --detach-sign -a sha256sums.txt"
            }
    }
    stage('Copy') {
        echo "Master branch received. Copying to production."
            files = ["${SOURCE}", "${RESUME}"]
            files.each { item ->
                sh "scp ${item}* ${PRODUCTION}"
            }
    }
}

