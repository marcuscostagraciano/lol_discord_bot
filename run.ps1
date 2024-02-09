# Gets the location of this file
$ScriptPath = ($MyInvocation.MyCommand).Path

# Gets the location of the parent container (folder)
$ScriptPath = Split-Path -Parent $ScriptPath

# Advanced logging /s
Write-Output "Switching to: $ScriptPath"

# Change directory to the folder of this project
cd $ScriptPath

# Activates the virtual environment
.\venv\Scripts\activate

# Runs the bot script
python .\main.py
