"""Logica das subjanelas do Booster."""
from PyQt5 import uic, QtWidgets
import utils


class Bops(QtWidgets.QWidget):
    """Controle das fontes de potencia do Booster."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.psbo = uic.loadUi("ui/psbo.ui")
        self._registrar_grupos()

    def _registrar_grupos(self):
        self.sinais_estado_0 = {
            # 'BO-Fam:PS-B-1:DiagStatus-Mon': self.psbo.led_bob1,
            'BO-Fam:PS-B-2:DiagStatus-Mon': self. psbo.led_bob2,
            'BO-Fam:PS-QF:DiagStatus-Mon': self.psbo.led_boqf,
            'BO-Fam:PS-QD:DiagStatus-Mon': self.psbo.led_boqd,
            'BO-02D:PS-QS:DiagStatus-Mon': self.psbo.led_boqs,
            # 'BO-Fam:PS-SD:DiagStatus-Mon': self.psbo.led_bosd,
            'BO-Fam:PS-SF:DiagStatus-Mon': self.psbo.led_bosf,
            'BO-01U:PS-CH:DiagStatus-Mon': self.psbo.led_ch01,
            'BO-03U:PS-CH:DiagStatus-Mon': self.psbo.led_ch03,
            'BO-05U:PS-CH:DiagStatus-Mon': self.psbo.led_ch05,
            'BO-07U:PS-CH:DiagStatus-Mon': self.psbo.led_ch07,
            'BO-09U:PS-CH:DiagStatus-Mon': self.psbo.led_ch09,
            'BO-11U:PS-CH:DiagStatus-Mon': self.psbo.led_ch11,
            'BO-13U:PS-CH:DiagStatus-Mon': self.psbo.led_ch13,
            'BO-15U:PS-CH:DiagStatus-Mon': self.psbo.led_ch15,
            'BO-17U:PS-CH:DiagStatus-Mon': self.psbo.led_ch17,
            'BO-19U:PS-CH:DiagStatus-Mon': self.psbo.led_ch19,
            'BO-21U:PS-CH:DiagStatus-Mon': self.psbo.led_ch21,
            'BO-23U:PS-CH:DiagStatus-Mon': self.psbo.led_ch23,
            'BO-25U:PS-CH:DiagStatus-Mon': self.psbo.led_ch25,
            'BO-27U:PS-CH:DiagStatus-Mon': self.psbo.led_ch27,
            'BO-29U:PS-CH:DiagStatus-Mon': self.psbo.led_ch29,
            'BO-31U:PS-CH:DiagStatus-Mon': self.psbo.led_ch31,
            'BO-33U:PS-CH:DiagStatus-Mon': self.psbo.led_ch33,
            'BO-35U:PS-CH:DiagStatus-Mon': self.psbo.led_ch35,
            'BO-37U:PS-CH:DiagStatus-Mon': self.psbo.led_ch37,
            'BO-39U:PS-CH:DiagStatus-Mon': self.psbo.led_ch39,
            'BO-41U:PS-CH:DiagStatus-Mon': self.psbo.led_ch41,
            'BO-43U:PS-CH:DiagStatus-Mon': self.psbo.led_ch43,
            'BO-45U:PS-CH:DiagStatus-Mon': self.psbo.led_ch45,
            'BO-47U:PS-CH:DiagStatus-Mon': self.psbo.led_ch47,
            'BO-49D:PS-CH:DiagStatus-Mon': self.psbo.led_ch49,
            'BO-01U:PS-CV:DiagStatus-Mon': self.psbo.led_cv01,
            'BO-03U:PS-CV:DiagStatus-Mon': self.psbo.led_cv03,
            'BO-05U:PS-CV:DiagStatus-Mon': self.psbo.led_cv05,
            'BO-07U:PS-CV:DiagStatus-Mon': self.psbo.led_cv07,
            'BO-09U:PS-CV:DiagStatus-Mon': self.psbo.led_cv09,
            'BO-11U:PS-CV:DiagStatus-Mon': self.psbo.led_cv11,
            'BO-13U:PS-CV:DiagStatus-Mon': self.psbo.led_cv13,
            'BO-15U:PS-CV:DiagStatus-Mon': self.psbo.led_cv15,
            'BO-17U:PS-CV:DiagStatus-Mon': self.psbo.led_cv17,
            'BO-19U:PS-CV:DiagStatus-Mon': self.psbo.led_cv19,
            'BO-21U:PS-CV:DiagStatus-Mon': self.psbo.led_cv21,
            'BO-23U:PS-CV:DiagStatus-Mon': self.psbo.led_cv23,
            'BO-25U:PS-CV:DiagStatus-Mon': self.psbo.led_cv25,
            'BO-27U:PS-CV:DiagStatus-Mon': self.psbo.led_cv27,
            'BO-29U:PS-CV:DiagStatus-Mon': self.psbo.led_cv29,
            'BO-31U:PS-CV:DiagStatus-Mon': self.psbo.led_cv31,
            'BO-33U:PS-CV:DiagStatus-Mon': self.psbo.led_cv33,
            'BO-35U:PS-CV:DiagStatus-Mon': self.psbo.led_cv35,
            'BO-37U:PS-CV:DiagStatus-Mon': self.psbo.led_cv37,
            'BO-39U:PS-CV:DiagStatus-Mon': self.psbo.led_cv39,
            'BO-41U:PS-CV:DiagStatus-Mon': self.psbo.led_cv41,
            'BO-43U:PS-CV:DiagStatus-Mon': self.psbo.led_cv43,
            'BO-45U:PS-CV:DiagStatus-Mon': self.psbo.led_cv45,
            'BO-47U:PS-CV:DiagStatus-Mon': self.psbo.led_cv47,
            'BO-49U:PS-CV:DiagStatus-Mon': self.psbo.led_cv49,
        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_psbo)
        self.atualizar_status()

    def mostrar_janela_psbo(self):
        """."""
        self.psbo.setVisible(not self.psbo.isVisible())

    def atualizar_status(self):
        """."""
        todos_ok = True
        for signal, led in self.sinais_estado_0.items():
            utils.verificar_psbo(signal, led, estado_esperado=0)
            if not getattr(led, "state", False):
                todos_ok = False
        self.estado_ok = todos_ok

        if self.botao_menu:
            cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
            self.botao_menu.setStyleSheet(f"background-color: {cor}")

        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel, "alarmbo")
        if alarme_widget:
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()


class Botemp(QtWidgets.QWidget):
    """Controle de temperatura dos subsistemas do Booster."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.tempbo = uic.loadUi("ui/tempbo.ui")
        self._registar_grupos()

    def _registar_grupos(self):
        self.sinais_tempbo = {
            "t1": (
                {
                    'BO-01U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam1,
                    'BO-01U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam2,
                    'BO-01U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam3,
                    'BO-02U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam4,
                    'BO-02U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam5,
                    'BO-02U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam6,
                    # 'BO-03U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam7,
                    # 'BO-03U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam8,
                    # 'BO-03U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam9,
                    'BO-04U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam10,
                    'BO-04U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam11,
                    'BO-04U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam12,
                    'BO-05U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam13,
                    'BO-05U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam14,
                    'BO-05U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam15,
                    'BO-06U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam16,
                    'BO-06U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam17,
                    'BO-06U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam18,
                    'BO-07U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam19,
                    'BO-07U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam20,
                    'BO-07U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam21,
                    'BO-08U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam22,
                    'BO-08U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam23,
                    'BO-08U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam24,
                    'BO-09U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam25,
                    'BO-09U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam26,
                    'BO-09U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam27,
                    'BO-10U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam28,
                    'BO-10U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam29,
                    'BO-10U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam30,
                    'BO-11U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam31,
                    'BO-11U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam32,
                    'BO-11U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam33,
                    'BO-12U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam34,
                    'BO-12U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam35,
                    'BO-12U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam36,
                    'BO-13U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam37,
                    'BO-13U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam38,
                    'BO-13U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam39,
                    'BO-14U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam40,
                    'BO-14U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam41,
                    'BO-14U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam42,
                    'BO-15U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam43,
                    'BO-15U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam44,
                    'BO-15U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam45,
                    'BO-16U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam46,
                    'BO-16U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam47,
                    'BO-16U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam48,
                    'BO-17U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam49,
                    'BO-17U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam50,
                    'BO-17U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam51,
                    'BO-18U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam52,
                    'BO-18U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam53,
                    'BO-18U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam54,
                    'BO-19U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam55,
                    'BO-19U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam56,
                    'BO-19U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam57,
                    'BO-20U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam58,
                    'BO-20U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam59,
                    'BO-20U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam60,
                    'BO-21U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam61,
                    'BO-21U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam62,
                    'BO-21U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam63,
                    'BO-22U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam64,
                    'BO-22U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam65,
                    'BO-22U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam66,
                    'BO-23U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam67,
                    'BO-23U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam68,
                    'BO-23U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam69,
                    'BO-24U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam70,
                    'BO-24U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam71,
                    'BO-24U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam72,
                    'BO-25U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam73,
                    'BO-25U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam74,
                    'BO-25U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam75,
                    'BO-26U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam76,
                    'BO-26U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam77,
                    'BO-26U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam78,
                    'BO-27U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam79,
                    'BO-27U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam80,
                    'BO-27U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam81,
                    'BO-28U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam82,
                    'BO-28U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam83,
                    'BO-28U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam84,
                    'BO-29U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam85,
                    'BO-29U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam86,
                    'BO-29U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam87,
                    'BO-30U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam88,
                    'BO-30U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam89,
                    'BO-30U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam90,
                    'BO-31U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam91,
                    'BO-31U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam92,
                    'BO-31U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam93,
                    'BO-32U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam94,
                    'BO-32U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam95,
                    'BO-32U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam96,
                    'BO-33U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam97,
                    'BO-33U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam98,
                    'BO-33U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam99,
                    'BO-34U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam100,
                    'BO-34U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam101,
                    'BO-34U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam102,
                    'BO-35U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam103,
                    'BO-35U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam104,
                    'BO-35U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam105,
                    'BO-36U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam106,
                    'BO-36U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam107,
                    'BO-36U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam108,
                    'BO-37U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam109,
                    'BO-37U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam110,
                    'BO-37U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam111,
                    'BO-38U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam112,
                    'BO-38U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam113,
                    'BO-38U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam114,
                    'BO-39U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam115,
                    'BO-39U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam116,
                    'BO-39U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam117,
                    'BO-40U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam118,
                    'BO-40U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam119,
                    'BO-40U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam120,
                    'BO-41U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam121,
                    'BO-41U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam122,
                    'BO-41U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam123,
                    'BO-42U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam124,
                    'BO-42U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam125,
                    'BO-42U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam126,
                    'BO-43U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam127,
                    'BO-43U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam128,
                    'BO-43U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam129,
                    'BO-44U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam130,
                    'BO-44U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam131,
                    'BO-44U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam132,
                    'BO-45U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam133,
                    'BO-45U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam134,
                    'BO-45U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam135,
                    'BO-46U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam136,
                    'BO-46U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam137,
                    'BO-46U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam138,
                    'BO-47U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam139,
                    'BO-47U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam140,
                    'BO-47U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam141,
                    'BO-48U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam142,
                    'BO-48U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam143,
                    'BO-48U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam144,
                    'BO-49U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam145,
                    # 'BO-49U:VA-PT100-ED:Temp-Mon': self.tempbo.
                    # led_tempcam146,
                    'BO-49U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam147,
                    'BO-50U:VA-PT100-BG:Temp-Mon': self.tempbo.led_tempcam148,
                    'BO-50U:VA-PT100-ED:Temp-Mon': self.tempbo.led_tempcam149,
                    'BO-50U:VA-PT100-MD:Temp-Mon': self.tempbo.led_tempcam150,
                },
                18, 26
            ),
        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_tempbo)
        self.atualizar_status()

    def mostrar_janela_tempbo(self):
        """."""
        self.tempbo.setVisible(not self.isVisible())

    def atualizar_status(self):
        """."""
        todos_verdes = True
        for _, (sinais, temp_min, temp_max) in self.sinais_tempbo.items():
            for signal, led in sinais.items():
                utils.verificar_templts(signal, led, temp_min, temp_max)
                if not getattr(led, "state", False):
                    todos_verdes = False

            self.estado_ok = todos_verdes

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_verdes else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")


