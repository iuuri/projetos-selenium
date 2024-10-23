import sys
import os
from cx_Freeze import setup, Executable

#Definir o que deve ser incluido na pasta final
arquivos = ['passos.txt', 'musica/']

# Saida de arquivos
configuracao = Executable(
    script='app.py',#arquivo principal com a automação
    icon='rede.ico' #icone 
)
# Configurar o executável
setup(
    name='Automatizador de login',#nome da aplicação
    version='1.0',
    description='Este programa automatizar o login deste site',
    author='Iuri Souza',
    options={'build_exe':{
        'include_files': arquivos,#incluir arquivos colocados acima
        'include_msvcr': True #sempre colocar essa configuração se o sistema operacional for windows
    }},
    executables=[configuracao]
)
