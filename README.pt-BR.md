# Repositório para um Bot de League of Legends para o Discord

[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)
[![pt-BR](https://img.shields.io/badge/lang-pt--BR-green.svg)](README.pt-BR.md)  
[![Static Badge](https://img.shields.io/badge/python-3.12.2-blue?logo=python)](https://www.python.org/downloads/release/python-3122/)
[![Static Badge](https://img.shields.io/badge/selenium-4.17.2-brightgreen?logo=selenium)](https://pypi.org/project/selenium/4.17.2/)
[![Static Badge](https://img.shields.io/badge/discord-2.3.2-blue?logo=discord)](https://discordpy.readthedocs.io/en/v2.3.2/)

## Conteúdo
- [Propósito do projeto](#propósito-do-projeto)
- [Instalação](#instalação)
- [Uso](#uso)
- [Comandos](#comandos)

### Propósito do projeto
Projeto criado com o próposito de agilizar e facilitar a jogatina do jogo _League of Legends_, através da busca de _builds_ e runas de campeões. Além da parte de entretenimento, esse projeto também tem como objetivo aprimorar e consolidar os conhecimentos sobre python e seus módulos.

### Instalação
A instalação consiste de 3 comandos:

- Passo 1: criação do ambiente virtual:  
`
python -m venv <nome_da_venv>
`

- Passo 2: ativação do ambiente virtual:
    - Caso 1: Linux:  
    `
    source <nome_da_venv>/bin/activate
    `
    - Caso 2: Windows:  
    `
    .\<nome_da_venv>\Scripts\activate
    `

- Passo 3: instalação dos módulos necessários:  
`
pip install -r requirements.txt
`  


### Uso
Após a instalação e ativação do ambiente virtual (passo 2 da [Instalação](#instalação)), é necessário criar um arquivo .env com a variável <DISCORD_TOKEN> (criada através [deste link](https://discord.com/developers/applications)) e adicionar o bot ao servidor desejado. Em seguida, executar o arquivo main.py ou o arquivo run.ps1 (funciona apenas no windows). Para terminar sua execução basta usa o comando Ctrl + C na janela onde o programa esteja sendo executado.

### Comandos
Todos os comandos funcionam tanto com o comando do bot (variável <BOT_COMMAND> do arquivo .env) quanto com a menção do bot (*@Bot*)

- Ajuda ("?"):
    - <BOT_COMMAND> ?

- Build ("b" ou "build"):
    - <BOT_COMMAND> b [nome_do_campeao] [rota (top, jg, mid, adc, sup)]
