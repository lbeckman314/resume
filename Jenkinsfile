SOURCE = 'resume-liam-beckman.tex'
RESUME = 'resume-liam-beckman.pdf'
<<<<<<< HEAD
PRODUCTION = 'pi@liambeckman.com:/var/www/pkgs/resume'
=======
PRODUCTION = '/var/www/pkgs/resume'
>>>>>>> opb

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

