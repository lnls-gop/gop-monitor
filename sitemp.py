"""Logica das Temperaturas do Anel de Armazenamento."""
from PyQt5 import uic, QtWidgets
import utils


class Si_rackpu(QtWidgets.QWidget):
    """Controle de temperatura do rack de Pulsados."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.temprackpu = uic.loadUi("ui/temprackpu.ui")
        self._registar_grupos()

    def _registar_grupos(self):
        self.sinais_temprackpu = {
            "rackpu": (
                    {
                        'IA-01RaNLK:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackpu.led_nlk,
                        'IA-01RaSepSI:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackpu.led_sepsi,
                        'IA-01RaInjBO:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackpu.led_injbo,
                    }, 21, 86
            ),
        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_temprackpu)
        self.atualizar_status()

    def mostrar_janela_temprackpu(self):
        """."""
        self.temprackpu.setVisible(not self.isVisible())

    def atualizar_status(self):
        """."""
        todos_verdes = True
        for _, (sinais, temp_min, temp_max) in self.sinais_temprackpu.items():
            for signal, led in sinais.items():
                utils.verificar_temprackpu(signal, led, temp_min, temp_max)
                if not getattr(led, "state", False):
                    todos_verdes = False

            self.estado_ok = todos_verdes

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_verdes else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")


class Si_racksimar(QtWidgets.QWidget):
    """Controle de Temperatura Rack Simar."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.temprackps = uic.loadUi("ui/temprackps.ui")
        self._registar_grupos()

    def _registar_grupos(self):
        self.sinais_temprackps = {
            "racksimar": (
                    {
                        # 'IA-01RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        # self.temprackps.led01raps01,
                        'IA-01RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led01raps02,
                        'IA-02RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led02raps01,
                        'IA-02RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led02raps02,
                        'IA-03RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led03raps01,
                        'IA-03RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led03raps02,
                        'IA-04RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led04raps01,
                        'IA-04RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led04raps02,
                        'IA-05RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led05raps01,
                        'IA-05RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led05raps02,
                        'IA-06RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led06raps01,
                        'IA-06RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led06raps02,
                        'IA-07RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led07raps01,
                        'IA-07RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led07raps02,
                        'IA-08RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led08raps01,
                        # 'IA-08RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        # self.temprackps.led08raps02,
                        'IA-09RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led09raps01,
                        'IA-09RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led09raps02,
                        'IA-10RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led10raps01,
                        'IA-10RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led10raps02,
                        'IA-11RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led11raps01,
                        'IA-11RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led11raps02,
                        'IA-12RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led12raps01,
                        'IA-12RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led12raps02,
                        'IA-13RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led13raps01,
                        'IA-13RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led13raps02,
                        'IA-14RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led14raps01,
                        'IA-14RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led14raps02,
                        'IA-15RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led15raps01,
                        'IA-15RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led15raps02,
                        'IA-16RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led16raps01,
                        'IA-16RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led16raps02,
                        'IA-17RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led17raps01,
                        'IA-17RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led17raps02,
                        'IA-18RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led18raps01,
                        'IA-18RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led18raps02,
                        'IA-20RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led20raps01,
                        'IA-20RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackps.led20raps02,
                    }, 21, 31
                ),
            }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_temprackps)
        self.atualizar_status()

    def mostrar_janela_temprackps(self):
        """."""
        self.temprackps.setVisible(not self.isVisible())

    def atualizar_status(self):
        """."""
        todos_verdes = True
        for _, (sinais, temp_min, temp_max) in self.sinais_temprackps.items():
            for signal, led in sinais.items():
                utils.verificar_temprackps(signal, led, temp_min, temp_max)
                if not getattr(led, "state", False):
                    todos_verdes = False

            self.estado_ok = todos_verdes

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_verdes else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")


