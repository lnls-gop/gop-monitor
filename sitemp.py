"""Logica das Temperaturas do Anel de Armazenamento."""
from PyQt5 import QtWidgets
import utils
import logging


class Si_circhid(utils.ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura Booster."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/tempcirchid.ui",
                         "temp")

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        self.sinais = {
            'SI-08-MBTemp-10-CH6': (self._gwidget('led10ch6'), 21, 24),
            'SI-18-MBTemp-13-CH5': (self._gwidget('led13ch5'), 21, 24),
            'SI-18-MBTemp-13-CH6': (self._gwidget('led13ch6'), 22, 25),
            'SI-08-MBTemp-10-CH8': (self._gwidget('led10ch8'), 21, 25),
            'SI-18-MBTemp-13-CH7': (self._gwidget('led13ch7'), 22, 25),
            'UA-21CHall:CR-IHMCtrl:dbAdsSta_strAdsA_m12CP2CW1035T-Mon':
            (self._gwidget('ledcp21035t'), 30, 34),
            'UA-21CHall:CR-IHMCtrl:dbAdsSta_strAdsA_m12CP1CW1065T-Mon':
            (self._gwidget('ledcp11065t'), 26, 30),
            'UA-21CHall:CR-IHMCtrl:dbAdsSta_strAdsA_m12CP2CW1065T-Mon':
            (self._gwidget('ledcp21065t'), 21, 25),
            'RA-TLSIA:RF-Circulator:Tout-Mon': (self._gwidget('ledcirctout'),
                                                18, 21),
            'RA-TLSIA:RF-Circulator:Tin-Mon': (self._gwidget('ledcirctin'),
                                               18, 21),
            'LA-CN:H1MPS-1:K1Temp1': (self._gwidget('ledk1temp1'), 18, 21),
            'LA-CN:H1MPS-1:K2Temp1': (self._gwidget('ledk2temp1'), 18, 21),
            'LA-CN:H1MPS-1:K1Temp2': (self._gwidget('ledk1temp2'), 18, 21),
            'LA-CN:H1MPS-1:K2Temp2': (self._gwidget('ledk2temp2'), 18, 21),
            'TB-Fam:PS-B:InductorTemperatureIIB-Mon':
            (self._gwidget('ledinductoriib'), 18, 21),
            'BO-15U:VA-PT100-BG:Temp-Mon':
            (self._gwidget('ledbo15vacpt100'), 22, 25),
            'BO-25U:VA-PT100-BG:Temp-Mon': (self._gwidget('ledbo25u'), 21, 24),
            'TS-Fam:PS-B:TemperatureIIBMod1-Mon':
            (self._gwidget('ledtsbtempmod1'), 31, 35),
            'TS-Fam:PS-B:TemperatureIIBMod4-Mon':
            (self._gwidget('ledtsbtempmod4'), 29, 33),
            'BO-05U:VA-PT100-BG:Temp-Mon':
            (self._gwidget('led05uvacpt100'), 21, 24),
            'BO-10U:VA-PT100-BG:Temp-Mon':
            (self._gwidget('led10uvacpt100'), 21, 24),
            'BO-14U:VA-PT100-BG:Temp-Mon':
            (self._gwidget('led14uvacpt100'), 21, 24),
            'SI-Fam:PS-QDA:InductorTemperatureIIB-Mon':
            (self._gwidget('ledqdainductor'), 18, 22),
            'SI-Fam:PS-QDA:HeatSinkTemperatureIIB-Mon':
            (self._gwidget('ledqdaheatsink'), 18, 22),
            'SI-Fam:PS-SDA0:HeatSinkTemperatureIIB-Mon':
            (self._gwidget('ledsda0heatsink'), 18, 22),
            'SI-Fam:PS-SFP1:HeatSinkTemperatureIIB-Mon':
            (self._gwidget('ledsfp1heatsink'), 18, 22),
        }


class Si_rackpu(utils.ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura Booster."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/temprackpu.ui", "temp")

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        self.sinais = {
            # 'IA-01RaNLK:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led_nlk'), 21, 25),
            'IA-01RaSepSI:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led_sepsi'), 21, 25),
            'IA-01RaInjBO:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led_injbo'), 21, 25),
        }


class Si_racksimar(utils.ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura Booster."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/temprackps.ui",
                         "temp")

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        self.sinais = {
            'IA-01RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led01raps01'), 21, 31),
            'IA-01RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led01raps02'), 21, 31),
            'IA-02RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led02raps01'), 21, 31),
            'IA-02RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led02raps02'), 21, 31),
            'IA-03RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led03raps01'), 21, 31),
            'IA-03RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led03raps02'), 21, 31),
            'IA-04RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led04raps01'), 21, 31),
            'IA-04RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led04raps02'), 21, 31),
            'IA-05RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led05raps01'), 21, 31),
            'IA-05RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led05raps02'), 21, 31),
            'IA-06RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led06raps01'), 21, 31),
            'IA-06RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led06raps02'), 21, 31),
            'IA-07RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led07raps01'), 21, 31),
            'IA-07RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led07raps02'), 21, 31),
            'IA-08RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led08raps01'), 21, 31),
            # 'IA-08RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led08raps02'), 21, 31),
            'IA-09RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led09raps01'), 21, 31),
            'IA-09RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led09raps02'), 21, 31),
            'IA-10RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led10raps01'), 21, 31),
            'IA-10RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led10raps02'), 21, 31),
            'IA-11RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led11raps01'), 21, 31),
            'IA-11RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led11raps02'), 21, 31),
            'IA-12RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led12raps01'), 21, 31),
            'IA-12RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led12raps02'), 21, 31),
            'IA-13RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led13raps01'), 21, 31),
            'IA-13RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led13raps02'), 21, 31),
            'IA-14RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led14raps01'), 21, 31),
            'IA-14RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led14raps02'), 21, 31),
            'IA-15RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led15raps01'), 21, 31),
            'IA-15RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led15raps02'), 21, 31),
            'IA-16RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led16raps01'), 21, 31),
            'IA-16RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led16raps02'), 21, 31),
            'IA-17RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led17raps01'), 21, 31),
            'IA-17RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led17raps02'), 21, 31),
            'IA-18RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led18raps01'), 21, 31),
            'IA-18RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led18raps02'), 21, 31),
            'IA-20RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20raps01'), 21, 31),
            'IA-20RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20raps02'), 21, 31),
        }


