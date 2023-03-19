import flask.mainapp as mainapp

def check_resalt(result, *args):
    if mainapp.energy(args) == result:
        return True
    return False

print(check_resalt([696, 5800, 199], ))

