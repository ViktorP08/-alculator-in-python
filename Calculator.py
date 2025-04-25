from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import resursiki_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(385, 504)
        MainWindow.setMinimumSize(QSize(270, 425))
        icon = QIcon()
        icon.addFile(u":/icons/icons/free-icon-calculator-8289106.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color: #F5FFFA;\n"
"    background-color: #483D8B;\n"
"    font-family: Kode Mono;\n"
"    font-size: 15pt;\n"
"    font-weight: 600;\n"
"} \n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E90FF	;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton: btn_1 {\n"
"    background-color: #000000;\n"
"}")
        MainWindow.setIconSize(QSize(35, 35))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_temp = QLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)
        self.lbl_temp.setMinimumSize(QSize(363, 30))
        self.lbl_temp.setStyleSheet(u"color: #808080;\n"
"border-radius: 15px;\n"
"font-size: 12pt;")
        self.lbl_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl_temp)

        self.le_entry = QLineEdit(self.centralwidget)
        self.le_entry.setObjectName(u"le_entry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_entry.sizePolicy().hasHeightForWidth())
        self.le_entry.setSizePolicy(sizePolicy1)
        self.le_entry.setMinimumSize(QSize(363, 120))
        self.le_entry.setStyleSheet(u"font-size: 80pt;\n"
"color: #F5F5F5;\n"
"border-radius: 15px;")
        self.le_entry.setMaxLength(35)
        self.le_entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.le_entry.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_entry)

        self.layout_buttons = QGridLayout()
        self.layout_buttons.setObjectName(u"layout_buttons")
        self.layout_buttons.setSizeConstraint(QLayout.SetFixedSize)
        self.btn_calc = QPushButton(self.centralwidget)
        self.btn_calc.setObjectName(u"btn_calc")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_calc.sizePolicy().hasHeightForWidth())
        self.btn_calc.setSizePolicy(sizePolicy2)
        self.btn_calc.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #191970;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E90FF;\n"
"}\n"
"")

        self.layout_buttons.addWidget(self.btn_calc, 6, 4, 1, 1)

        self.btn_dot = QPushButton(self.centralwidget)
        self.btn_dot.setObjectName(u"btn_dot")
        sizePolicy2.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy2)
        self.btn_dot.setStyleSheet(u"QPushButton {\n"
"    background-color: #00008B;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E90FF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4169E1;\n"
"}")

        self.layout_buttons.addWidget(self.btn_dot, 6, 3, 1, 1)

        self.btn_pi = QPushButton(self.centralwidget)
        self.btn_pi.setObjectName(u"btn_pi")
        sizePolicy2.setHeightForWidth(self.btn_pi.sizePolicy().hasHeightForWidth())
        self.btn_pi.setSizePolicy(sizePolicy2)
        self.btn_pi.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #191970;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E90FF;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/free-icon-pi-9800851.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pi.setIcon(icon1)
        self.btn_pi.setIconSize(QSize(27, 25))

        self.layout_buttons.addWidget(self.btn_pi, 1, 0, 1, 1)

        self.btn_step = QPushButton(self.centralwidget)
        self.btn_step.setObjectName(u"btn_step")
        sizePolicy2.setHeightForWidth(self.btn_step.sizePolicy().hasHeightForWidth())
        self.btn_step.setSizePolicy(sizePolicy2)
        self.btn_step.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #191970;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E90FF;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/free-icon-step.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_step.setIcon(icon2)
        self.btn_step.setIconSize(QSize(30, 35))

        self.layout_buttons.addWidget(self.btn_step, 4, 0, 1, 1)

        self.btn_backspace = QPushButton(self.centralwidget)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy2.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy2)
        self.btn_backspace.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_backspace.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #191970;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E90FF;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/free-icon-backspace-5456223.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_backspace.setIcon(icon3)
        self.btn_backspace.setIconSize(QSize(35, 35))

        self.layout_buttons.addWidget(self.btn_backspace, 1, 4, 1, 1)

        self.btn_rad = QPushButton(self.centralwidget)
        self.btn_rad.setObjectName(u"btn_rad")
        sizePolicy2.setHeightForWidth(self.btn_rad.sizePolicy().hasHeightForWidth())
        self.btn_rad.setSizePolicy(sizePolicy2)
        self.btn_rad.setSizeIncrement(QSize(50, 50))
        self.btn_rad.setBaseSize(QSize(60, 60))
        self.btn_rad.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #191970;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E90FF;\n"
