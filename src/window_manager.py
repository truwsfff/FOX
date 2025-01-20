from src.registration import Registration


class WindowManager:
    def __init__(self, screen):
        self.screen = screen
        self.windows = {
            'registration': Registration(screen)
        }
        self.current_window = None

    def set_window(self, name):
        self.current_window = self.windows.get(name)

    def run(self):
        while self.current_window:
            self.current_window.run()