class Si_rackint(utils.ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura Booster."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/temprackint.ui",
                         "temp")

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        self.sinais = {
            'IA-01RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led01ractrl'), 19, 32),
            'IA-01RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led01rabpm'), 19, 32),
            'IA-01RaSepSI:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led01rasepsi'), 19, 32),
            'IA-01RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led01raps01'), 19, 32),
            'IA-01RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led01raps02'), 19, 32),
            'IA-01RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led01ravac'), 19, 32),
            'IA-01RaInjBO:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led01rainjbo'), 19, 32),
            # 'IA-01RaNLK:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led01ranlk'), 19, 32),
            'IA-02RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led02ractrl'), 19, 32),
            'IA-02RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led02rabpm'), 19, 32),
            'IA-02RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led02raps01'), 19, 32),
            'IA-02RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led02raps02'), 19, 32),
            'IA-02RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led02ravac'), 19, 32),
            'IA-03RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led03ractrl'), 19, 32),
            'IA-03RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led03rabpm'), 19, 32),
            'IA-03RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led03raps01'), 19, 32),
            'IA-03RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led03raps02'), 19, 32),
            'IA-03RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led03ravac'), 19, 32),
            'IA-04RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led04ractrl'), 19, 32),
            'IA-04RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led04rabpm'), 19, 32),
            'IA-04RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led04raps01'), 19, 32),
            'IA-04RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led04raps02'), 19, 32),
            'IA-04RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led04ravac'), 19, 32),
            'IA-05RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led05ractrl'), 19, 32),
            'IA-05RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led05rabpm'), 19, 32),
            'IA-05RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led05raps01'), 19, 32),
            'IA-05RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led05raps02'), 19, 32),
            'IA-05RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led05ravac'), 19, 32),
            'IA-06RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led06ractrl'), 19, 32),
            'IA-06RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led06rabpm'), 19, 32),
            'IA-06RaUnd:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led06raund'), 19, 32),
            'IA-06RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led06raps01'), 19, 32),
            'IA-06RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led06raps02'), 19, 32),
            'IA-06RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led06ravac'), 19, 32),
            'IA-07RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led07ractrl'), 19, 32),
            'IA-07RaUnd:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led07raund'), 19, 32),
            'IA-07RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led07raps01'), 19, 32),
            'IA-07RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led07raps02'), 19, 32),
            # 'IA-07RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led07ravac'), 19, 32),
            'IA-08RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led08ractrl'), 19, 32),
            'IA-08RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led08rabpm'), 19, 32),
            'IA-08RaUnd:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led08raund'), 19, 32),
            'IA-08RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led08raps01'), 19, 32),
            # 'IA-08RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led08raps02'), 19, 32),
            'IA-08RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led08ravac'), 19, 32),
            'IA-09RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led09ractrl'), 19, 32),
            'IA-09RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led09rabpm'), 19, 32),
            'IA-09RaUnd:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led09raund'), 19, 32),
            'IA-09RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led09raps01'), 19, 32),
            'IA-09RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led09raps02'), 19, 32),
            'IA-09RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led09ravac'), 19, 32),
            'IA-10RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led10ractrl'), 19, 32),
            'IA-10RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led10rabpm'), 19, 32),
            'IA-10RaUnd:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led10raund'), 19, 32),
            'IA-10RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led10raps01'), 19, 32),
            'IA-10RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led10raps02'), 19, 32),
            'IA-10RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led10ravac'), 19, 32),
            'IA-11RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led11ractrl'), 19, 32),
            'IA-11RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led11rabpm'), 19, 32),
            'IA-11RaUnd:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led11raund'), 19, 32),
            'IA-11RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led11raps01'), 19, 32),
            'IA-11RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led11raps02'), 19, 32),
            'IA-11RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led11ravac'), 19, 32),
            'IA-12RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led12ractrl'), 19, 32),
            'IA-12RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led12rabpm'), 19, 32),
            'IA-12RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led12raps01'), 19, 32),
            'IA-12RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led12raps02'), 19, 32),
            'IA-12RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led12ravac'), 19, 32),
            'IA-13RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led13ractrl'), 19, 32),
            'IA-13RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led13rabpm'), 19, 32),
            'IA-13RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led13raps01'), 19, 32),
            'IA-13RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led13raps02'), 19, 32),
            'IA-13RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led13ravac'), 19, 32),
            'IA-14RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led14ractrl'), 19, 32),
            'IA-14RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led14rabpm'), 19, 32),
            'IA-14RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led14raps01'), 19, 32),
            'IA-14RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led14raps02'), 19, 32),
            'IA-14RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led14ravac'), 19, 32),
            'IA-14RaDiag03:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led14radiag'), 19, 32),
            'IA-15RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led15ractrl'), 19, 32),
            'IA-15RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led15rabpm'), 19, 32),
            'IA-15RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led15raps01'), 19, 32),
            'IA-15RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led15raps02'), 19, 32),
            'IA-15RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led15ravac'), 19, 32),
            'IA-16RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led16ractrl'), 19, 32),
            'IA-16RaBbB:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led16rabbb'), 19, 32),
            'IA-16RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led16rabpm'), 19, 32),
            'IA-16RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led16raps01'), 19, 32),
            'IA-16RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led16raps02'), 19, 32),
            'IA-16RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led16ravac'), 19, 32),
            'IA-17RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led17ractrl'), 19, 32),
            'IA-17RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led17rabpm'), 19, 32),
            'IA-17RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led17raps01'), 19, 32),
            'IA-17RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led17raps02'), 19, 32),
            'IA-17RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led17ravac'), 19, 32),
            'IA-18RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led18ractrl'), 19, 32),
            'IA-18RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led18rabpm'), 19, 32),
            'IA-18RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led18raps01'), 19, 32),
            'IA-18RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led18raps02'), 19, 32),
            # 'IA-18RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led18ravac'), 19, 32),
            # 'IA-19RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led19ractrl'), 19, 32),
            # 'IA-19RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led19rabpm'), 19, 32),
            # 'IA-19RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led19raps01'), 19, 32),
            # 'IA-19RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led19raps02'), 19, 32),
            'IA-19RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led19ravac'), 19, 32),
            'IA-19RaEPP:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led19raepp'), 19, 32),
            # 'IA-19RaVAC02:CO-SIMAR-02:RackInternalTemp-Mon':
            # (self._gwidget('led19ravac02'), 19, 32),
            'IA-20RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20ractrl'), 19, 32),
            'IA-20RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20rabpm'), 19, 32),
            'IA-20RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20raps01'), 19, 32),
            'IA-20RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20raps02'), 19, 32),
            'IA-20RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20ravac'), 19, 32),
            'IA-20RaDiag01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20radiag01'), 19, 32),
            'IA-20RaBPMTL:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20rabpmtl'), 19, 32),
            'IA-20RaEPP:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20raepp'), 19, 32),
            'IA-20RaDiag02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20radiag02'), 19, 32),
        }


class Si_conecserv(utils.ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura Booster."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/tempconecserv.ui",
                         "temp")

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        self.sinais = {
            'CA-RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led_ctrl'), 28, 33),
            'CA-RaInter:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led_inter'), 25, 29),
            'CA-RaTim:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led_tim'), 23, 27),
            'RoomSrv:CO-SIMAR-01:AmbientTemp-Mon':
            (self._gwidget('led_server'), 17, 21),
            'CA:CO-SIMAR-01:AmbientTemp-Mon':
            (self._gwidget('led_ambient'), 21, 24),

        }


