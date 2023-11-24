import datetime

def sveiciens():
    stunda = datetime.datetime.now().hour

    if 6 <= stunda < 12:
        return "Labrīt!"
    elif 12 <= stunda < 18:
        return "Labdien!"
    else:
        return "Labvakar!"

# Sveiciena izvade
print(sveiciens())
