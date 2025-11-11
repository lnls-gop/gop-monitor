#!/usr/bin/env python-sirius

"""."""
import logging
import sys

import epics
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import QTimer

import utils

from li import AllSubsys as AllSubsysLI
from tb import AllSubsys as AllSubsysTB
from bo import AllSubsys as AllSubsysBO
from ts import AllSubsys as AllSubsysTS
from si import AllSubsys as AllSubsysSI
from sips import Blocosips
from sitemp import Blocositemp


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def segundos_para_hhmmss(segundos: int) -> str:
    """."""
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return f"{horas:02}h{minutos:02}m{segundos_restantes:02}s"


def main():
    """."""
    app = QtWidgets.QApplication(sys.argv)
    janela_opr = uic.loadUi("ui/janela_opr.ui")

    # Carrega a subjanela de aviso de falha
    aviso_falha = uic.loadUi("ui/aviso.ui")
    aviso_falha.setWindowFlags(aviso_falha.windowFlags() | QtCore.Qt.
                               WindowStaysOnTopHint)

    aviso_persistente = False
    _beep_timers = []

    def tocar_bipes(count: int = 5, intervalo_ms: int = 300):
        nonlocal _beep_timers
        if _beep_timers:
            return
        for i in range(count):
            t = QtCore.QTimer()
            t.setSingleShot(True)
            t.timeout.connect(lambda: QtWidgets.QApplication.beep())
            t.timeout.connect(lambda t=t: _beep_timers.remove(t) if t in
                              _beep_timers else None)
            _beep_timers.append(t)
            t.start(i * intervalo_ms)

    def parar_bipes():
        nonlocal _beep_timers
        for t in list(_beep_timers):
            try:
                t.stop()
            except Exception:
                pass
        _beep_timers = []

    def fechar_aviso():
        nonlocal aviso_persistente
        parar_bipes()
        aviso_persistente = False
        aviso_falha.close()

    aviso_falha.btnfechar.clicked.connect(fechar_aviso)

    janela_opr.accesstime.setText("06h00m00s")

    def atualizar_accesstime_formatado():
        try:
            raw = epics.caget("AS-Glob:PP-Summary:TunAccessWaitTimeLeft-Mon")
            if raw is None:
                return
            try:
                segundos = int(float(raw))
            except (ValueError, TypeError):
                return
            if segundos == 0:
                texto = "00h00m00s"
                css = (
                    "background-color: rgb(0, 168, 0); color: "
                    "black; font-weight: bold;"
                )
                janela_opr.accesstime.setText(texto)
                janela_opr.accesstime.setStyleSheet(css)
                return
            if segundos < 0 or segundos > 7 * 24 * 3600:
                return
            texto = segundos_para_hhmmss(segundos)
            janela_opr.accesstime.setText(texto)
            if 0 < segundos < 21600:
                css = (
                    "background-color: yellow; "
                    "color: black; font-weight: bold;"
                )
            else:
                css = ""
            janela_opr.accesstime.setStyleSheet(css)
        except Exception:
            pass

    timer_formatador = QTimer()
    timer_formatador.timeout.connect(atualizar_accesstime_formatado)
    timer_formatador.start(500)

    def atualizar_gamma_status():
        valor = epics.caget("AS-Glob:MP-Summary:AlarmGammaShutter-Mon")
        if valor == 1:
            janela_opr.gammastatus.setText("Open")
            janela_opr.gammastatus.setStyleSheet(
                "color:green; font-weight: bold;")
        else:
            janela_opr.gammastatus.setText("Closed")
            janela_opr.gammastatus.setStyleSheet(
                "color: red; font-weight: bold;")

    timer_gamma = QTimer()
    timer_gamma.timeout.connect(atualizar_gamma_status)
    timer_gamma.start(1000)

    if not janela_opr.findChild(QtWidgets.QLabel, "alarmlinac"):
        logging.warning(
            "Label 'alarmlinac' não encontrada na janela principal")

    sinais_leds = {
        'SI-Glob:AP-OrbIntlk:Enable-Sts':          (janela_opr.ledorbitint, 1),
        'SI-Glob:DI-BbBProc-H:FBCTRL':             (janela_opr.ledbbbh,    1),
        'SI-Glob:DI-BbBProc-V:FBCTRL':             (janela_opr.ledbbbv,    1),
        'SI-Glob:DI-BbBProc-L:FBCTRL':             (janela_opr.ledbbbl,    1),
        'SI-Glob:AP-FOFB:LoopState-Sts':           (janela_opr.ledfofb,    1),
        'SI-Glob:AP-SOFB:LoopState-Sts':           (janela_opr.ledsofb,    1),
        'RA-RaSIA01:TI-EVE:Network-Mon':           (janela_opr.ledintlk1,  1),
        'RA-RaSIB01:TI-EVE:Network-Mon':           (janela_opr.ledintlk2,  1),
    }

    bloco_linac = AllSubsysLI(janela_opr)
    bloco_ltb = AllSubsysTB(janela_opr)
    bloco_lts = AllSubsysTS(janela_opr)
    bloco_bo = AllSubsysBO(janela_opr)
    bloco_si = AllSubsysSI(janela_opr)
    bloco_sitemp = Blocositemp(janela_opr)
    bloco_sips = Blocosips(janela_opr)

    def atualizar_tudo():
        """."""
        nonlocal aviso_persistente

        try:
            rede_a = epics.caget("RA-RaSIA01:TI-EVE:Network-Mon")
            rede_b = epics.caget("RA-RaSIB01:TI-EVE:Network-Mon")
            if rede_a == 0 and rede_b == 0:
                if not aviso_persistente:
                    aviso_falha.show()
                    aviso_falha.raise_()
                    aviso_falha.activateWindow()
                    aviso_persistente = True
                    tocar_bipes(count=15, intervalo_ms=350)
            else:
                parar_bipes()

            for pv, (led, esperado) in sinais_leds.items():
                utils.verificar_estado(pv, led, esperado)
            bloco_linac.atualizar_grupo()
            bloco_ltb.atualizar_grupo()
            bloco_lts.atualizar_grupo()
            bloco_bo.atualizar_grupo()
            bloco_si.atualizar_grupo()
            bloco_sitemp.atualizar_grupo()
            bloco_sips.atualizar_grupo()
        except Exception:
            raise
            # pass

    janela_opr._timer = QTimer(janela_opr)
    janela_opr._timer.timeout.connect(atualizar_tudo)
    janela_opr._timer.start(1000)
    # atualizar_tudo()

    janela_opr.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
