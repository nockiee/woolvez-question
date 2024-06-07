from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QDesktopServices
from random import *


class Ques:
    def __init__(self, que, cor, wrn1, wrn2, wrn3):
        self.que = que
        self.cor = cor
        self.wrn1 = wrn1
        self.wrn2 = wrn2
        self.wrn3 = wrn3


europa = [
    ["Кто такой волвез?", "Папа вививилки", "Админ сервера", "Мой фанатик", "мелстрой"],
    ["Что такое альхейм?", "Мусульманский городок", "городок волвеза", "село", "название торта"],
    ["Райский уголок строил:", "Сбириони", "Вулвез", "Куберок", "Вививилка"],
    ["Где у вулвеза яичко?", "Надо жать на кнопку", "Слева", "Справа", "На тарелке"],
    ["Сколько лет вививилка строил замок?", "11 лет (ему сток лет)", "1 день", "1488 секунд", "он его вставил!"],
    ["Сколько парней у вулвеза", "кубер ток", "у него нет парней", "вививилка", "михаил"],
    ["Сколько лет вулвезу?", "19", "26", "1488", "16"],
    ["Вулвез болотник?", "он огр", "да", "нет", "ку"],
]


app = QApplication([])
main = QWidget()

main.setWindowTitle("вопросы про волвеза")
main.resize(400, 200)

question = QLabel("donationalerts.com/r/kuberok52")
question.setFont(QFont("Arial", 18))

answer = QPushButton("Ответить")

# Варианты ответов
RadioGroupBox = QGroupBox("donationalerts.com/r/kuberok52")
rbtn_1 = QRadioButton("donationalerts.com/r/kuberok52")
rbtn_2 = QRadioButton("donationalerts.com/r/kuberok52")
rbtn_3 = QRadioButton("donationalerts.com/r/kuberok52")
rbtn_4 = QRadioButton("donationalerts.com/r/kuberok52")

# Лайоуты (ад)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# Результат
ResultGroupBox = QGroupBox("Результат теста")
shelly = QLabel("Правильно/Неправильно")
colt = QLabel("Правильный ответ")

ResultGroupBox.hide()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


#какие то пацанчики тут вроде функции зовут
def show_result():
    RadioGroupBox.hide()
    ResultGroupBox.show()
    answer.setText("Следующий вопрос")


def show_question():
    RadioGroupBox.show()
    ResultGroupBox.hide()
    answer.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


def ask(ku):
    shuffle(answers)
    answers[0].setText(ku.cor)
    answers[1].setText(ku.wrn1)
    answers[2].setText(ku.wrn2)
    answers[3].setText(ku.wrn3)
    question.setText(ku.que)
    colt.setText(ku.cor)
    show_question()


def show_correct(result):
    shelly.setText(result)
    show_result()


def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
        main.correct += 1
        print("\n| Статистика (Пользователь ответил правильно!)")
        print("\ Всего вопросов:", main.score)
        print("\ Правильных ответов:", main.correct)
        print("\ Рейтинг:", main.correct/main.score*100,"%")

    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неверно!")
            print("\n| Статистика (Пользователь ответил неверно!)")
            print("\ Рейтинг:", main.correct/main.score*100,"%")


poco = QVBoxLayout()
poco.addWidget(shelly, alignment=(Qt.AlignLeft | Qt.AlignTop))
poco.addWidget(colt, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
ResultGroupBox.setLayout(poco)

lomaster1 = QHBoxLayout()
lomaster2 = QHBoxLayout()
lomaster3 = QHBoxLayout()

lomaster1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

lomaster2.addWidget(RadioGroupBox)
lomaster2.addWidget(ResultGroupBox)

lomaster3.addStretch(1)
lomaster3.addWidget(answer, stretch=2)
lomaster3.addStretch(1)

amogus = QVBoxLayout()
amogus.setSpacing(4)

amogus.addLayout(lomaster1)
amogus.addLayout(lomaster2)
amogus.addLayout(lomaster3)

main.setLayout(amogus)

# окей гугл как избавить код от демона (оберег)


def europapa(current_countner):

    makaroshka = Ques(
        europa[current_countner][0],
        europa[current_countner][1],
        europa[current_countner][2],
        europa[current_countner][3],
        europa[current_countner][4],
    )
    ask(makaroshka)
    main.score += 1


def click_ok():
    if answer.text() == "Ответить":
        check_answer()

    else:
        current_countner = randint(0, 9)
        europapa(current_countner)


answer.clicked.connect(click_ok)
main.score = 1
main.correct = 0
main.show()
app.exec_()


# press f... ask("Какого амонгасика не существует?", "радужного", "зелёного", "жёлтого", "красного")