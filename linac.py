"""Lógica das subjanelas do LINAC."""
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

        elif self.check_type == 'lowlevel':

            todos_ok = True

            for pvname, value in self.sinais.items():
                led, estado_esperado = value
                utils.verificar_ledlowlevel(
                    pvname, led, estado_esperado=estado_esperado)
                if not getattr(led, "state", False):
                    todos_ok = False

            self.estado_ok = todos_ok

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")

            # Atualiza a label de alarme do bloco LOWLEVEL
            alarme_widget = self.janela_opr.findChild(
                QtWidgets.QLabel, "alarmlowlevel")

        elif self.check_type == 'vacuo':

            todos_ok = True

            for pvname, value in self.sinais.items():
                led, pressao_min = value
                utils.verificar_vacuo(
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

        elif self.check_type == 'pslinac':

            todos_ok = True

            for pvname, value in self.sinais.items():
                led, estado_esperado = value
                utils.verificar_ledpslinac(
                    pvname, led, estado_esperado=estado_esperado)
                if not getattr(led, "state", False):
                    todos_ok = False

            self.estado_ok = todos_ok

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")

            # Atualiza a label de alarme do bloco PSLinac
            alarme_widget = self.janela_opr.findChild(
                QtWidgets.QLabel, "alarmpslinac")

            if alarme_widget:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                alarme_widget.setStyleSheet(f"background-color: {cor};")
                alarme_widget.repaint()
                QtWidgets.QApplication.processEvents()
                alarme_widget.update()


class Templinac(ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura LINAC."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/templinac.ui", "temp")

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        self.sinais = {
            'LA-CN:H1MPS-1:K1Temp5': (self.uiobj.ledk1temp5, 18, 23),
            'LA-CN:H1MPS-1:K2Temp5': (self.uiobj.ledk2temp5, 18, 23),
            'LA-CN:H1MPS-1:K1Temp1': (self.uiobj.ledk1temp1, 18, 23),
            'LA-CN:H1MPS-1:K1Temp2': (self.uiobj.ledk1temp2, 18, 23),
            'LA-CN:H1MPS-1:K2Temp1': (self.uiobj.ledk2temp1, 18, 23),
            'LA-CN:H1MPS-1:K2Temp2': (self.uiobj.ledk2temp2, 18, 23),
            'LINAC:Umidade-Mon': (self.uiobj.led_umidade, 35, 55),
            'LINAC:Temperatura-Mon': (self.uiobj.ledtemptunel, 22, 24),
            'LA-CN:H1MPS-1:A1Temp1': (self.uiobj.leda1t1, 42, 46),
            'LA-CN:H1MPS-1:A1Temp2': (self.uiobj.leda1t2, 42, 46),
            'LA-CN:H1MPS-1:A2Temp1': (self.uiobj.leda2t1, 42, 46),
            'LA-CN:H1MPS-1:A2Temp2': (self.uiobj.leda2t2, 42, 46),
            'LA-CN:H1MPS-1:A3Temp1': (self.uiobj.leda3t1, 42, 46),
            'LA-CN:H1MPS-1:A3Temp2': (self.uiobj.leda3t2, 42, 46),
            'LA-CN:H1MPS-1:A4Temp1': (self.uiobj.leda4t1, 42, 46),
            'LA-CN:H1MPS-1:A4Temp2': (self.uiobj.leda4t2, 42, 46),
            'LI-01:PS-Slnd-1:Temperature-Mon': (self.uiobj.ledsol1, 20, 27),
            'LI-01:PS-Slnd-2:Temperature-Mon': (self.uiobj.ledsol2, 20, 27),
            'LI-01:PS-Slnd-3:Temperature-Mon': (self.uiobj.ledsol3, 20, 27),
            'LI-01:PS-Slnd-4:Temperature-Mon': (self.uiobj.ledsol4, 20, 27),
            'LI-01:PS-Slnd-5:Temperature-Mon': (self.uiobj.ledsol5, 20, 27),
            'LI-01:PS-Slnd-6:Temperature-Mon': (self.uiobj.ledsol6, 20, 27),
            'LI-01:PS-Slnd-7:Temperature-Mon': (self.uiobj.ledsol7, 20, 27),
            'LI-01:PS-Slnd-8:Temperature-Mon': (self.uiobj.ledsol8, 20, 27),
            'LI-01:PS-Slnd-9:Temperature-Mon': (self.uiobj.ledsol9, 20, 27),
            'LI-01:PS-Slnd-10:Temperature-Mon': (self.uiobj.ledsol10, 20, 27),
            'LI-01:PS-Slnd-11:Temperature-Mon': (self.uiobj.ledsol11, 20, 27),
            'LI-01:PS-Slnd-12:Temperature-Mon': (self.uiobj.ledsol12, 20, 27),
            'LI-01:PS-Slnd-13:Temperature-Mon': (self.uiobj.ledsol13, 20, 27),
        }


class Lowlevel(ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura LINAC."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/lowlevelrf.ui",
                         "lowlevel")

    def _registrar_grupos(self):
        self.sinais = {
            'LA-CN:H1MPS-1:K1TempState1': (self.uiobj.ledoiltank_k1, 1),
            'LA-CN:H1MPS-1:K2TempState1': (self.uiobj.ledoiltank_k2, 1),
            'LA-CN:H1MPS-1:K1TempState2': (self.uiobj.ledfocuscoil_k1, 1),
            'LA-CN:H1MPS-1:K2TempState2': (self.uiobj.ledfocuscoil_k2, 1),
            'LA-CN:H1MPS-1:K2PsState_L': (self.uiobj.ledstatus_k2, 0),
            'LA-CN:H1MPS-1:K1PsState_L': (self.uiobj.ledstatus_k1, 0),
            'LA-RF:LLRF:KLY1:GET_INTERLOCK': (self.uiobj.ledreflet_k1, 0),
            'LA-RF:LLRF:KLY2:GET_INTERLOCK': (self.uiobj.ledreflet_k2, 0),
        }


class Vacuo(ConnWidgetPVs):
    """Controle da subjanela de leitura de vácuo do Linac."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/vaclinac.ui", "vacuo")

    def _registrar_grupos(self):
        """Registra Pvs de vacuo e seus leds correspondentes."""
        self.sinais = {
            'LA-VA:H1VGC-01:RdPrs-1s': (self.uiobj.ledvac01, 1.0e-7),
            'LA-VA:H1VGC-01:RdPrs-2s': (self.uiobj.ledvac02, 1.0e-7),
            'LA-VA:H1VGC-02:RdPrs-1s': (self.uiobj.ledvac03, 1.0e-7),
            'LA-VA:H1VGC-02:RdPrs-2s': (self.uiobj.ledvac04, 1.0e-7),
            'LA-VA:H1VGC-03:RdPrs-1s': (self.uiobj.ledvac05, 1.0e-7),
            'LA-VA:H1VGC-03:RdPrs-2s': (self.uiobj.ledvac06, 1.0e-7),
            'LA-VA:H1VGC-04:RdPrs-1s': (self.uiobj.ledvac07, 1.0e-7),
            'LA-VA:H1VGC-04:RdPrs-2s': (self.uiobj.ledvac08, 1.0e-7),
            'LA-VA:H1VGC-05:RdPrs-1s': (self.uiobj.ledvac09, 1.0e-7),
            'LA-VA:H1VGC-05:RdPrs-2s': (self.uiobj.ledvac10, 1.0e-7),
        }


class Power_supply(ConnWidgetPVs):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/pslinac.ui", "pslinac")

    def _registrar_grupos(self):
        self.sinais = {
            'LI-01:EG-External:status': (self.uiobj.led_extintlk, 1),
            'LI-01:EG-Valve:status': (self.uiobj.led_valve, 1),
            'LI-01:EG-Gate:status': (self.uiobj.led_gate, 1),
            'LI-01:EG-TriggerPS:status': (self.uiobj.led_statusegun, 1),
            'LI-01:EG-TriggerPS:allow': (self.uiobj.led_trigallowegun, 1),
            'LI-01:EG-TriggerPS:enablereal': (self.uiobj.led_trigegun, 1),
            'LI-01:PS-QD1:DiagStatus-Mon': (self.uiobj.led_qd1, 0),
            'LI-01:PS-QD2:DiagStatus-Mon': (self.uiobj.led_qd2, 0),
            'LI-01:PS-QF3:DiagStatus-Mon': (self.uiobj.led_qf3, 0),
            'LI-Fam:PS-QF1:DiagStatus-Mon': (self.uiobj.led_qf1, 0),
            'LI-Fam:PS-QF2:DiagStatus-Mon': (self.uiobj.led_qf2, 0),
            'LI-01:PS-Spect:DiagStatus-Mon': (self.uiobj.led_spec, 0),
            'LI-01:PS-CH-1:DiagStatus-Mon': (self.uiobj.led_corrch1, 0),
            'LI-01:PS-CH-2:DiagStatus-Mon': (self.uiobj.led_corrch2, 0),
            'LI-01:PS-CH-3:DiagStatus-Mon': (self.uiobj.led_corrch3, 0),
            'LI-01:PS-CH-4:DiagStatus-Mon': (self.uiobj.led_corrch4, 0),
            'LI-01:PS-CH-5:DiagStatus-Mon': (self.uiobj.led_corrch5, 0),
            'LI-01:PS-CH-6:DiagStatus-Mon': (self.uiobj.led_corrch6, 0),
            'LI-01:PS-CH-7:DiagStatus-Mon': (self.uiobj.led_corrch7, 0),
            'LI-01:PS-CV-1:DiagStatus-Mon': (self.uiobj.led_corrcv1, 0),
            'LI-01:PS-CV-2:DiagStatus-Mon': (self.uiobj.led_corrcv2, 0),
            'LI-01:PS-CV-3:DiagStatus-Mon': (self.uiobj.led_corrcv3, 0),
            'LI-01:PS-CV-4:DiagStatus-Mon': (self.uiobj.led_corrcv4, 0),
            'LI-01:PS-CV-5:DiagStatus-Mon': (self.uiobj.led_corrcv5, 0),
            'LI-01:PS-CV-6:DiagStatus-Mon': (self.uiobj.led_corrcv6, 0),
            'LI-01:PS-CV-7:DiagStatus-Mon': (self.uiobj.led_corrcv7, 0),
            'LI-01:PS-LensRev:DiagStatus-Mon': (self.uiobj.led_lensrev, 0),
            'LI-01:PS-Lens-1:DiagStatus-Mon': (self.uiobj.led_lens1, 0),
            'LI-01:PS-Lens-2:DiagStatus-Mon': (self.uiobj.led_lens2, 0),
            'LI-01:PS-Lens-3:DiagStatus-Mon': (self.uiobj.led_lens3, 0),
            'LI-01:PS-Lens-4:DiagStatus-Mon': (self.uiobj.led_lens4, 0),
            'LI-01:PS-Slnd-1:DiagStatus-Mon': (self.uiobj.led_slnd1, 0),
            'LI-01:PS-Slnd-2:DiagStatus-Mon': (self.uiobj.led_slnd2, 0),
            'LI-01:PS-Slnd-3:DiagStatus-Mon': (self.uiobj.led_slnd3, 0),
            'LI-01:PS-Slnd-4:DiagStatus-Mon': (self.uiobj.led_slnd4, 0),
            'LI-01:PS-Slnd-5:DiagStatus-Mon': (self.uiobj.led_slnd5, 0),
            'LI-01:PS-Slnd-6:DiagStatus-Mon': (self.uiobj.led_slnd6, 0),
            'LI-01:PS-Slnd-7:DiagStatus-Mon': (self.uiobj.led_slnd7, 0),
            'LI-01:PS-Slnd-8:DiagStatus-Mon': (self.uiobj.led_slnd8, 0),
            'LI-01:PS-Slnd-9:DiagStatus-Mon': (self.uiobj.led_slnd9, 0),
            'LI-01:PS-Slnd-10:DiagStatus-Mon': (self.uiobj.led_slnd10, 0),
            'LI-01:PS-Slnd-11:DiagStatus-Mon': (self.uiobj.led_slnd11, 0),
            'LI-01:PS-Slnd-12:DiagStatus-Mon': (self.uiobj.led_slnd12, 0),
            'LI-01:PS-Slnd-13:DiagStatus-Mon': (self.uiobj.led_slnd13, 0),
            'LI-Fam:PS-Slnd-14:DiagStatus-Mon': (self.uiobj.led_slnd14, 0),
            'LI-Fam:PS-Slnd-15:DiagStatus-Mon': (self.uiobj.led_slnd15, 0),
            'LI-Fam:PS-Slnd-16:DiagStatus-Mon': (self.uiobj.led_slnd16, 0),
            'LI-Fam:PS-Slnd-17:DiagStatus-Mon': (self.uiobj.led_slnd17, 0),
            'LI-Fam:PS-Slnd-18:DiagStatus-Mon': (self.uiobj.led_slnd18, 0),
            'LI-Fam:PS-Slnd-19:DiagStatus-Mon': (self.uiobj.led_slnd19, 0),
            'LI-Fam:PS-Slnd-20:DiagStatus-Mon': (self.uiobj.led_slnd20, 0),
            'LI-Fam:PS-Slnd-21:DiagStatus-Mon': (self.uiobj.led_slnd21, 0),

        }


class BlocoLinac:
    """Gerencia o grupo LINAC e atualiza a label alarmlinac."""

    def __init__(self, janela_opr):
        """."""
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto
        self.templinac = Templinac(janela_opr, janela_opr.btntemplinac)
        self.lowlevel = Lowlevel(janela_opr, janela_opr.btnlowlevelrf)
        self.vaclinac = Vacuo(janela_opr, janela_opr.btnvaclinac)
        self.pslinac = Power_supply(janela_opr, janela_opr.btnpslinac)

        # Adiciona todas as subjanelas a lista
        self.subjanelas.extend([
            self.templinac,
            self.lowlevel,
            self.vaclinac,
            self.pslinac,
        ])

        # Configura cada subjanela
        for sub in self.subjanelas:
            sub.configurar_sistema()

    def atualizar_grupo(self):
        """Atualiza todas as subjanelas e a label alarmlinac."""
        falha_detectada = False

        for sub in self.subjanelas:
            sub.atualizar_status()
            if not getattr(sub, "estado_ok", True):
                falha_detectada = True

        # Atualiza a label principal do bloco LINAC
        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel,
                                                  "alarmlinac")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if not falha_detectada else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()
