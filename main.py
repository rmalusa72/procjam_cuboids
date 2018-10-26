from app.assets import INTERUPT_ERROR
from app.mechanics import initialize

if __name__ == '__main__':
    try:
        initialize()
    except KeyboardInterrupt:
        print(INTERUPT_ERROR)
