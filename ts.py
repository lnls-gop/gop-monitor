"""Lógica das subjanelas da Linha de Transporte LTS."""
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
    """Classe responsável pelo controle do sistema de temperatura LTB."""

    def plot_graph(self, url):
        """."""
        try:
            subprocess.Popen(["firefox", url])
        except Exception as e:
            logging.error(f"Erro ao abrir gráfico de temperaturas: {e}")

    def __init__(self, janela_opr, botao_menu):
        """."""
        self.ranges = ranges_manager.get_ranges("lts")
        super().__init__(janela_opr, botao_menu, "ui/templts.ui", "temp")

        # Conectar botão de configuração de ranges
        self.uiobj.btnltsRanges.clicked.connect(self.abrir_config_ranges)

        # Atualiza labels da subjanela com ranges persistentes
        self._atualizar_labels_ranges()

        # Conectar botões de gráfico (como já existia)
        url = self.create_archviewer_link(self.sinais['Septts01'])
        self.uiobj.btnseptts01.clicked.connect(lambda _, url=url: self.
                                               plot_graph(url))

        url = self.create_archviewer_link(self.sinais['SeptEje'])
        self.uiobj.btnsepteje.clicked.connect(lambda _, url=url: self.
                                              plot_graph(url))

        url = self.create_archviewer_link(self.sinais['Septts04'])
        self.uiobj.btnseptts04.clicked.connect(lambda _, url=url: self.
                                               plot_graph(url))

        url = self.create_archviewer_link(self.sinais['Septts04b'])
        self.uiobj.btnseptts04b.clicked.connect(lambda _, url=url: self.
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
                    f"Label {label_name} não encontrada em templts.ui"
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
        ranges_manager.update_range("lts", grupo, min_val, max_val)

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
            'Septts01': {
                'TS-01:VA-PT100-BG1:Temp-Mon':
                (self._gwidget('led_ltsbg1'), *self.ranges['Septts01']),
                'TS-01:VA-PT100-BG2:Temp-Mon':
                (self._gwidget('led_ltsbg2'), *self.ranges['Septts01']),
                'TS-01:VA-PT100-BG3:Temp-Mon':
                (self._gwidget('led_ltsbg3'), *self.ranges['Septts01']),
                'TS-01:VA-PT100-BG4:Temp-Mon':
                (self._gwidget('led_ltsbg4'), *self.ranges['Septts01']),
            },
            'SeptEje': {
                'TS-01:PU-EjeSF-BG:Temp-Mon':
                (self._gwidget('led_ejesfbg'), *self.ranges['SeptEje']),
                'TS-01:PU-EjeSG-BG:Temp-Mon':
                (self._gwidget('led_ejesgbg'), *self.ranges['SeptEje']),
                'TS-01:PU-EjeSF-ED:Temp-Mon':
                (self._gwidget('led_ejesfed'), *self.ranges['SeptEje']),
                'TS-01:PU-EjeSG-ED:Temp-Mon':
                (self._gwidget('led_ejesged'), *self.ranges['SeptEje']),
            },
            'Septts04': {
                'TS-04:VA-PT100-ED1:Temp-Mon':
                (self._gwidget('led_ltsed1'), *self.ranges['Septts04']),
                'TS-04:VA-PT100-ED2:Temp-Mon':
                (self._gwidget('led_ltsed2'), *self.ranges['Septts04']),
                'TS-04:VA-PT100-ED3:Temp-Mon':
                (self._gwidget('led_ltsed3'), *self.ranges['Septts04']),
                'TS-04:VA-PT100-ED4:Temp-Mon':
                (self._gwidget('led_ltsed4'), *self.ranges['Septts04']),
                'TS-04:VA-PT100-ED5:Temp-Mon':
                (self._gwidget('led_ltsed5'), *self.ranges['Septts04']),
                'TS-04:VA-PT100-ED6:Temp-Mon':
                (self._gwidget('led_ltsed6'), *self.ranges['Septts04']),
            },
            'Septts04b': {
                'TS-MBTemp-03-CH1':
                (self._gwidget('led_ltsch1'), *self.ranges['Septts04b']),
                'TS-MBTemp-03-CH2':
                (self._gwidget('led_ltsch2'), *self.ranges['Septts04b']),
                'TS-MBTemp-03-CH3':
                (self._gwidget('led_ltsch3'), *self.ranges['Septts04b']),
                'TS-MBTemp-03-CH4':
                (self._gwidget('led_ltsch4'), *self.ranges['Septts04b']),
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
