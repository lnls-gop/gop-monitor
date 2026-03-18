"""Lógida para os led's da aba inicial INFOBEAM."""

import logging
from PyQt5 import QtWidgets
import epics


class AllSubsysINFOBEAM:
    """Gerencia os LEDs da aba INFOBEAM e atualiza o botão infobeam."""

    def __init__(self, janela_opr, beep_func, stop_beep_func):
        """."""
        self.janela_opr = janela_opr
        self.tocar_bipes = beep_func
        self.parar_beeps = stop_beep_func

        janela_opr.infobeam.clicked.connect(self.aba_infobeam)

        # Registra os 8 PVs e seus LEDs correspondentes
        self.sinais = {
            "RA-RaSIA01:TI-EVE:Network-Mon": (janela_opr.ledintlk1, 1),
            "RA-RaSIB01:TI-EVE:Network-Mon": (janela_opr.ledintlk2, 1),
            "SI-Glob:AP-SOFB:LoopState-Sts": (janela_opr.ledsofb, 1),
            "SI-Glob:AP-FOFB:LoopState-Sts": (janela_opr.ledfofb, 1),
            "SI-Glob:DI-BbBProc-H:FBCTRL": (janela_opr.ledbbbh, 1),
            "SI-Glob:DI-BbBProc-V:FBCTRL": (janela_opr.ledbbbv, 1),
            "SI-Glob:DI-BbBProc-L:FBCTRL": (janela_opr.ledbbbl, 1),
            "SI-Glob:AP-OrbIntlk:Enable-Sts": (janela_opr.ledorbitint, 1),
        }

        # status inicial assume OK para todos
        self.pvs_status = {pv: True for pv in self.sinais}

    @property
    def estado_ok(self):
        """Retorna True se todas as PVs estão OK."""
        return all(self.pvs_status.values())

    def atualizar_grupo(self):
        """Atualiza LEDs e botão da aba INFOBEAM."""
        falha_detectada = False

        # PV do turno de trabalho
        turno = epics.caget("AS-Glob:AP-MachShift:Mode-Sts")
        if turno is None:
            turno = -1  # fallback

        for pvname, (led, esperado) in self.sinais.items():
            valor = epics.caget(pvname)
            status = (valor == esperado)

            # Se antes estava OK e agora falhou → beep se turno == 0
            if self.pvs_status[pvname] and not status:
                if turno == 0:  # só toca bipes no turno USERS
                    self.tocar_bipes(count=15, intervalo_ms=350)

            # Se voltou ao normal → parar beep
            if not self.pvs_status[pvname] and status:
                self.parar_beeps()

            self.pvs_status[pvname] = status
            falha_detectada |= not status

        # Atualiza o botão da aba
        botao = self.janela_opr.findChild(QtWidgets.QPushButton, "infobeam")
        if botao:
            cor = "rgb(0, 168, 0)" if not falha_detectada else "rgb(207, 0, 0)"
            botao.setStyleSheet(f"background-color: {cor};")

    def aba_infobeam(self):
        """."""
        try:
            self.janela_opr.janela_opr.setCurrentIndex(0)
        except Exception as e:
            logging.error(f"Erro ao mudar para aba LINAC: {e}")
