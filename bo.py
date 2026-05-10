"""Logica das subjanelas do Booster."""
import logging
import subprocess
from PyQt5 import uic, QtWidgets
from ranges_manager import RangesManager
from utils import AlarmDelayController
import utils

ranges_manager = RangesManager()


class PowerSupply(utils.ConnWidgetPVs):
    """."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/psbo.ui", "estado")

    def _registrar_grupos(self):
        self.sinais = {
            'BO-Fam:PS-B-1:DiagStatus-Mon': (self._gwidget('led_bob1'), 0),
            # 'BO-Fam:PS-SD:DiagStatus-Mon': (self._gwidget('led_bosd'), 0),
            'BO-Fam:PS-B-2:DiagStatus-Mon': (self._gwidget('led_bob2'), 0),
            'BO-Fam:PS-QF:DiagStatus-Mon': (self._gwidget('led_boqf'), 0),
            'BO-Fam:PS-QD:DiagStatus-Mon': (self._gwidget('led_boqd'), 0),
            'BO-02D:PS-QS:DiagStatus-Mon': (self._gwidget('led_boqs'), 0),
            'BO-Fam:PS-SF:DiagStatus-Mon': (self._gwidget('led_bosf'), 0),
            'BO-01U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch01'), 0),
            'BO-03U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch03'), 0),
            'BO-05U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch05'), 0),
            'BO-07U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch07'), 0),
            'BO-09U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch09'), 0),
            'BO-11U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch11'), 0),
            'BO-13U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch13'), 0),
            'BO-15U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch15'), 0),
            'BO-17U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch17'), 0),
            'BO-19U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch19'), 0),
            'BO-21U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch21'), 0),
            'BO-23U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch23'), 0),
            'BO-25U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch25'), 0),
            'BO-27U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch27'), 0),
            'BO-29U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch29'), 0),
            'BO-31U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch31'), 0),
            'BO-33U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch33'), 0),
            'BO-35U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch35'), 0),
            'BO-37U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch37'), 0),
            'BO-39U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch39'), 0),
            'BO-41U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch41'), 0),
            'BO-43U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch43'), 0),
            'BO-45U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch45'), 0),
            'BO-47U:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch47'), 0),
            'BO-49D:PS-CH:DiagStatus-Mon': (self._gwidget('led_ch49'), 0),
            'BO-01U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv01'), 0),
            'BO-03U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv03'), 0),
            'BO-05U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv05'), 0),
            'BO-07U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv07'), 0),
            'BO-09U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv09'), 0),
            'BO-11U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv11'), 0),
            'BO-13U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv13'), 0),
            'BO-15U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv15'), 0),
            'BO-17U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv17'), 0),
            'BO-19U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv19'), 0),
            'BO-21U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv21'), 0),
            'BO-23U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv23'), 0),
            'BO-25U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv25'), 0),
            'BO-27U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv27'), 0),
            'BO-29U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv29'), 0),
            'BO-31U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv31'), 0),
            'BO-33U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv33'), 0),
            'BO-35U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv35'), 0),
            'BO-37U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv37'), 0),
            'BO-39U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv39'), 0),
            'BO-41U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv41'), 0),
            'BO-43U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv43'), 0),
            'BO-45U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv45'), 0),
            'BO-47U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv47'), 0),
            'BO-49U:PS-CV:DiagStatus-Mon': (self._gwidget('led_cv49'), 0),
        }


class Temperature(utils.ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura Booster."""

    def plot_graph(self, url):
        """."""
        try:
            subprocess.Popen(["firefox", url])
        except Exception as e:
            logging.error(f"Erro ao abrir gráfico de temperaturas: {e}")

    def __init__(self, janela_opr, botao_menu):
        """."""
        self.ranges = ranges_manager.get_ranges("bo")
        super().__init__(janela_opr, botao_menu, "ui/tempbo.ui", "temp")

        # Conectar botão de configuração de ranges
        self.uiobj.btnboRanges.clicked.connect(self.abrir_config_ranges)

        # Atualiza labels da subjanela com ranges persistentes
        self._atualizar_labels_ranges()

    def _atualizar_labels_ranges(self):
        """Atualiza todas as labels range_<grupo> com valores persistentes."""
        for grupo, (min_val, max_val) in self.ranges.items():
            label_name = f"range_{grupo}"
            lbl = self.uiobj.findChild(QtWidgets.QLabel, label_name)
            if lbl:
                lbl.setText(f"{min_val} – {max_val} °C")
            else:
                logging.warning(
                    f"Label {label_name} não encontrada em tempbo.ui"
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
        ranges_manager.update_range("bo", grupo, min_val, max_val)

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
            'Group01_05': {
                'BO-01U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam1'),
                                                *self.ranges['Group01_05']),
                'BO-01U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam2'),
                                                *self.ranges['Group01_05']),
                'BO-01U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam3'),
                                                *self.ranges['Group01_05']),
                'BO-02U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam4'),
                                                *self.ranges['Group01_05']),
                'BO-02U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam5'),
                                                *self.ranges['Group01_05']),
                'BO-02U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam6'),
                                                *self.ranges['Group01_05']),
                # 'BO-03U:VA-PT100-BG:Temp-Mon': self._gwidget('led_tempcam7'),
                # *self.ranges['Group01_05']),
                # 'BO-03U:VA-PT100-ED:Temp-Mon': self._gwidget('led_tempcam8'),
                # *self.ranges['Group01_05']), 18, 27),
                # 'BO-03U:VA-PT100-MD:Temp-Mon': self._gwidget('led_tempcam9'),
                # *self.ranges['Group01_05']), 18, 27),
                'BO-04U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam10'),
                                                *self.ranges['Group01_05']),
                'BO-04U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam11'),
                                                *self.ranges['Group01_05']),
                'BO-04U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam12'),
                                                *self.ranges['Group01_05']),
                'BO-05U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam13'),
                                                *self.ranges['Group01_05']),
                'BO-05U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam14'),
                                                *self.ranges['Group01_05']),
                'BO-05U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam15'),
                                                *self.ranges['Group01_05']),
            },
            'Group06_10': {
                'BO-06U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam16'),
                                                *self.ranges['Group06_10']),
                'BO-06U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam17'),
                                                *self.ranges['Group06_10']),
                'BO-06U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam18'),
                                                *self.ranges['Group06_10']),
                'BO-07U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam19'),
                                                *self.ranges['Group06_10']),
                'BO-07U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam20'),
                                                *self.ranges['Group06_10']),
                'BO-07U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam21'),
                                                *self.ranges['Group06_10']),
                'BO-08U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam22'),
                                                *self.ranges['Group06_10']),
                'BO-08U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam23'),
                                                *self.ranges['Group06_10']),
                'BO-08U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam24'),
                                                *self.ranges['Group06_10']),
                'BO-09U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam25'),
                                                *self.ranges['Group06_10']),
                'BO-09U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam26'),
                                                *self.ranges['Group06_10']),
                'BO-09U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam27'),
                                                *self.ranges['Group06_10']),
                'BO-10U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam28'),
                                                *self.ranges['Group06_10']),
                'BO-10U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam29'),
                                                *self.ranges['Group06_10']),
                'BO-10U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam30'),
                                                *self.ranges['Group06_10']),
            },
            'Group11_15': {
                'BO-11U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam31'),
                                                *self.ranges['Group11_15']),
                'BO-11U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam32'),
                                                *self.ranges['Group11_15']),
                'BO-11U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam33'),
                                                *self.ranges['Group11_15']),
                'BO-12U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam34'),
                                                *self.ranges['Group11_15']),
                'BO-12U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam35'),
                                                *self.ranges['Group11_15']),
                'BO-12U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam36'),
                                                *self.ranges['Group11_15']),
                'BO-13U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam37'),
                                                *self.ranges['Group11_15']),
                'BO-13U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam38'),
                                                *self.ranges['Group11_15']),
                'BO-13U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam39'),
                                                *self.ranges['Group11_15']),
                'BO-14U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam40'),
                                                *self.ranges['Group11_15']),
                'BO-14U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam41'),
                                                *self.ranges['Group11_15']),
                'BO-14U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam42'),
                                                *self.ranges['Group11_15']),
                'BO-15U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam43'),
                                                *self.ranges['Group11_15']),
                'BO-15U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam44'),
                                                *self.ranges['Group11_15']),
                'BO-15U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam45'),
                                                *self.ranges['Group11_15']),
            },
            'Group16_20': {
                'BO-16U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam46'),
                                                *self.ranges['Group16_20']),
                'BO-16U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam47'),
                                                *self.ranges['Group16_20']),
                'BO-16U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam48'),
                                                *self.ranges['Group16_20']),
                'BO-17U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam49'),
                                                *self.ranges['Group16_20']),
                'BO-17U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam50'),
                                                *self.ranges['Group16_20']),
                'BO-17U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam51'),
                                                *self.ranges['Group16_20']),
                'BO-18U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam52'),
                                                *self.ranges['Group16_20']),
                'BO-18U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam53'),
                                                *self.ranges['Group16_20']),
                'BO-18U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam54'),
                                                *self.ranges['Group16_20']),
                'BO-19U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam55'),
                                                *self.ranges['Group16_20']),
                'BO-19U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam56'),
                                                *self.ranges['Group16_20']),
                'BO-19U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam57'),
                                                *self.ranges['Group16_20']),
                'BO-20U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam58'),
                                                *self.ranges['Group16_20']),
                'BO-20U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam59'),
                                                *self.ranges['Group16_20']),
                'BO-20U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam60'),
                                                *self.ranges['Group16_20']),
            },
            'Group21_25': {
                'BO-21U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam61'),
                                                *self.ranges['Group21_25']),
                'BO-21U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam62'),
                                                *self.ranges['Group21_25']),
                'BO-21U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam63'),
                                                *self.ranges['Group21_25']),
                'BO-22U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam64'),
                                                *self.ranges['Group21_25']),
                'BO-22U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam65'),
                                                *self.ranges['Group21_25']),
                'BO-22U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam66'),
                                                *self.ranges['Group21_25']),
                'BO-23U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam67'),
                                                *self.ranges['Group21_25']),
                'BO-23U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam68'),
                                                *self.ranges['Group21_25']),
                'BO-23U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam69'),
                                                *self.ranges['Group21_25']),
                'BO-24U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam70'),
                                                *self.ranges['Group21_25']),
                'BO-24U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam71'),
                                                *self.ranges['Group21_25']),
                'BO-24U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam72'),
                                                *self.ranges['Group21_25']),
                'BO-25U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam73'),
                                                *self.ranges['Group21_25']),
                'BO-25U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam74'),
                                                *self.ranges['Group21_25']),
                'BO-25U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam75'),
                                                *self.ranges['Group21_25']),
            },
            'Group26_30': {
                'BO-26U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam76'),
                                                *self.ranges['Group26_30']),
                'BO-26U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam77'),
                                                *self.ranges['Group26_30']),
                'BO-26U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam78'),
                                                *self.ranges['Group26_30']),
                'BO-27U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam79'),
                                                *self.ranges['Group26_30']),
                'BO-27U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam80'),
                                                *self.ranges['Group26_30']),
                'BO-27U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam81'),
                                                *self.ranges['Group26_30']),
                'BO-28U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam82'),
                                                *self.ranges['Group26_30']),
                'BO-28U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam83'),
                                                *self.ranges['Group26_30']),
                'BO-28U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam84'),
                                                *self.ranges['Group26_30']),
                'BO-29U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam85'),
                                                *self.ranges['Group26_30']),
                'BO-29U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam86'),
                                                *self.ranges['Group26_30']),
                'BO-29U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam87'),
                                                *self.ranges['Group26_30']),
                'BO-30U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam88'),
                                                *self.ranges['Group26_30']),
                'BO-30U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam89'),
                                                *self.ranges['Group26_30']),
                'BO-30U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam90'),
                                                *self.ranges['Group26_30']),
            },
            'Group31_35': {
                'BO-31U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam91'),
                                                *self.ranges['Group31_35']),
                'BO-31U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam92'),
                                                *self.ranges['Group31_35']),
                'BO-31U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam93'),
                                                *self.ranges['Group31_35']),
                'BO-32U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam94'),
                                                *self.ranges['Group31_35']),
                'BO-32U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam95'),
                                                *self.ranges['Group31_35']),
                'BO-32U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam96'),
                                                *self.ranges['Group31_35']),
                'BO-33U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam97'),
                                                *self.ranges['Group31_35']),
                'BO-33U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam98'),
                                                *self.ranges['Group31_35']),
                'BO-33U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam99'),
                                                *self.ranges['Group31_35']),
                'BO-34U:VA-PT100-BG:Temp-Mon': (
                    self._gwidget('led_tempcam100'), *self.ranges['Group31_35']
                    ),
                'BO-34U:VA-PT100-ED:Temp-Mon': (
                    self._gwidget('led_tempcam101'), *self.ranges['Group31_35']
                    ),
                'BO-34U:VA-PT100-MD:Temp-Mon': (
                    self._gwidget('led_tempcam102'), *self.ranges['Group31_35']
                    ),
                'BO-35U:VA-PT100-BG:Temp-Mon': (
                    self._gwidget('led_tempcam103'), *self.ranges['Group31_35']
                    ),
                'BO-35U:VA-PT100-ED:Temp-Mon': (
                    self._gwidget('led_tempcam104'), *self.ranges['Group31_35']
                    ),
                'BO-35U:VA-PT100-MD:Temp-Mon': (
                    self._gwidget('led_tempcam105'), *self.ranges['Group31_35']
                    ),
            },
            'Group36_40': {
                'BO-36U:VA-PT100-BG:Temp-Mon': (
                    self._gwidget('led_tempcam106'), *self.ranges['Group36_40']
                    ),
                'BO-36U:VA-PT100-ED:Temp-Mon': (
                    self._gwidget('led_tempcam107'), *self.ranges['Group36_40']
                    ),
                'BO-36U:VA-PT100-MD:Temp-Mon': (
                    self._gwidget('led_tempcam108'), *self.ranges['Group36_40']
                    ),
                'BO-37U:VA-PT100-BG:Temp-Mon': (
                    self._gwidget('led_tempcam109'), *self.ranges['Group36_40']
                    ),
                'BO-37U:VA-PT100-ED:Temp-Mon': (
                    self._gwidget('led_tempcam110'), *self.ranges['Group36_40']
                    ),
                'BO-37U:VA-PT100-MD:Temp-Mon': (
                    self._gwidget('led_tempcam111'), *self.ranges['Group36_40']
                    ),
                'BO-38U:VA-PT100-BG:Temp-Mon': (
                    self._gwidget('led_tempcam112'), *self.ranges['Group36_40']
                    ),
                'BO-38U:VA-PT100-ED:Temp-Mon': (
                    self._gwidget('led_tempcam113'), *self.ranges['Group36_40']
                    ),
                'BO-38U:VA-PT100-MD:Temp-Mon': (
                    self._gwidget('led_tempcam114'), *self.ranges['Group36_40']
                    ),
                'BO-39U:VA-PT100-BG:Temp-Mon': (
                    self._gwidget('led_tempcam115'), *self.ranges['Group36_40']
                    ),
                'BO-39U:VA-PT100-ED:Temp-Mon': (
                    self._gwidget('led_tempcam116'), *self.ranges['Group36_40']
                    ),
                'BO-39U:VA-PT100-MD:Temp-Mon': (
                    self._gwidget('led_tempcam117'), *self.ranges['Group36_40']
                    ),
                'BO-40U:VA-PT100-BG:Temp-Mon': (
                    self._gwidget('led_tempcam118'), *self.ranges['Group36_40']
                    ),
                'BO-40U:VA-PT100-ED:Temp-Mon': (
                    self._gwidget('led_tempcam119'), *self.ranges['Group36_40']
                    ),
                'BO-40U:VA-PT100-MD:Temp-Mon': (
                    self._gwidget('led_tempcam120'), *self.ranges['Group36_40']
                    ),
            },
            'Group41_45': {
                'BO-41U:VA-PT100-BG:Temp-Mon': (
                    self._gwidget('led_tempcam121'), *self.ranges['Group41_45']
                    ),
                'BO-41U:VA-PT100-ED:Temp-Mon': (
                    self._gwidget('led_tempcam122'), *self.ranges['Group41_45']
                    ),
                'BO-41U:VA-PT100-MD:Temp-Mon': (
                    self._gwidget('led_tempcam123'), *self.ranges['Group41_45']
                    ),
                # 'BO-42U:VA-PT100-BG:Temp-Mon': (
                #     self._gwidget('led_tempcam124'), *self.ranges
                # ['Group41_45']
                #     ),
                # 'BO-42U:VA-PT100-ED:Temp-Mon': (
                #     self._gwidget('led_tempcam125'), *self.ranges
                # ['Group41_45']
                #     ),
                # 'BO-42U:VA-PT100-MD:Temp-Mon': (
                #     self._gwidget('led_tempcam126'), *self.ranges
                # ['Group41_45']
                #     ),
                # 'BO-43U:VA-PT100-BG:Temp-Mon': (
                #     self._gwidget('led_tempcam127'), *self.ranges
                # ['Group41_45']
                #     ),
                # 'BO-43U:VA-PT100-ED:Temp-Mon': (
                #     self._gwidget('led_tempcam128'), *self.ranges
                # ['Group41_45']
                #     ),
                # 'BO-43U:VA-PT100-MD:Temp-Mon': (
                #     self._gwidget('led_tempcam129'), *self.ranges
                # ['Group41_45']
                #     ),
                # 'BO-44U:VA-PT100-BG:Temp-Mon': (
                #     self._gwidget('led_tempcam130'), *self.ranges
                # ['Group41_45']
                #     ),
                # 'BO-44U:VA-PT100-ED:Temp-Mon': (
                #     self._gwidget('led_tempcam131'), *self.ranges
                # ['Group41_45']
                #     ),
                # 'BO-44U:VA-PT100-MD:Temp-Mon': (
                #     self._gwidget('led_tempcam132'), *self.ranges
                # ['Group41_45']
                #     ),
                # 'BO-45U:VA-PT100-BG:Temp-Mon': (
                #     self._gwidget('led_tempcam133'), *self.ranges
                # ['Group41_45']
                #     ),
                # 'BO-45U:VA-PT100-ED:Temp-Mon': (
                #     self._gwidget('led_tempcam134'), *self.ranges
                # ['Group41_45']
                #     ),
                # 'BO-45U:VA-PT100-MD:Temp-Mon': (
                #     self._gwidget('led_tempcam135'), *self.ranges
                # ['Group41_45']
                #     ),
            },
            'Group46_50': {
                # 'BO-46U:VA-PT100-BG:Temp-Mon': (
                #     self._gwidget('led_tempcam136'), *self.ranges
                # ['Group46_50']
                #     ),
                # 'BO-46U:VA-PT100-ED:Temp-Mon': (
                #     self._gwidget('led_tempcam137'), *self.ranges
                # ['Group46_50']
                #     ),
                # 'BO-46U:VA-PT100-MD:Temp-Mon': (
                #     self._gwidget('led_tempcam138'), *self.ranges
                # ['Group46_50']
                #     ),
                'BO-47U:VA-PT100-BG:Temp-Mon': (
                    self._gwidget('led_tempcam139'), *self.ranges['Group46_50']
                    ),
                'BO-47U:VA-PT100-ED:Temp-Mon': (
                    self._gwidget('led_tempcam140'), *self.ranges['Group46_50']
                    ),
                'BO-47U:VA-PT100-MD:Temp-Mon': (
                    self._gwidget('led_tempcam141'), *self.ranges['Group46_50']
                    ),
                'BO-48U:VA-PT100-BG:Temp-Mon': (
                    self._gwidget('led_tempcam142'), *self.ranges['Group46_50']
                    ),
                'BO-48U:VA-PT100-ED:Temp-Mon': (
                    self._gwidget('led_tempcam143'), *self.ranges['Group46_50']
                    ),
                'BO-48U:VA-PT100-MD:Temp-Mon': (
                    self._gwidget('led_tempcam144'), *self.ranges['Group46_50']
                    ),
                'BO-49U:VA-PT100-BG:Temp-Mon': (
                    self._gwidget('led_tempcam145'), *self.ranges['Group46_50']
                    ),
                # 'BO-49U:VA-PT100-ED:Temp-Mon': (
                # self._gwidget('led_tempcam146'), *self.ranges['Group46_50']),
                'BO-49U:VA-PT100-MD:Temp-Mon': (
                    self._gwidget('led_tempcam147'), *self.ranges['Group46_50']
                    ),
                'BO-50U:VA-PT100-BG:Temp-Mon': (
                    self._gwidget('led_tempcam148'), *self.ranges['Group46_50']
                    ),
                'BO-50U:VA-PT100-ED:Temp-Mon': (
                    self._gwidget('led_tempcam149'), *self.ranges['Group46_50']
                    ),
                'BO-50U:VA-PT100-MD:Temp-Mon': (
                    self._gwidget('led_tempcam150'), *self.ranges['Group46_50']
                    ),
            }
        }


