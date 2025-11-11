"""Lógica das subjanelas da Linha de Transporte LTS."""
import logging

from PyQt5 import QtWidgets

import utils


class Vacuum(utils.ConnWidgetPVs):
    """Controle da subjanela de leitura de vácuo do Linac."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/vaclts.ui", "vacuo")

    def _registrar_grupos(self):
        """Registra Pvs de vacuo e seus leds correspondentes."""
        self.sinais = {
            'TS-01:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_lts01bg'), 1.0e-7),
            'TS-01:VA-CCG-ED:Pressure-Mon':
            (self._gwidget('led_lts01ed'), 1.0e-7),
            'TS-04:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_lts04bg'), 1.0e-7),
            'TS-04:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_lts04md'), 1.0e-7),
            'TS-01:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_lts01sip20bg'), 1.0e-7),
            'TS-01:VA-SIP20-ED:Pressure-Mon':
            (self._gwidget('led_lts01sip20ed'), 1.0e-7),
            'TS-01:VA-SIP20-MD1:Pressure-Mon':
            (self._gwidget('led_lts01sip20md1'), 1.0e-7),
            'TS-01:VA-SIP20-MD2:Pressure-Mon':
            (self._gwidget('led_lts01sip20md2'), 1.0e-7),
            'TS-02:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_lts02sip20bg'), 1.0E-7),
            'TS-02:VA-SIP20-ED:Pressure-Mon':
            (self._gwidget('led_lts02sip20ed'), 1.0E-7),
            'TS-03:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_lts03sip20bg'), 1.0E-7),
            'TS-03:VA-SIP20-ED:Pressure-Mon':
            (self._gwidget('led_lts03sip20ed'), 1.0E-7),
            'TS-04:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_lts04sip20bg'), 1.0E-7),
            'TS-04:VA-SIP20-ED:Pressure-Mon':
            (self._gwidget('led_lts04sip20ed'), 1.0E-7),
            'TS-04:VA-SIP20-MD1:Pressure-Mon':
            (self._gwidget('led_lts04sip20md1'), 1.0E-7),
            'TS-04:VA-SIP20-MD2:Pressure-Mon':
            (self._gwidget('led_lts04sip20md2'), 1.0E-7),
            'TS-04:VA-SIP20-MD3:Pressure-Mon':
            (self._gwidget('led_lts04sip20md3'), 1.0E-7),
        }


class Temperature(utils.ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura LINAC."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/templts.ui", "temp")

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        self.sinais = {
            'Group1': {
                'TS-01:VA-PT100-BG1:Temp-Mon':
                (self._gwidget('led_ltsbg1'), 22, 26.5),
                'TS-01:VA-PT100-BG2:Temp-Mon':
                (self._gwidget('led_ltsbg2'), 22, 26.5),
                'TS-01:VA-PT100-BG3:Temp-Mon':
                (self._gwidget('led_ltsbg3'), 22, 26.5),
                'TS-01:VA-PT100-BG4:Temp-Mon':
                (self._gwidget('led_ltsbg4'), 22, 26.5),
            },
            'Group2': {
                'TS-01:PU-EjeSF-BG:Temp-Mon':
                (self._gwidget('led_ejesfbg'), 22, 26.5),
                'TS-01:PU-EjeSG-BG:Temp-Mon':
                (self._gwidget('led_ejesgbg'), 22, 26.5),
                'TS-01:PU-EjeSF-ED:Temp-Mon':
                (self._gwidget('led_ejesfed'), 22, 26.5),
                'TS-01:PU-EjeSG-ED:Temp-Mon':
                (self._gwidget('led_ejesged'), 22, 26.5),
            },
            'Group3': {
                'TS-04:VA-PT100-ED1:Temp-Mon':
                (self._gwidget('led_ltsed1'), 22, 26.5),
                'TS-04:VA-PT100-ED2:Temp-Mon':
                (self._gwidget('led_ltsed2'), 22, 26.5),
                'TS-04:VA-PT100-ED3:Temp-Mon':
                (self._gwidget('led_ltsed3'), 22, 26.5),
                'TS-04:VA-PT100-ED4:Temp-Mon':
                (self._gwidget('led_ltsed4'), 22, 26.5),
                'TS-04:VA-PT100-ED5:Temp-Mon':
                (self._gwidget('led_ltsed5'), 22, 26.5),
                'TS-04:VA-PT100-ED6:Temp-Mon':
                (self._gwidget('led_ltsed6'), 22, 26.5),
            },
            'Group4': {
                'TS-MBTemp-03-CH1': (self._gwidget('led_ltsch1'), 22, 26.0),
                'TS-MBTemp-03-CH2': (self._gwidget('led_ltsch2'), 22, 26.0),
                'TS-MBTemp-03-CH3': (self._gwidget('led_ltsch3'), 22, 26.0),
                'TS-MBTemp-03-CH4': (self._gwidget('led_ltsch4'), 22, 26.0),
            },
        }


class PowerSupply(utils.ConnWidgetPVs):
    """."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/pslts.ui", "estado")

    def _registrar_grupos(self):
        self.sinais = {
            'TS-Fam:PS-B:DiagStatus-Mon': (self._gwidget('led_ltsb'), 0),
            'TS-01:PS-QF1A:DiagStatus-Mon': (self._gwidget('led_tsqf1a'), 0),
            'TS-01:PS-QF1B:DiagStatus-Mon': (self._gwidget('led_tsqf1b'), 0),
            'TS-02:PS-QD2:DiagStatus-Mon': (self._gwidget('led_tsqd2'), 0),
            'TS-02:PS-QF2:DiagStatus-Mon': (self._gwidget('led_tsqf2'), 0),
            'TS-03:PS-QF3:DiagStatus-Mon': (self._gwidget('led_tsqf3'), 0),
            'TS-04:PS-QD4A:DiagStatus-Mon': (self._gwidget('led_tsqd4a'), 0),
            'TS-04:PS-QD4B:DiagStatus-Mon': (self._gwidget('led_tsqd4b'), 0),
            'TS-04:PS-QF4:DiagStatus-Mon': (self._gwidget('led_tsqf4'), 0),
            'TS-01:PS-CH:DiagStatus-Mon': (self._gwidget('led_lts01ch'), 0),
            'TS-02:PS-CH:DiagStatus-Mon': (self._gwidget('led_lts02ch'), 0),
            'TS-03:PS-CH:DiagStatus-Mon': (self._gwidget('led_lts03ch'), 0),
            'TS-04:PS-CH:DiagStatus-Mon': (self._gwidget('led_lts04ch'), 0),
            'TS-01:PS-CV-1:DiagStatus-Mon': (self._gwidget('led_lts01cv1'), 0),
            'TS-01:PS-CV-1E2:DiagStatus-Mon':
            (self._gwidget('led_lts01cv1e2'), 0),
            'TS-01:PS-CV-2:DiagStatus-Mon': (self._gwidget('led_lts01cv2'), 0),
            'TS-02:PS-CV:DiagStatus-Mon': (self._gwidget('led_lts02cv'), 0),
            'TS-02:PS-CV-0:DiagStatus-Mon': (self._gwidget('led_lts02cv0'), 0),
            'TS-03:PS-CV:DiagStatus-Mon': (self._gwidget('led_lts03cv'), 0),
            'TS-04:PS-CV-0:DiagStatus-Mon': (self._gwidget('led_lts04cv0'), 0),
            'TS-04:PS-CV-1:DiagStatus-Mon': (self._gwidget('led_lts04cv1'), 0),
            'TS-04:PS-CV-1E2:DiagStatus-Mon':
            (self._gwidget('led_lts04cv2'), 0),
            'TS-04:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_lts04cv1e2'), 0),
            'SI-01M1:PS-FFCV:DiagStatus-Mon':
            (self._gwidget('led_lts01ffcv'), 0),
            'SI-01M2:PS-FFCH:DiagStatus-Mon':
            (self._gwidget('led_lts01ffch'), 0),
            'SI-01M2:PS-FFCV:DiagStatus-Mon':
            (self._gwidget('led_lts02ffcv'), 0),
            'SI-01M1:PS-FFCH:DiagStatus-Mon':
            (self._gwidget('led_lts02ffch'), 0),
        }


class AllSubsys:
    """Gerencia o grupo LTB e atualiza a label alarmltb."""

    def __init__(self, janela_opr):
        """."""
        janela_opr.alarmlts.clicked.connect(self.aba_lts)
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto
        self.vaclts = Vacuum(janela_opr, janela_opr.btnvaclts)
        self.templts = Temperature(janela_opr, janela_opr.btntemplts)
        self.pslts = PowerSupply(janela_opr, janela_opr.btnpslts)

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
            falha_detectada |= not sub.estado_ok

        # Atualiza a label principal do bloco LTS
        alarme_widget = self.janela_opr.findChild(QtWidgets.QPushButton,
                                                  "alarmlts")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if not falha_detectada else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()

    def aba_lts(self):
        """."""
        try:
            self.janela_opr.janela_opr.setCurrentIndex(4)
        except Exception as e:
            logging.error(f"Erro ao mudar para aba LTS: {e}")
