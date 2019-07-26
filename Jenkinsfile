SOURCE = 'resume-liam-beckman.tex'
RESUME = 'resume-liam-beckman.pdf'
PRODUCTION = '/var/www/pkgs/resume'
INSTALL = 'sudo apt-get --yes update; sudo apt-get --yes install'
DEPS = 'texlive'

node {
   stage('Update') {
      sh "git reset --hard"
      sh "git clean -fdx"
      git url: 'https://git.liambeckman.com/cgit/resume/'
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
        sh "gpg --pinentry-mode loopback --passphrase ${gpgpass} --yes --detach-sign -a sha256sums.txt"
      }
   }
   stage('Copy') {
      files = ["${SOURCE}", "${RESUME}"]
      files.each { item ->
        sh "cp ${item}* ${PRODUCTION}"
      }
   }
}
