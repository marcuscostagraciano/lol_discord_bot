from . import get_screenshot

# ver rotas

def get_reponse(user_input: str) -> str:
    user_input = user_input.upper().split(" ")
    champ_name: str = user_input[0]
    role: str = user_input[1]

    try:
        get_screenshot.get_screenshoot(champ_name, role)
        return f"{champ_name} {role}"
    except Exception as e:
        print(e)
