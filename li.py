"""Lógica das subjanelas do LINAC."""
import logging
import subprocess

from PyQt5 import QtWidgets

import utils


class Temperature(utils.ConnWidgetPVs):
    """Classe do sistema de temperatura LINAC."""

    def plot_graph(self, url):
        try:
            subprocess.Popen(["firefox", url])
        except Exception as e:
            logging.error(f"Erro ao abrir gráfico de temperaturas: {e}")

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/templinac.ui", "temp")

        url = self.create_archviewer_link(self.sinais['KlyTemp'])
        self.uiobj.btntempkly.clicked.connect(
            lambda _, url=url: self.plot_graph(url)
        )

        url = self.create_archviewer_link(self.sinais['KlyArea'])
        self.uiobj.btntempgaleria.clicked.connect(
            lambda _, url=url: self.plot_graph(url)
        )

        url = self.create_archviewer_link(self.sinais['Tunnel'])
        self.uiobj.btntemp_umid.clicked.connect(
            lambda _, url=url: self.plot_graph(url)
        )

        url = self.create_archviewer_link(self.sinais['45C'])
        self.uiobj.btntemplinac45.clicked.connect(
            lambda _, url=url: self.plot_graph(url)
        )

        url = self.create_archviewer_link(self.sinais['Solenoid'])
        self.uiobj.btntempsolenoid.clicked.connect(
            lambda _, url=url: self.plot_graph(url)
        )

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        self.sinais = {
            'KlyArea': {
                'LA-CN:H1MPS-1:K1Temp5': (self._gwidget('ledk1temp5'), 18, 23),
                'LA-CN:H1MPS-1:K2Temp5': (self._gwidget('ledk2temp5'), 18, 23),
            },
            'KlyTemp': {
                'LA-CN:H1MPS-1:K1Temp1': (self._gwidget('ledk1temp1'), 18, 23),
                'LA-CN:H1MPS-1:K1Temp2': (self._gwidget('ledk1temp2'), 18, 23),
                'LA-CN:H1MPS-1:K2Temp1': (self._gwidget('ledk2temp1'), 18, 23),
                'LA-CN:H1MPS-1:K2Temp2': (self._gwidget('ledk2temp2'), 18, 23),
            },
            'Tunnel': {
                'LINAC:Umidade-Mon': (self._gwidget('led_umidade'), 35, 55),
                'LINAC:Temperatura-Mon': (
                    self._gwidget('ledtemptunel'), 22, 24
                ),
            },
            '45C': {
                'LA-CN:H1MPS-1:A1Temp1': (self._gwidget('leda1t1'), 42, 46),
                'LA-CN:H1MPS-1:A1Temp2': (self._gwidget('leda1t2'), 42, 46),
                'LA-CN:H1MPS-1:A2Temp1': (self._gwidget('leda2t1'), 42, 46),
                'LA-CN:H1MPS-1:A2Temp2': (self._gwidget('leda2t2'), 42, 46),
                'LA-CN:H1MPS-1:A3Temp1': (self._gwidget('leda3t1'), 42, 46),
                'LA-CN:H1MPS-1:A3Temp2': (self._gwidget('leda3t2'), 42, 46),
                'LA-CN:H1MPS-1:A4Temp1': (self._gwidget('leda4t1'), 42, 46),
                'LA-CN:H1MPS-1:A4Temp2': (self._gwidget('leda4t2'), 42, 46),
            },
            'Solenoid': {
                'LI-01:PS-Slnd-1:Temperature-Mon':
                (self._gwidget('ledsol1'), 20, 27),
                'LI-01:PS-Slnd-2:Temperature-Mon':
                (self._gwidget('ledsol2'), 20, 27),
                'LI-01:PS-Slnd-3:Temperature-Mon':
                (self._gwidget('ledsol3'), 20, 27),
                'LI-01:PS-Slnd-4:Temperature-Mon':
                (self._gwidget('ledsol4'), 20, 27),
                'LI-01:PS-Slnd-5:Temperature-Mon':
                (self._gwidget('ledsol5'), 20, 27),
                'LI-01:PS-Slnd-6:Temperature-Mon':
                (self._gwidget('ledsol6'), 20, 27),
                'LI-01:PS-Slnd-7:Temperature-Mon':
                (self._gwidget('ledsol7'), 20, 27),
                'LI-01:PS-Slnd-8:Temperature-Mon':
                (self._gwidget('ledsol8'), 20, 27),
                'LI-01:PS-Slnd-9:Temperature-Mon':
                (self._gwidget('ledsol9'), 20, 27),
                'LI-01:PS-Slnd-10:Temperature-Mon':
                (self._gwidget('ledsol10'), 20, 27),
                'LI-01:PS-Slnd-11:Temperature-Mon':
                (self._gwidget('ledsol11'), 20, 27),
                'LI-01:PS-Slnd-12:Temperature-Mon':
                (self._gwidget('ledsol12'), 20, 27),
                'LI-01:PS-Slnd-13:Temperature-Mon':
                (self._gwidget('ledsol13'), 20, 27),
            },
        }


