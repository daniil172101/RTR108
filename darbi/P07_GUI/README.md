# 7. nodarbība - GUI

Šajā nodarbībā es izmēģināju vienu no GUI veidošanas piemēriem un 
izveidoju kalkulatoru izmantojot PyQt. Pēc tam es nedaudz izmainīju kodu.

## PyQt kalkulators

Sākumā es izveidoju kalkulatoru izmantojot instrukciju no https://realpython.com/python-pyqt-gui-calculator/ .
Izveidots kalkulators izskatās šādi:

![Kalkulators](https://github.com/daniil172101/RTR108/blob/master/darbi/P07_GUI/Figure_1.png)

Pēc tam es sāku izmainīt kodu. Sākumā es izmainīju kalkulatora izmēru:

Pirms izmaiņam:

	self.setFixedSize(235, 235)

Pēc izmaiņam:

	self.setFixedSize(250, 370)


Pēc tam es izmainīju pogu novietojumus un izmērus: 

Pirms izmaiņam:

	buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                  }
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)

Pēc izmaiņam:

        buttons = {'C': (0, 0),
                   '(': (0, 1),
                   ')': (0, 2),
                   '/': (0, 3),
                   '7': (1, 0),
                   '8': (1, 1),
                   '9': (1, 2),
                   '*': (1, 3),
                   '4': (2, 0),
                   '5': (2, 1),
                   '6': (2, 2),
                   '-': (2, 3),
                   '1': (3, 0),
                   '2': (3, 1),
                   '3': (3, 2),
                   '+': (3, 3),
                   '0': (4, 0),
                   '00': (4, 1),
                   '.': (4, 2),
                   '=': (4, 3),
                  }
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(50, 50)

Beigās es izmainīju displeja izmēru:

Pirms izmaiņam:

	self.display.setFixedHeight(35)

Pēc izmaiņam:

	self.display.setFixedHeight(40)

Modiicēts kalkulators izskatās šādi:


![Modificēts kalkulators](https://github.com/daniil172101/RTR108/blob/master/darbi/P07_GUI/Figure_2.png)