class Si_camvac(utils.ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura Booster."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/tempcamvac.ui",
                         "temp")

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        self.sinais = {
            # 'SI-01B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
            #                                   ('led01b2b'), 17, 42),
            'SI-01B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led01b1a'), 17, 42),
            'SI-01B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led01b2a'), 17, 42),
            # 'SI-01B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
            #                                   ('led01b1b'), 17, 42),
            'SI-01B2FE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led01b2fe'), 17, 42),
            'SI-01BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led01bc'), 17, 42),
            'SI-01C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led01c2'), 17, 42),
            'SI-01BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led01bcfe'), 17, 42),
            'SI-01SAFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led01safe'), 17, 42),
            'SI-01M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led01m1'), 17, 42),
            'SI-01C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led01c1'), 17, 42),
            'SI-02B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led02b1a'), 17, 42),
            'SI-02B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led02b1b'), 17, 42),
            # 'SI-02B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
            #                                   ('led02b2a'), 17, 42),
            'SI-02B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led02b2b'), 17, 42),
            'SI-02BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led02bc'), 17, 42),
            'SI-02BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led02bcfe'), 17, 42),
            # 'SI-02C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led02c1'), 17,
            #  42),
            'SI-02C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led02c2'), 17, 42),
            'SI-02M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led02m1'), 17, 42),
            'SI-02SBFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led02sbfe'), 17, 42),
            'SI-03B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led03b1a'), 17, 42),
            'SI-03B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led03b1b'), 17, 42),
            'SI-03B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led03b2a'), 17, 42),
            # 'SI-03B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
            #                                   ('led03b2b'), 17, 42),
            'SI-03B2FE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led03b2fe'), 17, 42),
            'SI-03BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led03bc'), 17, 42),
            'SI-03BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led03bcfe'), 17, 42),
            'SI-03C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led03c1'), 17, 42),
            'SI-03C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led03c2'), 17, 42),
            'SI-03M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led03m1'), 17, 42),
            'SI-03SPFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led03spfe'), 17, 42),
            'SI-04B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led04b1a'), 17, 42),
            # 'SI-04B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
            #                                   ('led04b1b'), 17, 42),
            # 'SI-04B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
            #                                   ('led04b2a'), 17, 42),
            'SI-04B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led04b2b'), 17, 42),
            'SI-04BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led04bc'), 17, 42),
            'SI-04BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led04bcfe'), 17, 42),
            'SI-04BCFE:VA-PT100-ED2:Temp-Mon': (self._gwidget
                                                ('led04bcfe_2'), 17, 42),
            'SI-04C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led04c1'), 17, 42),
            'SI-04C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led04c2'), 17, 42),
            'SI-04M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led04m1'), 17, 42),
            'SI-04SBFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led04sbfe'), 17, 42),
            'SI-05B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led05b1a'), 17, 42),
            # 'SI-05B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
            #                                   ('led05b1b'), 17, 42),
            'SI-05B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led05b2a'), 17, 42),
            'SI-05B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led05b2b'), 17, 42),
            'SI-05B2FE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led05b2fe'), 17, 42),
            'SI-05BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led05bc'), 17, 42),
            'SI-05BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led05bcfe'), 17, 42),
            'SI-05C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led05c1'), 17, 42),
            'SI-05C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led05c2'), 17, 42),
            'SI-05M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led05m1'), 17, 42),
            'SI-05SAFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led05safe'), 17, 42),
            'SI-06B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led06b1a'), 17, 42),
            # 'SI-06B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
            #                                   ('led06b1b'), 17, 42),
            'SI-06B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led06b2a'), 17, 42),
            'SI-06B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led06b2b'), 17, 42),
            'SI-06BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led06bc'), 17, 42),
            'SI-06BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led06bcfe'), 17, 42),
            'SI-06BCFE:VA-PT100-ED2:Temp-Mon': (self._gwidget
                                                ('led06bcfe_2'), 17, 42),
            'SI-06C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led06c1'), 17, 42),
            'SI-06C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led06c2'), 17, 42),
            'SI-06M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led06m1'), 17, 42),
            'SI-06SBFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led06sbfe'), 17, 42),
            'SI-07B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led07b1a'), 17, 42),
            'SI-07B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led07b1b'), 17, 42),
            'SI-07B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led07b2a'), 17, 42),
            'SI-07B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led07b2b'), 17, 42),
            'SI-07B2FE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led07b2fe'), 17, 42),
            'SI-07BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led07bc'), 17, 42),
            'SI-07BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led07bcfe'), 17, 42),
            'SI-07C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led07c1'), 17, 42),
            'SI-07C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led07c2'), 17, 42),
            'SI-07M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led07m1'), 17, 42),
            'SI-08B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led08b1a'), 17, 42),
            'SI-08B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led08b1b'), 17, 42),
            'SI-08B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led08b2a'), 17, 42),
            'SI-08B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led08b2b'), 17, 42),
            'SI-08BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led08bc'), 17, 42),
            'SI-08BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led08bcfe'), 17, 42),
            'SI-08C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led08c1'), 17, 42),
            'SI-08C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led08c2'), 17, 42),
            'SI-08M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led08m1'), 17, 42),
            # 'SI-08SBFE:VA-PT100-ED:Temp-Mon': (self._gwidget
            #                                    ('led08sbfe'), 17, 42,),
            'SI-09B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led09b1a'), 17, 42),
            'SI-09B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led09b1b'), 17, 42),
            'SI-09B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led09b2a'), 17, 42),
            'SI-09B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led09b2b'), 17, 42),
            'SI-09B2FE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led09b2fe'), 17, 42),
            'SI-09BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led09bc'), 17, 42),
            'SI-09BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led09bcfe'), 17, 42),
            'SI-09C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led09c1'), 17, 42),
            'SI-09C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led09c2'), 17, 42),
            'SI-09M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led09m1'), 17, 42),
            'SI-10B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led10b1a'), 17, 42),
            'SI-10B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led10b1b'), 17, 42),
            'SI-10B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led10b2a'), 17, 42),
            'SI-10B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led10b2b'), 17, 42),
            'SI-10BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led10bc'), 17, 42),
            'SI-10BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led10bcfe'), 17, 42),
            'SI-10C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led10c1'), 17, 42),
            'SI-10C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led10c2'), 17, 42),
            'SI-10M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led10m1'), 17, 42),
            'SI-10M2:VA-PT100-ED:Temp-Mon': (self._gwidget('led10m2'), 17, 42),
            'SI-11B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led11b1a'), 17, 39),
            'SI-11B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led11b1b'), 17, 39),
            'SI-11B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led11b2a'), 17, 39),
            # 'SI-11B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
            #                                   ('led11b2b'), 17, 39),
            'SI-11B2FE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led11b2fe'), 17, 39),
            'SI-11BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led11bc'), 17, 39),
            'SI-11BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led11bcfe'), 17, 39),
            'SI-11C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led11c1'), 17, 39),
            'SI-11C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led11c2'), 17, 39),
            'SI-11M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led11m1'), 17, 39),
            'SI-12B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led12b1a'), 17, 39),
            'SI-12B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led12b1b'), 17, 39),
            'SI-12B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led12b2a'), 17, 39),
            'SI-12B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led12b2b'), 17, 39),
            'SI-12BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led12bc'), 17, 39),
            'SI-12BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led12bcfe'), 17, 39),
            'SI-12C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led12c1'), 17, 39),
            'SI-12C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led12c2'), 17, 39),
            'SI-12M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led12m1'), 17, 39),
            'SI-12SBFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led12sbfe'), 17, 39),
            'SI-13B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led13b1a'), 17, 39),
            'SI-13B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led13b1b'), 17, 39),
            'SI-13B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led13b2a'), 17, 39),
            # 'SI-13B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
            #                                   ('led13b2b'), 17, 39),
            'SI-13B2FE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led13b2fe'), 17, 39),
            'SI-13BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led13bc'), 17, 39),
            'SI-13BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led13bcfe'), 17, 39),
            'SI-13C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led13c1'), 17, 39),
            'SI-13C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led13c2'), 17, 39),
            'SI-13M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led13m1'), 17, 39),
            'SI-13SAFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led13safe'), 17, 39),
            'SI-14B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led14b1a'), 17, 39),
            'SI-14B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led14b1b'), 17, 39),
            'SI-14B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led14b2a'), 17, 39),
            'SI-14B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led14b2b'), 17, 39),
            'SI-14BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led14bc'), 17, 39),
            'SI-14BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led14bcfe'), 17, 39),
            'SI-14C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led14c1'), 17, 39),
            'SI-14C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led14c2'), 17, 39),
            'SI-14M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led14m1'), 17, 39),
            'SI-14M2:VA-PT100-ED:Temp-Mon': (self._gwidget('led14m2'), 17, 39),
            'SI-15B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led15b1a'), 17, 39),
            'SI-15B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led15b1b'), 17, 39),
            'SI-15B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led15b2a'), 17, 39),
            'SI-15B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led15b2b'), 17, 39),
            'SI-15B2FE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led15b2fe'), 17, 39),
            'SI-15BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led15bc'), 17, 39),
            'SI-15BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led15bcfe'), 17, 39),
            'SI-15C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led15c1'), 17, 39),
            'SI-15C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led15c2'), 17, 39),
            'SI-15M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led15m1'), 17, 39),
            'SI-15SPFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led15spfe'), 17, 39),
            'SI-16B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led16b1a'), 17, 39),
            'SI-16B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led16b1b'), 17, 39),
            # 'SI-16B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
            #                                   ('led16b2a'), 17, 39),
            'SI-16B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led16b2b'), 17, 39),
            'SI-16BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led16bc'), 17, 39),
            'SI-16BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led16bcfe'), 17, 39),
            'SI-16C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led16c1'), 17, 39),
            'SI-16C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led16c2'), 17, 39),
            'SI-16M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led16m1'), 17, 39),
            'SI-16SBFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led16sbfe'), 17, 39),
            'SI-17B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led17b1a'), 17, 39),
            'SI-17B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led17b1b'), 17, 39),
            'SI-17B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led17b2a'), 17, 39),
            # 'SI-17B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
            #                                   ('led17b2b'), 17, 39),
            'SI-17B2FE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led17b2fe'), 17, 39),
            # 'SI-17BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led17bc'), 17,
            # 39),
            # 'SI-17BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
            #                                    ('led17bcfe'), 17, 39),
            'SI-17C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led17c1'), 17, 39),
            'SI-17C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led17c2'), 17, 39),
            'SI-17M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led17m1'), 17, 39),
            'SI-17SA:VA-PT100-ED:Temp-Mon': (self._gwidget('led17sa'), 17, 39),
            # 'SI-17SAFE:VA-PT100-ED:Temp-Mon': (self._gwidget
            #                                    ('led17safe'), 17, 39),
            'SI-18B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led18b1a'), 17, 39),
            'SI-18B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led18b1b'), 17, 39),
            'SI-18B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led18b2a'), 17, 39),
            'SI-18B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led18b2b'), 17, 39),
            # 'SI-18BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led18bc'), 17,
            # 39),
            'SI-18BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led18bcfe'), 17, 39),
            'SI-18C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led18c1'), 17, 39),
            'SI-18C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led18c2'), 17, 39),
            'SI-18M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led18m1'), 19, 39),
            'SI-18SBFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led18sbfe'), 19, 39),
            'SI-19B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led19b1a'), 19, 39),
            'SI-19B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led19b1b'), 19, 39),
            'SI-19B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led19b2a'), 19, 39),
            'SI-19B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led19b2b'), 19, 39),
            'SI-19B2FE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led19b2fe'), 19, 39),
            'SI-19BC:VA-PT100-ED:Temp-Mon': (self._gwidget
                                             ('led19bc'), 19, 39),
            'SI-19BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led19bcfe'), 19, 39),
            'SI-19C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led19c1'), 19, 39),
            'SI-19C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led19c2'), 19, 39),
            'SI-19M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led19m1'), 19, 39),
            'SI-19SPFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led19spfe'), 19, 39),
            'SI-20B1A:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led20b1a'), 19, 39),
            'SI-20B1B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led20b1b'), 19, 39),
            # 'SI-20B2A:VA-PT100-ED:Temp-Mon': (self._gwidget
            #                                   ('led20b2a'), 19, 39),
            'SI-20B2B:VA-PT100-ED:Temp-Mon': (self._gwidget
                                              ('led20b2b'), 19, 39),
            'SI-20BC:VA-PT100-ED:Temp-Mon': (self._gwidget('led20bc'), 19, 39),
            'SI-20BCFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led20bcfe'), 19, 39),
            'SI-20C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led20c1'), 19, 39),
            'SI-20C2:VA-PT100-ED:Temp-Mon': (self._gwidget('led20c2'), 19, 39),
            'SI-20M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led20m1'), 19, 39),
            'SI-20SBFE:VA-PT100-ED:Temp-Mon': (self._gwidget
                                               ('led20sbfe'), 19, 39),
        }