class Vacuum(utils.ConnWidgetPVs):
    """Controle da subjanela de leitura de vácuo do Linac."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/vacbo.ui", "vacuo")

    def _registrar_grupos(self):
        """Registra Pvs de vacuo e seus leds correspondentes."""
        self.sinais = {
            'BO-01U:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_ccg01'), 1.0e-7),
            'BO-04U:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_ccg04'), 1.0e-7),
            'BO-05D:VA-CCG-RFC:Pressure-Mon':
            (self._gwidget('led_ccg05'), 1.0e-7),
            'BO-06U:VA-CCG-ED:Pressure-Mon':
            (self._gwidget('led_ccg06'), 1.0e-7),
            'BO-09U:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_ccg09'), 1.0e-7),
            'BO-11U:VA-CCG-ED:Pressure-Mon':
            (self._gwidget('led_ccg11'), 1.0e-7),
            'BO-14U:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_ccg14'), 1.0e-7),
            'BO-16U:VA-CCG-ED:Pressure-Mon':
            (self._gwidget('led_ccg16'), 1.0e-7),
            'BO-19U:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_ccg19'), 1.0e-7),
            'BO-21U:VA-CCG-ED:Pressure-Mon':
            (self._gwidget('led_ccg21'), 1.0e-7),
            'BO-24U:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_ccg24'), 1.0e-7),
            'BO-26U:VA-CCG-ED:Pressure-Mon':
            (self._gwidget('led_ccg26'), 1.0e-7),
            'BO-29U:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_ccg29'), 1.0e-7),
            'BO-31U:VA-CCG-ED:Pressure-Mon':
            (self._gwidget('led_ccg31'), 1.0e-7),
            'BO-34U:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_ccg34'), 1.0e-7),
            'BO-36U:VA-CCG-ED:Pressure-Mon':
            (self._gwidget('led_ccg36'), 1.0e-7),
            'BO-39U:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_ccg39'), 1.0e-7),
            'BO-41U:VA-CCG-ED:Pressure-Mon':
            (self._gwidget('led_ccg41'), 1.0e-7),
            'BO-44U:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_ccg44'), 1.0e-7),
            'BO-46U:VA-CCG-ED:Pressure-Mon':
            (self._gwidget('led_ccg46'), 1.0e-7),
            'BO-47U:VA-CCG-ED:Pressure-Mon':
            (self._gwidget('led_ccg47'), 1.0e-7),
            'BO-01U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_1'), 1.0e-7),
            'BO-02U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_2'), 1.0e-7),
            'BO-03U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_3'), 1.0e-7),
            'BO-04U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_4'), 1.0e-7),
            'BO-05U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_5'), 1.0e-7),
            'BO-06U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_6'), 1.0e-7),
            'BO-07U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_7'), 1.0e-7),
            'BO-08U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_8'), 1.0e-7),
            'BO-09U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_9'), 1.0e-7),
            'BO-10U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_10'), 1.0e-7),
            'BO-11U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_11'), 1.0e-7),
            'BO-12U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_12'), 1.0e-7),
            'BO-01D:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_51'), 1.0e-7),
            'BO-13U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_13'), 1.0e-7),
            'BO-14U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_14'), 1.0e-7),
            'BO-15U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_15'), 1.0e-7),
            'BO-16U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_16'), 1.0e-7),
            'BO-17U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_17'), 1.0e-7),
            'BO-18U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_18'), 1.0e-7),
            'BO-19U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_19'), 1.0e-7),
            'BO-20U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_20'), 1.0e-7),
            'BO-21U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_21'), 1.0e-7),
            'BO-22U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_22'), 1.0e-7),
            'BO-23U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_23'), 1.0e-7),
            'BO-24U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_24'), 1.0e-7),
            'BO-25U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_25'), 1.0e-7),
            'BO-26U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_26'), 1.0e-7),
            'BO-27U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_27'), 1.0e-7),
            'BO-28U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_28'), 1.0e-7),
            'BO-29U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_29'), 1.0e-7),
            'BO-30U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_30'), 1.0e-7),
            'BO-31U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_31'), 1.0e-7),
            'BO-32U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_32'), 1.0e-7),
            'BO-33U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_33'), 1.0e-7),
            'BO-34U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_34'), 1.0e-7),
            'BO-35U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_35'), 1.0e-7),
            'BO-36U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_36'), 1.0e-7),
            'BO-37U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_37'), 1.0e-7),
            'BO-38U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_38'), 1.0e-7),
            'BO-39U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_39'), 1.0e-7),
            'BO-40U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_40'), 1.0e-7),
            'BO-41U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_41'), 1.0e-7),
            'BO-42U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_42'), 1.0e-7),
            'BO-43U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_43'), 1.0e-7),
            'BO-44U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_44'), 1.0e-7),
            'BO-45U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_45'), 1.0e-7),
            'BO-46U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_46'), 1.0e-7),
            'BO-47U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_47'), 1.0e-7),
            'BO-48U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_48'), 1.0e-7),
            'BO-49U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_49'), 1.0e-7),
            'BO-50U:VA-SIP20-BG:Pressure-Mon':
            (self._gwidget('led_sip20_50'), 1.0e-7),
        }


class Cavity(utils.ConnWidgetPVs):
    """Controle das fontes de potencia do Booster."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/bocavity.ui", "temp")

    def _registrar_grupos(self):
        self.sinais = {
            'BO-05D:RF-P5Cav:Cylin1T-Mon': (self._gwidget('led_cylin1'), 27,
                                            29),
            'BO-05D:RF-P5Cav:Cylin2T-Mon': (self._gwidget('led_cylin2'), 27,
                                            29),
            'BO-05D:RF-P5Cav:Cylin3T-Mon': (self._gwidget('led_cylin3'), 27,
                                            29),
            'BO-05D:RF-P5Cav:Cylin4T-Mon': (self._gwidget('led_cylin4'), 27,
                                            29),
            'BO-05D:RF-P5Cav:Cylin5T-Mon': (self._gwidget('led_cylin5'), 27,
                                            29),
            # 'RA-TLBO:RF-Circulator:TinUp-Mon': (self._gwidget
            # ('led_circulator1'), 19, 22),
            'RA-TLBO:RF-Circulator:Tin-Mon': (self._gwidget
                                              ('led_circulator2'), 19, 22),
            'RA-TLBO:RF-Circulator:Tout-Mon': (self._gwidget
                                               ('led_circulator3'), 19, 22),
            'RA-ToBO:RF-HeatSink-H01:T-Mon': (self._gwidget('led_tempamp1'),
                                              20, 24),
            'RA-ToBO:RF-HeatSink-H02:T-Mon': (self._gwidget('led_tempamp2'),
                                              20, 24),
            'RA-ToBO:RF-HeatSink-H03:T-Mon': (self._gwidget('led_tempamp3'),
                                              20, 24),
            'RA-ToBO:RF-HeatSink-H04:T-Mon': (self._gwidget('led_tempamp4'),
                                              20, 24),
            'RA-ToBO:RF-HeatSink-H05:T-Mon': (self._gwidget('led_tempamp5'),
                                              20, 24),
        }


