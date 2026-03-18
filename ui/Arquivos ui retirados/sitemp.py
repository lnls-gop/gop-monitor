"""Logica das fontes do Anel de Armazenamento."""
from PyQt5 import QtWidgets
# import utils


# SISTEMAS DE TEMPERATURAS

class AllSubsys:
    """Gerencia o grupo SI e atualiza a label alarmsi."""

    def __init__(self, janela_opr):
        """."""
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto

        # Adiciona todas as subjanelas à lista
        self.subjanelas.extend([


        ]),

        # Configura cada subjanela
        for sub in self.subjanelas:
            sub.configurar_sistema()

    def atualizar_grupo(self):
        """Atualiza todas as subjanelas e a label alarmsi."""
        falha_detectada = False
        for sub in self.subjanelas:
            sub.atualizar_status()
            falha_detectada |= not sub.estado_ok

        # Atualiza a label principal do bloco SI
        alarme_widget = self.janela_opr.findChild(QtWidgets.QPushButton,
                                                  "alarmsi")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if not falha_detectada else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()
