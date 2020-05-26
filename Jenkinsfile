SOURCE = 'resume-liam-beckman.tex'
RESUME = 'resume-liam-beckman.pdf'
PRODUCTION = 'pi@liambeckman.com:/var/www/pkgs/resume'

node {
    stage('Update') {
        git url: 'https://git.liambeckman.com/liam/resume/'
    }
    /*
       stage('Install') {
       sh "${INSTALL} ${DEPS}"
       sh "./install.sh"
       }
     */
    stage('Build') {
        sh "pdflatex $SOURCE"
    }
    stage('Sign') {
        sh "> sha256sums.txt"
            sh "sha256sum ${SOURCE} ${RESUME} >> sha256sums.txt"
            withCredentials([string(credentialsId: 'gpgpass', variable: 'gpgpass')]) {
                sh "gpg --pinentry-mode=loopback --passphrase=${gpgpass} --yes --detach-sign -a sha256sums.txt"
            }
    }
    if (env.BRANCH_NAME == 'master') {
        stage('Copy') {
            echo "Master branch received. Copying to production."
                sh "mkdir -p ${PRODUCTION}"
                files = ["${SOURCE}", "${RESUME}"]
                files.each { item ->
                    sh "cp ${item}* ${PRODUCTION}"
                }
        }
    } else {
        echo "Non-master branch received. Not copying to production."
    }
}

