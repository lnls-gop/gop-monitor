"""Lógica das subjanelas da Linha de Transporte LTB."""
import epics
from PyQt5 import uic, QtWidgets
import utils


class ConnWidgetPVs(QtWidgets.QWidget):
    """."""

    def __init__(self, janela_opr, botao_menu, ui_fname, check_type):
        """."""
        super().__init__()
        self.pvs = None
        self.check_type = check_type
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.uiobj = uic.loadUi(ui_fname)
        self.sinais = None
        self._registrar_grupos()
        self._connect_pvs()

    def disconnected_pvnames(self):
        """."""
        dpvns = list()
        for pvname, pv in self.pvs.items():
            if not pv.connected:
                dpvns.append(pvname)
        return dpvns

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        raise NotImplemented

    def _connect_pvs(self):
        self.pvs = dict()
        for pvname, _ in self.sinais.items():
            self.pvs[pvname] = epics.PV(pvname, connection_timeout=None)

    def configurar_sistema(self):
        """Conecta sinais da janela principal e prepara a subjanela."""
        # Botão/ação que mostra/oculta a janela de temperatura
        self.botao_menu.clicked.connect(self.mostrar_janela)
        # Primeira atualização inicial
        self.atualizar_status()

    def mostrar_janela(self):
        """Exibe/oculta a interface gráfica."""
        self.uiobj.setVisible(not self.uiobj.isVisible())

    def atualizar_status(self):
        """Atualiza LEDs da subjanela e define estado_ok."""
        if self.check_type == 'temp':

            todos_ok = True

            for pvname, value in self.sinais.items():
                led, temp_min, temp_max = value
                utils.verificar_temp(pvname, led, temp_min, temp_max)
                if not getattr(led, "state", False):
                    todos_ok = False

            self.estado_ok = todos_ok

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")

            # Atualiza a label de alarme do bloco LOWLEVEL
            alarme_widget = self.janela_opr.findChild(
                QtWidgets.QLabel, "alarmtempltb")

        elif self.check_type == 'vacuo':

            todos_ok = True

            for pvname, value in self.sinais.items():
                led, pressao_min = value
                utils.verificar_ltbvac(
                    pvname, led, pressao_min=pressao_min)
                if not getattr(led, "state", False):
                    todos_ok = False
            self.estado_ok = todos_ok

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")

            # Atualiza label de alarme da subjanela
            alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel,
                                                      "alarmvacuo")

        elif self.check_type == 'psltb':

            todos_ok = True

            for pvname, value in self.sinais.items():
                led, estado_esperado = value
                utils.verificar_psltb(
                    pvname, led, estado_esperado=estado_esperado)
                if not getattr(led, "state", False):
                    todos_ok = False

            self.estado_ok = todos_ok

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")

            # Atualiza a label de alarme do bloco LOWLEVEL
            alarme_widget = self.janela_opr.findChild(
                QtWidgets.QLabel, "alarmpsltb")

            if alarme_widget:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                alarme_widget.setStyleSheet(f"background-color: {cor};")
                alarme_widget.repaint()
                QtWidgets.QApplication.processEvents()
                alarme_widget.update()


