"""Logica das subjanelas do Booster."""
from PyQt5 import QtWidgets
import utils
import logging


class Bops(utils.ConnWidgetPVs):
    """."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/psbo.ui", "estado")

    def _registrar_grupos(self):
        self.sinais = {
            'BO-Fam:PS-B-1:DiagStatus-Mon': (self._gwidget('led_bob1'), 0),
            'BO-Fam:PS-SD:DiagStatus-Mon': (self._gwidget('led_bosd'), 0),
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


class Botemp(utils.ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura Booster."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/tempbo.ui", "temp")

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        self.sinais = {
            'BO-01U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam1'), 18,
                                            26),
            'BO-01U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam2'), 18,
                                            26),
            'BO-01U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam3'), 18,
                                            26),
            'BO-02U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam4'), 18,
                                            26),
            'BO-02U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam5'), 18,
                                            26),
            'BO-02U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam6'), 18,
                                            26),
            'BO-03U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam7'), 18,
                                            26),
            'BO-03U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam8'), 18,
                                            26),
            'BO-03U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam9'), 18,
                                            26),
            'BO-04U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam10'),
                                            18, 26),
            'BO-04U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam11'),
                                            18, 26),
            'BO-04U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam12'),
                                            18, 26),
            'BO-05U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam13'),
                                            18, 26),
            'BO-05U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam14'),
                                            18, 26),
            'BO-05U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam15'),
                                            18, 26),
            'BO-06U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam16'),
                                            18, 26),
            'BO-06U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam17'),
                                            18, 26),
            'BO-06U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam18'),
                                            18, 26),
            'BO-07U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam19'),
                                            18, 26),
            'BO-07U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam20'),
                                            18, 26),
            'BO-07U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam21'),
                                            18, 26),
            'BO-08U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam22'),
                                            18, 26),
            'BO-08U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam23'),
                                            18, 26),
            'BO-08U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam24'),
                                            18, 26),
            'BO-09U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam25'),
                                            18, 26),
            'BO-09U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam26'),
                                            18, 26),
            'BO-09U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam27'),
                                            18, 26),
            'BO-10U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam28'),
                                            18, 26),
            'BO-10U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam29'),
                                            18, 26),
            'BO-10U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam30'),
                                            18, 26),
            'BO-11U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam31'),
                                            18, 26),
            'BO-11U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam32'),
                                            18, 26),
            'BO-11U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam33'),
                                            18, 26),
            'BO-12U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam34'),
                                            18, 26),
            'BO-12U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam35'),
                                            18, 26),
            'BO-12U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam36'),
                                            18, 26),
            'BO-13U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam37'),
                                            18, 26),
            'BO-13U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam38'),
                                            18, 26),
            'BO-13U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam39'),
                                            18, 26),
            'BO-14U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam40'),
                                            18, 26),
            'BO-14U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam41'),
                                            18, 26),
            'BO-14U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam42'),
                                            18, 26),
            'BO-15U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam43'),
                                            18, 26),
            'BO-15U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam44'),
                                            18, 26),
            'BO-15U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam45'),
                                            18, 26),
            'BO-16U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam46'),
                                            18, 26),
            'BO-16U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam47'),
                                            18, 26),
            'BO-16U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam48'),
                                            18, 26),
            'BO-17U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam49'),
                                            18, 26),
            'BO-17U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam50'),
                                            18, 26),
            'BO-17U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam51'),
                                            18, 26),
            'BO-18U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam52'),
                                            18, 26),
            'BO-18U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam53'),
                                            18, 26),
            'BO-18U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam54'),
                                            18, 26),
            'BO-19U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam55'),
                                            18, 26),
            'BO-19U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam56'),
                                            18, 26),
            'BO-19U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam57'),
                                            18, 26),
            'BO-20U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam58'),
                                            18, 26),
            'BO-20U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam59'),
                                            18, 26),
            'BO-20U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam60'),
                                            18, 26),
            'BO-21U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam61'),
                                            18, 26),
            'BO-21U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam62'),
                                            18, 26),
            'BO-21U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam63'),
                                            18, 26),
            'BO-22U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam64'),
                                            18, 26),
            'BO-22U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam65'),
                                            18, 26),
            'BO-22U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam66'),
                                            18, 26),
            'BO-23U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam67'),
                                            18, 26),
            'BO-23U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam68'),
                                            18, 26),
            'BO-23U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam69'),
                                            18, 26),
            'BO-24U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam70'),
                                            18, 26),
            'BO-24U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam71'),
                                            18, 26),
            'BO-24U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam72'),
                                            18, 26),
            'BO-25U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam73'),
                                            18, 26),
            'BO-25U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam74'),
                                            18, 26),
            'BO-25U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam75'),
                                            18, 26),
            'BO-26U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam76'),
                                            18, 26),
            'BO-26U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam77'),
                                            18, 26),
            'BO-26U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam78'),
                                            18, 26),
            'BO-27U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam79'),
                                            18, 26),
            'BO-27U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam80'),
                                            18, 26),
            'BO-27U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam81'),
                                            18, 26),
            'BO-28U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam82'),
                                            18, 26),
            'BO-28U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam83'),
                                            18, 26),
            'BO-28U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam84'),
                                            18, 26),
            'BO-29U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam85'),
                                            18, 26),
            'BO-29U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam86'),
                                            18, 26),
            'BO-29U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam87'),
                                            18, 26),
            'BO-30U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam88'),
                                            18, 26),
            'BO-30U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam89'),
                                            18, 26),
            'BO-30U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam90'),
                                            18, 26),
            'BO-31U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam91'),
                                            18, 26),
            'BO-31U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam92'),
                                            18, 26),
            'BO-31U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam93'),
                                            18, 26),
            'BO-32U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam94'),
                                            18, 26),
            'BO-32U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam95'),
                                            18, 26),
            'BO-32U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam96'),
                                            18, 26),
            'BO-33U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam97'),
                                            18, 26),
            'BO-33U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam98'),
                                            18, 26),
            'BO-33U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam99'),
                                            18, 26),
            'BO-34U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam100'),
                                            18, 26),
            'BO-34U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam101'),
                                            18, 26),
            'BO-34U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam102'),
                                            18, 26),
            'BO-35U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam103'),
                                            18, 26),
            'BO-35U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam104'),
                                            18, 26),
            'BO-35U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam105'),
                                            18, 26),
            'BO-36U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam106'),
                                            18, 26),
            'BO-36U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam107'),
                                            18, 26),
            'BO-36U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam108'),
                                            18, 26),
            'BO-37U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam109'),
                                            18, 26),
            'BO-37U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam110'),
                                            18, 26),
            'BO-37U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam111'),
                                            18, 26),
            'BO-38U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam112'),
                                            18, 26),
            'BO-38U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam113'),
                                            18, 26),
            'BO-38U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam114'),
                                            18, 26),
            'BO-39U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam115'),
                                            18, 26),
            'BO-39U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam116'),
                                            18, 26),
            'BO-39U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam117'),
                                            18, 26),
            'BO-40U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam118'),
                                            18, 26),
            'BO-40U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam119'),
                                            18, 26),
            'BO-40U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam120'),
                                            18, 26),
            'BO-41U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam121'),
                                            18, 26),
            'BO-41U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam122'),
                                            18, 26),
            'BO-41U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam123'),
                                            18, 26),
            'BO-42U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam124'),
                                            18, 26),
            'BO-42U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam125'),
                                            18, 26),
            'BO-42U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam126'),
                                            18, 26),
            'BO-43U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam127'),
                                            18, 26),
            'BO-43U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam128'),
                                            18, 26),
            'BO-43U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam129'),
                                            18, 26),
            'BO-44U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam130'),
                                            18, 26),
            'BO-44U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam131'),
                                            18, 26),
            'BO-44U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam132'),
                                            18, 26),
            'BO-45U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam133'),
                                            18, 26),
            'BO-45U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam134'),
                                            18, 26),
            'BO-45U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam135'),
                                            18, 26),
            'BO-46U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam136'),
                                            18, 26),
            'BO-46U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam137'),
                                            18, 26),
            'BO-46U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam138'),
                                            18, 26),
            'BO-47U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam139'),
                                            18, 26),
            'BO-47U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam140'),
                                            18, 26),
            'BO-47U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam141'),
                                            18, 26),
            'BO-48U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam142'),
                                            18, 26),
            'BO-48U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam143'),
                                            18, 26),
            'BO-48U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam144'),
                                            18, 26),
            'BO-49U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam145'),
                                            18, 26),
            'BO-49U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam146'),
                                            18, 26),
            'BO-49U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam147'),
                                            18, 26),
            'BO-50U:VA-PT100-BG:Temp-Mon': (self._gwidget('led_tempcam148'),
                                            18, 26),
            'BO-50U:VA-PT100-ED:Temp-Mon': (self._gwidget('led_tempcam149'),
                                            18, 26),
            'BO-50U:VA-PT100-MD:Temp-Mon': (self._gwidget('led_tempcam150'),
                                            18, 26),
        }


class Bovac(utils.ConnWidgetPVs):
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


class Bocavity(utils.ConnWidgetPVs):
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
            'RA-TLBO:RF-Circulator:TinUp-Mon': (self._gwidget
                                                ('led_circulator1'), 19, 22),
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


class Blocobo:
    """Gerencia o grupo LTB e atualiza a label alarmltb."""

    def __init__(self, janela_opr):
        """."""
        janela_opr.alarmbo.clicked.connect(self.aba_booster)
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto
        self.vacbo = Bovac(janela_opr, janela_opr.btnvacbo)
        self.tempbo = Botemp(janela_opr, janela_opr.btntempbo)
        self.psbo = Bops(janela_opr, janela_opr.btnpsbo)
        self.bocavity = Bocavity(janela_opr, janela_opr.btnbocavity)

        # Adiciona todas as subjanelas à lista
        self.subjanelas.extend([
            self.vacbo,
            self.tempbo,
            self.psbo,
            self.bocavity,
        ])

        # Configura cada subjanela
        for sub in self.subjanelas:
            sub.configurar_sistema()

    def atualizar_grupo(self):
        """Atualiza todas as subjanelas e a label alarmbo."""
        falha_detectada = False
        for sub in self.subjanelas:
            sub.atualizar_status()
            falha_detectada |= not sub.estado_ok

        # Atualiza a label principal do bloco LTS
        alarme_widget = self.janela_opr.findChild(QtWidgets.QPushButton,
                                                  "alarmbo")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if not falha_detectada else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()

    def aba_booster(self):
        """."""
        try:
            self.janela_opr.janela_opr.setCurrentIndex(3)
        except Exception as e:
            logging.error(f"Erro ao mudar para aba LTB: {e}")