class Bovac(QtWidgets.QWidget):
    """Controle do Sistema de Vácuo do Booster."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.vacbo = uic.loadUi("ui/vacbo.ui")
        self._registrar_grupos()

    def _registrar_grupos(self):
        self.sinais_vac = {
            'BO-01U:VA-CCG-BG:Pressure-Mon': self.vacbo.led_ccg01,
            'BO-04U:VA-CCG-BG:Pressure-Mon': self.vacbo.led_ccg04,
            'BO-05D:VA-CCG-RFC:Pressure-Mon': self.vacbo.led_ccg05,
            'BO-06U:VA-CCG-ED:Pressure-Mon': self.vacbo.led_ccg06,
            'BO-09U:VA-CCG-BG:Pressure-Mon': self.vacbo.led_ccg09,
            'BO-11U:VA-CCG-ED:Pressure-Mon': self.vacbo.led_ccg11,
            'BO-14U:VA-CCG-BG:Pressure-Mon': self.vacbo.led_ccg14,
            'BO-16U:VA-CCG-ED:Pressure-Mon': self.vacbo.led_ccg16,
            'BO-19U:VA-CCG-BG:Pressure-Mon': self.vacbo.led_ccg19,
            'BO-21U:VA-CCG-ED:Pressure-Mon': self.vacbo.led_ccg21,
            'BO-24U:VA-CCG-BG:Pressure-Mon': self.vacbo.led_ccg24,
            'BO-26U:VA-CCG-ED:Pressure-Mon': self.vacbo.led_ccg26,
            'BO-29U:VA-CCG-BG:Pressure-Mon': self.vacbo.led_ccg29,
            'BO-31U:VA-CCG-ED:Pressure-Mon': self.vacbo.led_ccg31,
            'BO-34U:VA-CCG-BG:Pressure-Mon': self.vacbo.led_ccg34,
            'BO-36U:VA-CCG-ED:Pressure-Mon': self.vacbo.led_ccg36,
            'BO-39U:VA-CCG-BG:Pressure-Mon': self.vacbo.led_ccg39,
            'BO-41U:VA-CCG-ED:Pressure-Mon': self.vacbo.led_ccg41,
            'BO-44U:VA-CCG-BG:Pressure-Mon': self.vacbo.led_ccg44,
            'BO-46U:VA-CCG-ED:Pressure-Mon': self.vacbo.led_ccg46,
            'BO-47U:VA-CCG-ED:Pressure-Mon': self.vacbo.led_ccg47,
            'BO-01U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_1,
            'BO-02U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_2,
            'BO-03U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_3,
            'BO-04U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_4,
            'BO-05U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_5,
            'BO-06U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_6,
            'BO-07U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_7,
            'BO-08U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_8,
            'BO-09U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_9,
            'BO-10U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_10,
            'BO-11U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_11,
            'BO-12U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_12,
            'BO-01D:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_51,
            'BO-13U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_13,
            'BO-14U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_14,
            'BO-15U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_15,
            'BO-16U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_16,
            'BO-17U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_17,
            'BO-18U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_18,
            'BO-19U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_19,
            'BO-20U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_20,
            'BO-21U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_21,
            'BO-22U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_22,
            'BO-23U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_23,
            'BO-24U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_24,
            'BO-25U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_25,
            'BO-26U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_26,
            'BO-27U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_27,
            'BO-28U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_28,
            'BO-29U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_29,
            'BO-30U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_30,
            'BO-31U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_31,
            'BO-32U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_32,
            'BO-33U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_33,
            'BO-34U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_34,
            'BO-35U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_35,
            'BO-36U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_36,
            'BO-37U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_37,
            'BO-38U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_38,
            'BO-39U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_39,
            'BO-40U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_40,
            'BO-41U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_41,
            'BO-42U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_42,
            'BO-43U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_43,
            'BO-44U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_44,
            'BO-45U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_45,
            'BO-46U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_46,
            'BO-47U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_47,
            'BO-48U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_48,
            'BO-49U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_49,
            'BO-50U:VA-SIP20-BG:Pressure-Mon': self.vacbo.led_sip20_50,
        }
        self.pressao_max = 1.0e-7

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_vacbo)
        self.atualizar_status()

    def mostrar_janela_vacbo(self):
        """."""
        self.vacbo.setVisible(not self.vacbo.isVisible())

    def atualizar_status(self):
        """."""
        todos_ok = True
        for signal, led in self.sinais_vac.items():
            utils.verificar_vacbo(signal, led, self.pressao_max)
            if not getattr(led, "state", False):
                todos_ok = False
        self.estado_ok = todos_ok

        if self.botao_menu:
            cor = "rgb(0, 180, 0)" if todos_ok else "rgb(207, 0, 0)"
            self.botao_menu.setStyleSheet(f"background-color: {cor};")

        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel,
                                                  "alarmbo")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()


class Bocavity(QtWidgets.QWidget):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.bocavity = uic.loadUi("ui/bocavity.ui")
        self._registrar_grupos()

    def _registrar_grupos(self):
        """."""
        self.sinais_temperatura = {
            "t1_Cylin": (
                {
                    'BO-05D:RF-P5Cav:Cylin1T-Mon': self.bocavity.led_cylin1,
                    'BO-05D:RF-P5Cav:Cylin2T-Mon': self.bocavity.led_cylin2,
                    'BO-05D:RF-P5Cav:Cylin3T-Mon': self.bocavity.led_cylin3,
                    'BO-05D:RF-P5Cav:Cylin4T-Mon': self.bocavity.led_cylin4,
                    'BO-05D:RF-P5Cav:Cylin5T-Mon': self.bocavity.led_cylin5,
                }, 27, 29
            ),

            "t2_Circulator": (
                {
                    # 'RA-TLBO:RF-Circulator:TinUp-Mon': self.bocavity.
                    # led_circulator1,
                    'RA-TLBO:RF-Circulator:Tin-Mon': self.bocavity.
                    led_circulator2,
                    'RA-TLBO:RF-Circulator:Tout-Mon': self.bocavity.
                    led_circulator3,
                }, 20, 22
            ),

            "t3_TorreAmp": (
                {
                    'RA-ToBO:RF-HeatSink-H01:T-Mon': self.bocavity.
                    led_tempamp1,
                    'RA-ToBO:RF-HeatSink-H02:T-Mon': self.bocavity.
                    led_tempamp2,
                    'RA-ToBO:RF-HeatSink-H03:T-Mon': self.bocavity.
                    led_tempamp3,
                    'RA-ToBO:RF-HeatSink-H04:T-Mon': self.bocavity.
                    led_tempamp4,
                    'RA-ToBO:RF-HeatSink-H05:T-Mon': self.bocavity.
                    led_tempamp5,
                }, 20, 23.5
            ),
        }

    def configurar_sistema(self):
        """Conecta sinais da janela principal e prepara a subjanela."""
        # Botão/ação que mostra/oculta a janela de temperatura
        self.botao_menu.clicked.connect(self.mostrar_janela_temperatura)
        # Primeira atualização inicial
        self.atualizar_status()

    def mostrar_janela_temperatura(self):
        """Exibe/oculta a interface gráfica da temperatura LINAC."""
        self.bocavity.setVisible(not self.bocavity.isVisible())

    def atualizar_status(self):
        """Atualiza LEDs da subjanela e define estado_ok."""
        todos_verdes = True
        for _, (sinais, temp_min, temp_max) in self.sinais_temperatura.items():
            for signal, led in sinais.items():
                utils.verificar_bocavity(signal, led, temp_min, temp_max)
                if not getattr(led, "state", False):
                    todos_verdes = False

        self.estado_ok = todos_verdes
        # Atualiza cor do botão na aba LINAC
        if self.botao_menu:
            cor = "rgb(0, 168, 0)" if todos_verdes else "rgb(207, 0, 0)"
            self.botao_menu.setStyleSheet(f"background-color: {cor};")


class Blocobo:
    """Gerencia o grupo LTB e atualiza a label alarmltb."""

    def __init__(self, janela_opr):
        """."""
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto
        self.vacbo = Bovac(janela_opr, janela_opr.btnvacbo)
        self.tempbo = Botemp(janela_opr, janela_opr.btntempbo)
        self.psbo = Bops(janela_opr, janela_opr.btnpsbo)
        self.bocavity = Bocavity(janela_opr, janela_opr.btnbocavity)

        # Adiciona todas as subjanelas à lista
        self.subjanelas.extend([
            self.vacbo,
            self.tempbo,
            self.psbo,
            self.bocavity,
        ])

        # Configura cada subjanela
        for sub in self.subjanelas:
            sub.configurar_sistema()

    def atualizar_grupo(self):
        """Atualiza todas as subjanelas e a label alarmbo."""
        falha_detectada = False

        for sub in self.subjanelas:
            sub.atualizar_status()
            if not getattr(sub, "estado_ok", True):
                falha_detectada = True

        # Atualiza a label principal do bloco LTS
        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel, "alarmbo")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if not falha_detectada else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()
