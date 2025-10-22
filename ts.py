"""Lógica das subjanelas da Linha de Transporte LTS."""
from PyQt5 import uic, QtWidgets
import utils


class Ltsvac(QtWidgets.QWidget):
    """Controle do Sistema de Vácuo Linha de Transporte TS."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.vaclts = uic.loadUi("vaclts.ui")
        self._registrar_grupos()

    def _registrar_grupos(self):
        self.sinais_vac = {
            'TS-01:VA-CCG-BG:Pressure-Mon': self.vaclts.led_lts01bg,
            'TS-01:VA-CCG-ED:Pressure-Mon': self.vaclts.led_lts01ed,
            'TS-04:VA-CCG-BG:Pressure-Mon': self.vaclts.led_lts04bg,
            'TS-04:VA-CCG-MD:Pressure-Mon': self.vaclts.led_lts04md,
            'TS-01:VA-SIP20-BG:Pressure-Mon': self.vaclts.led_lts01sip20bg,
            'TS-01:VA-SIP20-ED:Pressure-Mon': self.vaclts.led_lts01sip20ed,
            'TS-01:VA-SIP20-MD1:Pressure-Mon': self.vaclts.led_lts01sip20md1,
            'TS-01:VA-SIP20-MD2:Pressure-Mon': self.vaclts.led_lts01sip20md2,
            'TS-02:VA-SIP20-BG:Pressure-Mon': self.vaclts.led_lts02sip20bg,
            'TS-02:VA-SIP20-ED:Pressure-Mon': self.vaclts.led_lts02sip20ed,
            'TS-03:VA-SIP20-BG:Pressure-Mon': self.vaclts.led_lts03sip20bg,
            'TS-03:VA-SIP20-ED:Pressure-Mon': self.vaclts.led_lts03sip20ed,
            'TS-04:VA-SIP20-BG:Pressure-Mon': self.vaclts.led_lts04sip20bg,
            'TS-04:VA-SIP20-ED:Pressure-Mon': self.vaclts.led_lts04sip20ed,
            'TS-04:VA-SIP20-MD1:Pressure-Mon': self.vaclts.led_lts04sip20md1,
            'TS-04:VA-SIP20-MD2:Pressure-Mon': self.vaclts.led_lts04sip20md2,
            'TS-04:VA-SIP20-MD3:Pressure-Mon': self.vaclts.led_lts04sip20md3,
        }
        self.pressao_max = 1.0e-7

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_vaclts)
        self.atualizar_status()

    def mostrar_janela_vaclts(self):
        """."""
        self.vaclts.setVisible(not self.vaclts.isVisible())

    def atualizar_status(self):
        """."""
        todos_ok = True
        for signal, led in self.sinais_vac.items():
            utils.verificar_vaclts(signal, led, self.pressao_max)
            if not getattr(led, "state", False):
                todos_ok = False
        self.estado_ok = todos_ok

        if self.botao_menu:
            cor = "rgb(0, 180, 0)" if todos_ok else "rgb(207, 0, 0)"
            self.botao_menu.setStyleSheet(f"background-color: {cor};")

        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel,
                                                  "alarmlts")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()


class Templts(QtWidgets.QWidget):
    """Controle de Temperatura da Linha de Transporte TS ."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.templts = uic.loadUi("templts.ui")
        self._registrar_grupos()

    def _registrar_grupos(self):
        self.sinais_ltbtemp = {
            "t1": (
                {
                    'TS-01:VA-PT100-BG1:Temp-Mon': self.templts.led_ltsbg1,
                    'TS-01:VA-PT100-BG2:Temp-Mon': self.templts.led_ltsbg2,
                    'TS-01:VA-PT100-BG3:Temp-Mon': self.templts.led_ltsbg3,
                    'TS-01:VA-PT100-BG4:Temp-Mon': self.templts.led_ltsbg4,
                    'TS-01:PU-EjeSF-BG:Temp-Mon': self.templts.led_ejesfbg,
                    'TS-01:PU-EjeSG-BG:Temp-Mon': self.templts.led_ejesgbg,
                    'TS-01:PU-EjeSF-ED:Temp-Mon': self.templts.led_ejesfed,
                    'TS-01:PU-EjeSG-ED:Temp-Mon': self.templts.led_ejesged,
                    'TS-04:VA-PT100-ED1:Temp-Mon': self.templts.led_ltsed1,
                    'TS-04:VA-PT100-ED2:Temp-Mon': self.templts.led_ltsed2,
                    'TS-04:VA-PT100-ED3:Temp-Mon': self.templts.led_ltsed3,
                    'TS-04:VA-PT100-ED4:Temp-Mon': self.templts.led_ltsed4,
                    'TS-04:VA-PT100-ED5:Temp-Mon': self.templts.led_ltsed5,
                    'TS-04:VA-PT100-ED6:Temp-Mon': self.templts.led_ltsed6,
                    'TS-MBTemp-03-CH1': self.templts.led_ltsch1,
                    'TS-MBTemp-03-CH2': self.templts.led_ltsch2,
                    'TS-MBTemp-03-CH3': self.templts.led_ltsch3,
                    'TS-MBTemp-03-CH4': self.templts.led_ltsch4,
                },
                22, 26
            ),
        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_temperatura)
        self.atualizar_status()

    def mostrar_janela_temperatura(self):
        """."""
        self.templts.setVisible(not self.templts.isVisible())

    def atualizar_status(self):
        """."""
        todos_verdes = True
        for _, (sinais, temp_min, temp_max) in self.sinais_ltbtemp.items():
            for signal, led in sinais.items():
                utils.verificar_templts(signal, led, temp_min, temp_max)
                if not getattr(led, "state", False):
                    todos_verdes = False

        self.estado_ok = todos_verdes

        if self.botao_menu:
            cor = "rgb(0, 168, 0)" if todos_verdes else "rgb(207, 0, 0)"
            self.botao_menu.setStyleSheet(f"background-color: {cor};")


