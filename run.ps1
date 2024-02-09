# Gets the location of this file
$script_path = ($MyInvocation.MyCommand).Path

# Gets the location of the parent container (folder)
$script_path = Split-Path -Parent $script_path

# Advanced logging /s
Write-Output "Switching to: $script_path"

# Change directory to the folder of this project
cd $script_path

$virtual_env_name = $null

if (Test-Path "venv") {
    $virtual_env_name = "venv"
} else {
    $virtual_env_name = Read-Host "Insert the venv folder name"
}

# Goes to the venv\scripts
cd ".\$virtual_env_name\Scripts\"

# Activate he venv
.\activate

# Returns to the parent folder
cd $script_path

# Runs the bot script
python .\main.py