class Si_magnets(utils.ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura Booster."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/tempmagnets.ui",
                         "temp")

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        self.sinais = {
            'SI-01-MBTemp-22-CH6': (self._gwidget('ledb2c3_22ch6'),
                                    19.5, 27.5),
            'SI-01-MBTemp-22-CH7': (self._gwidget('ledb2c3_22ch7'),
                                    19.5, 27.5),
            'SI-01-MBTemp-22-CH8': (self._gwidget('ledb2c3_22ch8'),
                                    19.5, 27.5),
            'SI-01-MBTemp-14-CH5': (self._gwidget('ledq1c1_14ch5'),
                                    19.5, 27.5),
            'SI-01-MBTemp-14-CH6': (self._gwidget('ledq1c1_14ch6'),
                                    19.5, 27.5),
            'SI-01-MBTemp-14-CH7': (self._gwidget('ledq1c1_14ch7'),
                                    19.5, 27.5),
            'SI-01-MBTemp-23-CH6': (self._gwidget('ledqfbm1_23ch6'),
                                    19.5, 27.5),
            'SI-01-MBTemp-23-CH7': (self._gwidget('ledqfbm1_23ch7'),
                                    19.5, 27.5),
            'SI-03-MBTemp-23-CH5': (self._gwidget('ledb1c4_23ch5'),
                                    19.5, 27.5),
            'SI-03-MBTemp-23-CH6': (self._gwidget('ledb1c4_23ch6'),
                                    19.5, 27.5),
            'SI-03-MBTemp-23-CH7': (self._gwidget('ledb1c4_13ch7'),
                                    19.5, 27.5),
            'SI-03-MBTemp-13-CH5': (self._gwidget('ledb2c3_13ch5'),
                                    9.5, 27.5),
            'SI-03-MBTemp-13-CH6': (self._gwidget('ledb2c3_13ch6'),
                                    19.5, 27.5),
            'SI-03-MBTemp-13-CH7': (self._gwidget('ledb2c3_13ch7'),
                                    19.5, 27.5),
            'SI-03-MBTemp-22-CH6': (self._gwidget('ledq3c3_22ch6'),
                                    19.5, 27.5),
            # 'SI-03-MBTemp-22-CH7': (self._gwidget('ledq3c3_22ch7'),
            #                         19.5, 27.5),
            'SI-03-MBTemp-22-CH8': (self._gwidget('ledq3c3_22ch8'),
                                    19.5, 27.5),
            'SI-06-MBTemp-23-CH5': (self._gwidget('led06b1c4_23ch5'),
                                    19.5, 27.5),
            'SI-06-MBTemp-23-CH6': (self._gwidget('led06b1c4_23ch6'),
                                    19.5, 27.5),
            # 'SI-06-MBTemp-23-CH7': (self._gwidget('led06b1c4_23ch7'),
            #                         19.5, 27.5),
            'SI-06-MBTemp-11-CH4': (self._gwidget('led06b2c2_11ch4'),
                                    19.5, 27.5),
            'SI-06-MBTemp-11-CH5': (self._gwidget('led06b2c2_11ch5'),
                                    19.5, 27.5),
            'SI-06-MBTemp-11-CH6': (self._gwidget('led06b2c2_11ch6'),
                                    19.5, 27.5),
            'SI-06-MBTemp-22-CH6': (self._gwidget('led06q3c3_22ch6'),
                                    19.5, 27.5),
            'SI-06-MBTemp-22-CH7': (self._gwidget('led06q3c3_22ch7'),
                                    19.5, 27.5),
            # 'SI-06-MBTemp-22-CH8': (self._gwidget('led06q3c3_22ch8'),
            #                         19.5, 27.5),
            'SI-08-MBTemp-23-CH5': (self._gwidget('led08b1c4_23ch5'),
                                    19.5, 27.5),
            'SI-08-MBTemp-23-CH6': (self._gwidget('led08b1c4_23ch6'),
                                    19.5, 27.5),
            'SI-08-MBTemp-23-CH7': (self._gwidget('led08b1c4_23ch7'),
                                    19.5, 27.5),
            'SI-08-MBTemp-10-CH3': (self._gwidget('led08b2c2_10ch3'),
                                    19.5, 27.5),
            'SI-08-MBTemp-10-CH4': (self._gwidget('led08b2c2_10ch4'),
                                    19.5, 27.5),
            'SI-08-MBTemp-10-CH5': (self._gwidget('led08b2c2_10ch5'),
                                    19.5, 27.5),
            'SI-08-MBTemp-22-CH6': (self._gwidget('led08q3c3_22ch6'),
                                    19.5, 27.5),
            'SI-08-MBTemp-22-CH7': (self._gwidget('led08q3c3_22ch7'),
                                    19.5, 27.5),
            'SI-08-MBTemp-22-CH8': (self._gwidget('led08q3c3_22ch8'),
                                    19.5, 27.5),
            'SI-11-MBTemp-23-CH5': (self._gwidget('led11b1c4_23ch5'),
                                    19.5, 27.5),
            'SI-11-MBTemp-23-CH6': (self._gwidget('led11b1c4_23ch6'),
                                    19.5, 27.5),
            'SI-11-MBTemp-23-CH7': (self._gwidget('led11b1c4_23ch7'),
                                    19.5, 27.5),
            'SI-11-MBTemp-13-CH3': (self._gwidget('led11b2c2_13ch3'),
                                    19.5, 27.5),
            'SI-11-MBTemp-13-CH5': (self._gwidget('led11b2c2_13ch5'),
                                    19.5, 27.5),
            'SI-11-MBTemp-12-CH8': (self._gwidget('led11b2c2_12ch8'),
                                    19.5, 27.5),
            'SI-11-MBTemp-22-CH6': (self._gwidget('led11q3c3_22ch6'),
                                    19.5, 27.5),
            'SI-11-MBTemp-22-CH7': (self._gwidget('led11q3c3_22ch7'),
                                    19.5, 27.5),
            'SI-11-MBTemp-22-CH8': (self._gwidget('led11q3c3_22ch8'),
                                    19.5, 27.5),
            # 'SI-13-MBTemp-22-CH7': (self._gwidget('led22b2c3_22ch7'),
            # 19.5, 27.5),
            'SI-13-MBTemp-22-CH8': (self._gwidget('led22b2c3_22ch8'),
                                    19.5, 27.5),
            'SI-13-MBTemp-13-CH5': (self._gwidget('led13q1c1_13ch5'),
                                    19.5, 27.5),
            'SI-13-MBTemp-13-CH6': (self._gwidget('led13q1c1_13ch6'),
                                    19.5, 27.5),
            'SI-13-MBTemp-13-CH7': (self._gwidget('led13q1c1_13ch7'),
                                    19.5, 27.5),
            'SI-13-MBTemp-23-CH5': (self._gwidget('led13qfbm1_23ch5'),
                                    19.5, 27.5),
            # 'SI-13-MBTemp-23-CH6': (self._gwidget('led13qfbm1_23ch6'),
            #                         19.5, 27.5),
            'SI-13-MBTemp-23-CH7': (self._gwidget('led13qfbm1_23ch7'),
                                    19.5, 27.5),
            'SI-16-MBTemp-22-CH6': (self._gwidget('led16b2c3_22ch6'),
                                    9.5, 27.5),
            'SI-16-MBTemp-22-CH7': (self._gwidget('led16b2c3_22ch7'),
                                    19.5, 27.5),
            'SI-16-MBTemp-22-CH8': (self._gwidget('led16b2c3_22ch8'),
                                    19.5, 27.5),
            'SI-16-MBTemp-11-CH6': (self._gwidget('led16q1c1_11ch6'),
                                    19.5, 27.5),
            'SI-16-MBTemp-11-CH7': (self._gwidget('led16q1c1_11ch7'),
                                    19.5, 27.5),
            'SI-16-MBTemp-11-CH8': (self._gwidget('led16q1c1_11ch8'),
                                    19.5, 27.5),
            'SI-16-MBTemp-23-CH5': (self._gwidget('led16qfbm1_23ch5'),
                                    19.5, 27.5),
            'SI-16-MBTemp-23-CH6': (self._gwidget('led16qfbm1_23ch6'),
                                    19.5, 27.5),
            'SI-16-MBTemp-23-CH7': (self._gwidget('led16qfbm1_23ch7'),
                                    19.5, 27.5),
            'SI-18-MBTemp-23-CH5': (self._gwidget('led18b1c4_23ch5'),
                                    19.5, 27.5),
            'SI-18-MBTemp-23-CH6': (self._gwidget('led18b1c4_23ch6'),
                                    19.5, 27.5),
            'SI-18-MBTemp-23-CH7': (self._gwidget('led18b1c4_23ch7'),
                                    19.5, 27.5),
            'SI-18-MBTemp-11-CH5': (self._gwidget('led18b2c2_11ch5'),
                                    19.5, 27.5),
            'SI-18-MBTemp-11-CH6': (self._gwidget('led18b2c2_11ch6'),
                                    19.5, 27.5),
            'SI-18-MBTemp-11-CH7': (self._gwidget('led18b2c2_11ch7'),
                                    19.5, 27.5),
            'SI-18-MBTemp-22-CH6': (self._gwidget('led18q3c3_22ch6'),
                                    19.5, 27.5),
            'SI-18-MBTemp-22-CH7': (self._gwidget('led18q3c3_22ch7'),
                                    19.5, 27.5),
            'SI-18-MBTemp-22-CH8': (self._gwidget('led18q3c3_22ch8'),
                                    19.5, 27.5),
        }


