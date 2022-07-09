import subprocess
import sys
import get_pip


# Installing Function
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])


# Installing python-chess
try:
    print("[GAME] Trying to import python-chess")
    import chess
except:
    print("[EXCEPTION] python-chess not installed")

    try:
        print("[GAME] Trying to install python-chess via pip")
        import pip

        install("python-chess")
        print("[GAME] python-chess has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")
        print("[GAME] Trying to install pip")
        get_pip.main()
        print("[GAME] Pip has been installed")
        try:
            print("[GAME] Trying to install python-chess")
            import pip

            install("python-chess")
            print("[GAME] python-chess has been installed")
        except:
            print("[ERROR 1] python-chess could not be  (Kindly check internet connection)")


# Installing pygame
try:
    print("[GAME] Trying to import pygame")
    import pygame
except:
    print("[EXCEPTION] pygame not installed")

    try:
        print("[GAME] Trying to install pygame via pip")
        import pip

        install("pygame")
        print("[GAME] pygame has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")
        print("[GAME] Trying to install pip")
        get_pip.main()
        print("[GAME] Pip has been installed")
        try:
            print("[GAME] Trying to install pygame")
            import pip

            install("pygame")
            print("[GAME] pygame has been installed")
        except:
            print("[ERROR 1] pygame could not be installed (Kindly check internet connection)")


#Installing random
try:
    print("[GAME] Trying to import random")
    import random
except:
    print("[EXCEPTION] random not installed")

    try:
        print("[GAME] Trying to install random via pip")
        import pip

        install("random")
        print("[GAME] random has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")
        print("[GAME] Trying to install pip")
        get_pip.main()
        print("[GAME] Pip has been installed")
        try:
            print("[GAME] Trying to install random")
            import pip

            install("random")
            print("[GAME] random has been installed")
        except:
            print("[ERROR 1] random could not be installed (Kindly check internet connection)")