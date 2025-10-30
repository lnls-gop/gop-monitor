"""Lógica das subjanelas da Linha de Transporte LTS."""
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

            # Atualiza a label de alarme do bloco LOWLEVEL
            alarme_widget = self.janela_opr.findChild(
                QtWidgets.QLabel, "alarmtemplts")

        elif self.check_type == 'vacuo':

            todos_ok = True

            for pvname, value in self.sinais.items():
                led, pressao_min = value
                utils.verificar_vaclts(
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
                utils.verificar_pslts(
                    pvname, led, estado_esperado=estado_esperado)
                if not getattr(led, "state", False):
                    todos_ok = False

            self.estado_ok = todos_ok

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")

            # Atualiza a label de alarme do bloco LOWLEVEL
            alarme_widget = self.janela_opr.findChild(
                QtWidgets.QLabel, "alarmpslts")

            if alarme_widget:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                alarme_widget.setStyleSheet(f"background-color: {cor};")
                alarme_widget.repaint()
                QtWidgets.QApplication.processEvents()
                alarme_widget.update()


class Ltsvac(ConnWidgetPVs):
    """Controle da subjanela de leitura de vácuo do Linac."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/vaclts.ui", "vacuo")

    def _registrar_grupos(self):
        """Registra Pvs de vacuo e seus leds correspondentes."""
        self.sinais = {
            'TS-01:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_lts01bg, 1.0e-7),
            'TS-01:VA-CCG-ED:Pressure-Mon': (self.uiobj.led_lts01ed, 1.0e-7),
            'TS-04:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_lts04bg, 1.0e-7),
            'TS-04:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_lts04md, 1.0e-7),
            'TS-01:VA-SIP20-BG:Pressure-Mon': (self.uiobj.led_lts01sip20bg,
                                               1.0e-7),
            'TS-01:VA-SIP20-ED:Pressure-Mon': (self.uiobj.led_lts01sip20ed,
                                               1.0e-7),
            'TS-01:VA-SIP20-MD1:Pressure-Mon': (self.uiobj.led_lts01sip20md1,
                                                1.0e-7),
            'TS-01:VA-SIP20-MD2:Pressure-Mon': (self.uiobj.led_lts01sip20md2,
                                                1.0e-7),
            'TS-02:VA-SIP20-BG:Pressure-Mon': (self.uiobj.led_lts02sip20bg,
                                               1.0E-7),
            'TS-02:VA-SIP20-ED:Pressure-Mon': (self.uiobj.led_lts02sip20ed,
                                               1.0E-7),
            'TS-03:VA-SIP20-BG:Pressure-Mon': (self.uiobj.led_lts03sip20bg,
                                               1.0E-7),
            'TS-03:VA-SIP20-ED:Pressure-Mon': (self.uiobj.led_lts03sip20ed,
                                               1.0E-7),
            'TS-04:VA-SIP20-BG:Pressure-Mon': (self.uiobj.led_lts04sip20bg,
                                               1.0E-7),
            'TS-04:VA-SIP20-ED:Pressure-Mon': (self.uiobj.led_lts04sip20ed,
                                               1.0E-7),
            'TS-04:VA-SIP20-MD1:Pressure-Mon': (self.uiobj.led_lts04sip20md1,
                                                1.0E-7),
            'TS-04:VA-SIP20-MD2:Pressure-Mon': (self.uiobj.led_lts04sip20md2,
                                                1.0E-7),
            'TS-04:VA-SIP20-MD3:Pressure-Mon': (self.uiobj.led_lts04sip20md3,
                                                1.0E-7),
        }


class Templts(ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura LINAC."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/templts.ui", "temp")

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        self.sinais = {
            'TS-01:VA-PT100-BG1:Temp-Mon': (self.uiobj.led_ltsbg1, 22, 26.5),
            'TS-01:VA-PT100-BG2:Temp-Mon': (self.uiobj.led_ltsbg2, 22, 26.5),
            'TS-01:VA-PT100-BG3:Temp-Mon': (self.uiobj.led_ltsbg3, 22, 26.5),
            'TS-01:VA-PT100-BG4:Temp-Mon': (self.uiobj.led_ltsbg4, 22, 26.5),
            'TS-01:PU-EjeSF-BG:Temp-Mon': (self.uiobj.led_ejesfbg, 22, 26.5),
            'TS-01:PU-EjeSG-BG:Temp-Mon': (self.uiobj.led_ejesgbg, 22, 26.5),
            'TS-01:PU-EjeSF-ED:Temp-Mon': (self.uiobj.led_ejesfed, 22, 26.5),
            'TS-01:PU-EjeSG-ED:Temp-Mon': (self.uiobj.led_ejesged, 22, 26.5),
            'TS-04:VA-PT100-ED1:Temp-Mon': (self.uiobj.led_ltsed1, 22, 26.5),
            'TS-04:VA-PT100-ED2:Temp-Mon': (self.uiobj.led_ltsed2, 22, 26.5),
            'TS-04:VA-PT100-ED3:Temp-Mon': (self.uiobj.led_ltsed3, 22, 26.5),
            'TS-04:VA-PT100-ED4:Temp-Mon': (self.uiobj.led_ltsed4, 22, 26.5),
            'TS-04:VA-PT100-ED5:Temp-Mon': (self.uiobj.led_ltsed5, 22, 26.5),
            'TS-04:VA-PT100-ED6:Temp-Mon': (self.uiobj.led_ltsed6, 22, 26.5),
            'TS-MBTemp-03-CH1': (self.uiobj.led_ltsch1, 22, 26),
            'TS-MBTemp-03-CH2': (self.uiobj.led_ltsch2, 22, 26),
            'TS-MBTemp-03-CH3': (self.uiobj.led_ltsch3, 22, 26),
            'TS-MBTemp-03-CH4': (self.uiobj.led_ltsch4, 22, 26),
        }


class Ltsps(ConnWidgetPVs):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/pslts.ui", "psltb")

    def _registrar_grupos(self):
        self.sinais = {
            'TS-Fam:PS-B:DiagStatus-Mon': (self.uiobj.led_ltsb, 0),
            'TS-01:PS-QF1A:DiagStatus-Mon': (self.uiobj.led_tsqf1a, 0),
            'TS-01:PS-QF1B:DiagStatus-Mon': (self.uiobj.led_tsqf1b, 0),
            'TS-02:PS-QD2:DiagStatus-Mon': (self.uiobj.led_tsqd2, 0),
            'TS-02:PS-QF2:DiagStatus-Mon': (self.uiobj.led_tsqf2, 0),
            'TS-03:PS-QF3:DiagStatus-Mon': (self.uiobj.led_tsqf3, 0),
            'TS-04:PS-QD4A:DiagStatus-Mon': (self.uiobj.led_tsqd4a, 0),
            'TS-04:PS-QD4B:DiagStatus-Mon': (self.uiobj.led_tsqd4b, 0),
            'TS-04:PS-QF4:DiagStatus-Mon': (self.uiobj.led_tsqf4, 0),
            'TS-01:PS-CH:DiagStatus-Mon': (self.uiobj.led_lts01ch, 0),
            'TS-02:PS-CH:DiagStatus-Mon': (self.uiobj.led_lts02ch, 0),
            'TS-03:PS-CH:DiagStatus-Mon': (self.uiobj.led_lts03ch, 0),
            'TS-04:PS-CH:DiagStatus-Mon': (self.uiobj.led_lts04ch, 0),
            'TS-01:PS-CV-1:DiagStatus-Mon': (self.uiobj.led_lts01cv1, 0),
            'TS-01:PS-CV-1E2:DiagStatus-Mon': (self.uiobj.led_lts01cv1e2, 0),
            'TS-01:PS-CV-2:DiagStatus-Mon': (self.uiobj.led_lts01cv2, 0),
            'TS-02:PS-CV:DiagStatus-Mon': (self.uiobj.led_lts02cv, 0),
            'TS-02:PS-CV-0:DiagStatus-Mon': (self.uiobj.led_lts02cv0, 0),
            'TS-03:PS-CV:DiagStatus-Mon': (self.uiobj.led_lts03cv, 0),
            'TS-04:PS-CV-0:DiagStatus-Mon': (self.uiobj.led_lts04cv0, 0),
            'TS-04:PS-CV-1:DiagStatus-Mon': (self.uiobj.led_lts04cv1, 0),
            'TS-04:PS-CV-1E2:DiagStatus-Mon': (self.uiobj.led_lts04cv2, 0),
            'TS-04:PS-CV-2:DiagStatus-Mon': (self.uiobj.led_lts04cv1e2, 0),
            'SI-01M1:PS-FFCV:DiagStatus-Mon': (self.uiobj.led_lts01ffcv, 0),
            'SI-01M2:PS-FFCH:DiagStatus-Mon': (self.uiobj.led_lts01ffch, 0),
            'SI-01M2:PS-FFCV:DiagStatus-Mon': (self.uiobj.led_lts02ffcv, 0),
            'SI-01M1:PS-FFCH:DiagStatus-Mon': (self.uiobj.led_lts02ffch, 0),
        }


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
