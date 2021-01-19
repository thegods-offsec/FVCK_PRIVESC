#/usr/bin/python3
# salve para os que estão em call comigo, gl4sya e stolas !
#---
import os
from time import sleep
#---
fVermelho = "\033[1;31m"
tVerde = "\033[1;32m"
tAmarelo = "\033[1;33m"
tBranco = "\033[1;97m"
#---
def ascii():
    sleep(1)
    print(tBranco + """
        \   /\\  
        )  ( ')  death to windows.
        (  /  )
        \(__)| """)
def shell_ty():
    print(" ")
    pergunta = input(tVerde + "[!] Deseja spawnar uma shell TTY? (s/n) -> ")
    if pergunta == "s":
        print(" ")

        print(tBranco + '[!] spawnando shell tty ..')
        sleep(1)
        ascii()
        os.system("/bin/bash -i")
    if pergunta == "n":
        exit
def privilege_esc():
    os.system(['clear', 'cls'][os.name == 'nt'])
    ascii()
    print(" ")
    print(tAmarelo + '┌─ Tentando elevar privilégio ..')
    print(tAmarelo + '└──╼ Mostrando os possíveis' + fVermelho + ' SUIDs ..')
    print(tBranco + " ")
    sleep(1)
    os.system('find / -perm /4000 2>/dev/null')
    sleep(3)
    print(" ")
    print(tAmarelo + '┌─ Aguarde um segundo .. aceita um café?')
    print(tAmarelo + '└──╼ Exibindo os ' + fVermelho +  'capabilities ..')
    print(tBranco + " ")
    sleep(1)
    os.system('getcap -r / 2>/dev/null')
    print(" ")
    print(tAmarelo +'┌─ Verificando arquivos por SGID ..')
    print(tAmarelo + '└──╼ Exibindo os arquivos ' + fVermelho +  'SGID')
    print(tBranco + " ")
    os.system("find / -perm /2000 2>/dev/null")
def backups():
    print(" ")
    print(tAmarelo + '┌─ Varrendo por arquivos sensíveis ..')
    print(tAmarelo + '└──╼ Exibindo pastas de ' + fVermelho + 'backups ..')
    print(tBranco + " ")
    os.system("find / -name '*.bak' 2>/dev/null") 
def passwd():
    print(" ")
    print(tAmarelo + '┌─ Listando por usuários na máquina ..')
    print(tAmarelo + '└──╼ Exibindo o arquivo ' + fVermelho + '/etc/passwd ..')
    print(tBranco + " ")
    os.system("cat /etc/passwd")
def ssh():
    print(" ")
    print(tAmarelo + '┌─ Verificando resquícios SSH na máquina ..')
    print(tAmarelo + '└──╼ Exibindo arquivos de ' + fVermelho + 'rsa keys ..')
    print(tBranco + " ")
    os.system("find / -name 'id_rsa' 2>/dev/null; find / -name '*.pub' 2>/dev/null")
def bash():
    print (" ")
    print(tAmarelo + '┌─ Verificando arquivos em bash script na máquina ..')
    print(tAmarelo + '└──╼ Exibindo os arquivos com extensão' + fVermelho + '.sh ..')
    print(tBranco + " ")
    os.system("find / -name '*.sh' 2>/dev/null")
def uname():
    print (" ")
    print(tAmarelo + '┌─ Verificando informações de kernel na máquina ..')
    print(tAmarelo + '└──╼ Exibindo dados de ' + fVermelho + 'Kernel Linux ..')
    print(tBranco + " ")
    os.system("uname -a")
def passwords():
    print (" ")
    print(tAmarelo + '┌─ Verificando arquivos com password no nome ..')
    print(tAmarelo + '└──╼ Exibindo arquivos de ' + fVermelho + 'senhas no nome..')
    print(tBranco + " ")
    os.system("find / | grep password 2>/dev/null")
    print(tAmarelo + '┌─ Verificando arquivos com password no conteúdo ..')
    print(tAmarelo + '└──╼ Exibindo arquivos que podem conter ' + fVermelho + 'senhas ..')
    print(tBranco + " ")
    os.system("grep -r password /* 2>/dev/null")
def databases():
    print (" ")
    print(tAmarelo + '┌─ Verificando possíveis arquivos SQL ..')
    print(tAmarelo + '└──╼ Exibindo arquivos de ' + fVermelho + 'SQL ..')
    print(tBranco + " ")
    os.system("find / -name '*.sql' 2>/dev/null")
def sudol():
    print (" ")
    print(tAmarelo + '┌─ Verificando possíveis binários que você tem autorização a executar como root ..')
    print(tAmarelo + '└──╼ Exibindo binários de ' + fVermelho + 'sudo -l ..')
    print(tBranco + " ")
    os.system("sudo -l")


privilege_esc()
backups()
passwd()
ssh()
bash()
uname()
passwords()
shell_ty()