class Ltsps(QtWidgets.QWidget):
    """Controle das fontes de potencia LTS."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.pslts = uic.loadUi("pslts.ui")
        self._registrar_grupos()

    def _registrar_grupos(self):
        self.sinais_estado_0 = {
            'TS-Fam:PS-B:DiagStatus-Mon': self.pslts.led_ltsb,
            'TS-01:PS-QF1A:DiagStatus-Mon': self.pslts.led_tsqf1a,
            'TS-01:PS-QF1B:DiagStatus-Mon': self.pslts.led_tsqf1b,
            'TS-02:PS-QD2:DiagStatus-Mon': self.pslts.led_tsqd2,
            'TS-02:PS-QF2:DiagStatus-Mon': self.pslts.led_tsqf2,
            'TS-03:PS-QF3:DiagStatus-Mon': self.pslts.led_tsqf3,
            'TS-04:PS-QD4A:DiagStatus-Mon': self.pslts.led_tsqd4a,
            'TS-04:PS-QD4B:DiagStatus-Mon': self.pslts.led_tsqd4b,
            'TS-04:PS-QF4:DiagStatus-Mon': self.pslts.led_tsqf4,
            'TS-01:PS-CH:DiagStatus-Mon': self.pslts.led_lts01ch,
            'TS-02:PS-CH:DiagStatus-Mon': self.pslts.led_lts02ch,
            'TS-03:PS-CH:DiagStatus-Mon': self.pslts.led_lts03ch,
            'TS-04:PS-CH:DiagStatus-Mon': self.pslts.led_lts04ch,
            'TS-01:PS-CV-1:DiagStatus-Mon': self.pslts.led_lts01cv1,
            'TS-01:PS-CV-1E2:DiagStatus-Mon': self.pslts.led_lts01cv1e2,
            'TS-01:PS-CV-2:DiagStatus-Mon': self.pslts.led_lts01cv2,
            'TS-02:PS-CV:DiagStatus-Mon': self.pslts.led_lts02cv,
            'TS-02:PS-CV-0:DiagStatus-Mon': self.pslts.led_lts02cv0,
            'TS-03:PS-CV:DiagStatus-Mon': self.pslts.led_lts03cv,
            'TS-04:PS-CV-0:DiagStatus-Mon': self.pslts.led_lts04cv0,
            'TS-04:PS-CV-1:DiagStatus-Mon': self.pslts.led_lts04cv1,
            'TS-04:PS-CV-1E2:DiagStatus-Mon': self.pslts.led_lts04cv2,
            'TS-04:PS-CV-2:DiagStatus-Mon': self.pslts.led_lts04cv1e2,
            'SI-01M1:PS-FFCV:DiagStatus-Mon': self.pslts.led_lts01ffcv,
            'SI-01M2:PS-FFCH:DiagStatus-Mon': self.pslts.led_lts01ffch,
            'SI-01M2:PS-FFCV:DiagStatus-Mon': self.pslts.led_lts02ffcv,
            'SI-01M1:PS-FFCH:DiagStatus-Mon': self.pslts.led_lts02ffch,
        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_pslts)
        self.atualizar_status()

    def mostrar_janela_pslts(self):
        """."""
        self.pslts.setVisible(not self.pslts.isVisible())

    def atualizar_status(self):
        """."""
        todos_ok = True
        for signal, led in self.sinais_estado_0.items():
            utils.verificar_pslts(signal, led, estado_esperado=0)
            if not getattr(led, "state", False):
                todos_ok = False
        self.estado_ok = todos_ok

        if self.botao_menu:
            cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
            self.botao_menu.setStyleSheet(f"background-color: {cor}")

        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel, "alarmlts")
        if alarme_widget:
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()


class Blocolts:
    """Gerencia o grupo LTB e atualiza a label alarmltb."""

    def __init__(self, janela_opr):
        """."""
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto
        self.vaclts = Ltsvac(janela_opr, janela_opr.btnvaclts)
        self.templts = Templts(janela_opr, janela_opr.btntemplts)
        self.pslts = Ltsps(janela_opr, janela_opr.btnpslts)

        # Adiciona todas as subjanelas à lista
        self.subjanelas.extend([
            self.vaclts,
            self.templts,
            self.pslts,
        ])

        # Configura cada subjanela
        for sub in self.subjanelas:
            sub.configurar_sistema()

    def atualizar_grupo(self):
        """Atualiza todas as subjanelas e a label alarmlts."""
        falha_detectada = False

        for sub in self.subjanelas:
            sub.atualizar_status()
            if not getattr(sub, "estado_ok", True):
                falha_detectada = True

        # Atualiza a label principal do bloco LTS
        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel, "alarmlts")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if not falha_detectada else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()