"}\n"
"")
        self.btn_rad.setIconSize(QSize(40, 40))

        self.layout_buttons.addWidget(self.btn_rad, 1, 1, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy2.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy2)
        self.btn_8.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #00008B;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E90FF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4169E1;\n"
"}")

        self.layout_buttons.addWidget(self.btn_8, 3, 2, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy2.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy2)
        self.btn_9.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #00008B;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E90FF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4169E1;\n"
"}")

        self.layout_buttons.addWidget(self.btn_9, 3, 3, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy2.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy2)
        self.btn_7.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #00008B;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E90FF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4169E1;\n"
"}")

        self.layout_buttons.addWidget(self.btn_7, 3, 1, 1, 1)

        self.btn_div = QPushButton(self.centralwidget)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy2.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy2)
        self.btn_div.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #191970;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E90FF;\n"
"}\n"
"")

        self.layout_buttons.addWidget(self.btn_div, 2, 4, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy2.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy2)
        self.btn_4.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #00008B;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E90FF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4169E1;\n"
"}")

        self.layout_buttons.addWidget(self.btn_4, 4, 1, 1, 1)

        self.btn_sin = QPushButton(self.centralwidget)
        self.btn_sin.setObjectName(u"btn_sin")
        sizePolicy2.setHeightForWidth(self.btn_sin.sizePolicy().hasHeightForWidth())
        self.btn_sin.setSizePolicy(sizePolicy2)
        self.btn_sin.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #191970;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E90FF;\n"
"}\n"
"")

        self.layout_buttons.addWidget(self.btn_sin, 2, 0, 1, 1)

        self.btn_sqrt = QPushButton(self.centralwidget)
        self.btn_sqrt.setObjectName(u"btn_sqrt")
        sizePolicy2.setHeightForWidth(self.btn_sqrt.sizePolicy().hasHeightForWidth())
        self.btn_sqrt.setSizePolicy(sizePolicy2)
        self.btn_sqrt.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #191970;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E90FF;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/free-icon-math-763284.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sqrt.setIcon(icon4)
        self.btn_sqrt.setIconSize(QSize(40, 35))

        self.layout_buttons.addWidget(self.btn_sqrt, 3, 0, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy2.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy2)
        self.btn_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #191970;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E90FF;\n"
"}\n"
"")

        self.layout_buttons.addWidget(self.btn_clear, 1, 3, 1, 1)

        self.btn_mul = QPushButton(self.centralwidget)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy2.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy2)
        self.btn_mul.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #191970;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E90FF;\n"
"}\n"
"")

        self.layout_buttons.addWidget(self.btn_mul, 3, 4, 1, 1)

        self.btn__grad = QPushButton(self.centralwidget)
        self.btn__grad.setObjectName(u"btn__grad")
        sizePolicy2.setHeightForWidth(self.btn__grad.sizePolicy().hasHeightForWidth())
        self.btn__grad.setSizePolicy(sizePolicy2)
        self.btn__grad.setMaximumSize(QSize(16777215, 16777215))
        self.btn__grad.setSizeIncrement(QSize(50, 50))
        self.btn__grad.setBaseSize(QSize(50, 50))
        self.btn__grad.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #191970;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E90FF;\n"
"}\n"
"")
        self.btn__grad.setIconSize(QSize(120, 40))

        self.layout_buttons.addWidget(self.btn__grad, 1, 2, 1, 1)

        self.btn_cos = QPushButton(self.centralwidget)
        self.btn_cos.setObjectName(u"btn_cos")
        sizePolicy2.setHeightForWidth(self.btn_cos.sizePolicy().hasHeightForWidth())
        self.btn_cos.setSizePolicy(sizePolicy2)
        self.btn_cos.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #191970;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E90FF;\n"
"}\n"
"")

        self.layout_buttons.addWidget(self.btn_cos, 2, 1, 1, 1)

        self.btn_tan = QPushButton(self.centralwidget)
        self.btn_tan.setObjectName(u"btn_tan")
        sizePolicy2.setHeightForWidth(self.btn_tan.sizePolicy().hasHeightForWidth())
        self.btn_tan.setSizePolicy(sizePolicy2)
        self.btn_tan.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #191970;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E90FF;\n"
"}\n"
"")

        self.layout_buttons.addWidget(self.btn_tan, 2, 2, 1, 1)

        self.btn_cot = QPushButton(self.centralwidget)
        self.btn_cot.setObjectName(u"btn_cot")
        sizePolicy2.setHeightForWidth(self.btn_cot.sizePolicy().hasHeightForWidth())
        self.btn_cot.setSizePolicy(sizePolicy2)
        self.btn_cot.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #191970;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E90FF;\n"
