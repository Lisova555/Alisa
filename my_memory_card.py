from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
      QLabel, QVBoxLayout, QGroupBox, QRadioButton,QHBoxLayout, QButtonGroup)
from random import shuffle, randint
#создание элементов интерфейса

#привязка элементов к вертикальной линии

#обработка событий

#запуск приложения

class Question():
    def __init__(self, question, right_answer,wrong1, wrong2, wrong3 ):
        # все строки надо задавать при создании объекта, они запоминаются в свойства 
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3= wrong3

questions_list = []
questions_list.append(Question('Государственный язык Бразилии','Португальский','Английский','Испанский','Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?','Зеленый', 'Красный', 'Белый', 'Синий'))

app = QApplication([])

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)




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


AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


# Размещаем все виджеты в окне:
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()






layout_line1.addWidget(lb_Question , alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()




layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)


layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    ''' показать панель вопросов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    # сбросить выбранную радио-кнопку
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

    

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()



def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
        if answers[0].isChecked():
            show_correct('Правильно!')
            main_win.score += 1
            
            
        else:

            if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
                show_correct('Неправильно!')
        print(main_win.score/main_win.total * 100)


def next_question():
        cur_question = randint(0, len(questions_list)-1)
        main_win.total += 1
        q = questions_list[cur_question] # взяли вопрос 
        ask(q) # спросили

 







def click_OK():
    '''определяет, надо ли показывать другой вопрос либо поверить ответ на этот'''
    if btn_OK.text() == 'Ответить':
        check_answer() # проверка ответа
    else:
        next_question() # следующий вопрос


 


main_win = QWidget()
main_win.setLayout(layout_card)
main_win.setWindowTitle('Memory Card')
main_win.cur_question = -1
main_win.score = 0
main_win.total = 0
btn_OK.clicked.connect(click_OK)

next_question()

main_win.resize(400, 300)
main_win.show()
app.exec()


