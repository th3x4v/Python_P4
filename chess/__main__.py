from .controllers.app import AppController


def main():
    controller = AppController()
    controller.start()


if __name__ == "__main__":
    main()
