"""Logica das das subjanelas de infraestrutura."""
import logging
import subprocess

from PyQt5 import QtWidgets

import utils


class Temptunel(utils.ConnWidgetPVs):
    """Controle da subjanela de temperatura do tunel."""

    def plot_graph(self, url):
        """."""
        try:
            subprocess.Popen(["firefox", url])
        except Exception as e:
            logging.error(f"Erro ao abrir gráfico de temperaturas: {e}")

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/temptunel.ui", "temp")

        url = self.create_archviewer_link(self.sinais['tunel'])
        self.uiobj.btntemptunel.clicked.connect(
            lambda _, url=url: self.plot_graph(url)
        )

    def _registrar_grupos(self):
        """Registra Pvs de vacuo e seus leds correspondentes."""
        self.sinais = {
            'tunel': {
                'TU-5156:AC-PT101:MeanTemperature-Mon':
                (self._gwidget('led_fc05'), 23.5, 24.5),
                'TU-0160:AC-PT100:MeanTemperature-Mon':
                (self._gwidget('led_fc10'), 23.5, 24.5),
                'TU-0308:AC-PT100:MeanTemperature-Mon':
                (self._gwidget('led_fc15'), 23.5, 24.5),
                'TU-0914:AC-PT100:MeanTemperature-Mon':
                (self._gwidget('led_fc20'), 23.5, 24.5),
                'TU-1520:AC-PT100:MeanTemperature-Mon':
                (self._gwidget('led_fc25'), 23.5, 24.5),
                'TU-2126:AC-PT100:MeanTemperature-Mon':
                (self._gwidget('led_fc30'), 23.5, 24.5),
                'TU-2732:AC-PT100:MeanTemperature-Mon':
                (self._gwidget('led_fc31'), 23.5, 24.5),
                'TU-3338:AC-PT100:MeanTemperature-Mon':
                (self._gwidget('led_fc36'), 23.5, 24.5),
                'TU-3944:AC-PT101:MeanTemperature-Mon':
                (self._gwidget('led_fc41'), 23.5, 24.5),
                'TU-4550:AC-PT100:MeanTemperature-Mon':
                (self._gwidget('led_fc46'), 23.5, 24.5),
            }
        }


class Temphall(utils.ConnWidgetPVs):
    """Controle da subjanela de temperatura do tunel."""

    def plot_graph(self, url):
        """."""
        try:
            subprocess.Popen(["firefox", url])
        except Exception as e:
            logging.error(f"Erro ao abrir gráfico de temperaturas: {e}")

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/temphall.ui", "temp")

        url = self.create_archviewer_link(self.sinais['hall'])
        self.uiobj.btntemphall.clicked.connect(
            lambda _, url=url: self.plot_graph(url)
        )

    def _registrar_grupos(self):
        """Registra Pvs de vacuo e seus leds correspondentes."""
        self.sinais = {
            'hall': {
                'UA-52Hall58:AC-PT100-FC61401:MeanTemperature-Mon':
                (self._gwidget('led_hall0104'), 22, 25),
                'UA-55Hall02:AC-PT100-FC61406:MeanTemperature-Mon':
                (self._gwidget('led_hall0609'), 22, 25),
                'UA-04Hall10:AC-PT100-FC61411:MeanTemperature-Mon':
                (self._gwidget('led_hall1114'), 22, 25),
                'UA-10Hall16:AC-PT100-FC61416:MeanTemperature-Mon':
                (self._gwidget('led_hall1619'), 22, 25),
                'UA-16Hall22:AC-PT100-FC61421:MeanTemperature-Mon':
                (self._gwidget('led_hall2124'), 22, 25),
                'UA-22Hall28:AC-PT100-FC61426:MeanTemperature-Mon':
                (self._gwidget('led_hall2629'), 22, 25),
                'UA-28Hall34:AC-PT100-FC61432:MeanTemperature-Mon':
                (self._gwidget('led_hall3235'), 22, 25),
                'UA-34Hall40:AC-PT100-FC61437:MeanTemperature-Mon':
                (self._gwidget('led_hall3740'), 22, 25),
                'UA-40Hall46:AC-PT101-FC61442:MeanTemperature-Mon':
                (self._gwidget('led_hall4245'), 22, 25),
                'UA-46Hall52:AC-PT100-FC61447:MeanTemperature-Mon':
                (self._gwidget('led_hall4750'), 22, 25),
            }
        }


class AllSubsys:
    """Gerencia o grupo Infraestrutura e atualiza a label ."""

    def __init__(self, janela_opr):
        """."""
        janela_opr.alarminfra.clicked.connect(self.aba_infra)
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto
        self.temptunel = Temptunel(janela_opr, janela_opr.btntempblindagem)
        self.temphall = Temphall(janela_opr, janela_opr.btntemphall)

        # Adiciona todas as subjanelas à lista
        self.subjanelas.extend([
            self.temptunel,
            self.temphall,
        ])

        # Configura cada subjanela
        for sub in self.subjanelas:
            sub.configurar_sistema()

    def atualizar_grupo(self):
        """Atualiza todas as subjanelas e a label alarminfra."""
        falha_detectada = False
        for sub in self.subjanelas:
            sub.atualizar_status()
            falha_detectada |= not sub.estado_ok

        # Atualiza a label principal do bloco SI
        alarme_widget = self.janela_opr.findChild(QtWidgets.QPushButton,
                                                  "alarminfra")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if not falha_detectada else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()

    def aba_infra(self):
        """."""
        try:
            self.janela_opr.janela_opr.setCurrentIndex(6)
        except Exception as e:
            logging.error(f"Erro ao mudar para aba INFRA: {e}")