class Lowlevel(utils.ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura LINAC."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/lowlevelrf.ui",
                         "estado")

    def _registrar_grupos(self):
        self.sinais = {
            'LA-CN:H1MPS-1:K1TempState1': (self._gwidget('ledoiltank_k1'), 1),
            'LA-CN:H1MPS-1:K2TempState1': (self._gwidget('ledoiltank_k2'), 1),
            'LA-CN:H1MPS-1:K1TempState2':
            (self._gwidget('ledfocuscoil_k1'), 1),
            'LA-CN:H1MPS-1:K2TempState2':
            (self._gwidget('ledfocuscoil_k2'), 1),
            'LA-CN:H1MPS-1:K2PsState_L': (self._gwidget('ledstatus_k2'), 0),
            'LA-CN:H1MPS-1:K1PsState_L': (self._gwidget('ledstatus_k1'), 0),
            'LA-RF:LLRF:KLY1:GET_INTERLOCK':
            (self._gwidget('ledreflet_k1'), 0),
            'LA-RF:LLRF:KLY2:GET_INTERLOCK':
            (self._gwidget('ledreflet_k2'), 0),
        }


class Vacuum(utils.ConnWidgetPVs):
    """Controle da subjanela de leitura de vácuo do Linac."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/vaclinac.ui", "vacuo")

    def _registrar_grupos(self):
        """Registra Pvs de vacuo e seus leds correspondentes."""
        self.sinais = {
            'LA-VA:H1VGC-01:RdPrs-1s': (self._gwidget('ledvac01'), 1.0e-7),
            'LA-VA:H1VGC-01:RdPrs-2s': (self._gwidget('ledvac02'), 1.0e-7),
            'LA-VA:H1VGC-02:RdPrs-1s': (self._gwidget('ledvac03'), 1.0e-7),
            'LA-VA:H1VGC-02:RdPrs-2s': (self._gwidget('ledvac04'), 1.0e-7),
            'LA-VA:H1VGC-03:RdPrs-1s': (self._gwidget('ledvac05'), 1.0e-7),
            'LA-VA:H1VGC-03:RdPrs-2s': (self._gwidget('ledvac06'), 1.0e-7),
            'LA-VA:H1VGC-04:RdPrs-1s': (self._gwidget('ledvac07'), 1.0e-7),
            'LA-VA:H1VGC-04:RdPrs-2s': (self._gwidget('ledvac08'), 1.0e-7),
            'LA-VA:H1VGC-05:RdPrs-1s': (self._gwidget('ledvac09'), 1.0e-7),
            'LA-VA:H1VGC-05:RdPrs-2s': (self._gwidget('ledvac10'), 1.0e-7),
        }


class PowerSupply(utils.ConnWidgetPVs):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/pslinac.ui", "estado")

    def _registrar_grupos(self):
        self.sinais = {
            'LI-01:EG-External:status': (self._gwidget('led_extintlk'), 1),
            'LI-01:EG-Valve:status': (self._gwidget('led_valve'), 1),
            'LI-01:EG-Gate:status': (self._gwidget('led_gate'), 1),
            'LI-01:EG-TriggerPS:status': (self._gwidget('led_statusegun'), 1),
            'LI-01:EG-TriggerPS:allow':
            (self._gwidget('led_trigallowegun'), 1),
            'LI-01:EG-TriggerPS:enablereal':
            (self._gwidget('led_trigegun'), 1),
            'LI-01:PS-QD1:DiagStatus-Mon': (self._gwidget('led_qd1'), 0),
            'LI-01:PS-QD2:DiagStatus-Mon': (self._gwidget('led_qd2'), 0),
            'LI-01:PS-QF3:DiagStatus-Mon': (self._gwidget('led_qf3'), 0),
            'LI-Fam:PS-QF1:DiagStatus-Mon': (self._gwidget('led_qf1'), 0),
            'LI-Fam:PS-QF2:DiagStatus-Mon': (self._gwidget('led_qf2'), 0),
            'LI-01:PS-Spect:DiagStatus-Mon': (self._gwidget('led_spec'), 0),
            'LI-01:PS-CH-1:DiagStatus-Mon': (self._gwidget('led_corrch1'), 0),
            'LI-01:PS-CH-2:DiagStatus-Mon': (self._gwidget('led_corrch2'), 0),
            'LI-01:PS-CH-3:DiagStatus-Mon': (self._gwidget('led_corrch3'), 0),
            'LI-01:PS-CH-4:DiagStatus-Mon': (self._gwidget('led_corrch4'), 0),
            'LI-01:PS-CH-5:DiagStatus-Mon': (self._gwidget('led_corrch5'), 0),
            'LI-01:PS-CH-6:DiagStatus-Mon': (self._gwidget('led_corrch6'), 0),
            'LI-01:PS-CH-7:DiagStatus-Mon': (self._gwidget('led_corrch7'), 0),
            'LI-01:PS-CV-1:DiagStatus-Mon': (self._gwidget('led_corrcv1'), 0),
            'LI-01:PS-CV-2:DiagStatus-Mon': (self._gwidget('led_corrcv2'), 0),
            'LI-01:PS-CV-3:DiagStatus-Mon': (self._gwidget('led_corrcv3'), 0),
            'LI-01:PS-CV-4:DiagStatus-Mon': (self._gwidget('led_corrcv4'), 0),
            'LI-01:PS-CV-5:DiagStatus-Mon': (self._gwidget('led_corrcv5'), 0),
            'LI-01:PS-CV-6:DiagStatus-Mon': (self._gwidget('led_corrcv6'), 0),
            'LI-01:PS-CV-7:DiagStatus-Mon': (self._gwidget('led_corrcv7'), 0),
            'LI-01:PS-LensRev:DiagStatus-Mon':
            (self._gwidget('led_lensrev'), 0),
            'LI-01:PS-Lens-1:DiagStatus-Mon': (self._gwidget('led_lens1'), 0),
            'LI-01:PS-Lens-2:DiagStatus-Mon': (self._gwidget('led_lens2'), 0),
            'LI-01:PS-Lens-3:DiagStatus-Mon': (self._gwidget('led_lens3'), 0),
            'LI-01:PS-Lens-4:DiagStatus-Mon': (self._gwidget('led_lens4'), 0),
            'LI-01:PS-Slnd-1:DiagStatus-Mon': (self._gwidget('led_slnd1'), 0),
            'LI-01:PS-Slnd-2:DiagStatus-Mon': (self._gwidget('led_slnd2'), 0),
            'LI-01:PS-Slnd-3:DiagStatus-Mon': (self._gwidget('led_slnd3'), 0),
            'LI-01:PS-Slnd-4:DiagStatus-Mon': (self._gwidget('led_slnd4'), 0),
            'LI-01:PS-Slnd-5:DiagStatus-Mon': (self._gwidget('led_slnd5'), 0),
            'LI-01:PS-Slnd-6:DiagStatus-Mon': (self._gwidget('led_slnd6'), 0),
            'LI-01:PS-Slnd-7:DiagStatus-Mon': (self._gwidget('led_slnd7'), 0),
            'LI-01:PS-Slnd-8:DiagStatus-Mon': (self._gwidget('led_slnd8'), 0),
            'LI-01:PS-Slnd-9:DiagStatus-Mon': (self._gwidget('led_slnd9'), 0),
            'LI-01:PS-Slnd-10:DiagStatus-Mon':
            (self._gwidget('led_slnd10'), 0),
            'LI-01:PS-Slnd-11:DiagStatus-Mon':
            (self._gwidget('led_slnd11'), 0),
            'LI-01:PS-Slnd-12:DiagStatus-Mon':
            (self._gwidget('led_slnd12'), 0),
            'LI-01:PS-Slnd-13:DiagStatus-Mon':
            (self._gwidget('led_slnd13'), 0),
            'LI-Fam:PS-Slnd-14:DiagStatus-Mon':
            (self._gwidget('led_slnd14'), 0),
            'LI-Fam:PS-Slnd-15:DiagStatus-Mon':
            (self._gwidget('led_slnd15'), 0),
            'LI-Fam:PS-Slnd-16:DiagStatus-Mon':
            (self._gwidget('led_slnd16'), 0),
            'LI-Fam:PS-Slnd-17:DiagStatus-Mon':
            (self._gwidget('led_slnd17'), 0),
            'LI-Fam:PS-Slnd-18:DiagStatus-Mon':
            (self._gwidget('led_slnd18'), 0),
            'LI-Fam:PS-Slnd-19:DiagStatus-Mon':
            (self._gwidget('led_slnd19'), 0),
            'LI-Fam:PS-Slnd-20:DiagStatus-Mon':
            (self._gwidget('led_slnd20'), 0),
            'LI-Fam:PS-Slnd-21:DiagStatus-Mon':
            (self._gwidget('led_slnd21'), 0),

        }


class AllSubsys:
    """Gerencia o grupo LINAC e atualiza a label alarmlinac."""

    def __init__(self, janela_opr):
        """."""
        janela_opr.alarmlinac.clicked.connect(self.aba_linac)
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto
        self.templinac = Temperature(janela_opr, janela_opr.btntemplinac)
        self.lowlevel = Lowlevel(janela_opr, janela_opr.btnlowlevelrf)
        self.vaclinac = Vacuum(janela_opr, janela_opr.btnvaclinac)
        self.pslinac = PowerSupply(janela_opr, janela_opr.btnpslinac)

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
            falha_detectada |= not sub.estado_ok

        # Atualiza a label principal do bloco LINAC
        alarme_widget = self.janela_opr.findChild(QtWidgets.QPushButton,
                                                  "alarmlinac")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if not falha_detectada else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()

    def aba_linac(self):
        """."""
        try:
            self.janela_opr.janela_opr.setCurrentIndex(1)
        except Exception as e:
            logging.error(f"Erro ao mudar para aba LINAC: {e}")