class AllSubsys:
    """Gerencia o grupo LTB e atualiza a label alarmltb."""

    def __init__(self, janela_opr=None):
        """."""
        if janela_opr:
            janela_opr.alarmbo.clicked.connect(self.aba_booster)
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto
        self.vacbo = Vacuum(janela_opr, janela_opr.btnvacbo)
        self.tempbo = Temperature(janela_opr, janela_opr.btntempbo)
        self.psbo = PowerSupply(janela_opr, janela_opr.btnpsbo)
        self.bocavity = Cavity(janela_opr, janela_opr.btnbocavity)

        # Adiciona todas as subjanelas à lista
        self.subjanelas.extend([
            self.vacbo,
            self.tempbo,
            self.psbo,
            self.bocavity,
        ])

        # Usa controlador centralizado para btntemplinac → alarmlinac
        self.alarm_ctrl = AlarmDelayController(
            janela_opr,
            alarm_btn_name="alarmbo",
            delay_ms=3500
        )

        # Configura cada subjanela
        for sub in self.subjanelas:
            sub.configurar_sistema()

    def atualizar_grupo(self):
        """Atualiza as subjanelas e delega lógica ao controlador."""
        falha_detectada = False
        for sub in self.subjanelas:
            sub.atualizar_status()
            falha_detectada |= not sub.estado_ok

        # Usa controlador centralizado
        self.alarm_ctrl.atualizar(falha_detectada)

    def aba_booster(self):
        """."""
        try:
            self.janela_opr.janela_opr.setCurrentIndex(3)
        except Exception as e:
            logging.error(f"Erro ao mudar para aba LTB: {e}")
