from time import sleep

def printLyrics():
    lines = [
        ("Love is just a history", 0.1),
        ("that they may prove", 0.09),
        ("And when you're gone, I'll", 0.1),
        ("tell them all my religionss", 0.07),
        ("you When punctures come", 0.1),
        ("to kill the king upon", 0.1),
        ("his throne", 0.1),
        ("I'm ready for their stone", 0.15),
        ("I'll dance, dance", 0.1),
        ("dance with my", 0.09),
        ("hands hands above my head", 0.1),
        ("head head Like Jesus said", 0.1),
        ("I'm gonna ", 0.09),
        ("i am gonna dance", 0.09),
        ("dance, dance with", 0.09),
        ("hands, hands, hands above my head", 0.09),
        ("and together forgive them", 0.09),
        ("before he's dead", 0.1),
        ("because I won't cry for you", 0.15),
        ("I won't crucify ", 0.15),
        ("the things you do", 0.2),
        ("I won't cry for you", 0.2),
        ("See me when you're gone", 0.15),
        ("i will still be bloody mary", 0.2),
    ]

    # print with per-line typing speed
    for text, delay in lines:
        for char in text:
            print(char, end="", flush=True)
            sleep(delay)
        print()

printLyrics()
