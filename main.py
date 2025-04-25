# Импортируем все данные Qt
import sys
import math
from typing import Union, Optional
from operator import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from Calculator import *

# Создадим словарь с операциями
operations = {
    "+": add,
    "-": sub,
    "×": mul,
    "÷": truediv
}

error_zero_division = "Деление на ноль запрещено"
error_undefined = "Результат неопределен"

def_font_size = 15
def_entry_font_size = 50

# Создадим класс с методами и командами
class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.entry = self.ui.le_entry
        self.tempt = self.ui.lbl_temp
        self.maxlength = self.ui.le_entry.maxLength()

        QFontDatabase.addApplicationFont("fonts/Kode Mono-Regular.ttf")

        # Взаимодействие с цифрами
        self.ui.btn_0.clicked.connect(lambda: self.add_digit("0"))
        self.ui.btn_1.clicked.connect(lambda: self.add_digit("1"))
        self.ui.btn_2.clicked.connect(lambda: self.add_digit("2"))
        self.ui.btn_3.clicked.connect(lambda: self.add_digit("3"))
        self.ui.btn_4.clicked.connect(lambda: self.add_digit("4"))
        self.ui.btn_5.clicked.connect(lambda: self.add_digit("5"))
        self.ui.btn_6.clicked.connect(lambda: self.add_digit("6"))
        self.ui.btn_7.clicked.connect(lambda: self.add_digit("7"))
        self.ui.btn_8.clicked.connect(lambda: self.add_digit("8"))
        self.ui.btn_9.clicked.connect(lambda: self.add_digit("9"))
        self.ui.btn_pi.clicked.connect(lambda: self.add_digit(str(math.pi)))

        # Взаимодействие с прочими элементами
        self.ui.btn_clear.clicked.connect(self.all_clear)
        self.ui.btn_dot.clicked.connect(self.add_dot)
        self.ui.btn_neg.clicked.connect(self.neg)
        self.ui.btn_backspace.clicked.connect(self.backspace)
        self.ui.btn_sqrt.clicked.connect(self.btn_sqrt)
        self.ui.btn_ln.clicked.connect(self.btn_ln)   
        self.ui.btn_fact.clicked.connect(self.factorial)
        self.ui.btn_step.clicked.connect(self.square)
        self.ui.btn_pi.clicked.connect(self.pi_button_pressed)
     

        # Взаимодействие с тригометрическими функциями
        self.ui.btn_sin.clicked.connect(self.btn_sin)
        self.ui.btn_cos.clicked.connect(self.btn_cos)
        self.ui.btn_tan.clicked.connect(self.btn_tan)
        self.ui.btn_cot.clicked.connect(self.btn_cot)
        self.ui.btn_rad.clicked.connect(self.degrees_to_radians)
        self.ui.btn__grad.clicked.connect(self.radians_to_degrees)

        # Взаимодействие с операциями
        self.ui.btn_calc.clicked.connect(self.calculate)
        self.ui.btn_add.clicked.connect(lambda: self.add_temp("+"))
        self.ui.btn_sub.clicked.connect(lambda: self.add_temp("-"))
        self.ui.btn_mul.clicked.connect(lambda: self.add_temp("×"))
        self.ui.btn_div.clicked.connect(lambda: self.add_temp("÷"))
    
    # Создадим метод для нажатия кнопок
    def add_digit(self, btn_text: str) -> None:
        self.remove_error()
        if self.ui.le_entry.text() == "0":
            self.ui.le_entry.setText(btn_text)
        else:
            self.ui.le_entry.setText(self.ui.le_entry.text() + btn_text)

        self.adjust_entry_font_size()

    # Добавим метод для обработки нажатия кнопки "π"
    def pi_button_pressed(self) -> None:
        if self.ui.le_entry.text() and self.ui.le_entry.text() != "0":
            self.ui.le_entry.setText(str(math.pi))
            self.adjust_entry_font_size()


    # Создадим метод для нажатия запятой
    def add_dot(self) -> None:
        if "." not in self.ui.le_entry.text():
            self.ui.le_entry.setText(self.ui.le_entry.text() + ".")
            self.adjust_entry_font_size()

    # Создадим метод для вычисления квадратного корня
    def btn_sqrt(self):
        num = self.get_entry_num()
        result = math.sqrt(num)
        self.ui.le_entry.setText(str(result))
        self.adjust_entry_font_size()
    
    # Метод для возведения числа во вторую степень
    def square(self):
        num = self.get_entry_num()
        result = num ** 2
        self.ui.le_entry.setText(str(result))
        self.adjust_entry_font_size()

    # Метод для вычисления факториала
    def factorial(self):
        num = self.get_entry_num()
        result = math.factorial(num)
        self.ui.le_entry.setText(str(result))
        self.adjust_entry_font_size()

    # Создадим методы для тригонометрических функций
    def btn_sin(self):
        num = self.get_entry_num()
        result = math.sin(num)
        self.ui.le_entry.setText(str(result))
        self.adjust_entry_font_size()

    def btn_cos(self):
        num = self.get_entry_num()
        result = math.cos(num)
        self.ui.le_entry.setText(str(result))
        self.adjust_entry_font_size()

    def btn_tan(self):
        num = self.get_entry_num()
        result = math.tan(num)
        self.ui.le_entry.setText(str(result)) 
        self.adjust_entry_font_size()

    def btn_cot(self):
        num = self.get_entry_num()
        result = 1 / math.tan(num)
        self.ui.le_entry.setText(str(result))
        self.adjust_entry_font_size()

    # Метод для перевода радиан в градусы
    def radians_to_degrees(self):
        entry_text = self.entry.text()
        if entry_text:
            radians = float(entry_text)
            degrees = math.degrees(radians)
            self.entry.setText(str(degrees))
            self.adjust_entry_font_size()

    # Метод для перевода градусов в радианы
    def degrees_to_radians(self):
        entry_text = self.entry.text()
        if entry_text:
            degrees = float(entry_text)
            radians = math.radians(degrees)
            self.entry.setText(str(radians))
            self.adjust_entry_font_size()
    
    # Создадим метод для вычисления натурального логарифма
    def btn_ln(self):
        num = self.get_entry_num()
        result = math.log(num)
        self.ui.le_entry.setText(str(result))
        self.adjust_entry_font_size()   
    
    # Создадим метод для отрицания
    def neg(self):
        entry = self.ui.le_entry.text()

        if "-" not in entry:
            if entry != "0":
                entry = "-" + entry
        else:
            entry = entry[1:]

        if len(entry) == self.maxlength + 1 and "-" in entry:
            self.ui.le_entry.setMaxLength(self.maxlength + 1)
        else:
            self.ui.le_entry.setMaxLength(self.maxlength)

        self.ui.le_entry.setText(entry)
        self.adjust_entry_font_size()
    
     # Создадим метод для BackSpace
    def backspace(self) -> None:
        self.remove_error()
        entry = self.ui.le_entry.text()

        if len(entry) != 1:
            if len(entry) == 2 and "-" in entry:
                self.ui.le_entry.setText("0")
            else:
                self.ui.le_entry.setText(entry[:-1])
        else:
            self.ui.le_entry.setText("0")

        self.adjust_entry_font_size()

    # Создадим метод для стирания всех полей ввода 
    def all_clear(self) -> None:
        self.remove_error()
        self.ui.le_entry.setText("0")
        self.adjust_entry_font_size()
        self.ui.lbl_temp.clear()

    # Создадим статистический метод
    @staticmethod
    def obr_numbs(num: str) -> str:
        n = str(float(num))
        return n[:-2] if n[-2:] == ".0" else n
        
    def add_temp(self, math_sign: str):
        if not self.ui.lbl_temp.text() or self.get_sign() != "=":
            self.ui.lbl_temp.setText(self.obr_numbs(self.ui.le_entry.text()) + f" {math_sign} ")
            self.ui.le_entry.setText("0")
            self.adjust_entry_font_size()

    # Создадим метод для получения числа из поля ввода
    def get_entry_num(self) -> Union[int, float, str]:
        entry = self.ui.le_entry.text().strip(".")

        return float(entry) if "." in entry else int(entry)

    # Созаддим метод для получения числа из временного выражения
    def get_temp_num(self) -> Union[int, float, None]:
        if self.ui.lbl_temp.text():
            temp = self.ui.lbl_temp.text().strip(".").split()[0]
            return float(temp) if "." in temp else int(temp)

    # Создадим метод для получения знака из временного выражения
    def get_sign(self) -> Optional[str]:
        if self.ui.lbl_temp.text():
            return self.ui.lbl_temp.text().strip(".").split()[-1]

    # Создадим вспомогательный метод для получения ширины текста в пикселях из поля и лейбла
    def get_entry_text_width(self) -> int:
        return self.ui.le_entry.fontMetrics().boundingRect(self.ui.le_entry.text()).width()

    # Создадим функцию вычисления
    def calculate(self) -> Optional[str]:
        entry = self.ui.le_entry.text()
        temp = self.ui.lbl_temp.text()

        if temp:
            try:
                result = self.obr_numbs(
                    str(operations[self.get_sign()](self.get_temp_num(), self.get_entry_num()))
                )
                self.ui.lbl_temp.setText(temp + self.obr_numbs(entry) + "=")
                self.ui.le_entry.setText(result)
                self.adjust_entry_font_size()
                return result

            except KeyError:
                pass

            except ZeroDivisionError:
                if self.get_entry_num() == 0:
                    self.show_error(error_undefined)
                else:
                    self.show_error(error_zero_division)

    # Напишем функцию для математической оперции
    def math_op(self, math_sign: str):
        temp = self.ui.lbl_temp.text()

        if not temp:
            self.add_temp(math_sign)
        else:
            if self.get_sign() != math_sign:
                if self.get_sign() == "=":
                    self.add_temp(math_sign)
                else:
                    self.ui.lbl_temp.setText(temp[:-2] + f" {math_sign} ")
            else:
                self.ui.lbl_temp.setText(self.calculate() + f" {math_sign} ")
                

    # Создадим метод для передачи сообщения при ошибке
    def show_error(self, text: str) -> None:
        self.ui.le_entry.setMaxLength(len(text))
        self.ui.le_entry.setText(text)
        self.adjust_entry_font_size()
        self.disable_buttons(True)

    # Уберем вылезающий за границы окна текст об ошибке
    def remove_error(self) -> None:
        if self.ui.le_entry.text() in (error_undefined, error_zero_division):
            self.ui.le_entry.setMaxLength(self.maxlength)
            self.ui.le_entry.setText("0")
            self.adjust_entry_font_size()
            self.disable_buttons(False)

    # Заблокируем кнопки знаков, точек, функций, а также отрицания
    def disable_buttons(self, disable: bool) -> None:
        self.ui.btn_calc.setDisabled(disable)
        self.ui.btn_add.setDisabled(disable)
        self.ui.btn_sub.setDisabled(disable)
        self.ui.btn_mul.setDisabled(disable)
        self.ui.btn_div.setDisabled(disable)
        self.ui.btn_neg.setDisabled(disable)
        self.ui.btn_dot.setDisabled(disable)

        color = "color: #9370DB" if disable else "color: #F5FFFA"
        self.change_color(color)

    # Напишем метод для изменения цвета кнопок, при их блокировке во время ошибок
    def change_color(self, css_color: str) -> None:
        self.ui.btn_calc.setStyleSheet(css_color)
        self.ui.btn_add.setStyleSheet(css_color)
        self.ui.btn_sub.setStyleSheet(css_color)
        self.ui.btn_mul.setStyleSheet(css_color)
        self.ui.btn_div.setStyleSheet(css_color)
        self.ui.btn_neg.setStyleSheet(css_color)
        self.ui.btn_dot.setStyleSheet(css_color)

    # Регулируем размер шрифта в поле ввода
    def adjust_entry_font_size(self) -> None:
        font_size = def_entry_font_size
        while self.get_entry_text_width() > self.ui.le_entry.width() - 10:
            font_size -= 1
            self.ui.le_entry.setStyleSheet("font-size: " + str(font_size) + "pt; border: none;")

        font_size = 1

        while self.get_entry_text_width() < self.ui.le_entry.width() - 60:
            font_size += 1

            if font_size > 50:
                break
            self.ui.le_entry.setStyleSheet("font-size: " + str(font_size) + "pt; border: none;")

    # Меняем размер шрифта при растягивании окна
    def resizeEvent(self, event) -> None:
        self.adjust_entry_font_size()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())