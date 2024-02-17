# Repo for a League of Legends Discord Bot

[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)
[![pt-BR](https://img.shields.io/badge/lang-pt--BR-green.svg)](README.pt-BR.md)  
[![Static Badge](https://img.shields.io/badge/python-3.12.2-blue?logo=python)](https://www.python.org/downloads/release/python-3122/)
[![Static Badge](https://img.shields.io/badge/selenium-4.17.2-brightgreen?logo=selenium)](https://pypi.org/project/selenium/4.17.2/)
[![Static Badge](https://img.shields.io/badge/discord-2.3.2-blue?logo=discord)](https://discordpy.readthedocs.io/en/v2.3.2/)


## Content
- [Project purpose](#project-purpose)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)

### Project purpose
This project was created with the aim of speeding up and making it easier to play the game League of Legends, by searching for builds and champion runes. As well as entertainment, this project also aims to improve and consolidate knowledge of Python and its modules.

### Installation
The installation consists of 3 steps:

- Step 1: creating the virtual environment:  
`
python -m venv <venv_name>
`

- Step 2: activating the virtual environment:
    - Case 1: Linux:  
    `
    source <venv_name>/bin/activate
    `
    - Case 2: Windows:  
    `
    .\<venv_name>\Scripts\activate
    `

- Step 3: installing the necessary modules:  
`
pip install -r requirements.txt
`  

### Usage
After installing and activating the virtual environment (step 2 of [Installation](#installation)), you need to create an .env file with the <DISCORD_TOKEN> variable (created via [this link](https://discord.com/developers/applications)) and add the bot to the desired server. Then run the main.py file or the run.ps1 file (only works on windows). To end its execution, simply use the Ctrl + C command in the window where the program is running.

### Commands
All commands work with both the bot command (variable <BOT_COMMAND> in the .env file) and the bot mention (*@Bot*)

- Help ("?"):
    - <BOT_COMMAND> ?

- Build ("b" or "build"):
    - <BOT_COMMAND> b [champion_name] [role (top, jg, mid, adc, sup)]
