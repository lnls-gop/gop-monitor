"""Logica das subjanelas do Anel de Armazenamento."""
from PyQt5 import QtWidgets
import utils
import logging


class Sivac(utils.ConnWidgetPVs):
    """Controle da subjanela de leitura de vácuo do Anel."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/vacsi.ui", "vacuo")

    def _registrar_grupos(self):
        """Registra Pvs de vacuo e seus leds correspondentes."""
        self.sinais = {
            'SI-01C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac01c1'), 1.0e-7),
            'SI-01C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac01c3'), 1.0e-7),
            'SI-01SA:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac01sa'), 1.0e-7),
            'SI-02C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac02c1'), 1.0e-7),
            'SI-02C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac02c3'), 1.0e-7),
            'SI-02SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac02sb'), 1.0e-7),
            'SI-03C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac03c1'), 1.0e-7),
            'SI-03C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac03c3'), 1.0e-7),
            'SI-03SP:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac03sp'), 1.0e-7),
            'SI-04C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac04c1'), 1.0e-7),
            'SI-04C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac04c3'), 1.0e-7),
            'SI-04SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac04sb'), 1.0e-7),
            'SI-05C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac05c1'), 1.0e-7),
            'SI-05C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac05c3'), 1.0e-7),
            'SI-05SA:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac05sa'), 1.0e-7),
            'SI-06C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac06c1'), 1.0e-7),
            'SI-06C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac06c3'), 1.0e-7),
            'SI-06SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac06sb'), 1.0e-7),
            'SI-07C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac07c1'), 1.0e-7),
            'SI-07C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac07c3'), 1.0e-7),
            'SI-07SP:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac07sp'), 1.0e-7),
            'SI-08C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac08c1'), 1.0e-7),
            'SI-08C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac08c3'), 1.0e-7),
            'SI-08SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac08sb'), 1.0e-7),
            'SI-09C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac09c1'), 1.0e-7),
            'SI-09C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac09c3'), 1.0e-7),
            'SI-09SA:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac09sa'), 1.0e-7),
            'SI-10C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac10c1'), 1.0e-7),
            'SI-10C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac10c3'), 1.0e-7),
            'SI-10SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac10sb'), 1.0e-7),
            'SI-11C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac11c1'), 1.0e-7),
            'SI-11C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac11c3'), 1.0e-7),
            'SI-11SP:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac11sp'), 1.0e-7),
            'SI-12C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac12c1'), 1.0e-7),
            'SI-12C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac12c3'), 1.0e-7),
            'SI-12SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac12sb'), 1.0e-7),
            'SI-13C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac13c1'), 1.0e-7),
            'SI-13C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac13c3'), 1.0e-7),
            'SI-13SA:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac13sa'), 1.0e-7),
            'SI-14C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac14c1'), 1.0e-7),
            'SI-14C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac14c3'), 1.0e-7),
            'SI-14SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac14sb'), 1.0e-7),
            'SI-15C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac15c1'), 1.0e-7),
            'SI-15C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac15c3'), 1.0e-7),
            'SI-15SP:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac15sp'), 1.0e-7),
            'SI-16C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac16c1'), 1.0e-7),
            'SI-16C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac16c3'), 1.0e-7),
            'SI-16SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac16sb'), 1.0e-7),
            'SI-17C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac17c1'), 1.0e-7),
            'SI-17C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac17c3'), 1.0e-7),
            'SI-17SA:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac17sa'), 1.0e-7),
            'SI-18C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac18c1'), 1.0e-7),
            'SI-18C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac18c3'), 1.0e-7),
            'SI-18SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac18sb'), 1.0e-7),
            'SI-19C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac19c1'), 1.0e-7),
            'SI-19C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac19c3'), 1.0e-7),
            'SI-19SP:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac19sp'), 1.0e-7),
            'SI-20C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac20c1'), 1.0e-7),
            'SI-20C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac20c3'), 1.0e-7),
            'SI-20SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac20sb'), 1.0e-7),
            'SI-01BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_01bcfe'), 1.0e-7),
            'SI-01C2FE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_01c2fe'), 1.0e-7),
            'SI-01SAFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_01safe'), 1.0e-7),
            'SI-02BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_02bcfe'), 1.0e-7),
            'SI-02SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_02sbfe'), 1.0e-7),
            'SI-03BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_03bcfe'), 1.0e-7),
            'SI-03C2FE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_03c2fe'), 1.0e-7),
            'SI-03SPFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_03spfe'), 1.0e-7),
            'SI-04BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_04bcfe'), 1.0e-7),
            'SI-04SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_04sbfe'), 1.0e-7),
            'SI-05BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_05bcfe'), 1.0e-7),
            'SI-05C2FE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_05c2fe'), 1.0e-7),
            'SI-05SAFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_05safe'), 1.0e-7),
            'SI-06BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_06bcfe'), 1.0e-7),
            'SI-06SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_06sbfe'), 1.0e-7),
            'SI-07BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_07bcfe'), 1.0e-7),
            'SI-07C2FE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_07c2fe'), 1.0e-7),
            'SI-07SPFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_07spfe'), 1.0e-7),
            'SI-08BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_08bcfe'), 1.0e-7),
            'SI-08SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_08sbfe'), 1.0e-7),
            'SI-09BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_09bcfe'), 1.0e-7),
            'SI-09C2FE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_09c2fe'), 1.0e-7),
            'SI-09SAFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_09safe'), 1.0e-7),
            'SI-10BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_10bcfe'), 1.0e-7),
            'SI-10SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_10sbfe'), 1.0e-7),
            'SI-11BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_11bcfe'), 1.0e-7),
            'SI-11C2FE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_11c2fe'), 1.0e-7),
            'SI-11SPFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_11spfe'), 1.0e-7),
            'SI-12BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_12bcfe'), 1.0e-7),
            'SI-12SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_12sbfe'), 1.0e-7),
            'SI-13BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_13bcfe'), 1.0e-7),
            'SI-13C2FE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_13c2fe'), 1.0e-7),
            'SI-13SAFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_13safe'), 1.0e-7),
            'SI-14BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_14bcfe'), 1.0e-7),
            'SI-14SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_14sbfe'), 1.0e-7),
            'SI-15BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_15bcfe'), 1.0e-7),
            'SI-15C2FE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_15c2fe'), 1.0e-7),
            'SI-15SPFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_15spfe'), 1.0e-7),
            'SI-16BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_16bcfe'), 1.0e-7),
            'SI-16SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_16sbfe'), 1.0e-7),
            'SI-17BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_17bcfe'), 1.0e-7),
            'SI-17C2FE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_17c2fe'), 1.0e-7),
            'SI-17SAFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_17safe'), 1.0e-7),
            'SI-18BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_18bcfe'), 1.0e-7),
            'SI-18SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_18sbfe'), 1.0e-7),
            'SI-19BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_19bcfe'), 1.0e-7),
            'SI-19SPFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_19spfe'), 1.0e-7),
            'SI-20BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_20bcfe'), 1.0e-7),
            'SI-20SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_20sbfe'), 1.0e-7),
        }


class Blocosi:
    """Gerencia o grupo SI e atualiza a label alarmsi."""

    def __init__(self, janela_opr):
        """."""
        janela_opr.alarmsi.clicked.connect(self.aba_si)
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto
        self.vacsi = Sivac(janela_opr, janela_opr.btnvacsi)
        # self.cryoplant = Sicryo(janela_opr, janela_opr.btncryo)
        # self.cavitysi = Sicavity(janela_opr, janela_opr.btncavitysi)

        # Adiciona todas as subjanelas à lista
        self.subjanelas.extend([
            self.vacsi,
            # self.pwmsi,
            # self.cryoplant,
            # cavitysi
        ])

        # Configura cada subjanela
        for sub in self.subjanelas:
            sub.configurar_sistema()

    def atualizar_grupo(self):
        """Atualiza todas as subjanelas e a label alarmsi."""
        falha_detectada = False
        for sub in self.subjanelas:
            sub.atualizar_status()
            falha_detectada |= not sub.estado_ok

        # Atualiza a label principal do bloco LTS
        alarme_widget = self.janela_opr.findChild(QtWidgets.QPushButton,
                                                  "alarmsi")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if not falha_detectada else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()

    def aba_si(self):
        """."""
        try:
            self.janela_opr.janela_opr.setCurrentIndex(5)
        except Exception as e:
            logging.error(f"Erro ao mudar para aba LTB: {e}")
