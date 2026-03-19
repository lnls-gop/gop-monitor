"""Lógica das subjanelas da Linha de Transporte LTB."""
import logging
import subprocess
from PyQt5 import uic, QtWidgets
from ranges_manager import RangesManager

import utils

ranges_manager = RangesManager()


class Vacuum(utils.ConnWidgetPVs):
    """Controle da subjanela de leitura de vácuo do Linac."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/vacltb.ui", "vacuo")

    def _registrar_grupos(self):
        """Registra Pvs de vacuo e seus leds correspondentes."""
        self.sinais = {
            'TB-01:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('ledvacltb01'), 1.0e-7),
            'TB-01:VA-SIP20-ED:Pressure-Mon':
            (self._gwidget('ledvacltb02'), 1.0e-7),
            'TB-02:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('ledvacltb03'), 1.0e-7),
            'TB-02:VA-SIP20-ED:Pressure-Mon':
            (self._gwidget('ledvacltb04'), 1.0e-7),
            'TB-02:VA-SIP20-MD:Pressure-Mon':
            (self._gwidget('ledvacltb05'), 1.0e-7),
            'TB-03:VA-SIP20-ED:Pressure-Mon':
            (self._gwidget('ledvacltb06'), 1.0e-7),
            'TB-04:VA-SIP20-ED:Pressure-Mon':
            (self._gwidget('ledvacltb07'), 1.0e-7),
        }


class PowerSupply(utils.ConnWidgetPVs):
    """."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/psltb.ui", "estado")

    def _registrar_grupos(self):
        self.sinais = {
            'TB-Fam:PS-B:DiagStatus-Mon': (self._gwidget('led_statusb'), 0),
            'TB-01:PS-QD1:DiagStatus-Mon': (self._gwidget('led_statusqd1'), 0),
            'TB-02:PS-QD2A:DiagStatus-Mon': (self._gwidget('led_statusqd2a'),
                                             0),
            'TB-02:PS-QD2B:DiagStatus-Mon': (self._gwidget('led_statusqd2b'),
                                             0),
            'TB-03:PS-QD3:DiagStatus-Mon': (self._gwidget('led_statusqd3'), 0),
            'TB-04:PS-QD4:DiagStatus-Mon': (self._gwidget('led_statusqd4'), 0),
            'TB-01:PS-QF1:DiagStatus-Mon': (self._gwidget('led_statusqf1'), 0),
            'TB-02:PS-QF2A:DiagStatus-Mon': (self._gwidget('led_statusqf2a'),
                                             0),
            'TB-02:PS-QF2B:DiagStatus-Mon': (self._gwidget('led_statusqf2b'),
                                             0),
            'TB-03:PS-QF3:DiagStatus-Mon': (self._gwidget('led_statusqf3'), 0),
            'TB-04:PS-QF4:DiagStatus-Mon': (self._gwidget('led_statusqf4'), 0),
            'TB-01:PS-CH-1:DiagStatus-Mon': (self._gwidget('led_ch1_01'), 0),
            'TB-01:PS-CH-2:DiagStatus-Mon': (self._gwidget('led_ch2_01'), 0),
            'TB-02:PS-CH-1:DiagStatus-Mon': (self._gwidget('led_ch1_02'), 0),
            'TB-02:PS-CH-2:DiagStatus-Mon': (self._gwidget('led_ch2_02'), 0),
            'TB-04:PS-CH-1:DiagStatus-Mon': (self._gwidget('led_ch1_04'), 0),
            'TB-04:PS-CH-2:DiagStatus-Mon': (self._gwidget('led_ch2_04'), 0),
            'TB-01:PS-CV-1:DiagStatus-Mon': (self._gwidget('led_cv1_01'), 0),
            'TB-01:PS-CV-2:DiagStatus-Mon': (self._gwidget('led_cv2_01'), 0),
            'TB-02:PS-CV-1:DiagStatus-Mon': (self._gwidget('led_cv1_02'), 0),
            'TB-02:PS-CV-2:DiagStatus-Mon': (self._gwidget('led_cv2_02'), 0),
            'TB-04:PS-CV-1:DiagStatus-Mon': (self._gwidget('led_cv1_04'), 0),
            'TB-04:PS-CV-2:DiagStatus-Mon': (self._gwidget('led_cv2_04'), 0),
        }


