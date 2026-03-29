import sys
import threading
import itertools


class Spinner:
    def __init__(self, message="A pensar"):
        self.message = message
        self._stop_event = threading.Event()
        self._thread = None

    def _spin(self):
        for char in itertools.cycle("⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"):
            if self._stop_event.is_set():
                break
            sys.stdout.write(f"\r{char} {self.message}...")
            sys.stdout.flush()
            self._stop_event.wait(0.1)
        sys.stdout.write(f"\r{' ' * (len(self.message) + 5)}\r")
        sys.stdout.flush()

    def __enter__(self):
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._spin, daemon=True)
        self._thread.start()
        return self

    def __exit__(self, *args):
        self._stop_event.set()
        self._thread.join()