class Si_dclinks(utils.ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura Booster."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/tempdclinks.ui",
                         "temp")

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        self.sinais = {
            'PA-RaPSD01:PS-DCLink-1A:IGBTT-Mon':
            (self._gwidget('led1aigbt_01'), 15, 33),
            'PA-RaPSD01:PS-DCLink-1B:IGBTT-Mon':
            (self._gwidget('led1bigbt_01'), 15, 33),
            'PA-RaPSD01:PS-DCLink-3A:IGBTT-Mon':
            (self._gwidget('led3aigbt_01'), 15, 33),
            'PA-RaPSD01:PS-DCLink-3B:IGBTT-Mon':
            (self._gwidget('led3bigbt_01'), 15, 33),
            'PA-RaPSD03:PS-DCLink-2A:IGBTT-Mon':
            (self._gwidget('led2aigbt_03'), 15, 33),
            'PA-RaPSD03:PS-DCLink-2B:IGBTT-Mon':
            (self._gwidget('led2bigbt_03'), 15, 33),
            'PA-RaPSD03:PS-DCLink-4A:IGBTT-Mon':
            (self._gwidget('led4aigbt_03'), 15, 33),
            'PA-RaPSD03:PS-DCLink-4B:IGBTT-Mon':
            (self._gwidget('led4bigbt_03'), 15, 33),
            'PA-RaPSD05:PS-DCLink-1A:IGBTT-Mon':
            (self._gwidget('led1aigbt_05'), 15, 33),
            'PA-RaPSD05:PS-DCLink-1B:IGBTT-Mon':
            (self._gwidget('led1bigbt_05'), 15, 33),
            'PA-RaPSD05:PS-DCLink-3A:IGBTT-Mon':
            (self._gwidget('led3aigbt_05'), 15, 33),
            'PA-RaPSD05:PS-DCLink-3B:IGBTT-Mon':
            (self._gwidget('led3bigbt_05'), 15, 33),
            'PA-RaPSD07:PS-DCLink-2A:IGBTT-Mon':
            (self._gwidget('led2aigbt_07'), 15, 33),
            'PA-RaPSD07:PS-DCLink-2B:IGBTT-Mon':
            (self._gwidget('led2bigbt_07'), 15, 33),
            'PA-RaPSD07:PS-DCLink-4A:IGBTT-Mon':
            (self._gwidget('led4aigbt_07'), 15, 33),
            'PA-RaPSD07:PS-DCLink-4B:IGBTT-Mon':
            (self._gwidget('led4bigbt_07'), 15, 33),
            'PA-RaPSD01:PS-DCLink-1A:RectifierT-Mon':
            (self._gwidget('led1arectifier_01'), 15, 33),
            'PA-RaPSD01:PS-DCLink-1B:RectifierT-Mon':
            (self._gwidget('led1brectifier_01'), 15, 33),
            'PA-RaPSD01:PS-DCLink-3A:RectifierT-Mon':
            (self._gwidget('led3arectifier_01'), 15, 33),
            'PA-RaPSD01:PS-DCLink-3B:RectifierT-Mon':
            (self._gwidget('led3brectifier_01'), 15, 33),
            'PA-RaPSD03:PS-DCLink-2A:RectifierT-Mon':
            (self._gwidget('led2arectifier_03'), 15, 33),
            'PA-RaPSD03:PS-DCLink-2B:RectifierT-Mon':
            (self._gwidget('led2brectifier_03'), 15, 33),
            'PA-RaPSD03:PS-DCLink-4A:RectifierT-Mon':
            (self._gwidget('led4arectifier_03'), 15, 33),
            'PA-RaPSD03:PS-DCLink-4B:RectifierT-Mon':
            (self._gwidget('led4brectifier_03'), 15, 33),
            'PA-RaPSD05:PS-DCLink-1A:RectifierT-Mon':
            (self._gwidget('led1arectifier_05'), 15, 33),
            'PA-RaPSD05:PS-DCLink-1B:RectifierT-Mon':
            (self._gwidget('led1brectifier_05'), 15, 33),
            'PA-RaPSD05:PS-DCLink-3A:RectifierT-Mon':
            (self._gwidget('led3arectifier_05'), 15, 33),
            'PA-RaPSD05:PS-DCLink-3B:RectifierT-Mon':
            (self._gwidget('led3brectifier_05'), 15, 33),
            'PA-RaPSD07:PS-DCLink-2A:RectifierT-Mon':
            (self._gwidget('led2arectifier_07'), 15, 33),
            'PA-RaPSD07:PS-DCLink-2B:RectifierT-Mon':
            (self._gwidget('led2brectifier_07'), 15, 33),
            'PA-RaPSD07:PS-DCLink-4A:RectifierT-Mon':
            (self._gwidget('led4arectifier_07'), 15, 33),
            'PA-RaPSD07:PS-DCLink-4B:RectifierT-Mon':
            (self._gwidget('led4brectifier_07'), 15, 33),
            'PA-RaPSD01:PS-DCLink-1A:PCBT-Mon':
            (self._gwidget('led1apcb_01'), 15, 33),
            'PA-RaPSD01:PS-DCLink-1B:PCBT-Mon':
            (self._gwidget('led1bpcb_01'), 15, 33),
            'PA-RaPSD01:PS-DCLink-3A:PCBT-Mon':
            (self._gwidget('led3apcb_01'), 15, 33),
            'PA-RaPSD01:PS-DCLink-3B:PCBT-Mon':
            (self._gwidget('led3bpcb_01'), 15, 33),
            'PA-RaPSD03:PS-DCLink-2A:PCBT-Mon':
            (self._gwidget('led2apcb_03'), 15, 33),
            'PA-RaPSD03:PS-DCLink-2B:PCBT-Mon':
            (self._gwidget('led2bpcb_03'), 15, 33),
            'PA-RaPSD03:PS-DCLink-4A:PCBT-Mon':
            (self._gwidget('led4apcb_03'), 15, 33),
            'PA-RaPSD03:PS-DCLink-4B:PCBT-Mon':
            (self._gwidget('led4bpcb_03'), 15, 33),
            'PA-RaPSD05:PS-DCLink-1A:PCBT-Mon':
            (self._gwidget('led1apcb_05'), 15, 33),
            'PA-RaPSD05:PS-DCLink-1B:PCBT-Mon':
            (self._gwidget('led1bpcb_05'), 15, 33),
            'PA-RaPSD05:PS-DCLink-3A:PCBT-Mon':
            (self._gwidget('led3apcb_05'), 15, 33),
            'PA-RaPSD05:PS-DCLink-3B:PCBT-Mon':
            (self._gwidget('led3bpcb_05'), 15, 33),
            'PA-RaPSD07:PS-DCLink-2A:PCBT-Mon':
            (self._gwidget('led2apcb_07'), 15, 33),
            'PA-RaPSD07:PS-DCLink-2B:PCBT-Mon':
            (self._gwidget('led2bpcb_07'), 15, 33),
            'PA-RaPSD07:PS-DCLink-4A:PCBT-Mon':
            (self._gwidget('led4apcb_07'), 15, 33),
            'PA-RaPSD07:PS-DCLink-4B:PCBT-Mon':
            (self._gwidget('led4bpcb_07'), 15, 33),
            'PA-RaPSA01:PS-DCLink-QFAP:IGBTT-Mon':
            (self._gwidget('led01qfap_igbt'), 15, 33),
            'PA-RaPSA01:PS-DCLink-QFB:IGBTT-Mon':
            (self._gwidget('led01qfb_igbt'), 15, 33),
            'PA-RaPSA03:PS-DCLink-QDAP:IGBTT-Mon':
            (self._gwidget('led03qdap_igbt'), 15, 33),
            'PA-RaPSA04:PS-DCLink-QDB:IGBTT-Mon':
            (self._gwidget('led04qdb_igbt'), 15, 33),
            'PA-RaPSA06:PS-DCLink-Q13A:IGBTT-Mon':
            (self._gwidget('led06q13a_igbt'), 15, 33),
            'PA-RaPSA06:PS-DCLink-Q13B:IGBTT-Mon':
            (self._gwidget('led06q13b_igbt'), 15, 33),
            'PA-RaPSA06:PS-DCLink-Q13C:IGBTT-Mon':
            (self._gwidget('led06q13c_igbt'), 15, 33),
            'PA-RaPSA07:PS-DCLink-Q24A:IGBTT-Mon':
            (self._gwidget('led07q24a_igbt'), 15, 33),
            'PA-RaPSA07:PS-DCLink-Q24B:IGBTT-Mon':
            (self._gwidget('led07q24b_igbt'), 15, 33),
            'PA-RaPSA07:PS-DCLink-Q24C:IGBTT-Mon':
            (self._gwidget('led07q24c_igbt'), 15, 33),
            'PA-RaPSA01:PS-DCLink-QFAP:RectifierT-Mon':
            (self._gwidget('led01qfap_rectifier'), 15, 33),
            'PA-RaPSA01:PS-DCLink-QFB:RectifierT-Mon':
            (self._gwidget('led01qfb_rectifier'), 15, 33),
            'PA-RaPSA03:PS-DCLink-QDAP:RectifierT-Mon':
            (self._gwidget('led03qdap_rectifier'), 15, 33),
            'PA-RaPSA04:PS-DCLink-QDB:RectifierT-Mon':
            (self._gwidget('led04qdb_rectifier'), 15, 33),
            'PA-RaPSA06:PS-DCLink-Q13A:RectifierT-Mon':
            (self._gwidget('led06q13a_rectifier'), 15, 33),
            'PA-RaPSA06:PS-DCLink-Q13B:RectifierT-Mon':
            (self._gwidget('led06q13b_rectifier'), 15, 33),
            'PA-RaPSA06:PS-DCLink-Q13C:RectifierT-Mon':
            (self._gwidget('led06q13c_rectifier'), 15, 33),
            'PA-RaPSA07:PS-DCLink-Q24A:RectifierT-Mon':
            (self._gwidget('led07q24a_rectifier'), 15, 33),
            'PA-RaPSA07:PS-DCLink-Q24B:RectifierT-Mon':
            (self._gwidget('led07q24b_rectifier'), 15, 33),
            'PA-RaPSA07:PS-DCLink-Q24C:RectifierT-Mon':
            (self._gwidget('led07q24c_rectifier'), 15, 33),
            'PA-RaPSA01:PS-DCLink-QFAP:PCBT-Mon':
            (self._gwidget('led01qfap_pcb'), 15, 33),
            'PA-RaPSA01:PS-DCLink-QFB:PCBT-Mon':
            (self._gwidget('led01qfb_pcb'), 15, 33),
            'PA-RaPSA03:PS-DCLink-QDAP:PCBT-Mon':
            (self._gwidget('led03qdap_pcb'), 15, 33),
            'PA-RaPSA04:PS-DCLink-QDB:PCBT-Mon':
            (self._gwidget('led04qdb_pcb'), 15, 33),
            'PA-RaPSA06:PS-DCLink-Q13A:PCBT-Mon':
            (self._gwidget('led06q13a_pcb'), 15, 33),
            'PA-RaPSA06:PS-DCLink-Q13B:PCBT-Mon':
            (self._gwidget('led06q13b_pcb'), 15, 33),
            'PA-RaPSA06:PS-DCLink-Q13C:PCBT-Mon':
            (self._gwidget('led06q13c_pcb'), 15, 33),
            'PA-RaPSA07:PS-DCLink-Q24A:PCBT-Mon':
            (self._gwidget('led07q24a_pcb'), 15, 33),
            'PA-RaPSA07:PS-DCLink-Q24B:PCBT-Mon':
            (self._gwidget('led07q24b_pcb'), 15, 33),
            'PA-RaPSA07:PS-DCLink-Q24C:PCBT-Mon':
            (self._gwidget('led07q24c_pcb'), 15, 33),
            'PA-RaPSB03:PS-DCLink-SFAP0:IGBTT-Mon':
            (self._gwidget('led03sfap0_igbt'), 15, 33),
            'PA-RaPSB03:PS-DCLink-SFB0:IGBTT-Mon':
            (self._gwidget('led03sfb0_igbt'), 15, 33),
            'PA-RaPSB07:PS-DCLink-SFA2SDP1:IGBTT-Mon':
            (self._gwidget('led07sfa2dp1_igbt'), 15, 33),
            'PA-RaPSB08:PS-DCLink-SFB1:IGBTT-Mon':
            (self._gwidget('led08sfb1_igbt'), 15, 33),
            'PA-RaPSB10:PS-DCLink-SFP12:IGBTT-Mon':
            (self._gwidget('led10sfp12_igbt'), 15, 33),
            'PA-RaPSB10:PS-DCLink-SFB2:IGBTT-Mon':
            (self._gwidget('led10sfb2_igbt'), 15, 33),
            'PA-RaPSB03:PS-DCLink-SFAP0:RectifierT-Mon':
            (self._gwidget('led03sfap0_rectifier'), 15, 33),
            'PA-RaPSB03:PS-DCLink-SFB0:RectifierT-Mon':
            (self._gwidget('led03sfb0_rectifier'), 15, 33),
            'PA-RaPSB07:PS-DCLink-SFA2SDP1:RectifierT-Mon':
            (self._gwidget('led07sfa2dp1_rectifier'), 15, 33),
            'PA-RaPSB08:PS-DCLink-SFB1:RectifierT-Mon':
            (self._gwidget('led08sfb1_rectifier'), 15, 33),
            'PA-RaPSB10:PS-DCLink-SFP12:RectifierT-Mon':
            (self._gwidget('led10sfp12_rectifier'), 15, 33),
            'PA-RaPSB10:PS-DCLink-SFB2:RectifierT-Mon':
            (self._gwidget('led10sfb2_rectifier'), 15, 33),
            'PA-RaPSB03:PS-DCLink-SFB0:PCBT-Mon':
            (self._gwidget('led03sfb0_pcb'), 15, 33),
            'PA-RaPSB03:PS-DCLink-SFAP0:PCBT-Mon':
            (self._gwidget('led03sfap0_pcb'), 15, 33),
            'PA-RaPSB07:PS-DCLink-SFA2SDP1:PCBT-Mon':
            (self._gwidget('led07sfa2sdp1_pcb'), 15, 33),
            'PA-RaPSB08:PS-DCLink-SFB1:PCBT-Mon':
            (self._gwidget('led08sfb1_pcb'), 15, 33),
            'PA-RaPSB10:PS-DCLink-SFB2:PCBT-Mon':
            (self._gwidget('led10sfb2_pcb'), 15, 33),
            'PA-RaPSB10:PS-DCLink-SFP12:PCBT-Mon':
            (self._gwidget('led10sfp12_pcb'), 15, 33),
            'PA-RaPSB01:PS-DCLink-SDB0:IGBTT-Mon':
            (self._gwidget('ledsdb0_igbt'), 17, 43),
            'PA-RaPSB01:PS-DCLink-SDAP0:IGBTT-Mon':
            (self._gwidget('ledsdap0_igbt'), 17, 43),
            'PA-RaPSB04:PS-DCLink-SDA12:IGBTT-Mon':
            (self._gwidget('ledsda12_igbt'), 17, 43),
            'PA-RaPSB04:PS-DCLink-SDB1:IGBTT-Mon':
            (self._gwidget('ledsdb1_igbt'), 17, 43),
            'PA-RaPSB05:PS-DCLink-SDA3SFA1:IGBTT-Mon':
            (self._gwidget('ledsda3sfa1_igbt'), 17, 43),
            'PA-RaPSB05:PS-DCLink-SDB2:IGBTT-Mon':
            (self._gwidget('ledsdb2_igbt'), 17, 43),
            # 'PA-RaPSB07:PS-DCLink-SFA2SDP1:IGBTT-Mon':
            # (self._gwidget('ledsfa2sdp1_igbt'), 17, 43),
            'PA-RaPSB07:PS-DCLink-SDB3:IGBTT-Mon':
            (self._gwidget('ledsdb3_igbt'), 17, 43),
            'PA-RaPSB08:PS-DCLink-SDP23:IGBTT-Mon':
            (self._gwidget('ledsdp23_igbt'), 17, 43),
            'PA-RaPSB01:PS-DCLink-SDB0:RectifierT-Mon':
            (self._gwidget('ledsdb0_rectifier'), 17, 43),
            'PA-RaPSB01:PS-DCLink-SDAP0:RectifierT-Mon':
            (self._gwidget('ledsdap0_rectifier'), 17, 43),
            'PA-RaPSB04:PS-DCLink-SDA12:RectifierT-Mon':
            (self._gwidget('ledsda12_rectifier'), 17, 43),
            'PA-RaPSB04:PS-DCLink-SDB1:RectifierT-Mon':
            (self._gwidget('ledsdb1_rectifier'), 17, 43),
            'PA-RaPSB05:PS-DCLink-SDA3SFA1:RectifierT-Mon':
            (self._gwidget('ledsda3sfa1_rectifier'), 17, 43),
            'PA-RaPSB05:PS-DCLink-SDB2:RectifierT-Mon':
            (self._gwidget('ledsdb2_rectifier'), 17, 43),
            # 'PA-RaPSB07:PS-DCLink-SFA2SDP1:RectifierT-Mon':
            # (self._gwidget('ledsfa2sdp1_rectifier'), 17, 43),
            'PA-RaPSB07:PS-DCLink-SDB3:RectifierT-Mon':
            (self._gwidget('ledsdb3_rectifier'), 17, 43),
            'PA-RaPSB08:PS-DCLink-SDP23:RectifierT-Mon':
            (self._gwidget('ledsdp23_rectifier'), 17, 43),
            'PA-RaPSB01:PS-DCLink-SDAP0:PCBT-Mon':
            (self._gwidget('ledsdap0_pcb'), 17, 43),
            'PA-RaPSB01:PS-DCLink-SDB0:PCBT-Mon':
            (self._gwidget('ledsdb0_pcb'), 17, 43),
            'PA-RaPSB04:PS-DCLink-SDA12:PCBT-Mon':
            (self._gwidget('ledsda12_pcb'), 17, 43),
            'PA-RaPSB04:PS-DCLink-SDB1:PCBT-Mon':
            (self._gwidget('ledsdb1_pcb'), 17, 43),
            'PA-RaPSB05:PS-DCLink-SDA3SFA1:PCBT-Mon':
            (self._gwidget('ledsda3sfa1_pcb'), 17, 43),
            'PA-RaPSB05:PS-DCLink-SDB2:PCBT-Mon':
            (self._gwidget('ledsdb2_pcb'), 17, 43),
            'PA-RaPSB07:PS-DCLink-SDB3:PCBT-Mon':
            (self._gwidget('ledsdb3_pcb'), 17, 43),
            # 'PA-RaPSB07:PS-DCLink-SFA2SDP1:PCBT-Mon':
            # (self._gwidget('ledsfa2sdp1_pcb'), 17, 43),
            'PA-RaPSB08:PS-DCLink-SDP23:PCBT-Mon':
            (self._gwidget('ledsdp23_pcb'), 17, 43),

        }


