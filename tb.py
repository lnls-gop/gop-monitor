"""Lógica das subjanelas da Linha de Transporte LTB."""
from PyQt5 import uic, QtWidgets
import utils


class Ltbvac(QtWidgets.QWidget):
    """Controle do sistema de vácuo da LTB."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.vacltb = uic.loadUi("vacltb.ui")
        self._registrar_grupos()

    def _registrar_grupos(self):
        self.sinais_vac = {
            'TB-01:VA-SIP20-BG:Pressure-Mon': self.vacltb.ledvacltb01,
            'TB-01:VA-SIP20-ED:Pressure-Mon': self.vacltb.ledvacltb02,
            'TB-02:VA-SIP20-BG:Pressure-Mon': self.vacltb.ledvacltb03,
            'TB-02:VA-SIP20-ED:Pressure-Mon': self.vacltb.ledvacltb04,
            'TB-02:VA-SIP20-MD:Pressure-Mon': self.vacltb.ledvacltb05,
            'TB-03:VA-SIP20-ED:Pressure-Mon': self.vacltb.ledvacltb06,
            'TB-04:VA-SIP20-ED:Pressure-Mon': self.vacltb.ledvacltb07,
        }
        self.pressao_max = 1.0e-7

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_vacltb)
        self.atualizar_status()

    def mostrar_janela_vacltb(self):
        """."""
        self.vacltb.setVisible(not self.vacltb.isVisible())

    def atualizar_status(self):
        """."""
        todos_ok = True
        for signal, led in self.sinais_vac.items():
            utils.verificar_ltbvac(signal, led, self.pressao_max)
            if not getattr(led, "state", False):
                todos_ok = False
        self.estado_ok = todos_ok

        if self.botao_menu:
            cor = "rgb(0, 180, 0)" if todos_ok else "rgb(207, 0, 0)"
            self.botao_menu.setStyleSheet(f"background-color: {cor};")

        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel,
                                                  "alarmvacuo")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()


class Power_supplay(QtWidgets.QWidget):
    """Controle das fontes de potência da LTB."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.psltb = uic.loadUi("psltb.ui")
        self._registrar_grupos()

    def _registrar_grupos(self):
        self.sinais_estado_0 = {
            'TB-Fam:PS-B:DiagStatus-Mon': self.psltb.led_statusb,
            'TB-01:PS-QD1:DiagStatus-Mon': self.psltb.led_statusqd1,
            'TB-02:PS-QD2A:DiagStatus-Mon': self.psltb.led_statusqd2a,
            'TB-02:PS-QD2B:DiagStatus-Mon': self.psltb.led_statusqd2b,
            'TB-03:PS-QD3:DiagStatus-Mon': self.psltb.led_statusqd3,
            'TB-04:PS-QD4:DiagStatus-Mon': self.psltb.led_statusqd4,
            'TB-01:PS-QF1:DiagStatus-Mon': self.psltb.led_statusqf1,
            'TB-02:PS-QF2A:DiagStatus-Mon': self.psltb.led_statusqf2a,
            'TB-02:PS-QF2B:DiagStatus-Mon': self.psltb.led_statusqf2b,
            'TB-03:PS-QF3:DiagStatus-Mon': self.psltb.led_statusqf3,
            'TB-04:PS-QF4:DiagStatus-Mon': self.psltb.led_statusqf4,
            'TB-01:PS-CH-1:DiagStatus-Mon': self.psltb.led_ch1_01,
            'TB-01:PS-CH-2:DiagStatus-Mon': self.psltb.led_ch2_01,
            'TB-02:PS-CH-1:DiagStatus-Mon': self.psltb.led_ch1_02,
            'TB-02:PS-CH-2:DiagStatus-Mon': self.psltb.led_ch2_02,
            'TB-04:PS-CH-1:DiagStatus-Mon': self.psltb.led_ch1_04,
            'TB-04:PS-CH-2:DiagStatus-Mon': self.psltb.led_ch2_04,
            'TB-01:PS-CV-1:DiagStatus-Mon': self.psltb.led_cv1_01,
            'TB-01:PS-CV-2:DiagStatus-Mon': self.psltb.led_cv2_01,
            'TB-02:PS-CV-1:DiagStatus-Mon': self.psltb.led_cv1_02,
            'TB-02:PS-CV-2:DiagStatus-Mon': self.psltb.led_cv2_02,
            'TB-04:PS-CV-1:DiagStatus-Mon': self.psltb.led_cv1_04,
            'TB-04:PS-CV-2:DiagStatus-Mon': self.psltb.led_cv2_04,
        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_psltb)
        self.atualizar_status()

    def mostrar_janela_psltb(self):
        """."""
        self.psltb.setVisible(not self.psltb.isVisible())

    def atualizar_status(self):
        """."""
        todos_ok = True
        for signal, led in self.sinais_estado_0.items():
            utils.verificar_psltb(signal, led, estado_esperado=0)
            if not getattr(led, "state", False):
                todos_ok = False
        self.estado_ok = todos_ok

        if self.botao_menu:
            cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
            self.botao_menu.setStyleSheet(f"background-color: {cor}")

        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel, "alarmltb")
        if alarme_widget:
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()


class Templtb(QtWidgets.QWidget):
    """Controle do sistema de temperatura da LTB."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.templtb = uic.loadUi("templtb.ui")
        self._registrar_grupos()

    def _registrar_grupos(self):
        self.sinais_ltbtemp = {
            "t1": (
                {
                    'TB-04:VA-PT100-ED1:Temp-Mon': self.templtb.ledtemp_ltb1,
                    'TB-04:VA-PT100-ED2:Temp-Mon': self.templtb.ledtemp_ltb2,
                }, 22, 25
            ),
        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_temperatura)
        self.atualizar_status()

    def mostrar_janela_temperatura(self):
        """."""
        self.templtb.setVisible(not self.templtb.isVisible())

    def atualizar_status(self):
        """."""
        todos_verdes = True
        for _, (sinais, temp_min, temp_max) in self.sinais_ltbtemp.items():
            for signal, led in sinais.items():
                utils.verificar_templtb(signal, led, temp_min, temp_max)
                if not getattr(led, "state", False):
                    todos_verdes = False

        self.estado_ok = todos_verdes

        if self.botao_menu:
            cor = "rgb(0, 168, 0)" if todos_verdes else "rgb(207, 0, 0)"
            self.botao_menu.setStyleSheet(f"background-color: {cor};")


class Blocoltb:
    """Gerencia o grupo LTB e atualiza a label alarmltb."""

    def __init__(self, janela_opr):
        """."""
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto
        self.templtb = Templtb(janela_opr, janela_opr.btntempltb)
        self.vacltb = Ltbvac(janela_opr, janela_opr.btnvacltb)
        self.psltb = Power_supplay(janela_opr, janela_opr.btnpsltb)

        # Adiciona todas as subjanelas à lista
        self.subjanelas.extend([
            self.templtb,
            self.vacltb,
            self.psltb,
        ])

        # Configura cada subjanela
        for sub in self.subjanelas:
            sub.configurar_sistema()

    def atualizar_grupo(self):
        """Atualiza todas as subjanelas e a label alarmltb."""
        falha_detectada = False

        for sub in self.subjanelas:
            sub.atualizar_status()
            if not getattr(sub, "estado_ok", True):
                falha_detectada = True

        # Atualiza a label principal do bloco LTB
        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel, "alarmltb")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if not falha_detectada else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()