class Temperature(utils.ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura LINAC."""

    def plot_graph(self, url):
        """."""
        try:
            subprocess.Popen(["firefox", url])
        except Exception as e:
            logging.error(f"Erro ao abrir gráfico de temperaturas: {e}")

    def __init__(self, janela_opr, botao_menu):
        """."""
        self.ranges = ranges_manager.get_ranges("users","tb")
        super().__init__(janela_opr, botao_menu, "ui/templtb.ui", "temp")

        # Conectar botão de configuração de ranges
        self.uiobj.btnltbRanges.clicked.connect(self.abrir_config_ranges)

        # Atualiza labels da subjanela com ranges persistentes
        self._atualizar_labels_ranges()

        # Conectar botões de gráfico (como já existia)
        url = self.create_archviewer_link(self.sinais['Septum'])
        self.uiobj.btntempsept.clicked.connect(lambda _, url=url: self.
                                               plot_graph(url))

        url = self.create_archviewer_link(self.sinais['Dipolo'])
        self.uiobj.btntempdip.clicked.connect(lambda _, url=url: self.
                                              plot_graph(url))

        url = self.create_archviewer_link(self.sinais['Board'])
        self.uiobj.btntempboard.clicked.connect(lambda _, url=url: self.
                                                plot_graph(url))

    def _atualizar_labels_ranges(self):
        """Atualiza todas as labels range_<grupo> com valores persistentes."""
        for grupo, (min_val, max_val) in self.ranges.items():
            label_name = f"range_{grupo}"
            lbl = self.uiobj.findChild(QtWidgets.QLabel, label_name)
            if lbl:
                lbl.setText(f"{min_val} – {max_val} °C")
            else:
                logging.warning(
                    f"Label {label_name} não encontrada em templtb.ui"
                    )

    def abrir_config_ranges(self):
        """Abre subjanela de configuração de ranges."""
        self.config_ui = uic.loadUi("ui/configranges.ui")

        # Preenche combo com todos os grupos
        self.config_ui.comboGrupos.addItems(self.ranges.keys())

        # Conecta eventos
        self.config_ui.comboGrupos.currentTextChanged.connect(
            self.atualizar_spinboxes
        )
        self.config_ui.btnSalvar.clicked.connect(self.salvar_range)
        self.config_ui.btnFechar.clicked.connect(self.config_ui.close)

        # Força seleção do primeiro grupo
        self.config_ui.comboGrupos.setCurrentIndex(0)
        grupo_inicial = self.config_ui.comboGrupos.itemText(0)
        self.atualizar_spinboxes(grupo_inicial)

        self.config_ui.show()

    def atualizar_spinboxes(self, grupo):
        """Atualiza spinboxes com valores atuais do grupo selecionado."""
        min_val, max_val = self.ranges[grupo]
        self.config_ui.spinMin.setValue(min_val)
        self.config_ui.spinMax.setValue(max_val)
        self.config_ui.lblRangeAtual.setText(
            f"Range atual: {min_val:.2f} -{max_val:.2f} °C")

    def salvar_range(self):
        """."""
        grupo = self.config_ui.comboGrupos.currentText()
        min_val = round(float(self.config_ui.spinMin.value()), 2)
        max_val = round(float(self.config_ui.spinMax.value()), 2)

        # atualiza local
        self.ranges[grupo] = (min_val, max_val)

        # atualiza global
        ranges_manager.update_range("tb", grupo, min_val, max_val)

        self.config_ui.lblRangeAtual.setText(
            f"Current Range: {min_val:.2f} – {max_val:.2f} °C"
            )

        # Atualiza label da subjanela templinac.ui
        label_name = f"range_{grupo}"
        lbl_principal = self.uiobj.findChild(QtWidgets.QLabel, label_name)
        if lbl_principal:
            lbl_principal.setText(f"{min_val:.2f} – {max_val:.2f} °C")

        self._registrar_grupos()
        self.atualizar_status()

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        self.sinais = {
            'Septum': {
                'TB-04:VA-PT100-ED1:Temp-Mon':
                (self._gwidget('ledtemp_ltb1'), *self.ranges['Septum']),
                'TB-04:VA-PT100-ED2:Temp-Mon':
                (self._gwidget('ledtemp_ltb2'), *self.ranges['Septum']),
            },
            'Dipolo': {
                'TB-Fam:PS-B:HeatSinkTemperatureIIB-Mon':
                (self._gwidget('led_heatsink'), *self.ranges['Dipolo']),
                'TB-Fam:PS-B:InductorTemperatureIIB-Mon':
                (self._gwidget('led_inductor'), *self.ranges['Dipolo']),
            },
            'Board': {
                'TB-Fam:PS-B:BoardTemperatureIIB-Mon':
                (self._gwidget('led_board'), *self.ranges['Board']),
            },
        }


class AllSubsys:
    """Gerencia o grupo LTB e atualiza a label alarmltb."""

    def __init__(self, janela_opr):
        """."""
        janela_opr.alarmltb.clicked.connect(self.aba_ltb)
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto
        self.templtb = Temperature(janela_opr, janela_opr.btntempltb)
        self.vacltb = Vacuum(janela_opr, janela_opr.btnvacltb)
        self.psltb = PowerSupply(janela_opr, janela_opr.btnpsltb)

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
            falha_detectada |= not sub.estado_ok

        # Atualiza a label principal do bloco LTB
        alarme_widget = self.janela_opr.findChild(QtWidgets.QPushButton,
                                                  "alarmltb")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if not falha_detectada else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()

    def aba_ltb(self):
        """."""
        try:
            self.janela_opr.janela_opr.setCurrentIndex(2)
        except Exception as e:
            logging.error(f"Erro ao mudar para aba LTB: {e}")
