import tkinter as tk
import unittest

from resmonitor import resmonitor


class FakePsUtil:
    @staticmethod
    def cpu_count():
        return 3

    @staticmethod
    def cpu_percent(percpu):
        return [1, 1, 1]


class TkinterTest(unittest.TestCase):
    def setUp(self):
        self.master = tk.Tk()
        self.master.withdraw()

    def tearDown(self):
        self.master.destroy()

    def process_events(self):
        self.master.update()


class TestMainPage(TkinterTest):
    def test_cpu_percent(self):
        app = resmonitor.Application(self.master, FakePsUtil)
        app.update_cpu_usage()
        self.assertEqual('1 1 1', app.cpu_percent['text'])


if __name__ == '__main__':
    unittest.main()
