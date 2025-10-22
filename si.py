"""Logica das subjanelas do Anel de Armazenamento."""
from PyQt5 import uic, QtWidgets
import utils


class Sivac(QtWidgets.QWidget):
    """Controle do Sistema de Vácuo do Anel."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.vacsi = uic.loadUi("vacsi.ui")
        self._registrar_grupos()

    def _registrar_grupos(self):
        self.sinais_vac = {
            'SI-01C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac01c1,
            'SI-01C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac01c3,
            'SI-01SA:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac01sa,
            'SI-02C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac02c1,
            'SI-02C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac02c3,
            'SI-02SB:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac02sb,
            'SI-03C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac03c1,
            'SI-03C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac03c3,
            'SI-03SP:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac03sp,
            'SI-04C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac04c1,
            'SI-04C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac04c3,
            'SI-04SB:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac04sb,
            'SI-05C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac05c1,
            'SI-05C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac05c3,
            'SI-05SA:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac05sa,
            'SI-06C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac06c1,
            'SI-06C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac06c3,
            'SI-06SB:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac06sb,
            'SI-07C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac07c1,
            'SI-07C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac07c3,
            'SI-07SP:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac07sp,
            'SI-08C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac08c1,
            'SI-08C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac08c3,
            'SI-08SB:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac08sb,
            'SI-09C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac09c1,
            'SI-09C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac09c3,
            'SI-09SA:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac09sa,
            'SI-10C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac10c1,
            'SI-10C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac10c3,
            'SI-10SB:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac10sb,
            'SI-11C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac11c1,
            'SI-11C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac11c3,
            'SI-11SP:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac11sp,
            'SI-12C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac12c1,
            'SI-12C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac12c3,
            'SI-12SB:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac12sb,
            'SI-13C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac13c1,
            'SI-13C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac13c3,
            'SI-13SA:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac13sa,
            'SI-14C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac14c1,
            'SI-14C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac14c3,
            'SI-14SB:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac14sb,
            'SI-15C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac15c1,
            'SI-15C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac15c3,
            'SI-15SP:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac15sp,
            'SI-16C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac16c1,
            'SI-16C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac16c3,
            'SI-16SB:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac16sb,
            'SI-17C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac17c1,
            'SI-17C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac17c3,
            'SI-17SA:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac17sa,
            'SI-18C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac18c1,
            'SI-18C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac18c3,
            'SI-18SB:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac18sb,
            'SI-19C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac19c1,
            'SI-19C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac19c3,
            'SI-19SP:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac19sp,
            'SI-20C1:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac20c1,
            'SI-20C3:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac20c3,
            'SI-20SB:VA-CCG-BG:Pressure-Mon': self.vacsi.led_vac20sb,
            'SI-01BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_01bcfe,
            'SI-01C2FE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_01c2fe,
            'SI-01SAFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_01safe,
            'SI-02BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_02bcfe,
            'SI-02SBFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_02sbfe,
            'SI-03BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_03bcfe,
            'SI-03C2FE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_03c2fe,
            'SI-03SPFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_03spfe,
            'SI-04BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_04bcfe,
            'SI-04SBFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_04sbfe,
            'SI-05BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_05bcfe,
            'SI-05C2FE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_05c2fe,
            'SI-05SAFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_05safe,
            'SI-06BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_06bcfe,
            'SI-06SBFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_06sbfe,
            'SI-07BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_07bcfe,
            'SI-07C2FE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_07c2fe,
            'SI-07SPFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_07spfe,
            'SI-08BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_08bcfe,
            'SI-08SBFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_08sbfe,
            'SI-09BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_09bcfe,
            'SI-09C2FE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_09c2fe,
            'SI-09SAFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_09safe,
            'SI-10BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_10bcfe,
            'SI-10SBFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_10sbfe,
            'SI-11BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_11bcfe,
            'SI-11C2FE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_11c2fe,
            'SI-11SPFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_11spfe,
            'SI-12BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_12bcfe,
            'SI-12SBFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_12sbfe,
            'SI-13BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_13bcfe,
            'SI-13C2FE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_13c2fe,
            'SI-13SAFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_13safe,
            'SI-14BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_14bcfe,
            'SI-14SBFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_14sbfe,
            'SI-15BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_15bcfe,
            'SI-15C2FE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_15c2fe,
            'SI-15SPFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_15spfe,
            'SI-16BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_16bcfe,
            'SI-16SBFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_16sbfe,
            'SI-17BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_17bcfe,
            'SI-17C2FE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_17c2fe,
            'SI-17SAFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_17safe,
            'SI-18BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_18bcfe,
            'SI-18SBFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_18sbfe,
            'SI-19BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_19bcfe,
            'SI-19SPFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_19spfe,
            'SI-20BCFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_20bcfe,
            'SI-20SBFE:VA-CCG-MD:Pressure-Mon': self.vacsi.led_20sbfe,
        }
        self.pressao_max = 1.0e-7

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_vacsi)
        self.atualizar_status()

    def mostrar_janela_vacsi(self):
        """."""
        self.vacsi.setVisible(not self.vacsi.isVisible())

    def atualizar_status(self):
        """."""
        todos_ok = True
        for signal, led in self.sinais_vac.items():
            utils.verificar_vacsi(signal, led, self.pressao_max)
            if not getattr(led, "state", False):
                todos_ok = False
        self.estado_ok = todos_ok

        if self.botao_menu:
            cor = "rgb(0, 180, 0)" if todos_ok else "rgb(207, 0, 0)"
            self.botao_menu.setStyleSheet(f"background-color: {cor};")

        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel,
                                                  "alarmsi")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
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
#         self.sicavity = uic.loadUi("sicavity.ui")
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


class Si_pwm(QtWidgets.QWidget):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.pwmsi = uic.loadUi("pwmsi.ui")
        self._registrar_grupos()

    def _registrar_grupos(self):
        self.sinais_pwmsi = {
            "pwm_dipolo":    (
                {
                   'SI-Fam:PS-B1B2-1:IGBT1PWMDutyCycleMod1-Mon': self.pwmsi.
                   led_b1b2_1igbt1mod1,
                   'SI-Fam:PS-B1B2-1:IGBT1PWMDutyCycleMod2-Mon': self.pwmsi.
                   led_b1b2_1igbt2mod1,
                   'SI-Fam:PS-B1B2-1:IGBT1PWMDutyCycleMod3-Mon': self.pwmsi.
                   led_b1b2_2igbt1mod1,
                   'SI-Fam:PS-B1B2-1:IGBT1PWMDutyCycleMod4-Mon': self.pwmsi.
                   led_b1b2_2igbt2mod1,
                   'SI-Fam:PS-B1B2-2:IGBT1PWMDutyCycleMod1-Mon': self.pwmsi.
                   led_b1b2_1igbt1mod2,
                   'SI-Fam:PS-B1B2-2:IGBT1PWMDutyCycleMod2-Mon': self.pwmsi.
                   led_b1b2_2igbt1mod2,
                   'SI-Fam:PS-B1B2-2:IGBT1PWMDutyCycleMod3-Mon': self.pwmsi.
                   led_b1b2_1igbt2mod2,
                   'SI-Fam:PS-B1B2-2:IGBT1PWMDutyCycleMod4-Mon': self.pwmsi.
                   led_b1b2_2igbt2mod2,
                   'SI-Fam:PS-B1B2-1:IGBT2PWMDutyCycleMod1-Mon': self.pwmsi.
                   led_b1b2_1igbt1mod3,
                   'SI-Fam:PS-B1B2-1:IGBT2PWMDutyCycleMod2-Mon': self.pwmsi.
                   led_b1b2_2igbt1mod3,
                   'SI-Fam:PS-B1B2-1:IGBT2PWMDutyCycleMod3-Mon': self.pwmsi.
                   led_b1b2_1igbt2mod3,
                   'SI-Fam:PS-B1B2-1:IGBT2PWMDutyCycleMod4-Mon': self.pwmsi.
                   led_b1b2_2igbt2mod3,
                   'SI-Fam:PS-B1B2-2:IGBT2PWMDutyCycleMod1-Mon': self.pwmsi.
                   led_b1b2_1igbt1mod4,
                   'SI-Fam:PS-B1B2-2:IGBT2PWMDutyCycleMod2-Mon': self.pwmsi.
                   led_b1b2_2igbt1mod4,
                   'SI-Fam:PS-B1B2-2:IGBT2PWMDutyCycleMod3-Mon': self.pwmsi.
                   led_b1b2_1igbt2mod4,
                   'SI-Fam:PS-B1B2-2:IGBT2PWMDutyCycleMod4-Mon': self.pwmsi.
                   led_b1b2_2igbt2mod4,
                }, 0.8, 0.9
            ),
        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_pwmsi)
        self.atualizar_status()

    def mostrar_janela_pwmsi(self):
        """."""
        self.pwmsi.setVisible(not self.pwmsi.isVisible())

    def atualizar_status(self):
        """."""
        todos_verdes = True
        for _, (sinais, temp_min, temp_max) in self.sinais_pwmsi.items():
            for signal, led in sinais.items():
                utils.verificar_pwmsi(signal, led, temp_min, temp_max)
                if not getattr(led, "state", False):
                    todos_verdes = False

            self.estado_ok = todos_verdes

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_verdes else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")


class Blocosi:
    """Gerencia o grupo SI e atualiza a label alarmsi."""

    def __init__(self, janela_opr):
        """."""
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto
        self.vacsi = Sivac(janela_opr, janela_opr.btnvacsi)
        self.pwmsi = Si_pwm(janela_opr, janela_opr.btnpwmsi)
        # self.psbo = Bops(janela_opr, janela_opr.btnpsbo)
        # self.bocavity = Bocavity(janela_opr, janela_opr.btnbocavity )

        # Adiciona todas as subjanelas à lista
        self.subjanelas.extend([
            self.vacsi,
            self.pwmsi,
            # self.psbo,
            # self.bocavity,
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
