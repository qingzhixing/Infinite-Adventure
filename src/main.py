from PyQt6.QtWidgets import QApplication, QWidget
import sys

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("无尽的冒险: Infinite-Adventure")
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    print("正在运行 Infinite Adventure...")
    main()
