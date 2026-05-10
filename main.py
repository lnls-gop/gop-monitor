#!/usr/bin/env python-sirius
"""."""
import logging
import sys

import epics
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui

from li import AllSubsys as AllSubsysLI
from tb import AllSubsys as AllSubsysTB
from bo import AllSubsys as AllSubsysBO
from ts import AllSubsys as AllSubsysTS
from sips import AllSubsys as AllSubsysSIPS
from infobeam import AllSubsysINFOBEAM
from infra import AllSubsys as AllSubsysINFRA


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


BEEP_TIMERS = []
AVISO_PERSISTENTE = False


def segundos_para_hhmmss(segundos: int) -> str:
    """."""
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return f"{horas:02}h{minutos:02}m{segundos_restantes:02}s"


def parar_bipes():
    """."""
    global BEEP_TIMERS
    for t in BEEP_TIMERS:
        try:
            t.stop()
        except Exception:
            pass
    BEEP_TIMERS = list()


def fechar_aviso(aviso_falha):
    """."""
    global AVISO_PERSISTENTE
    parar_bipes()
    AVISO_PERSISTENTE = False
    aviso_falha.close()


def tocar_bipes(count: int = 5, intervalo_ms: int = 300):
    """."""
    parar_bipes()

    t = QtCore.QTimer()
    t.setInterval(intervalo_ms)
    t.setSingleShot(False)

    beeps_restantes = {"count": count}

    def emitir_beep():
        QtWidgets.QApplication.beep()
        beeps_restantes["count"] -= 1
        if beeps_restantes["count"] <= 0:
            t.stop()
            if t in BEEP_TIMERS:
                BEEP_TIMERS.remove(t)

    t.timeout.connect(emitir_beep)
    BEEP_TIMERS.append(t)
    t.start()


def atualizar_accesstime_formatado(janela_opr):
    """."""
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


def atualizar_gamma_status(janela_opr):
    """."""
    valor = epics.caget("AS-Glob:MP-Summary:AlarmGammaShutter-Mon")
    if valor == 1:
        janela_opr.gammastatus.setText("Open")
        janela_opr.gammastatus.setStyleSheet(
            "color:green; font-weight: bold;")
    else:
        janela_opr.gammastatus.setText("Closed")
        janela_opr.gammastatus.setStyleSheet(
            "color: red; font-weight: bold;")


def main():
    """."""
    app = QtWidgets.QApplication(sys.argv)

    # Splash com logo
    splash_pix = QtGui.QPixmap(
        "/home/sirius/shared/gop-services/gop-monitor/icon.png"
    )

    # Redimensiona a imagem para metade do tamanho original
    splash_pix = splash_pix.scaled(
        splash_pix.width() // 2,
        splash_pix.height() // 2,
        QtCore.Qt.KeepAspectRatio,
        QtCore.Qt.SmoothTransformation
    )

    splash = QtWidgets.QSplashScreen(
        splash_pix, QtCore.Qt.WindowStaysOnTopHint
    )
    splash.show()
    app.processEvents()

    # Barra de progresso sobre o splash
    progress = QtWidgets.QProgressBar(splash)
    progress.setGeometry(
        10, splash_pix.height() - 30, splash_pix.width() - 20, 20
    )
    progress.setRange(0, 7)  # 7 blocos
    progress.setValue(0)
    progress.show()

    # Label para mensagens acima da barra
    label_msg = QtWidgets.QLabel(splash)
    label_msg.setGeometry(
        10, splash_pix.height() - 60, splash_pix.width() - 20, 20
        )
    label_msg.setAlignment(QtCore.Qt.AlignCenter)
    label_msg.setStyleSheet("color: white; font: bold 12px;")
    label_msg.show()

    # Carrega a janela principal
    janela_opr = uic.loadUi("ui/janela_opr.ui")
    app.setWindowIcon(
        QtGui.QIcon("/home/sirius/shared/gop-services/gop-monitor/icon.png")
    )

    # Carrega a subjanela de aviso de falha
    aviso_falha = uic.loadUi("ui/aviso.ui")
    aviso_falha.setWindowFlags(
        aviso_falha.windowFlags() | QtCore.Qt.WindowStaysOnTopHint
    )
    aviso_falha.btnfechar.clicked.connect(lambda: fechar_aviso(aviso_falha))

    janela_opr.accesstime.setText("06h00m00s")

    # Inicialização dos blocos com mensagens dinâmicas
    subsistemas = [
        ("Carregando LINAC", AllSubsysLI),
        ("Carregando LTB", AllSubsysTB),
        ("Carregando LTS", AllSubsysTS),
        ("Carregando Booster", AllSubsysBO),
        ("Carregando SIPS", AllSubsysSIPS),
        ("Carregando INFOBEAM", AllSubsysINFOBEAM),
        ("Carregando INFRA", AllSubsysINFRA),
    ]

    blocos = []
    for i, (mensagem, Subsys) in enumerate(subsistemas, start=1):
        label_msg.setText(mensagem)
        app.processEvents()

        if Subsys is AllSubsysINFOBEAM:
            bloco = Subsys(janela_opr, tocar_bipes, parar_bipes)
        else:
            bloco = Subsys(janela_opr)

        blocos.append(bloco)
        progress.setValue(i)
        app.processEvents()

    # Timers
    timer_formatador = QTimer()
    timer_formatador.timeout.connect(
        lambda: atualizar_accesstime_formatado(janela_opr)
    )
    timer_formatador.start(500)

    timer_gamma = QTimer()
    timer_gamma.timeout.connect(lambda: atualizar_gamma_status(janela_opr))
    timer_gamma.start(1000)

    janela_opr._timer = QTimer(janela_opr)
    janela_opr._timer.timeout.connect(
        lambda: [bloco.atualizar_grupo() for bloco in blocos]
    )
    janela_opr._timer.start(3000)

    # Atualização inicial
    for bloco in blocos:
        bloco.atualizar_grupo()

    # Fecha o splash e mostra a janela principal
    splash.finish(janela_opr)
    janela_opr.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
