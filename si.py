"""Logica das subjanelas do Anel de Armazenamento."""
import epics
from PyQt5 import uic, QtWidgets
import utils


class ConnWidgetPVs_orig(QtWidgets.QWidget):
    """."""

    def __init__(self, janela_opr, botao_menu, ui_fname, check_type):
        """."""
        super().__init__()
        self.pvs = None
        self.check_type = check_type
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.uiobj = uic.loadUi(ui_fname)
        self.sinais = None
        self._registrar_grupos()
        self._connect_pvs()

    def disconnected_pvnames(self):
        """."""
        dpvns = list()
        for pvname, pv in self.pvs.items():
            if not pv.connected:
                dpvns.append(pvname)
        return dpvns

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        raise NotImplemented

    def _connect_pvs(self):
        self.pvs = dict()
        for pvname, _ in self.sinais.items():
            self.pvs[pvname] = epics.PV(pvname, connection_timeout=None)

    def configurar_sistema(self):
        """Conecta sinais da janela principal e prepara a subjanela."""
        # Botão/ação que mostra/oculta a janela de temperatura
        self.botao_menu.clicked.connect(self.mostrar_janela)
        # Primeira atualização inicial
        self.atualizar_status()

    def mostrar_janela(self):
        """Exibe/oculta a interface gráfica."""
        self.uiobj.setVisible(not self.uiobj.isVisible())

    def atualizar_status(self):
        """Atualiza LEDs da subjanela e define estado_ok."""
        if self.check_type == 'vacuo':

            todos_ok = True

            for pvname, value in self.sinais.items():
                led, pressao_min = value
                utils.verificar_vacbo(
                    pvname, led, pressao_min=pressao_min)
                if not getattr(led, "state", False):
                    todos_ok = False
            self.estado_ok = todos_ok

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")

            # Atualiza label de alarme da subjanela
            alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel,
                                                      "alarmvacuo")

            if alarme_widget:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                alarme_widget.setStyleSheet(f"background-color: {cor};")
                alarme_widget.repaint()
                QtWidgets.QApplication.processEvents()
                alarme_widget.update()


class ConnWidgetPVs(utils.ConnWidgetPVs):
    """."""

    def __init__(self, janela_opr, botao_menu, ui_fname, check_type):
        """."""
        super().__init__(janela_opr, botao_menu, ui_fname, check_type)

    def atualizar_status(self):
        """Atualiza LEDs da subjanela e define estado_ok."""
        if self.check_type == 'vacuo':

            todos_ok = True

            for pvname, value in self.sinais.items():
                led, pressao_min = value
                utils.verificar_vacbo(
                    pvname, led, pressao_min=pressao_min)
                if not getattr(led, "state", False):
                    todos_ok = False
            self.estado_ok = todos_ok

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")

            # Atualiza label de alarme da subjanela
            alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel,
                                                      "alarmvacuo")

            if alarme_widget:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                alarme_widget.setStyleSheet(f"background-color: {cor};")
                alarme_widget.repaint()
                QtWidgets.QApplication.processEvents()
                alarme_widget.update()