class Ltbvac(ConnWidgetPVs):
    """Controle da subjanela de leitura de vácuo do Linac."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/vacltb.ui", "vacuo")

    def _registrar_grupos(self):
        """Registra Pvs de vacuo e seus leds correspondentes."""
        self.sinais = {
            'TB-01:VA-SIP20-BG:Pressure-Mon': (self.uiobj.ledvacltb01, 1.0e-7),
            'TB-01:VA-SIP20-ED:Pressure-Mon': (self.uiobj.ledvacltb02, 1.0e-7),
            'TB-02:VA-SIP20-BG:Pressure-Mon': (self.uiobj.ledvacltb03, 1.0e-7),
            'TB-02:VA-SIP20-ED:Pressure-Mon': (self.uiobj.ledvacltb04, 1.0e-7),
            'TB-02:VA-SIP20-MD:Pressure-Mon': (self.uiobj.ledvacltb05, 1.0e-7),
            'TB-03:VA-SIP20-ED:Pressure-Mon': (self.uiobj.ledvacltb06, 1.0e-7),
            'TB-04:VA-SIP20-ED:Pressure-Mon': (self.uiobj.ledvacltb07, 1.0e-7),
        }


class Power_supply(ConnWidgetPVs):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/psltb.ui", "psltb")

    def _registrar_grupos(self):
        self.sinais = {
            'TB-Fam:PS-B:DiagStatus-Mon': (self.uiobj.led_statusb, 0),
            'TB-01:PS-QD1:DiagStatus-Mon': (self.uiobj.led_statusqd1, 0),
            'TB-02:PS-QD2A:DiagStatus-Mon': (self.uiobj.led_statusqd2a, 0),
            'TB-02:PS-QD2B:DiagStatus-Mon': (self.uiobj.led_statusqd2b, 0),
            'TB-03:PS-QD3:DiagStatus-Mon': (self.uiobj.led_statusqd3, 0),
            'TB-04:PS-QD4:DiagStatus-Mon': (self.uiobj.led_statusqd4, 0),
            'TB-01:PS-QF1:DiagStatus-Mon': (self.uiobj.led_statusqf1, 0),
            'TB-02:PS-QF2A:DiagStatus-Mon': (self.uiobj.led_statusqf2a, 0),
            'TB-02:PS-QF2B:DiagStatus-Mon': (self.uiobj.led_statusqf2b, 0),
            'TB-03:PS-QF3:DiagStatus-Mon': (self.uiobj.led_statusqf3, 0),
            'TB-04:PS-QF4:DiagStatus-Mon': (self.uiobj.led_statusqf4, 0),
            'TB-01:PS-CH-1:DiagStatus-Mon': (self.uiobj.led_ch1_01, 0),
            'TB-01:PS-CH-2:DiagStatus-Mon': (self.uiobj.led_ch2_01, 0),
            'TB-02:PS-CH-1:DiagStatus-Mon': (self.uiobj.led_ch1_02, 0),
            'TB-02:PS-CH-2:DiagStatus-Mon': (self.uiobj.led_ch2_02, 0),
            'TB-04:PS-CH-1:DiagStatus-Mon': (self.uiobj.led_ch1_04, 0),
            'TB-04:PS-CH-2:DiagStatus-Mon': (self.uiobj.led_ch2_04, 0),
            'TB-01:PS-CV-1:DiagStatus-Mon': (self.uiobj.led_cv1_01, 0),
            'TB-01:PS-CV-2:DiagStatus-Mon': (self.uiobj.led_cv2_01, 0),
            'TB-02:PS-CV-1:DiagStatus-Mon': (self.uiobj.led_cv1_02, 0),
            'TB-02:PS-CV-2:DiagStatus-Mon': (self.uiobj.led_cv2_02, 0),
            'TB-04:PS-CV-1:DiagStatus-Mon': (self.uiobj.led_cv1_04, 0),
            'TB-04:PS-CV-2:DiagStatus-Mon': (self.uiobj.led_cv2_04, 0),
        }


class Templtb(ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura LINAC."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/templtb.ui", "temp")

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        self.sinais = {
            'TB-04:VA-PT100-ED1:Temp-Mon': (self.uiobj.ledtemp_ltb1, 22, 25),
            'TB-04:VA-PT100-ED2:Temp-Mon': (self.uiobj.ledtemp_ltb2, 22, 25),
        }

    # def _connect_pvs(self):
    #     self.pvs = dict()
    #     for pvname, _ in self.sinais.items():
    #         self.pvs[pvname] = epics.PV(
    #             pvname, connection_timeout=None, callback=self.callback)

    # def callback(self, pvname, value, **kwargs):
    #     """."""
    #     print(pvname, value)


class Blocoltb:
    """Gerencia o grupo LTB e atualiza a label alarmltb."""

    def __init__(self, janela_opr):
        """."""
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto
        self.templtb = Templtb(janela_opr, janela_opr.btntempltb)
        self.vacltb = Ltbvac(janela_opr, janela_opr.btnvacltb)
        self.psltb = Power_supply(janela_opr, janela_opr.btnpsltb)

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
