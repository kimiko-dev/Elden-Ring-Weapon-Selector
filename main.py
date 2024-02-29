import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle('Elden Ring Weapon Selector') # title

        inputs_layout = qtw.QFormLayout()
        self.setLayout(inputs_layout) # vert layout

        # input prompt
        input_prompt = qtw.QLabel('Please enter your character stats') # lable
        input_prompt.setFont(qtg.QFont('Arial', 17)) # changing font and size

        #str spin box
        str_spin = qtw.QSpinBox(self, 
        value=10,
        maximum=99,
        minimum=1,
        singleStep=1)
        str_spin.setFont(qtg.QFont('Arial')) # changing font and size of spin box

        #dex spin box
        dex_spin = qtw.QSpinBox(self, 
        value=10,
        maximum=99,
        minimum=1,
        singleStep=1)
        dex_spin.setFont(qtg.QFont('Arial')) # changing font and size of spin box

        #int spin box
        int_spin = qtw.QSpinBox(self, 
        value=10,
        maximum=99,
        minimum=1,
        singleStep=1)
        int_spin.setFont(qtg.QFont('Arial')) # changing font and size of spin box

        #fai spin box
        fai_spin = qtw.QSpinBox(self, 
        value=10,
        maximum=99,
        minimum=1,
        singleStep=1)
        fai_spin.setFont(qtg.QFont('Arial')) # changing font and size of spin box

        #arc spin box
        arc_spin = qtw.QSpinBox(self, 
        value=10,
        maximum=99,
        minimum=1,
        singleStep=1)
        arc_spin.setFont(qtg.QFont('Arial')) # changing font and size of spin box

        #button
        confrim_button = qtw.QPushButton('Generate Weapons', clicked= lambda: button_press())

        inputs_layout.addRow(input_prompt)
        inputs_layout.addRow('Strength:', str_spin)
        inputs_layout.addRow('Dexterity:', dex_spin)
        inputs_layout.addRow('Intellignce:', int_spin)
        inputs_layout.addRow('Faith:', fai_spin)
        inputs_layout.addRow('Arcane:', arc_spin)
        inputs_layout.addRow(confrim_button)



        #show app
        self.show()

        def button_press():
            pass


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()