class Sivac(ConnWidgetPVs):
    """Controle da subjanela de leitura de vácuo do Anel."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/vacsi.ui", "vacuo")

    def _registrar_grupos(self):
        """Registra Pvs de vacuo e seus leds correspondentes."""
        self.sinais = {
            'SI-01C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac01c1, 1.0e-7),
            'SI-01C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac01c3, 1.0e-7),
            'SI-01SA:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac01sa, 1.0e-7),
            'SI-02C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac02c1, 1.0e-7),
            'SI-02C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac02c3, 1.0e-7),
            'SI-02SB:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac02sb, 1.0e-7),
            'SI-03C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac03c1, 1.0e-7),
            'SI-03C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac03c3, 1.0e-7),
            'SI-03SP:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac03sp, 1.0e-7),
            'SI-04C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac04c1, 1.0e-7),
            'SI-04C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac04c3, 1.0e-7),
            'SI-04SB:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac04sb, 1.0e-7),
            'SI-05C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac05c1, 1.0e-7),
            'SI-05C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac05c3, 1.0e-7),
            'SI-05SA:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac05sa, 1.0e-7),
            'SI-06C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac06c1, 1.0e-7),
            'SI-06C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac06c3, 1.0e-7),
            'SI-06SB:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac06sb, 1.0e-7),
            'SI-07C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac07c1, 1.0e-7),
            'SI-07C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac07c3, 1.0e-7),
            'SI-07SP:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac07sp, 1.0e-7),
            'SI-08C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac08c1, 1.0e-7),
            'SI-08C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac08c3, 1.0e-7),
            'SI-08SB:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac08sb, 1.0e-7),
            'SI-09C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac09c1, 1.0e-7),
            'SI-09C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac09c3, 1.0e-7),
            'SI-09SA:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac09sa, 1.0e-7),
            'SI-10C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac10c1, 1.0e-7),
            'SI-10C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac10c3, 1.0e-7),
            'SI-10SB:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac10sb, 1.0e-7),
            'SI-11C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac11c1, 1.0e-7),
            'SI-11C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac11c3, 1.0e-7),
            'SI-11SP:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac11sp, 1.0e-7),
            'SI-12C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac12c1, 1.0e-7),
            'SI-12C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac12c3, 1.0e-7),
            'SI-12SB:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac12sb, 1.0e-7),
            'SI-13C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac13c1, 1.0e-7),
            'SI-13C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac13c3, 1.0e-7),
            'SI-13SA:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac13sa, 1.0e-7),
            'SI-14C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac14c1, 1.0e-7),
            'SI-14C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac14c3, 1.0e-7),
            'SI-14SB:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac14sb, 1.0e-7),
            'SI-15C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac15c1, 1.0e-7),
            'SI-15C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac15c3, 1.0e-7),
            'SI-15SP:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac15sp, 1.0e-7),
            'SI-16C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac16c1, 1.0e-7),
            'SI-16C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac16c3, 1.0e-7),
            'SI-16SB:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac16sb, 1.0e-7),
            'SI-17C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac17c1, 1.0e-7),
            'SI-17C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac17c3, 1.0e-7),
            'SI-17SA:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac17sa, 1.0e-7),
            'SI-18C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac18c1, 1.0e-7),
            'SI-18C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac18c3, 1.0e-7),
            'SI-18SB:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac18sb, 1.0e-7),
            'SI-19C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac19c1, 1.0e-7),
            'SI-19C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac19c3, 1.0e-7),
            'SI-19SP:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac19sp, 1.0e-7),
            'SI-20C1:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac20c1, 1.0e-7),
            'SI-20C3:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac20c3, 1.0e-7),
            'SI-20SB:VA-CCG-BG:Pressure-Mon': (self.uiobj.led_vac20sb, 1.0e-7),
            'SI-01BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_01bcfe,
                                                 1.0e-7),
            'SI-01C2FE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_01c2fe,
                                                 1.0e-7),
            'SI-01SAFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_01safe,
                                                 1.0e-7),
            'SI-02BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_02bcfe,
                                                 1.0e-7),
            'SI-02SBFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_02sbfe,
                                                 1.0e-7),
            'SI-03BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_03bcfe,
                                                 1.0e-7),
            'SI-03C2FE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_03c2fe,
                                                 1.0e-7),
            'SI-03SPFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_03spfe,
                                                 1.0e-7),
            'SI-04BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_04bcfe,
                                                 1.0e-7),
            'SI-04SBFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_04sbfe,
                                                 1.0e-7),
            'SI-05BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_05bcfe,
                                                 1.0e-7),
            'SI-05C2FE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_05c2fe,
                                                 1.0e-7),
            'SI-05SAFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_05safe,
                                                 1.0e-7),
            'SI-06BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_06bcfe,
                                                 1.0e-7),
            'SI-06SBFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_06sbfe,
                                                 1.0e-7),
            'SI-07BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_07bcfe,
                                                 1.0e-7),
            'SI-07C2FE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_07c2fe,
                                                 1.0e-7),
            'SI-07SPFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_07spfe,
                                                 1.0e-7),
            'SI-08BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_08bcfe,
                                                 1.0e-7),
            'SI-08SBFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_08sbfe,
                                                 1.0e-7),
            'SI-09BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_09bcfe,
                                                 1.0e-7),
            'SI-09C2FE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_09c2fe,
                                                 1.0e-7),
            'SI-09SAFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_09safe,
                                                 1.0e-7),
            'SI-10BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_10bcfe,
                                                 1.0e-7),
            'SI-10SBFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_10sbfe,
                                                 1.0e-7),
            'SI-11BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_11bcfe,
                                                 1.0e-7),
            'SI-11C2FE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_11c2fe,
                                                 1.0e-7),
            'SI-11SPFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_11spfe,
                                                 1.0e-7),
            'SI-12BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_12bcfe,
                                                 1.0e-7),
            'SI-12SBFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_12sbfe,
                                                 1.0e-7),
            'SI-13BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_13bcfe,
                                                 1.0e-7),
            'SI-13C2FE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_13c2fe,
                                                 1.0e-7),
            'SI-13SAFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_13safe,
                                                 1.0e-7),
            'SI-14BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_14bcfe,
                                                 1.0e-7),
            'SI-14SBFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_14sbfe,
                                                 1.0e-7),
            'SI-15BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_15bcfe,
                                                 1.0e-7),
            'SI-15C2FE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_15c2fe,
                                                 1.0e-7),
            'SI-15SPFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_15spfe,
                                                 1.0e-7),
            'SI-16BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_16bcfe,
                                                 1.0e-7),
            'SI-16SBFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_16sbfe,
                                                 1.0e-7),
            'SI-17BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_17bcfe,
                                                 1.0e-7),
            'SI-17C2FE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_17c2fe,
                                                 1.0e-7),
            'SI-17SAFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_17safe,
                                                 1.0e-7),
            'SI-18BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_18bcfe,
                                                 1.0e-7),
            'SI-18SBFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_18sbfe,
                                                 1.0e-7),
            'SI-19BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_19bcfe,
                                                 1.0e-7),
            'SI-19SPFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_19spfe,
                                                 1.0e-7),
            'SI-20BCFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_20bcfe,
                                                 1.0e-7),
            'SI-20SBFE:VA-CCG-MD:Pressure-Mon': (self.uiobj.led_20sbfe,
                                                 1.0e-7),
        }


class Blocosi:
    """Gerencia o grupo SI e atualiza a label alarmsi."""

    def __init__(self, janela_opr):
        """."""
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto
        self.vacsi = Sivac(janela_opr, janela_opr.btnvacsi)
        # self.pwmsi = Sipwm(janela_opr, janela_opr.btnpwmsi)
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
            if not getattr(sub, "estado_ok", True):
                falha_detectada = True

        # Atualiza a label principal do bloco LTS
        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel, "alarmsi")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if not falha_detectada else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()


# class Sicavity(QtWidgets.QWidget):
#     """."""
#
#     def __init__(self, janela_opr, botao_menu):
#         """."""
#         super().__init__()
#         self.janela_opr = janela_opr
#         self.botao_menu = botao_menu
#         self.sicavity = uic.loadUi("ui/sicavity.ui")
#         self._registrar_grupos()
#
#     def _registrar_grupos(self):
#         """."""
#         self.sinais_temperatura = {}
#
#     def configurar_sistema(self):
#         """Conecta sinais da janela principal e prepara a subjanela."""
#         self.botao_menu.clicked.connect(self.mostrar_janela_temperatura)
#         self.atualizar_status()
#
#     def mostrar_janela_temperatura(self):
#         """Exibe/oculta a interface gráfica da temperatura LINAC."""
#         self.bocavity.setVisible(not self.bocavity.isVisible())
#
#     def atualizar_status(self):
#         """Atualiza LEDs da subjanela e define estado_ok."""
#         todos_verdes = True
#         for _, (sinais, temp_min, temp_max) in self.sinais_temperatura.items
# ():
#             for signal, led in sinais.items():
#                 utils.verificar_bocavity(signal, led, temp_min, temp_max)
#                 if not getattr(led, "state", False):
#                     todos_verdes = False
#
#         self.estado_ok = todos_verdes
#         # Atualiza cor do botão na aba LINAC
#         if self.botao_menu:
#             cor = "rgb(0, 168, 0)" if todos_verdes else "rgb(207, 0, 0)"
#             self.botao_menu.setStyleSheet(f"background-color: {cor};")
