import sys
import requests
from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
from requests import HTTPError


class Whether_Map(QWidget):
    def __init__(self):
        super().__init__()
        self.whether_label = QLabel("City name", self)
        self.lat_label = QLineEdit(self)
        self.lat_label.setToolTip("Lat cords")
        self.lon_label = QLineEdit(self)
        self.lon_label.setToolTip("Lon cords")
        self.w_button = QPushButton("Check whether", self)
        self.temp_label = QLabel(self)
        self.emoji = QLabel(self)

        self.des_label = QLabel(self)

        self.innitUi()

    def innitUi(self):
        self.setWindowTitle("")
        vbox = QVBoxLayout()

        vbox.addWidget(self.whether_label)
        vbox.addWidget(self.lat_label)
        vbox.addWidget(self.lon_label)
        vbox.addWidget(self.w_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji)
        vbox.addWidget(self.des_label)
        self.setLayout(vbox)
        self.whether_label.setAlignment(Qt.AlignCenter)
        self.lat_label.setAlignment(Qt.AlignCenter)
        self.lon_label.setAlignment(Qt.AlignCenter)
        self.emoji.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.des_label.setAlignment(Qt.AlignCenter)

        self.whether_label.setObjectName("whether_label")
        self.lat_label.setObjectName("lat")
        self.lon_label.setObjectName("lon")
        self.emoji.setObjectName("emoji")
        self.temp_label.setObjectName("temp_label")
        self.des_label.setObjectName("des_label")
        self.w_button.setObjectName("button")

        self.setStyleSheet("""


       QLabel#whether_label{font-size: 50px;

        border-radius: 35px;
        font-style: bold;}


       QPushButton#button{font-size: 50px;
        background-color: grey;
        border-radius: 35px;
        }

         QLineEdit#lat, QLineEdit#lon{font-size: 50px;

        border-radius: 35px;
        font-family: arial;}

         QLabel#temp_label{font-size: 75px;

        border-radius: 35px;
        font-family: arial;}

         QLabel#emoji{
          font-size: 120px;

        border-radius: 35px;
        font-family: "Segoe UI Emoji";
        padding: 20px;

        }

        QLabel#des_label{font-size: 50px;

        border-radius: 35px;
        }
        """)

        self.w_button.clicked.connect(self.check)

    def catch_errors(self, mes):
        self.temp_label.clear()
        self.emoji.clear()
        self.des_label.clear()

        self.temp_label.setText(mes)

    def check(self):
        global respons
        api_key = "a27e174c461bf97b7b1a935eacc6a540"
        lon = self.lon_label.text()
        lat = self.lat_label.text()
        URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

        try:
            respons = requests.get(URL)
            data = respons.json()

            if data["cod"] == 200:
                self.update_display(data)

        except requests.exceptions.HTTPError:
            self.catch_errors("HTTP errors")
        except requests.exceptions.ConnectionError:
            self.catch_errors("Time out, check internet connection")
        except requests.exceptions.Timeout:
            self.catch_errors("Time out, try later")
        except requests.exceptions.TooManyRedirects:
            self.catch_errors("Too many redirects, check URL")
        except requests.exceptions.RequestException:
            match respons.status_code:
                case 400:
                    self.catch_errors(f"Error, request code: {respons.status_code}")
                case 401:
                    self.catch_errors(f"Error, request code: {respons.status_code}")
                case 403:
                    self.catch_errors(f"Error, request code: {respons.status_code}")
                case 404:
                    self.catch_errors(f"Error, request code: {respons.status_code}")
                case 500:
                    self.catch_errors(f"Error, request code: {respons.status_code}")
                case 502:
                    self.catch_errors(f"Error, request code: {respons.status_code}")
                case 503:
                    self.catch_errors(f"Error, request code: {respons.status_code}")
                case 504:
                    self.catch_errors(f"Error, request code: {respons.status_code}")
                case _:
                    self.catch_errors(f"HTTP error: {HTTPError}")

    def update_display(self, data):
        self.whether_label.setText(f"{data['name']}")
        temp = data['main']['temp'] - 273.15
        self.temp_label.setText(f"{temp:.2f}°C")
        icon_code = data['weather'][0]['icon']
        clean_code = icon_code[:2]
        match clean_code:
            case "01":
                emoji = "☀️"

            case "02":
                emoji = "⛅"

            case "03" | "04":
                emoji = "☁️"

            case "09" | "10":
                emoji = "🌧️"

            case "11":
                emoji = "⛈️"

            case "13":
                emoji = "❄️"

            case "50":
                emoji = "🌫️"  # Туман

            case _:
                emoji = "🌍"

        self.emoji.setText(emoji)
        desc = data['weather'][0]['description']
        self.des_label.setText(desc)
        print(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    whether_app = Whether_Map()
    whether_app.show()
    sys.exit(app.exec_())
