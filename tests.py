from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QRunnable, QThreadPool
import time


class TestSignals(QObject):
    test_signal = pyqtSignal(str)


class TestRunnable(QRunnable):
    def __init__(self):
        super(TestRunnable, self).__init__()
        self.test_string = "Hello this is a test"
        self.signals = TestSignals()

    @pyqtSlot()
    def run(self):
        while True:
            self.signals.test_signal.emit(self.test_string)
            time.sleep(2)


class TestController:
    def __init__(self):
        self.test_runnable = TestRunnable()
        self.test_runnable.signals.test_signal.connect(print)
        self.test_thread_pool = QThreadPool()
        self.test_thread_pool.start(self.test_runnable)