class Blocositemp:
    """Gerencia o grupo SItemp e atualiza a label alarmsitemp."""

    def __init__(self, janela_opr):
        """."""
        janela_opr.alarmsitemp.clicked.connect(self.aba_sitemp)
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto
        self.tempcamvac = Si_camvac(janela_opr, janela_opr.btntempcamvac)
        self.temprackpu = Si_rackpu(janela_opr, janela_opr.btnrackpu)
        self.temprackps = Si_racksimar(janela_opr, janela_opr.btnrackps)
        self.temprackint = Si_rackint(janela_opr, janela_opr.btntemprackint)
        self.tempcirchid = Si_circhid(janela_opr, janela_opr.btntempcirchid)
        self.tempconecserv = Si_conecserv(janela_opr, janela_opr.
                                          btntempconecserv)
        self.tempmagnets = Si_magnets(janela_opr, janela_opr.btntempmagnets)
        # self.temphls = Si_hls(janela_opr, janela_opr.btntemphls)
        self.tempdclinks = Si_dclinks(janela_opr, janela_opr.btntempdclinks)

        # Adiciona todas as subjanelas à lista
        self.subjanelas.extend([
            self.tempcamvac,
            self.temprackpu,
            self.temprackps,
            self.temprackint,
            self.tempcirchid,
            self.tempconecserv,
            self.tempmagnets,
            # self.temphls,
            self.tempdclinks,
        ])

        # Configura cada subjanela
        for sub in self.subjanelas:
            sub.configurar_sistema()

    def atualizar_grupo(self):
        """Atualiza todas as subjanelas e a label alarmsitemp."""
        falha_detectada = False
        for sub in self.subjanelas:
            sub.atualizar_status()
            falha_detectada |= not sub.estado_ok

        # Atualiza a label principal do bloco SI Temp
        alarme_widget = self.janela_opr.findChild(QtWidgets.QPushButton,
                                                  "alarmsitemp")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if not falha_detectada else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()

    def aba_sitemp(self):
        """."""
        try:
            self.janela_opr.janela_opr.setCurrentIndex(7)
        except Exception as e:
            logging.error(f"Erro ao mudar para aba LTB: {e}")
