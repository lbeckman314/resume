TEX='src/resume-liam-beckman.tex'
RESUME='build/resume-liam-beckman.pdf'
COVER='build/coverletter-liam-beckman.pdf'
PROD='/var/www/pkgs/resume'

node {
    stage('Build') {
        sh "make"
    }
    stage('Deploy') {
        sh "mkdir -p ${PROD}"
        files = ["${TEX}", "${RESUME}", "${COVER}"]
        files.each { item ->
            sh "cp ${item}* ${PROD}"
        }
    }
}