class Si_roomrack(QtWidgets.QWidget):
    """Controle de Temperatura dos Racks das Fontes."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.temprackint = uic.loadUi("ui/temprackint.ui")
        self._registar_grupos()

    def _registar_grupos(self):
        self.sinais_temprackint = {
            "temprackint": (
                {
                        'IA-01RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led01ractrl,
                        'IA-01RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led01rabpm,
                        'IA-01RaSepSI:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led01rasepsi,
                        # 'IA-01RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        # self.temprackint.led01raps01,
                        'IA-01RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led01raps02,
                        'IA-01RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led01ravac,
                        'IA-01RaInjBO:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led01rainjbo,
                        # 'IA-01RaNLK:CO-SIMAR-01:RackInternalTemp-Mon':
                        # self.temprackint.led01ranlk,
                        'IA-02RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led02ractrl,
                        'IA-02RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led02rabpm,
                        'IA-02RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led02raps01,
                        'IA-02RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led02raps02,
                        'IA-02RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led02ravac,
                        'IA-03RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led03ractrl,
                        'IA-03RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led03rabpm,
                        'IA-03RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led03raps01,
                        'IA-03RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led03raps02,
                        'IA-03RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led03ravac,
                        'IA-04RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led04ractrl,
                        'IA-04RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led04rabpm,
                        'IA-04RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led04raps01,
                        'IA-04RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led04raps02,
                        'IA-04RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led04ravac,
                        'IA-05RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led05ractrl,
                        'IA-05RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led05rabpm,
                        'IA-05RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led05raps01,
                        'IA-05RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led05raps02,
                        'IA-05RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led05ravac,
                        'IA-06RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led06ractrl,
                        'IA-06RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led06rabpm,
                        'IA-06RaUnd:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led06raund,
                        'IA-06RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led06raps01,
                        'IA-06RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led06raps02,
                        'IA-06RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led06ravac,
                        'IA-07RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led07ractrl,
                        'IA-07RaUnd:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led07raund,
                        'IA-07RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led07raps01,
                        'IA-07RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led07raps02,
                        # 'IA-07RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        # self.temprackint.led07ravac,
                        'IA-08RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led08ractrl,
                        'IA-08RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led08rabpm,
                        'IA-08RaUnd:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led08raund,
                        'IA-08RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led08raps01,
                        # 'IA-08RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        # self.temprackint.led08raps02,
                        'IA-08RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led08ravac,
                        'IA-09RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led09ractrl,
                        'IA-09RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led09rabpm,
                        'IA-09RaUnd:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led09raund,
                        'IA-09RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led09raps01,
                        'IA-09RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led09raps02,
                        'IA-09RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led09ravac,
                        'IA-10RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led10ractrl,
                        'IA-10RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led10rabpm,
                        'IA-10RaUnd:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led10raund,
                        'IA-10RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led10raps01,
                        'IA-10RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led10raps02,
                        'IA-10RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led10ravac,
                        'IA-11RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led11ractrl,
                        'IA-11RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led11rabpm,
                        'IA-11RaUnd:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led11raund,
                        'IA-11RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led11raps01,
                        'IA-11RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led11raps02,
                        'IA-11RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led11ravac,
                        'IA-12RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led12ractrl,
                        'IA-12RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led12rabpm,
                        'IA-12RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led12raps01,
                        'IA-12RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led12raps02,
                        'IA-12RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led12ravac,
                        'IA-13RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led13ractrl,
                        'IA-13RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led13rabpm,
                        'IA-13RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led13raps01,
                        'IA-13RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led13raps02,
                        'IA-13RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led13ravac,
                        'IA-14RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led14ractrl,
                        'IA-14RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led14rabpm,
                        'IA-14RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led14raps01,
                        'IA-14RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led14raps02,
                        'IA-14RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led14ravac,
                        'IA-14RaDiag03:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led14radiag,
                        'IA-15RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led15ractrl,
                        'IA-15RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led15rabpm,
                        'IA-15RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led15raps01,
                        'IA-15RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led15raps02,
                        'IA-15RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led15ravac,
                        'IA-16RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led16ractrl,
                        'IA-16RaBbB:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led16rabbb,
                        'IA-16RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led16rabpm,
                        'IA-16RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led16raps01,
                        'IA-16RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led16raps02,
                        'IA-16RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led16ravac,
                        'IA-17RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led17ractrl,
                        'IA-17RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led17rabpm,
                        'IA-17RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led17raps01,
                        'IA-17RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led17raps02,
                        'IA-17RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led17ravac,
                        'IA-18RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led18ractrl,
                        'IA-18RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led18rabpm,
                        'IA-18RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led18raps01,
                        'IA-18RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led18raps02,
                        # 'IA-18RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        # self.temprackint.led18ravac,
                        # 'IA-19RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        # self.temprackint.led19ractrl,
                        # 'IA-19RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        # self.temprackint.led19rabpm,
                        # 'IA-19RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        # self.temprackint.led19raps01,
                        # 'IA-19RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        # self.temprackint.led19raps02,
                        'IA-19RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led19ravac,
                        'IA-19RaEPP:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led19raepp,
                        # 'IA-19RaVAC02:CO-SIMAR-02:RackInternalTemp-Mon':
                        # self.temprackint.led19ravac02,
                        'IA-20RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led20ractrl,
                        'IA-20RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led20rabpm,
                        'IA-20RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led20raps01,
                        'IA-20RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led20raps02,
                        'IA-20RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led20ravac,
                        'IA-20RaDiag01:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led20radiag01,
                        'IA-20RaBPMTL:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led20rabpmtl,
                        'IA-20RaEPP:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led20raepp,
                        'IA-20RaDiag02:CO-SIMAR-01:RackInternalTemp-Mon':
                        self.temprackint.led20radiag02,
                    }, 19, 32
                ),
            }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_temprackint)
        self.atualizar_status()

    def mostrar_janela_temprackint(self):
        """."""
        self.temprackint.setVisible(not self.isVisible())

    def atualizar_status(self):
        """."""
        todos_verdes = True
        for _, (sinais, temp_min, temp_max) in self.sinais_temprackint.items():
            for signal, led in sinais.items():
                utils.verificar_temprackint(signal, led, temp_min, temp_max)
                if not getattr(led, "state", False):
                    todos_verdes = False

            self.estado_ok = todos_verdes

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_verdes else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")


class Si_camvac(QtWidgets.QWidget):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.tempcamvac = uic.loadUi("ui/tempcamvac.ui")
        self._registar_grupos()

    def _registar_grupos(self):
        self.sinais_tempcamvac = {
            "tempcamvac1": (
                {
                    # 'SI-01B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    # led01b2b,
                    'SI-01B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led01b1a,
                    'SI-01B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led01b2a,
                    # 'SI-01B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    # led01b1b,
                    'SI-01B2FE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led01b2fe,
                    'SI-01BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led01bc,
                    'SI-01C2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led01c2,
                    'SI-01BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led01bcfe,
                    'SI-01SAFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led01safe,
                    'SI-01M1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led01m1,
                    'SI-01C1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led01c1,
                    'SI-02B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led02b1a,
                    'SI-02B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led02b1b,
                    # 'SI-02B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    # led02b2a,
                    'SI-02B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led02b2b,
                    'SI-02BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led02bc,
                    'SI-02BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led02bcfe,
                    # 'SI-02C1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led02c1,
                    'SI-02C2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led02c2,
                    'SI-02M1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led02m1,
                    'SI-02SBFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led02sbfe,
                    'SI-03B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led03b1a,
                    'SI-03B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led03b1b,
                    'SI-03B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led03b2a,
                    # 'SI-03B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    # led03b2b,
                    'SI-03B2FE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led03b2fe,
                    'SI-03BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led03bc,
                    'SI-03BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led03bcfe,
                    'SI-03C1:VA-PT100-ED:Temp-Mon':  self.tempcamvac.led03c1,
                    'SI-03C2:VA-PT100-ED:Temp-Mon':  self.tempcamvac.led03c2,
                    'SI-03M1:VA-PT100-ED:Temp-Mon':  self.tempcamvac.led03m1,
                    'SI-03SPFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led03spfe,
                    'SI-04B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led04b1a,
                    # 'SI-04B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    # led04b1b,
                    # 'SI-04B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    # led04b2a,
                    'SI-04B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led04b2b,
                    'SI-04BC:VA-PT100-ED:Temp-Mon':  self.tempcamvac.led04bc,
                    'SI-04BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led04bcfe,
                    'SI-04BCFE:VA-PT100-ED2:Temp-Mon': self.tempcamvac.
                    led04bcfe_2,
                    'SI-04C1:VA-PT100-ED:Temp-Mon':  self.tempcamvac.led04c1,
                    'SI-04C2:VA-PT100-ED:Temp-Mon':  self.tempcamvac.led04c2,
                    'SI-04M1:VA-PT100-ED:Temp-Mon':  self.tempcamvac.led04m1,
                    'SI-04SBFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led04sbfe,
                    'SI-05B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led05b1a,
                    # 'SI-05B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    # led05b1b,
                    'SI-05B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led05b2a,
                    'SI-05B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led05b2b,
                    'SI-05B2FE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led05b2fe,
                    'SI-05BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led05bc,
                    'SI-05BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led05bcfe,
                    'SI-05C1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led05c1,
                    'SI-05C2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led05c2,
                    'SI-05M1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led05m1,
                    'SI-05SAFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led05safe,
                    'SI-06B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led06b1a,
                    # 'SI-06B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    # led06b1b,
                    'SI-06B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led06b2a,
                    'SI-06B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led06b2b,
                    'SI-06BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led06bc,
                    'SI-06BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led06bcfe,
                    'SI-06BCFE:VA-PT100-ED2:Temp-Mon': self.tempcamvac.
                    led06bcfe_2,
                    'SI-06C1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led06c1,
                    'SI-06C2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led06c2,
                    'SI-06M1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led06m1,
                    'SI-06SBFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led06sbfe,
                    'SI-07B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led07b1a,
                    'SI-07B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led07b1b,
                    'SI-07B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led07b2a,
                    'SI-07B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led07b2b,
                    'SI-07B2FE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led07b2fe,
                    'SI-07BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led07bc,
                    'SI-07BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led07bcfe,
                    'SI-07C1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led07c1,
                    'SI-07C2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led07c2,
                    'SI-07M1:VA-PT100-ED:Temp-Mon':  self.tempcamvac.led07m1,
                    'SI-08B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led08b1a,
                    'SI-08B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led08b1b,
                    'SI-08B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led08b2a,
                    'SI-08B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led08b2b,
                    'SI-08BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led08bc,
                    'SI-08BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led08bcfe,
                    'SI-08C1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led08c1,
                    'SI-08C2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led08c2,
                    'SI-08M1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led08m1,
                    # 'SI-08SBFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    # led08sbfe,
                    'SI-09B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led09b1a,
                    'SI-09B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led09b1b,
                    'SI-09B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led09b2a,
                    'SI-09B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led09b2b,
                    'SI-09B2FE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led09b2fe,
                    'SI-09BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led09bc,
                    'SI-09BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led09bcfe,
                    'SI-09C1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led09c1,
                    'SI-09C2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led09c2,
                    'SI-09M1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led09m1,
                    'SI-10B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led10b1a,
                    'SI-10B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led10b1b,
                    'SI-10B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led10b2a,
                    'SI-10B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led10b2b,
                    'SI-10BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led10bc,
                    'SI-10BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led10bcfe,
                    'SI-10C1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led10c1,
                    'SI-10C2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led10c2,
                    'SI-10M1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led10m1,
                    'SI-10M2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led10m2,
                }, 17, 42
            ),
            "tempcamvac2": (
                {
                    'SI-11B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led11b1a,
                    'SI-11B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led11b1b,
                    'SI-11B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led11b2a,
                    # 'SI-11B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    # led11b2b,
                    'SI-11B2FE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led11b2fe,
                    'SI-11BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led11bc,
                    'SI-11BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led11bcfe,
                    'SI-11C1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led11c1,
                    'SI-11C2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led11c2,
                    'SI-11M1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led11m1,
                    'SI-12B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led12b1a,
                    'SI-12B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led12b1b,
                    'SI-12B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led12b2a,
                    'SI-12B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led12b2b,
                    'SI-12BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led12bc,
                    'SI-12BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led12bcfe,
                    'SI-12C1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led12c1,
                    'SI-12C2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led12c2,
                    'SI-12M1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led12m1,
                    'SI-12SBFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led12sbfe,
                    'SI-13B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led13b1a,
                    'SI-13B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led13b1b,
                    'SI-13B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led13b2a,
                    # 'SI-13B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    # led13b2b,
                    'SI-13B2FE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led13b2fe,
                    'SI-13BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led13bc,
                    'SI-13BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led13bcfe,
                    'SI-13C1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led13c1,
                    'SI-13C2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led13c2,
                    'SI-13M1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led13m1,
                    'SI-13SAFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led13safe,
                    'SI-14B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led14b1a,
                    'SI-14B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led14b1b,
                    'SI-14B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led14b2a,
                    'SI-14B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led14b2b,
                    'SI-14BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led14bc,
                    'SI-14BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led14bcfe,
                    'SI-14C1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led14c1,
                    'SI-14C2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led14c2,
                    'SI-14M1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led14m1,
                    'SI-14M2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led14m2,
                    'SI-15B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led15b1a,
                    'SI-15B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led15b1b,
                    'SI-15B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led15b2a,
                    'SI-15B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led15b2b,
                    'SI-15B2FE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led15b2fe,
                    'SI-15BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led15bc,
                    'SI-15BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led15bcfe,
                    'SI-15C1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led15c1,
                    # 'SI-15C2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led15c2,
                    'SI-15M1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led15m1,
                    'SI-15SPFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led15spfe,
                    'SI-16B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led16b1a,
                    'SI-16B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led16b1b,
                    # 'SI-16B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    # led16b2a,
                    'SI-16B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led16b2b,
                    'SI-16BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led16bc,
                    'SI-16BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led16bcfe,
                    'SI-16C1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led16c1,
                    'SI-16C2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led16c2,
                    'SI-16M1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led16m1,
                    'SI-16SBFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led16sbfe,
                    'SI-17B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led17b1a,
                    'SI-17B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led17b1b,
                    'SI-17B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led17b2a,
                    # 'SI-17B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    # led17b2b,
                    'SI-17B2FE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led17b2fe,
                    # 'SI-17BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led17bc,
                    # 'SI-17BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    # led17bcfe,
                    'SI-17C1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led17c1,
                    'SI-17C2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led17c2,
                    'SI-17M1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led17m1,
                    'SI-17SA:VA-PT100-ED:Temp-Mon': self.tempcamvac.led17sa,
                    # 'SI-17SAFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    # led17safe,
                    'SI-18B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led18b1a,
                    'SI-18B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led18b1b,
                    'SI-18B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led18b2a,
                    'SI-18B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led18b2b,
                    # 'SI-18BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led18bc,
                    'SI-18BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led18bcfe,
                    'SI-18C1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led18c1,
                    'SI-18C2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led18c2,
                    'SI-18M1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led18m1,
                    'SI-18SBFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led18sbfe,
                    'SI-19B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led19b1a,
                    'SI-19B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led19b1b,
                    'SI-19B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led19b2a,
                    'SI-19B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led19b2b,
                    'SI-19B2FE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led19b2fe,
                    'SI-19BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led19bc,
                    'SI-19BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led19bcfe,
                    'SI-19C1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led19c1,
                    'SI-19C2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led19c2,
                    'SI-19M1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led19m1,
                    'SI-19SPFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led19spfe,
                    'SI-20B1A:VA-PT100-ED:Temp-Mon': self.tempcamvac.led20b1a,
                    'SI-20B1B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led20b1b,
                    # 'SI-20B2A:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    # led20b2a,
                    'SI-20B2B:VA-PT100-ED:Temp-Mon': self.tempcamvac.led20b2b,
                    'SI-20BC:VA-PT100-ED:Temp-Mon': self.tempcamvac.led20bc,
                    'SI-20BCFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led20bcfe,
                    'SI-20C1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led20c1,
                    'SI-20C2:VA-PT100-ED:Temp-Mon': self.tempcamvac.led20c2,
                    'SI-20M1:VA-PT100-ED:Temp-Mon': self.tempcamvac.led20m1,
                    'SI-20SBFE:VA-PT100-ED:Temp-Mon': self.tempcamvac.
                    led20sbfe,
                }, 17, 39
            ),
        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_tempcamvac)
        self.atualizar_status()

    def mostrar_janela_tempcamvac(self):
        """."""
        self.tempcamvac.setVisible(not self.isVisible())

    def atualizar_status(self):
        """."""
        todos_verdes = True
        for _, (sinais, temp_min, temp_max) in self.sinais_tempcamvac.items():
            for signal, led in sinais.items():
                utils.verificar_tempcamvac(signal, led, temp_min, temp_max)
                if not getattr(led, "state", False):
                    todos_verdes = False

            self.estado_ok = todos_verdes

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_verdes else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")


class Si_circhid(QtWidgets.QWidget):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.tempcirchid = uic.loadUi("ui/tempcirchid.ui")
        self._registar_grupos()

    def _registar_grupos(self):
        self.sinais_tempcirchid = {
            "circ_c1": (
                {
                    'SI-08-MBTemp-10-CH6': self.tempcirchid.led10ch6,
                    'SI-18-MBTemp-13-CH5': self.tempcirchid.led13ch5,
                    'SI-18-MBTemp-13-CH6': self.tempcirchid.led13ch6,
                }, 20, 24
            ),
            "circ2_c1": (
                {
                    'SI-08-MBTemp-10-CH8': self.tempcirchid.led10ch8,
                    'SI-18-MBTemp-13-CH7': self.tempcirchid.led13ch7,
                }, 23, 27
            ),
            "circ_c2": (
                {
                    'UA-21CHall:CR-IHMCtrl:dbAdsSta_strAdsA_m12CP2CW1035T-Mon':
                    self.tempcirchid.ledcp21035t,
                    'UA-21CHall:CR-IHMCtrl:dbAdsSta_strAdsA_m12CP1CW1065T-Mon':
                    self.tempcirchid.ledcp11065t,
                    'UA-21CHall:CR-IHMCtrl:dbAdsSta_strAdsA_m12CP2CW1065T-Mon':
                    self.tempcirchid.ledcp21065t,
                }, 21, 33.5
            ),
            "circ_c3": (
                {
                    'RA-TLSIA:RF-Circulator:Tout-Mon': self.tempcirchid.
                    ledcirctout,
                    'RA-TLSIA:RF-Circulator:Tin-Mon': self.tempcirchid.
                    ledcirctin,

                }, 20, 22
            ),
            "circ_c4": (
                {
                    'LA-CN:H1MPS-1:K1Temp1': self.tempcirchid.ledk1temp1,
                    'LA-CN:H1MPS-1:K2Temp1': self.tempcirchid.ledk2temp1,
                    'LA-CN:H1MPS-1:K1Temp2': self.tempcirchid.ledk1temp2,
                    'LA-CN:H1MPS-1:K2Temp2': self.tempcirchid.ledk2temp2,
                }, 18, 21
            ),
            "circ_c5_1": (
                {
                    'TB-Fam:PS-B:InductorTemperatureIIB-Mon': self.tempcirchid.
                    ledinductoriib,
                }, 22, 24
            ),
            "circ2_c5_1": (
                {
                    'BO-15U:VA-PT100-BG:Temp-Mon': self.tempcirchid.
                    ledbo15vacpt100,
                }, 24, 26
            ),
            "circ3_c5_1": (
                {
                    'SI-18-MBTemp-13-CH5': self.tempcirchid.ledsi18mbtemp,
                }, 20, 22
            ),
            "circ4_c5_1": (
                {
                    'TS-Fam:PS-B:TemperatureIIBMod1-Mon': self.tempcirchid.
                    ledtsbtempmod1,
                }, 44, 46
            ),
            "circ5_c5_1": (
                {
                    'TS-Fam:PS-B:TemperatureIIBMod4-Mon': self.tempcirchid.
                    ledtsbtempmod4,
                }, 38, 40
            ),
            "circ_c5_2": (
                {
                    'BO-05U:VA-PT100-BG:Temp-Mon': self.tempcirchid.
                    led05uvacpt100,
                    'BO-10U:VA-PT100-BG:Temp-Mon': self.tempcirchid.
                    led10uvacpt100,
                    'BO-14U:VA-PT100-BG:Temp-Mon': self.tempcirchid.
                    led14uvacpt100,
                }, 22, 26
            ),
            "circ_c8": (
                {
                    'SI-Fam:PS-QDA:InductorTemperatureIIB-Mon': self.
                    tempcirchid.ledqdainductor,
                    'SI-Fam:PS-QDA:HeatSinkTemperatureIIB-Mon': self.
                    tempcirchid.ledqdaheatsink,
                    'SI-Fam:PS-SDA0:HeatSinkTemperatureIIB-Mon': self.
                    tempcirchid.ledsda0heatsink,
                    'SI-Fam:PS-SFP1:HeatSinkTemperatureIIB-Mon': self.
                    tempcirchid.ledsfp1heatsink,
                }, 19, 24
            ),
        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_tempcirchid)
        self.atualizar_status()

    def mostrar_janela_tempcirchid(self):
        """."""
        self.tempcirchid.setVisible(not self.isVisible())

    def atualizar_status(self):
        """."""
        todos_verdes = True
        for _, (sinais, temp_min, temp_max) in self.sinais_tempcirchid.items():
            for signal, led in sinais.items():
                utils.verificar_tempcamvac(signal, led, temp_min, temp_max)
                if not getattr(led, "state", False):
                    todos_verdes = False

            self.estado_ok = todos_verdes

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_verdes else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")


class Si_conecserv(QtWidgets.QWidget):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.tempconecserv = uic.loadUi("ui/tempconecserv.ui")
        self._registar_grupos()

    def _registar_grupos(self):
        self.sinais_tempconecserv = {
                "ctrl":    (
                    {
                        'CA-RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon': self.
                        tempconecserv.led_ctrl,
                    }, 28, 31.5
                ),
                "rainter":    (
                    {
                        'CA-RaInter:CO-SIMAR-01:RackInternalTemp-Mon': self.
                        tempconecserv.led_inter,
                    }, 25, 30
                ),
                "ratim":    (
                    {
                        'CA-RaTim:CO-SIMAR-01:RackInternalTemp-Mon': self.
                        tempconecserv.led_tim,
                    }, 23, 25
                ),
                "server":    (
                    {
                        'RoomSrv:CO-SIMAR-01:AmbientTemp-Mon': self.
                        tempconecserv.led_server,
                    }, 17.5, 20.5
                ),
                "ambient":    (
                    {
                        'CA:CO-SIMAR-01:AmbientTemp-Mon': self.tempconecserv.
                        led_ambient,
                    }, 21, 23.5
                ),
        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_tempconecserv)
        self.atualizar_status()

    def mostrar_janela_tempconecserv(self):
        """."""
        self.tempconecserv.setVisible(not self.isVisible())

    def atualizar_status(self):
        """."""
        todos_verdes = True
        for _, (sinais, temp_min, temp_max) in self.sinais_tempconecserv.items():
            for signal, led in sinais.items():
                utils.verificar_temprackpu(signal, led, temp_min, temp_max)
                if not getattr(led, "state", False):
                    todos_verdes = False

            self.estado_ok = todos_verdes

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_verdes else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")


class Si_magnets(QtWidgets.QWidget):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.tempmagnets = uic.loadUi("ui/tempmagnets.ui")
        self._registar_grupos()

    def _registar_grupos(self):
        self.sinais_tempmagnets = {
            "magnets":    (
                {
                    'SI-01-MBTemp-22-CH6': self.tempmagnets.ledb2c3_22ch6,
                    'SI-01-MBTemp-22-CH7': self.tempmagnets.ledb2c3_22ch7,
                    'SI-01-MBTemp-22-CH8': self.tempmagnets.ledb2c3_22ch8,
                    'SI-01-MBTemp-14-CH5': self.tempmagnets.ledq1c1_14ch5,
                    'SI-01-MBTemp-14-CH6': self.tempmagnets.ledq1c1_14ch6,
                    'SI-01-MBTemp-14-CH7': self.tempmagnets.ledq1c1_14ch7,
                    'SI-01-MBTemp-23-CH6': self.tempmagnets.ledqfbm1_23ch6,
                    'SI-01-MBTemp-23-CH7': self.tempmagnets.ledqfbm1_23ch7,
                    'SI-03-MBTemp-23-CH5': self.tempmagnets.ledb1c4_23ch5,
                    'SI-03-MBTemp-23-CH6': self.tempmagnets.ledb1c4_23ch6,
                    'SI-03-MBTemp-23-CH7': self.tempmagnets.ledb1c4_13ch7,
                    'SI-03-MBTemp-13-CH5': self.tempmagnets.ledb2c3_13ch5,
                    'SI-03-MBTemp-13-CH6': self.tempmagnets.ledb2c3_13ch6,
                    'SI-03-MBTemp-13-CH7': self.tempmagnets.ledb2c3_13ch7,
                    'SI-03-MBTemp-22-CH6': self.tempmagnets.ledq3c3_22ch6,
                    # 'SI-03-MBTemp-22-CH7': self.tempmagnets.ledq3c3_22ch7,
                    'SI-03-MBTemp-22-CH8': self.tempmagnets.ledq3c3_22ch8,
                    'SI-06-MBTemp-23-CH5': self.tempmagnets.led06b1c4_23ch5,
                    'SI-06-MBTemp-23-CH6': self.tempmagnets.led06b1c4_23ch6,
                    # 'SI-06-MBTemp-23-CH7': self.tempmagnets.led06b1c4_23ch7,
                    'SI-06-MBTemp-11-CH4': self.tempmagnets.led06b2c2_11ch4,
                    'SI-06-MBTemp-11-CH5': self.tempmagnets.led06b2c2_11ch5,
                    'SI-06-MBTemp-11-CH6': self.tempmagnets.led06b2c2_11ch6,
                    'SI-06-MBTemp-22-CH6': self.tempmagnets.led06q3c3_22ch6,
                    'SI-06-MBTemp-22-CH7': self.tempmagnets.led06q3c3_22ch7,
                    # 'SI-06-MBTemp-22-CH8': self.tempmagnets.led06q3c3_22ch8,
                    'SI-08-MBTemp-23-CH5': self.tempmagnets.led08b1c4_23ch5,
                    'SI-08-MBTemp-23-CH6': self.tempmagnets.led08b1c4_23ch6,
                    # 'SI-08-MBTemp-23-CH7': self.tempmagnets.led08b1c4_23ch7,
                    'SI-08-MBTemp-10-CH3': self.tempmagnets.led08b2c2_10ch3,
                    'SI-08-MBTemp-10-CH4': self.tempmagnets.led08b2c2_10ch4,
                    'SI-08-MBTemp-10-CH5': self.tempmagnets.led08b2c2_10ch5,
                    'SI-08-MBTemp-22-CH6': self.tempmagnets.led08q3c3_22ch6,
                    'SI-08-MBTemp-22-CH7': self.tempmagnets.led08q3c3_22ch7,
                    'SI-08-MBTemp-22-CH8': self.tempmagnets.led08q3c3_22ch8,
                    'SI-11-MBTemp-23-CH5': self.tempmagnets.led11b1c4_23ch5,
                    'SI-11-MBTemp-23-CH6': self.tempmagnets.led11b1c4_23ch6,
                    'SI-11-MBTemp-23-CH7': self.tempmagnets.led11b1c4_23ch7,
                    'SI-11-MBTemp-13-CH3': self.tempmagnets.led11b2c2_13ch3,
                    'SI-11-MBTemp-13-CH5': self.tempmagnets.led11b2c2_13ch5,
                    'SI-11-MBTemp-12-CH8': self.tempmagnets.led11b2c2_12ch8,
                    'SI-11-MBTemp-22-CH6': self.tempmagnets.led11q3c3_22ch6,
                    'SI-11-MBTemp-22-CH7': self.tempmagnets.led11q3c3_22ch7,
                    'SI-11-MBTemp-22-CH8': self.tempmagnets.led11q3c3_22ch8,
                    # 'SI-13-MBTemp-22-CH7': self.tempmagnets.led22b2c3_22ch7,
                    'SI-13-MBTemp-22-CH8': self.tempmagnets.led22b2c3_22ch8,
                    'SI-13-MBTemp-13-CH5': self.tempmagnets.led13q1c1_13ch5,
                    'SI-13-MBTemp-13-CH6': self.tempmagnets.led13q1c1_13ch6,
                    'SI-13-MBTemp-13-CH7': self.tempmagnets.led13q1c1_13ch7,
                    'SI-13-MBTemp-23-CH5': self.tempmagnets.led13qfbm1_23ch5,
                    # 'SI-13-MBTemp-23-CH6': self.tempmagnets.led13qfbm1_23ch6,
                    'SI-13-MBTemp-23-CH7': self.tempmagnets.led13qfbm1_23ch7,
                    'SI-16-MBTemp-22-CH6': self.tempmagnets.led16b2c3_22ch6,
                    'SI-16-MBTemp-22-CH7': self.tempmagnets.led16b2c3_22ch7,
                    'SI-16-MBTemp-22-CH8': self.tempmagnets.led16b2c3_22ch8,
                    'SI-16-MBTemp-11-CH6': self.tempmagnets.led16q1c1_11ch6,
                    'SI-16-MBTemp-11-CH7': self.tempmagnets.led16q1c1_11ch7,
                    'SI-16-MBTemp-11-CH8': self.tempmagnets.led16q1c1_11ch8,
                    'SI-16-MBTemp-23-CH5': self.tempmagnets.led16qfbm1_23ch5,
                    'SI-16-MBTemp-23-CH6': self.tempmagnets.led16qfbm1_23ch6,
                    'SI-16-MBTemp-23-CH7': self.tempmagnets.led16qfbm1_23ch7,
                    'SI-18-MBTemp-23-CH5': self.tempmagnets.led18b1c4_23ch5,
                    'SI-18-MBTemp-23-CH6': self.tempmagnets.led18b1c4_23ch6,
                    'SI-18-MBTemp-23-CH7': self.tempmagnets.led18b1c4_23ch7,
                    'SI-18-MBTemp-11-CH5': self.tempmagnets.led18b2c2_11ch5,
                    'SI-18-MBTemp-11-CH6': self.tempmagnets.led18b2c2_11ch6,
                    'SI-18-MBTemp-11-CH7': self.tempmagnets.led18b2c2_11ch7,
                    'SI-18-MBTemp-22-CH6': self.tempmagnets.led18q3c3_22ch6,
                    'SI-18-MBTemp-22-CH7': self.tempmagnets.led18q3c3_22ch7,
                    'SI-18-MBTemp-22-CH8': self.tempmagnets.led18q3c3_22ch8,
                }, 19, 27
            ),
        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_tempmagnets)
        self.atualizar_status()

    def mostrar_janela_tempmagnets(self):
        """."""
        self.tempmagnets.setVisible(not self.isVisible())

    def atualizar_status(self):
        """."""
        todos_verdes = True
        for _, (sinais, temp_min, temp_max) in self.sinais_tempmagnets.items():
            for signal, led in sinais.items():
                utils.verificar_tempmagnets(signal, led, temp_min, temp_max)
                if not getattr(led, "state", False):
                    todos_verdes = False

            self.estado_ok = todos_verdes

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_verdes else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")


class Si_hls(QtWidgets.QWidget):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.temphls = uic.loadUi("ui/temphls.ui")
        self._registrar_grupos()

    def _registrar_grupos(self):
        self.sinais_temphls = {
            "hls":      (
                {
                    # 'TU-03C:SS-HLS-Ax24SW1:Temp-Mon': self.temphls.
                    # led_hlsax24sw1,
                    # 'TU-04C:SS-HLS-Ax27SW2:Temp-Mon': self.temphls.
                    # led_hlsax27sw2,
                    # 'TU-05C:SS-HLS-Ax29SW3:Temp-Mon': self.temphls.
                    # led_hlsax29sw3,
                    # 'TU-06C:SS-HLS-Ax31SW4:Temp-Mon': self.temphls.
                    # led_hlsax31sw4,
                    # 'TU-06C:SS-HLS-Ax33SW5:Temp-Mon': self.temphls.
                    # led_hlsax33sw5,
                    # 'TU-18C:SS-HLS-Ax09SE1:Temp-Mon': self.temphls.
                    # led_hlsax19se1,
                    # 'TU-19C:SS-HLS-Ax12SE2:Temp-Mon': self.temphls.
                    # led_hlsax12se2,
                    # 'TU-20C:SS-HLS-Ax14SE3:Temp-Mon': self.temphls.
                    # led_hlsax14se3,
                    # 'TU-01C:SS-HLS-Ax16SE4:Temp-Mon': self.temphls.
                    # led_hlsax16se4,
                    # 'TU-01C:SS-HLS-Ax18SE5:Temp-Mon': self.temphls.
                    # led_hlsax18se5,
                    # 'TU-13C:SS-HLS-Ax54NE1:Temp-Mon': self.temphls.
                    # led_hlsax54ne1,
                    # 'TU-14C:SS-HLS-Ax57NE2:Temp-Mon': self.temphls.
                    # led_hlsax57ne2,
                    # 'TU-15C:SS-HLS-Ax59NE3:Temp-Mon': self.temphls.
                    # led_hlsax59ne3,
                    # 'TU-16C:SS-HLS-Ax01NE4:Temp-Mon': self.temphls.
                    # led_hlsax01ne4,
                    # 'TU-17C:SS-HLS-Ax04NE5:Temp-Mon': self.temphls.
                    # led_hlsax04ne5,
                    # 'TU-08C:SS-HLS-Ax39NW1:Temp-Mon': self.temphls.
                    # led_hlsax39nw1,
                    # 'TU-09C:SS-HLS-Ax42NW2:Temp-Mon': self.temphls.
                    # led_hlsax42nw2,
                    # 'TU-10C:SS-HLS-Ax44NW3:Temp-Mon': self.temphls.
                    # led_hlsax44nw3,
                    # 'TU-11C:SS-HLS-Ax46NW4:Temp-Mon': self.temphls.
                    # led_hlsax46nw4,
                    # 'TU-11C:SS-HLS-Ax48NW5:Temp-Mon': self.temphls.
                    # led_hlsax48nw5,
                }, 24, 26
            ),
        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_temphls)
        self.atualizar_status()

    def mostrar_janela_temphls(self):
        """."""
        self.temphls.setVisible(not self.isVisible())

    def atualizar_status(self):
        """."""
        todos_verdes = True
        for _, (sinais, temp_min, temp_max) in self.sinais_temphls.items():
            for signal, led in sinais.items():
                utils.verificar_temphls(signal, led, temp_min, temp_max)
                if not getattr(led, "state", False):
                    todos_verdes = False

            self.estado_ok = todos_verdes

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_verdes else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")


class Si_dclinks(QtWidgets.QWidget):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.tempdclinks = uic.loadUi("ui/tempdclinks.ui")
        self._registar_grupos()

    def _registar_grupos(self):
        self.sinais_tempdclinks = {
            "dipolo":   (
                {
                    'PA-RaPSD01:PS-DCLink-1A:IGBTT-Mon': self.tempdclinks.
                    led1aigbt_01,
                    'PA-RaPSD01:PS-DCLink-1B:IGBTT-Mon': self.tempdclinks.
                    led1bigbt_01,
                    'PA-RaPSD01:PS-DCLink-3A:IGBTT-Mon': self.tempdclinks.
                    led3aigbt_01,
                    'PA-RaPSD01:PS-DCLink-3B:IGBTT-Mon': self.tempdclinks.
                    led3bigbt_01,
                    'PA-RaPSD03:PS-DCLink-2A:IGBTT-Mon': self.tempdclinks.
                    led2aigbt_03,
                    'PA-RaPSD03:PS-DCLink-2B:IGBTT-Mon': self.tempdclinks.
                    led2bigbt_03,
                    'PA-RaPSD03:PS-DCLink-4A:IGBTT-Mon': self.tempdclinks.
                    led4aigbt_03,
                    'PA-RaPSD03:PS-DCLink-4B:IGBTT-Mon': self.tempdclinks.
                    led4bigbt_03,
                    'PA-RaPSD05:PS-DCLink-1A:IGBTT-Mon': self.tempdclinks.
                    led1aigbt_05,
                    'PA-RaPSD05:PS-DCLink-1B:IGBTT-Mon': self.tempdclinks.
                    led1bigbt_05,
                    'PA-RaPSD05:PS-DCLink-3A:IGBTT-Mon': self.tempdclinks.
                    led3aigbt_05,
                    'PA-RaPSD05:PS-DCLink-3B:IGBTT-Mon': self.tempdclinks.
                    led3bigbt_05,
                    'PA-RaPSD07:PS-DCLink-2A:IGBTT-Mon': self.tempdclinks.
                    led2aigbt_07,
                    'PA-RaPSD07:PS-DCLink-2B:IGBTT-Mon': self.tempdclinks.
                    led2bigbt_07,
                    'PA-RaPSD07:PS-DCLink-4A:IGBTT-Mon': self.tempdclinks.
                    led4aigbt_07,
                    'PA-RaPSD07:PS-DCLink-4B:IGBTT-Mon': self.tempdclinks.
                    led4bigbt_07,
                    'PA-RaPSD01:PS-DCLink-1A:RectifierT-Mon': self.tempdclinks.
                    led1arectifier_01,
                    'PA-RaPSD01:PS-DCLink-1B:RectifierT-Mon': self.tempdclinks.
                    led1brectifier_01,
                    'PA-RaPSD01:PS-DCLink-3A:RectifierT-Mon': self.tempdclinks.
                    led3arectifier_01,
                    'PA-RaPSD01:PS-DCLink-3B:RectifierT-Mon': self.tempdclinks.
                    led3brectifier_01,
                    'PA-RaPSD03:PS-DCLink-2A:RectifierT-Mon': self.tempdclinks.
                    led2arectifier_03,
                    'PA-RaPSD03:PS-DCLink-2B:RectifierT-Mon': self.tempdclinks.
                    led2brectifier_03,
                    'PA-RaPSD03:PS-DCLink-4A:RectifierT-Mon': self.tempdclinks.
                    led4arectifier_03,
                    'PA-RaPSD03:PS-DCLink-4B:RectifierT-Mon': self.tempdclinks.
                    led4brectifier_03,
                    'PA-RaPSD05:PS-DCLink-1A:RectifierT-Mon': self.tempdclinks.
                    led1arectifier_05,
                    'PA-RaPSD05:PS-DCLink-1B:RectifierT-Mon': self.tempdclinks.
                    led1brectifier_05,
                    'PA-RaPSD05:PS-DCLink-3A:RectifierT-Mon': self.tempdclinks.
                    led3arectifier_05,
                    'PA-RaPSD05:PS-DCLink-3B:RectifierT-Mon': self.tempdclinks.
                    led3brectifier_05,
                    'PA-RaPSD07:PS-DCLink-2A:RectifierT-Mon': self.tempdclinks.
                    led2arectifier_07,
                    'PA-RaPSD07:PS-DCLink-2B:RectifierT-Mon': self.tempdclinks.
                    led2brectifier_07,
                    'PA-RaPSD07:PS-DCLink-4A:RectifierT-Mon': self.tempdclinks.
                    led4arectifier_07,
                    'PA-RaPSD07:PS-DCLink-4B:RectifierT-Mon': self.tempdclinks.
                    led4brectifier_07,
                    'PA-RaPSD01:PS-DCLink-1A:PCBT-Mon': self.tempdclinks.
                    led1apcb_01,
                    'PA-RaPSD01:PS-DCLink-1B:PCBT-Mon': self.tempdclinks.
                    led1bpcb_01,
                    'PA-RaPSD01:PS-DCLink-3A:PCBT-Mon': self.tempdclinks.
                    led3apcb_01,
                    'PA-RaPSD01:PS-DCLink-3B:PCBT-Mon': self.tempdclinks.
                    led3bpcb_01,
                    'PA-RaPSD03:PS-DCLink-2A:PCBT-Mon': self.tempdclinks.
                    led2apcb_03,
                    'PA-RaPSD03:PS-DCLink-2B:PCBT-Mon': self.tempdclinks.
                    led2bpcb_03,
                    'PA-RaPSD03:PS-DCLink-4A:PCBT-Mon': self.tempdclinks.
                    led4apcb_03,
                    'PA-RaPSD03:PS-DCLink-4B:PCBT-Mon': self.tempdclinks.
                    led4bpcb_03,
                    'PA-RaPSD05:PS-DCLink-1A:PCBT-Mon': self.tempdclinks.
                    led1apcb_05,
                    'PA-RaPSD05:PS-DCLink-1B:PCBT-Mon': self.tempdclinks.
                    led1bpcb_05,
                    'PA-RaPSD05:PS-DCLink-3A:PCBT-Mon': self.tempdclinks.
                    led3apcb_05,
                    'PA-RaPSD05:PS-DCLink-3B:PCBT-Mon': self.tempdclinks.
                    led3bpcb_05,
                    'PA-RaPSD07:PS-DCLink-2A:PCBT-Mon': self.tempdclinks.
                    led2apcb_07,
                    'PA-RaPSD07:PS-DCLink-2B:PCBT-Mon': self.tempdclinks.
                    led2bpcb_07,
                    'PA-RaPSD07:PS-DCLink-4A:PCBT-Mon': self.tempdclinks.
                    led4apcb_07,
                    'PA-RaPSD07:PS-DCLink-4B:PCBT-Mon': self.tempdclinks.
                    led4bpcb_07,
                }, 27, 57
            ),
            "quadrupolo":   (
                {
                    'PA-RaPSA01:PS-DCLink-QFAP:IGBTT-Mon': self.tempdclinks.
                    led01qfap_igbt,
                    'PA-RaPSA01:PS-DCLink-QFB:IGBTT-Mon': self.tempdclinks.
                    led01qfb_igbt,
                    'PA-RaPSA03:PS-DCLink-QDAP:IGBTT-Mon': self.tempdclinks.
                    led03qdap_igbt,
                    'PA-RaPSA04:PS-DCLink-QDB:IGBTT-Mon': self.tempdclinks.
                    led04qdb_igbt,
                    'PA-RaPSA06:PS-DCLink-Q13A:IGBTT-Mon': self.tempdclinks.
                    led06q13a_igbt,
                    'PA-RaPSA06:PS-DCLink-Q13B:IGBTT-Mon': self.tempdclinks.
                    led06q13b_igbt,
                    'PA-RaPSA06:PS-DCLink-Q13C:IGBTT-Mon': self.tempdclinks.
                    led06q13c_igbt,
                    'PA-RaPSA07:PS-DCLink-Q24A:IGBTT-Mon': self.tempdclinks.
                    led07q24a_igbt,
                    'PA-RaPSA07:PS-DCLink-Q24B:IGBTT-Mon': self.tempdclinks.
                    led07q24b_igbt,
                    'PA-RaPSA07:PS-DCLink-Q24C:IGBTT-Mon': self.tempdclinks.
                    led07q24c_igbt,
                    'PA-RaPSA01:PS-DCLink-QFAP:RectifierT-Mon': self.
                    tempdclinks.led01qfap_rectifier,
                    'PA-RaPSA01:PS-DCLink-QFB:RectifierT-Mon': self.
                    tempdclinks.led01qfb_rectifier,
                    'PA-RaPSA03:PS-DCLink-QDAP:RectifierT-Mon': self.
                    tempdclinks.led03qdap_rectifier,
                    'PA-RaPSA04:PS-DCLink-QDB:RectifierT-Mon': self.
                    tempdclinks.led04qdb_rectifier,
                    'PA-RaPSA06:PS-DCLink-Q13A:RectifierT-Mon': self.
                    tempdclinks.led06q13a_rectifier,
                    'PA-RaPSA06:PS-DCLink-Q13B:RectifierT-Mon': self.
                    tempdclinks.led06q13b_rectifier,
                    'PA-RaPSA06:PS-DCLink-Q13C:RectifierT-Mon': self.
                    tempdclinks.led06q13c_rectifier,
                    'PA-RaPSA07:PS-DCLink-Q24A:RectifierT-Mon': self.
                    tempdclinks.led07q24a_rectifier,
                    'PA-RaPSA07:PS-DCLink-Q24B:RectifierT-Mon': self.
                    tempdclinks.led07q24b_rectifier,
                    'PA-RaPSA07:PS-DCLink-Q24C:RectifierT-Mon': self.
                    tempdclinks.led07q24c_rectifier,
                    'PA-RaPSA01:PS-DCLink-QFAP:PCBT-Mon': self.tempdclinks.
                    led01qfap_pcb,
                    'PA-RaPSA01:PS-DCLink-QFB:PCBT-Mon': self.tempdclinks.
                    led01qfb_pcb,
                    'PA-RaPSA03:PS-DCLink-QDAP:PCBT-Mon': self.tempdclinks.
                    led03qdap_pcb,
                    'PA-RaPSA04:PS-DCLink-QDB:PCBT-Mon': self.tempdclinks.
                    led04qdb_pcb,
                    'PA-RaPSA06:PS-DCLink-Q13A:PCBT-Mon': self.tempdclinks.
                    led06q13a_pcb,
                    'PA-RaPSA06:PS-DCLink-Q13B:PCBT-Mon': self.tempdclinks.
                    led06q13b_pcb,
                    'PA-RaPSA06:PS-DCLink-Q13C:PCBT-Mon': self.tempdclinks.
                    led06q13c_pcb,
                    'PA-RaPSA07:PS-DCLink-Q24A:PCBT-Mon': self.tempdclinks.
                    led07q24a_pcb,
                    'PA-RaPSA07:PS-DCLink-Q24B:PCBT-Mon': self.tempdclinks.
                    led07q24b_pcb,
                    'PA-RaPSA07:PS-DCLink-Q24C:PCBT-Mon': self.tempdclinks.
                    led07q24c_pcb,
                }, 26, 57
            ),
            "sextupolo_foc":   (
                {
                        'PA-RaPSB03:PS-DCLink-SFAP0:IGBTT-Mon': self.
                        tempdclinks.led03sfap0_igbt,
                        'PA-RaPSB03:PS-DCLink-SFB0:IGBTT-Mon': self.
                        tempdclinks.led03sfb0_igbt,
                        'PA-RaPSB07:PS-DCLink-SFA2SDP1:IGBTT-Mon': self.
                        tempdclinks.led07sfa2dp1_igbt,
                        'PA-RaPSB08:PS-DCLink-SFB1:IGBTT-Mon': self.
                        tempdclinks.led08sfb1_igbt,
                        'PA-RaPSB10:PS-DCLink-SFP12:IGBTT-Mon': self.
                        tempdclinks.led10sfp12_igbt,
                        'PA-RaPSB10:PS-DCLink-SFB2:IGBTT-Mon': self.
                        tempdclinks.led10sfb2_igbt,
                        'PA-RaPSB03:PS-DCLink-SFAP0:RectifierT-Mon': self.
                        tempdclinks.led03sfap0_rectifier,
                        'PA-RaPSB03:PS-DCLink-SFB0:RectifierT-Mon': self.
                        tempdclinks.led03sfb0_rectifier,
                        'PA-RaPSB07:PS-DCLink-SFA2SDP1:RectifierT-Mon': self.
                        tempdclinks.led07sfa2dp1_rectifier,
                        'PA-RaPSB08:PS-DCLink-SFB1:RectifierT-Mon': self.
                        tempdclinks.led08sfb1_rectifier,
                        'PA-RaPSB10:PS-DCLink-SFP12:RectifierT-Mon': self.
                        tempdclinks.led10sfp12_rectifier,
                        'PA-RaPSB10:PS-DCLink-SFB2:RectifierT-Mon': self.
                        tempdclinks.led10sfb2_rectifier,
                        'PA-RaPSB03:PS-DCLink-SFB0:PCBT-Mon': self.tempdclinks.
                        led03sfb0_pcb,
                        'PA-RaPSB03:PS-DCLink-SFAP0:PCBT-Mon': self.
                        tempdclinks.led03sfap0_pcb,
                        'PA-RaPSB07:PS-DCLink-SFA2SDP1:PCBT-Mon': self.
                        tempdclinks.led07sfa2sdp1_pcb,
                        'PA-RaPSB08:PS-DCLink-SFB1:PCBT-Mon': self.tempdclinks.
                        led08sfb1_pcb,
                        'PA-RaPSB10:PS-DCLink-SFB2:PCBT-Mon': self.tempdclinks.
                        led10sfb2_pcb,
                        'PA-RaPSB10:PS-DCLink-SFP12:PCBT-Mon': self.
                        tempdclinks.led10sfp12_pcb,
                }, 17, 47
            ),
            "sextupolo_defoc":   (
                {
                        'PA-RaPSB01:PS-DCLink-SDB0:IGBTT-Mon':
                        self.tempdclinks.ledsdb0_igbt,
                        'PA-RaPSB01:PS-DCLink-SDAP0:IGBTT-Mon':
                        self.tempdclinks.ledsdap0_igbt,
                        'PA-RaPSB04:PS-DCLink-SDA12:IGBTT-Mon':
                        self.tempdclinks.ledsda12_igbt,
                        'PA-RaPSB04:PS-DCLink-SDB1:IGBTT-Mon':
                        self.tempdclinks.ledsdb1_igbt,
                        'PA-RaPSB05:PS-DCLink-SDA3SFA1:IGBTT-Mon':
                        self.tempdclinks.ledsda3sfa1_igbt,
                        'PA-RaPSB05:PS-DCLink-SDB2:IGBTT-Mon':
                        self.tempdclinks.ledsdb2_igbt,
                        'PA-RaPSB07:PS-DCLink-SFA2SDP1:IGBTT-Mon':
                        self.tempdclinks.ledsfa2sdp1_igbt,
                        'PA-RaPSB07:PS-DCLink-SDB3:IGBTT-Mon':
                        self.tempdclinks.ledsdb3_igbt,
                        'PA-RaPSB08:PS-DCLink-SDP23:IGBTT-Mon':
                        self.tempdclinks.ledsdp23_igbt,
                        'PA-RaPSB01:PS-DCLink-SDB0:RectifierT-Mon':
                        self.tempdclinks.ledsdb0_rectifier,
                        'PA-RaPSB01:PS-DCLink-SDAP0:RectifierT-Mon':
                        self.tempdclinks.ledsdap0_rectifier,
                        'PA-RaPSB04:PS-DCLink-SDA12:RectifierT-Mon':
                        self.tempdclinks.ledsda12_rectifier,
                        'PA-RaPSB04:PS-DCLink-SDB1:RectifierT-Mon':
                        self.tempdclinks.ledsdb1_rectifier,
                        'PA-RaPSB05:PS-DCLink-SDA3SFA1:RectifierT-Mon':
                        self.tempdclinks.ledsda3sfa1_rectifier,
                        'PA-RaPSB05:PS-DCLink-SDB2:RectifierT-Mon':
                        self.tempdclinks.ledsdb2_rectifier,
                        'PA-RaPSB07:PS-DCLink-SFA2SDP1:RectifierT-Mon':
                        self.tempdclinks.ledsfa2sdp1_rectifier,
                        'PA-RaPSB07:PS-DCLink-SDB3:RectifierT-Mon':
                        self.tempdclinks.ledsdb3_rectifier,
                        'PA-RaPSB08:PS-DCLink-SDP23:RectifierT-Mon':
                        self.tempdclinks.ledsdp23_rectifier,
                        'PA-RaPSB01:PS-DCLink-SDAP0:PCBT-Mon':
                        self.tempdclinks.ledsdap0_pcb,
                        'PA-RaPSB01:PS-DCLink-SDB0:PCBT-Mon':
                        self.tempdclinks.ledsdb0_pcb,
                        'PA-RaPSB04:PS-DCLink-SDA12:PCBT-Mon':
                        self.tempdclinks.ledsda12_pcb,
                        'PA-RaPSB04:PS-DCLink-SDB1:PCBT-Mon':
                        self.tempdclinks.ledsdb1_pcb,
                        'PA-RaPSB05:PS-DCLink-SDA3SFA1:PCBT-Mon':
                        self.tempdclinks.ledsda3sfa1_pcb,
                        'PA-RaPSB05:PS-DCLink-SDB2:PCBT-Mon':
                        self.tempdclinks.ledsdb2_pcb,
                        'PA-RaPSB07:PS-DCLink-SDB3:PCBT-Mon':
                        self.tempdclinks.ledsdb3_pcb,
                        'PA-RaPSB07:PS-DCLink-SFA2SDP1:PCBT-Mon':
                        self.tempdclinks.ledsfa2sdp1_pcb,
                        'PA-RaPSB08:PS-DCLink-SDP23:PCBT-Mon':
                        self.tempdclinks.ledsdp23_pcb
                }, 17, 43
            ),

        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_tempdclinks)
        self.atualizar_status()

    def mostrar_janela_tempdclinks(self):
        """."""
        self.tempdclinks.setVisible(not self.isVisible())

    def atualizar_status(self):
        """."""
        todos_verdes = True
        for _, (sinais, temp_min, temp_max) in self.sinais_tempdclinks.items():
            for signal, led in sinais.items():
                utils.verificar_tempdclinks(signal, led, temp_min, temp_max)
                if not getattr(led, "state", False):
                    todos_verdes = False

            self.estado_ok = todos_verdes

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_verdes else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")


class Blocositemp:
    """Gerencia o grupo SItemp e atualiza a label alarmsitemp."""

    def __init__(self, janela_opr):
        """."""
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto
        self.tempcamvac = Si_camvac(janela_opr, janela_opr.btntempcamvac)
        self.temprackpu = Si_rackpu(janela_opr, janela_opr.btnrackpu)
        self.temprackps = Si_racksimar(janela_opr, janela_opr.btnrackps)
        self.temprackint = Si_roomrack(janela_opr, janela_opr.btntemprackint)
        self.tempcirchid = Si_circhid(janela_opr, janela_opr.btntempcirchid)
        self.tempconecserv = Si_conecserv(janela_opr, janela_opr.
                                          btntempconecserv)
        self.tempmagnets = Si_magnets(janela_opr, janela_opr.btntempmagnets)
        self.temphls = Si_hls(janela_opr, janela_opr.btntemphls)
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
            self.temphls,
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
            if not getattr(sub, "estado_ok", True):
                falha_detectada = True

        # Atualiza a label principal do bloco SI Temp
        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel,
                                                  "alarmsitemp")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if not falha_detectada else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()
