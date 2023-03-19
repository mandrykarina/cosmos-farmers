import MainApp

def check_resalt(result, *args):
    if MainApp.energy(args) == result:
        return True
    return False

print(check_resalt([696, 5800, 199], ))