"}\n"
"")

        self.layout_buttons.addWidget(self.btn_cot, 2, 3, 1, 1)

        self.btn_sub = QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy2.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy2)
        self.btn_sub.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #191970;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E90FF;\n"
"}\n"
"")

        self.layout_buttons.addWidget(self.btn_sub, 4, 4, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy2.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy2)
        self.btn_6.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #00008B;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E90FF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4169E1;\n"
"}")

        self.layout_buttons.addWidget(self.btn_6, 4, 3, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy2.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy2)
        self.btn_0.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #00008B;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E90FF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4169E1;\n"
"}")

        self.layout_buttons.addWidget(self.btn_0, 6, 2, 1, 1)

        self.btn_neg = QPushButton(self.centralwidget)
        self.btn_neg.setObjectName(u"btn_neg")
        sizePolicy2.setHeightForWidth(self.btn_neg.sizePolicy().hasHeightForWidth())
        self.btn_neg.setSizePolicy(sizePolicy2)
        self.btn_neg.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #00008B;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E90FF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4169E1;\n"
"}")

        self.layout_buttons.addWidget(self.btn_neg, 6, 1, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy2.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy2)
        self.btn_3.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #00008B;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E90FF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4169E1;\n"
"}")

        self.layout_buttons.addWidget(self.btn_3, 5, 3, 1, 1)

        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy2.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy2)
        self.btn_add.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #191970;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E90FF;\n"
"}\n"
"")

        self.layout_buttons.addWidget(self.btn_add, 5, 4, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy2.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy2)
        self.btn_1.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #00008B;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E90FF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4169E1;\n"
"}")

        self.layout_buttons.addWidget(self.btn_1, 5, 1, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy2.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy2)
        self.btn_5.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #00008B;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E90FF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4169E1;\n"
"}")

        self.layout_buttons.addWidget(self.btn_5, 4, 2, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy2.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy2)
        self.btn_2.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #00008B;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E90FF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4169E1;\n"
"}")

        self.layout_buttons.addWidget(self.btn_2, 5, 2, 1, 1)

        self.btn_fact = QPushButton(self.centralwidget)
        self.btn_fact.setObjectName(u"btn_fact")
        sizePolicy2.setHeightForWidth(self.btn_fact.sizePolicy().hasHeightForWidth())
        self.btn_fact.setSizePolicy(sizePolicy2)
        self.btn_fact.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #191970;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E90FF;\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/free-icon-factorial.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fact.setIcon(icon5)
        self.btn_fact.setIconSize(QSize(30, 35))

        self.layout_buttons.addWidget(self.btn_fact, 5, 0, 1, 1)

        self.btn_ln = QPushButton(self.centralwidget)
        self.btn_ln.setObjectName(u"btn_ln")
        self.btn_ln.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.btn_ln.sizePolicy().hasHeightForWidth())
        self.btn_ln.setSizePolicy(sizePolicy2)
        self.btn_ln.setStyleSheet(u"QPushButton {\n"
"    color: #F5F5F5;\n"
"    background-color: #191970;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E90FF;\n"
"}\n"
"")

        self.layout_buttons.addWidget(self.btn_ln, 6, 0, 1, 1)


        self.verticalLayout.addLayout(self.layout_buttons)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.lbl_temp.setText("")
        self.le_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_calc.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.btn_calc.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.btn_dot.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.btn_pi.setText("")
        self.btn_step.setText("")
        self.btn_backspace.setText("")
#if QT_CONFIG(shortcut)
        self.btn_backspace.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.btn_rad.setText(QCoreApplication.translate("MainWindow", u"rad", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
#if QT_CONFIG(shortcut)
        self.btn_div.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_sin.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.btn_sqrt.setText("")
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"\u0421", None))
        self.btn_mul.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
#if QT_CONFIG(shortcut)
        self.btn_mul.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.btn__grad.setText(QCoreApplication.translate("MainWindow", u"grad", None))
        self.btn_cos.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.btn_tan.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.btn_cot.setText(QCoreApplication.translate("MainWindow", u"cot", None))
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_sub.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_neg.setText(QCoreApplication.translate("MainWindow", u"\u00b1", None))
#if QT_CONFIG(shortcut)
        self.btn_neg.setShortcut(QCoreApplication.translate("MainWindow", u"-, +", None))
#endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_add.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_fact.setText("")
        self.btn_ln.setText(QCoreApplication.translate("MainWindow", u"ln", None))
    # retranslateUi

