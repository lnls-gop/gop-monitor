"""Logica das fontes do Anel de Armazenamento."""
from PyQt5 import uic, QtWidgets
import utils


class Si_psfamily(QtWidgets.QWidget):
    """Controle das fontes de familia do Anel de Armazenamento."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.psfamilysi = uic.loadUi("psfamilysi.ui")
        self._registrar_grupos()

    def _registrar_grupos(self):
        self.sinais_estado_0 = {
            'SI-Fam:PS-B1B2-1:DiagStatus-Mon': self.psfamilysi.led_psfamb1,
            'SI-Fam:PS-B1B2-2:DiagStatus-Mon': self.psfamilysi.led_psfamb2,
            'SI-Fam:PS-Q1:DiagStatus-Mon': self.psfamilysi.led_psfamq1,
            'SI-Fam:PS-Q2:DiagStatus-Mon': self.psfamilysi.led_psfamq2,
            'SI-Fam:PS-Q3:DiagStatus-Mon': self.psfamilysi.led_psfamq3,
            'SI-Fam:PS-Q4:DiagStatus-Mon': self.psfamilysi.led_psfamq4,
            'SI-Fam:PS-QDA:DiagStatus-Mon': self.psfamilysi.led_psfamqda,
            'SI-Fam:PS-QFP:DiagStatus-Mon': self.psfamilysi.led_psfamqfp,
            'SI-Fam:PS-QDB1:DiagStatus-Mon': self.psfamilysi.led_psfamqdb1,
            'SI-Fam:PS-QDB2:DiagStatus-Mon': self.psfamilysi.led_psfamqdb2,
            'SI-Fam:PS-QDP1:DiagStatus-Mon': self.psfamilysi.led_psfamqdp1,
            'SI-Fam:PS-QDP2:DiagStatus-Mon': self.psfamilysi.led_psfamqdp2,
            'SI-Fam:PS-QFA:DiagStatus-Mon': self. psfamilysi.led_psfamqfa,
            'SI-Fam:PS-QFB:DiagStatus-Mon': self. psfamilysi.led_psfamqfb,
            'SI-Fam:PS-SFP2:DiagStatus-Mon': self.psfamilysi.led_psfamsfp2,
            'SI-Fam:PS-SDA0:DiagStatus-Mon': self.psfamilysi.led_psfamsda0,
            'SI-Fam:PS-SDA1:DiagStatus-Mon': self.psfamilysi.led_psfamsda1,
            'SI-Fam:PS-SDA2:DiagStatus-Mon': self.psfamilysi.led_psfamsda2,
            'SI-Fam:PS-SDA3:DiagStatus-Mon': self.psfamilysi.led_psfamsda3,
            'SI-Fam:PS-SDB0:DiagStatus-Mon': self.psfamilysi.led_psfamsdb0,
            'SI-Fam:PS-SDB1:DiagStatus-Mon': self.psfamilysi.led_psfamsdb1,
            'SI-Fam:PS-SDB2:DiagStatus-Mon': self.psfamilysi.led_psfamsdb2,
            'SI-Fam:PS-SDB3:DiagStatus-Mon': self.psfamilysi.led_psfamsdb3,
            'SI-Fam:PS-SDP0:DiagStatus-Mon': self.psfamilysi.led_psfamsdp0,
            'SI-Fam:PS-SDP1:DiagStatus-Mon': self.psfamilysi.led_psfamsdp1,
            'SI-Fam:PS-SDP2:DiagStatus-Mon': self.psfamilysi.led_psfamsdp2,
            'SI-Fam:PS-SDP3:DiagStatus-Mon': self.psfamilysi.led_psfamsdp3,
            'SI-Fam:PS-SFA0:DiagStatus-Mon': self.psfamilysi.led_psfamsfa0,
            'SI-Fam:PS-SFA1:DiagStatus-Mon': self.psfamilysi.led_psfamsfa1,
            'SI-Fam:PS-SFA2:DiagStatus-Mon': self.psfamilysi.led_psfamsfa2,
            'SI-Fam:PS-SFB0:DiagStatus-Mon': self.psfamilysi.led_psfamsfb0,
            'SI-Fam:PS-SFB1:DiagStatus-Mon': self.psfamilysi.led_psfamsfb1,
            'SI-Fam:PS-SFB2:DiagStatus-Mon': self.psfamilysi.led_psfamsfb2,
            'SI-Fam:PS-SFP0:DiagStatus-Mon': self.psfamilysi.led_psfamsfp0,
            'SI-Fam:PS-SFP1:DiagStatus-Mon': self.psfamilysi.led_psfamsfp1,
        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_psfamilysi)
        self.atualizar_status()

    def mostrar_janela_psfamilysi(self):
        """."""
        self.psfamilysi.setVisible(not self.psfamilysi.isVisible())

    def atualizar_status(self):
        """."""
        todos_ok = True
        for signal, led in self.sinais_estado_0.items():
            utils.verificar_psfamilysi(signal, led, estado_esperado=0)
            if not getattr(led, "state", False):
                todos_ok = False
        self.estado_ok = todos_ok

        if self.botao_menu:
            cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
            self.botao_menu.setStyleSheet(f"background-color: {cor}")

        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel,
                                                  "alarmsips")
        if alarme_widget:
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()


class Si_skewquad(QtWidgets.QWidget):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.skewquad = uic.loadUi("skewquad.ui")
        self._registrar_grupos()

    def _registrar_grupos(self):
        self.sinais_estado_0 = {
            'SI-01M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew01m1,
            'SI-01M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew01m2,
            'SI-01C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew01c1,
            'SI-01C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew01c2,
            'SI-01C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew01c3,
            'SI-02M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew02m1,
            'SI-02M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew02m2,
            'SI-02C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew02c1,
            'SI-02C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew02c2,
            'SI-02C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew02c3,
            'SI-03M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew03m1,
            'SI-03M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew03m2,
            'SI-03C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew03c1,
            'SI-03C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew03c2,
            'SI-03C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew03c3,
            'SI-04M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew04m1,
            'SI-04M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew04m2,
            'SI-04C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew04c1,
            'SI-04C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew04c2,
            'SI-04C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew04c3,
            'SI-05M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew05m1,
            'SI-05M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew05m2,
            'SI-05C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew05c1,
            'SI-05C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew05c2,
            'SI-05C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew05c3,
            'SI-06M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew06m1,
            'SI-06M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew06m2,
            'SI-06C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew06c1,
            'SI-06C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew06c2,
            'SI-06C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew06c3,
            'SI-07M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew07m1,
            'SI-07M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew07m2,
            'SI-07C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew07c1,
            'SI-07C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew07c2,
            'SI-07C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew07c3,
            'SI-08M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew08m1,
            'SI-08M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew08m2,
            'SI-08C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew08c1,
            'SI-08C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew08c2,
            'SI-08C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew08c3,
            'SI-09M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew09m1,
            'SI-09M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew09m2,
            'SI-09C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew09c1,
            'SI-09C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew09c2,
            'SI-09C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew09c3,
            'SI-10M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew10m1,
            'SI-10M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew10m2,
            'SI-10C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew10c1,
            'SI-10C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew10c2,
            'SI-10C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew10c3,
            'SI-11M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew11m1,
            'SI-11M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew11m2,
            'SI-11C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew11c1,
            'SI-11C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew11c2,
            'SI-11C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew11c3,
            'SI-12M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew12m1,
            'SI-12M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew12m2,
            'SI-12C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew12c1,
            'SI-12C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew12c2,
            'SI-12C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew12c3,
            'SI-13M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew13m1,
            'SI-13M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew13m2,
            'SI-13C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew13c1,
            'SI-13C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew13c2,
            'SI-13C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew13c3,
            'SI-14M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew14m1,
            'SI-14M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew14m2,
            'SI-14C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew14c1,
            'SI-14C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew14c2,
            'SI-14C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew14c3,
            'SI-15M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew15m1,
            'SI-15M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew15m2,
            'SI-15C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew15c1,
            'SI-15C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew15c2,
            'SI-15C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew15c3,
            'SI-16M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew16m1,
            'SI-16M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew16m2,
            'SI-16C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew16c1,
            'SI-16C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew16c2,
            'SI-16C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew16c3,
            'SI-17M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew17m1,
            'SI-17M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew17m2,
            'SI-17C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew17c1,
            'SI-17C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew17c2,
            'SI-17C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew17c3,
            'SI-18M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew18m1,
            'SI-18M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew18m2,
            'SI-18C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew18c1,
            'SI-18C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew18c2,
            'SI-18C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew18c3,
            'SI-19M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew19m1,
            'SI-19M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew19m2,
            'SI-19C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew19c1,
            'SI-19C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew19c2,
            'SI-19C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew19c3,
            'SI-20M1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew20m1,
            'SI-20M2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew20m2,
            'SI-20C1:PS-QS:DiagStatus-Mon': self.skewquad.led_skew20c1,
            'SI-20C2:PS-QS:DiagStatus-Mon': self.skewquad.led_skew20c2,
            'SI-20C3:PS-QS:DiagStatus-Mon': self.skewquad.led_skew20c3,
        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_skewquad)
        self.atualizar_status()

    def mostrar_janela_skewquad(self):
        """."""
        self.skewquad.setVisible(not self.skewquad.isVisible())

    def atualizar_status(self):
        """."""
        todos_ok = True
        for signal, led in self.sinais_estado_0.items():
            utils.verificar_skewquad(signal, led, estado_esperado=0)
            if not getattr(led, "state", False):
                todos_ok = False
        self.estado_ok = todos_ok

        if self.botao_menu:
            cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
            self.botao_menu.setStyleSheet(f"background-color: {cor}")

        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel,
                                                  "alarmsips")
        if alarme_widget:
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()


class Si_ffwcorr(QtWidgets.QWidget):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.ffwcorr = uic.loadUi("ffwcorr.ui")
        self._registrar_grupos()

    def _registrar_grupos(self):
        self.sinais_estado_0 = {
            'SI-14SB:PS-LCH:DiagStatus-Mon': self.ffwcorr.led_ff14sblch,
            # 'SI-08SB:PS-CH-1:DiagStatus-Mon': self.ffwcorr.led_ff08sbch1,
            # 'SI-08SB:PS-CH-2:DiagStatus-Mon': self.ffwcorr.led_ff08sbch2,
            # 'SI-08SB:PS-CV-1:DiagStatus-Mon': self.ffwcorr.led_ff08sbcv1,
            # 'SI-08SB:PS-CV-2:DiagStatus-Mon': self.ffwcorr.led_ff08sbcv2,
            # 'SI-08SB:PS-LCH:DiagStatus-Mon': self.ffwcorr.led_ff14sblch,
            'SI-10SB:PS-CH-1:DiagStatus-Mon': self.ffwcorr.led_ff10sbch1,
            'SI-10SB:PS-CH-2:DiagStatus-Mon': self.ffwcorr.led_ff10sbch2,
            'SI-10SB:PS-CV-1:DiagStatus-Mon': self.ffwcorr.led_ff10sbcv1,
            'SI-10SB:PS-CV-2:DiagStatus-Mon': self.ffwcorr.led_ff10sbcv2,
            'SI-10SB:PS-QS-1:DiagStatus-Mon': self.ffwcorr.led_ff10sbqs1,
            'SI-10SB:PS-QS-2:DiagStatus-Mon': self.ffwcorr.led_ff10sbqs2,
            # 'SI-14SB:PS-CH-1:DiagStatus-Mon': self.ffwcorr.led_ff14sbch1,
            # 'SI-14SB:PS-CH-2:DiagStatus-Mon': self.ffwcorr.led_ff14sbch2,
            # 'SI-14SB:PS-CV-1:DiagStatus-Mon': self.ffwcorr.led_ff14sbcv1,
            # 'SI-14SB:PS-CV-2:DiagStatus-Mon': self.ffwcorr.led_ff14sbcv2,
            # 'SI-01M1:PS-FFCH:PwrState-Sts': self.ffwcorr.led_ff01m1septacv,
            # 'SI-01M2:PS-FFCH:PwrState-Sts': self.ffwcorr.led_ff01m2septach,
            # 'SI-01M1:PS-FFCV:PwrState-Sts': self.ffwcorr.led_ff01m2septacv,
            # 'SI-01M2:PS-FFCV:PwrState-Sts': self.ffwcorr.led_ff01m1septach,
        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_ffwcorr)
        self.atualizar_status()

    def mostrar_janela_ffwcorr(self):
        """."""
        self.ffwcorr.setVisible(not self.ffwcorr.isVisible())

    def atualizar_status(self):
        """."""
        todos_ok = True
        for signal, led in self.sinais_estado_0.items():
            utils.verificar_ffwcorr(signal, led, estado_esperado=0)
            if not getattr(led, "state", False):
                todos_ok = False
        self.estado_ok = todos_ok

        if self.botao_menu:
            cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
            self.botao_menu.setStyleSheet(f"background-color: {cor}")

        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel,
                                                  "alarmsips")
        if alarme_widget:
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()


class Si_trims(QtWidgets.QWidget):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.trims = uic.loadUi("trims.ui")
        self._registrar_grupos()

    def _registrar_grupos(self):
        self.sinais_estado_0 = {
            'SI-02M1:PS-QFB:DiagStatus-Mon': self.trims.led_02m1qfb,
            'SI-02M1:PS-QDB1:DiagStatus-Mon': self. trims.led_02m1qdb1,
            'SI-02M1:PS-QDB2:DiagStatus-Mon': self. trims.led_02m1qdb2,
            'SI-02M2:PS-QFB:DiagStatus-Mon': self.trims.led_02m2qfb,
            'SI-02M2:PS-QDB1:DiagStatus-Mon': self.trims.led_02m2qdb1,
            'SI-02M2:PS-QDB2:DiagStatus-Mon': self.trims.led_02m2qdb2,
            'SI-02C1:PS-Q1:DiagStatus-Mon': self.trims.led_02c1q1,
            'SI-02C1:PS-Q2:DiagStatus-Mon': self.trims.led_02c1q2,
            'SI-02C2:PS-Q3:DiagStatus-Mon': self.trims.led_02c2q3,
            'SI-02C2:PS-Q4:DiagStatus-Mon': self.trims.led_02c2q4,
            'SI-02C3:PS-Q3:DiagStatus-Mon': self.trims.led_02c3q3,
            'SI-02C3:PS-Q4:DiagStatus-Mon': self.trims.led_02c3q4,
            'SI-02C4:PS-Q1:DiagStatus-Mon': self.trims.led_02c4q1,
            'SI-02C4:PS-Q2:DiagStatus-Mon': self.trims.led_02c4q2,
            'SI-03M1:PS-QFP:DiagStatus-Mon': self.trims.led_03m1qfp,
            'SI-03M1:PS-QDP1:DiagStatus-Mon': self.trims.led_03m1qdp1,
            'SI-03M1:PS-QDP2:DiagStatus-Mon': self.trims.led_03m1qdp2,
            'SI-03M2:PS-QDP1:DiagStatus-Mon': self.trims.led_03m2qdp1,
            'SI-03M2:PS-QDP2:DiagStatus-Mon': self.trims.led_03m2qdp2,
            'SI-03M2:PS-QFP:DiagStatus-Mon': self.trims.led_03m2qfp,
            'SI-03C1:PS-Q1:DiagStatus-Mon': self.trims.led_03c1q1,
            'SI-03C1:PS-Q2:DiagStatus-Mon': self.trims.led_03c1q2,
            'SI-03C2:PS-Q3:DiagStatus-Mon': self.trims.led_03c2q3,
            'SI-03C2:PS-Q4:DiagStatus-Mon': self.trims.led_03c2q4,
            'SI-03C3:PS-Q3:DiagStatus-Mon': self.trims.led_03c3q3,
            'SI-03C3:PS-Q4:DiagStatus-Mon': self.trims.led_03c3q4,
            'SI-03C4:PS-Q1:DiagStatus-Mon': self.trims.led_03c4q1,
            'SI-03C4:PS-Q2:DiagStatus-Mon': self.trims.led_03c4q2,
            'SI-04M1:PS-QDB1:DiagStatus-Mon': self.trims.led_04m1qdb1,
            'SI-04M1:PS-QDB2:DiagStatus-Mon': self.trims.led_04m1qdb2,
            'SI-04M1:PS-QFB:DiagStatus-Mon': self.trims.led_04m1qfb,
            'SI-04M2:PS-QDB1:DiagStatus-Mon': self.trims.led_04m2qdb1,
            'SI-04M2:PS-QDB2:DiagStatus-Mon': self.trims.led_04m2qdb2,
            'SI-04M2:PS-QFB:DiagStatus-Mon': self.trims.led_04m2qfb,
            'SI-04C1:PS-Q1:DiagStatus-Mon': self.trims.led_04c1q1,
            'SI-04C1:PS-Q2:DiagStatus-Mon': self.trims.led_04c1q2,
            'SI-04C2:PS-Q3:DiagStatus-Mon': self.trims.led_04c2q3,
            'SI-04C2:PS-Q4:DiagStatus-Mon': self.trims.led_04c2q4,
            'SI-04C3:PS-Q3:DiagStatus-Mon': self.trims.led_04c3q3,
            'SI-04C3:PS-Q4:DiagStatus-Mon': self.trims.led_04c3q4,
            'SI-04C4:PS-Q1:DiagStatus-Mon': self.trims.led_04c4q1,
            'SI-04C4:PS-Q2:DiagStatus-Mon': self.trims.led_04c4q2,
            'SI-06M1:PS-QDB1:DiagStatus-Mon': self.trims.led_06m1qdb1,
            'SI-06M1:PS-QDB2:DiagStatus-Mon': self.trims.led_06m1qdb2,
            'SI-06M1:PS-QFB:DiagStatus-Mon': self.trims.led_06m1qfb,
            'SI-06M2:PS-QDB1:DiagStatus-Mon': self.trims.led_06m2qdb1,
            'SI-06M2:PS-QDB2:DiagStatus-Mon': self.trims.led_06m2qdb2,
            'SI-06M2:PS-QFB:DiagStatus-Mon': self.trims.led_06m2qfb,
            'SI-06C1:PS-Q1:DiagStatus-Mon': self.trims.led_06c1q1,
            'SI-06C1:PS-Q2:DiagStatus-Mon': self.trims.led_06c1q2,
            'SI-06C2:PS-Q3:DiagStatus-Mon': self.trims.led_06c2q3,
            'SI-06C2:PS-Q4:DiagStatus-Mon': self.trims.led_06c2q4,
            'SI-06C3:PS-Q3:DiagStatus-Mon': self.trims.led_06c3q3,
            'SI-06C3:PS-Q4:DiagStatus-Mon': self.trims.led_06c3q4,
            'SI-06C4:PS-Q1:DiagStatus-Mon': self.trims.led_06c4q1,
            'SI-06C4:PS-Q2:DiagStatus-Mon': self.trims.led_06c4q2,
            'SI-07M1:PS-QDP1:DiagStatus-Mon': self.trims.led_07m1qdp1,
            'SI-07M1:PS-QDP2:DiagStatus-Mon': self.trims.led_07m1qdp2,
            'SI-07M1:PS-QFP:DiagStatus-Mon': self.trims.led_07m1qfp,
            'SI-07M2:PS-QDP1:DiagStatus-Mon': self.trims.led_07m2qdp1,
            'SI-07M2:PS-QDP2:DiagStatus-Mon': self.trims.led_07m2qdp2,
            'SI-07M2:PS-QFP:DiagStatus-Mon': self.trims.led_07m2qfp,
            'SI-07C1:PS-Q1:DiagStatus-Mon': self.trims.led_07c1q1,
            'SI-07C1:PS-Q2:DiagStatus-Mon': self.trims.led_07c1q2,
            'SI-07C2:PS-Q3:DiagStatus-Mon': self.trims.led_07c2q3,
            'SI-07C2:PS-Q4:DiagStatus-Mon': self.trims.led_07c2q4,
            'SI-07C3:PS-Q3:DiagStatus-Mon': self.trims.led_07c3q3,
            'SI-07C3:PS-Q4:DiagStatus-Mon': self.trims.led_07c3q4,
            'SI-07C4:PS-Q1:DiagStatus-Mon': self.trims.led_07c4q1,
            'SI-07C4:PS-Q2:DiagStatus-Mon': self.trims.led_07c4q2,
            'SI-08M1:PS-QDB1:DiagStatus-Mon': self.trims.led_08m1qdb1,
            'SI-08M1:PS-QDB2:DiagStatus-Mon': self.trims.led_08m1qdb2,
            'SI-08M1:PS-QFB:DiagStatus-Mon': self.trims.led_08m1qfb,
            'SI-08M2:PS-QDB1:DiagStatus-Mon': self.trims.led_08m2qdb1,
            'SI-08M2:PS-QDB2:DiagStatus-Mon': self.trims.led_08m2qdb2,
            'SI-08M2:PS-QFB:DiagStatus-Mon': self.trims.led_08m2qfb,
            'SI-08C1:PS-Q1:DiagStatus-Mon': self.trims.led_08c1q1,
            'SI-08C1:PS-Q2:DiagStatus-Mon': self.trims.led_08c1q2,
            'SI-08C2:PS-Q3:DiagStatus-Mon': self.trims.led_08c2q3,
            'SI-08C2:PS-Q4:DiagStatus-Mon': self.trims.led_08c2q4,
            'SI-08C3:PS-Q3:DiagStatus-Mon': self.trims.led_08c3q3,
            'SI-08C3:PS-Q4:DiagStatus-Mon': self.trims.led_08c3q4,
            'SI-08C4:PS-Q1:DiagStatus-Mon': self.trims.led_08c4q1,
            'SI-08C4:PS-Q2:DiagStatus-Mon': self.trims.led_08c4q2,
            'SI-10M1:PS-QDB1:DiagStatus-Mon': self.trims.led_10m1qdb1,
            'SI-10M1:PS-QDB2:DiagStatus-Mon': self.trims.led_10m1qdb2,
            'SI-10M1:PS-QFB:DiagStatus-Mon': self.trims.led_10m1qfb,
            'SI-10M2:PS-QDB1:DiagStatus-Mon': self.trims.led_10m2qdb1,
            'SI-10M2:PS-QDB2:DiagStatus-Mon': self.trims.led_10m2qdb2,
            'SI-10M2:PS-QFB:DiagStatus-Mon': self.trims.led_10m2qfb,
            'SI-10C1:PS-Q1:DiagStatus-Mon': self.trims.led_10c1q1,
            'SI-10C1:PS-Q2:DiagStatus-Mon': self.trims.led_10c1q2,
            'SI-10C2:PS-Q3:DiagStatus-Mon': self.trims.led_10c2q3,
            'SI-10C2:PS-Q4:DiagStatus-Mon': self.trims.led_10c2q4,
            'SI-10C3:PS-Q3:DiagStatus-Mon': self.trims.led_10c3q3,
            'SI-10C3:PS-Q4:DiagStatus-Mon': self.trims.led_10c3q4,
            'SI-10C4:PS-Q1:DiagStatus-Mon': self.trims.led_10c4q1,
            'SI-10C4:PS-Q2:DiagStatus-Mon': self.trims.led_10c4q2,
            'SI-11M1:PS-QDP1:DiagStatus-Mon': self.trims.led_11m1qdp1,
            'SI-11M1:PS-QDP2:DiagStatus-Mon': self.trims.led_11m1qdp2,
            'SI-11M1:PS-QFP:DiagStatus-Mon': self.trims.led_11m1qfp,
            'SI-11M2:PS-QDP1:DiagStatus-Mon': self.trims.led_11m2qdp1,
            'SI-11M2:PS-QDP2:DiagStatus-Mon': self.trims.led_11m2qdp2,
            'SI-11M2:PS-QFP:DiagStatus-Mon': self.trims.led_11m2qfp,
            'SI-11C1:PS-Q1:DiagStatus-Mon': self.trims.led_11c1q1,
            'SI-11C1:PS-Q2:DiagStatus-Mon': self.trims.led_11c1q2,
            'SI-11C2:PS-Q3:DiagStatus-Mon': self.trims.led_11c2q3,
            'SI-11C2:PS-Q4:DiagStatus-Mon': self.trims.led_11c2q4,
            'SI-11C3:PS-Q3:DiagStatus-Mon': self.trims.led_11c3q3,
            'SI-11C3:PS-Q4:DiagStatus-Mon': self.trims.led_11c3q4,
            'SI-11C4:PS-Q1:DiagStatus-Mon': self.trims.led_11c4q1,
            'SI-11C4:PS-Q2:DiagStatus-Mon': self.trims.led_11c4q2,
            'SI-12M1:PS-QDB1:DiagStatus-Mon': self.trims.led_12m1qdb1,
            'SI-12M1:PS-QDB2:DiagStatus-Mon': self.trims.led_12m1qdb2,
            'SI-12M1:PS-QFB:DiagStatus-Mon': self.trims.led_12m1qfb,
            'SI-12M2:PS-QDB1:DiagStatus-Mon': self.trims.led_12m2qdb1,
            'SI-12M2:PS-QDB2:DiagStatus-Mon': self.trims.led_12m2qdb2,
            'SI-12M2:PS-QFB:DiagStatus-Mon': self.trims.led_12m2qfb,
            'SI-12C1:PS-Q1:DiagStatus-Mon': self.trims.led_12c1q1,
            'SI-12C1:PS-Q2:DiagStatus-Mon': self.trims.led_12c1q2,
            'SI-12C2:PS-Q3:DiagStatus-Mon': self.trims.led_12c2q3,
            'SI-12C2:PS-Q4:DiagStatus-Mon': self.trims.led_12c2q4,
            'SI-12C3:PS-Q3:DiagStatus-Mon': self.trims.led_12c3q3,
            'SI-12C3:PS-Q4:DiagStatus-Mon': self.trims.led_12c3q4,
            'SI-12C4:PS-Q1:DiagStatus-Mon': self.trims.led_12c4q1,
            'SI-12C4:PS-Q2:DiagStatus-Mon': self.trims.led_12c4q2,
            'SI-14M1:PS-QDB1:DiagStatus-Mon': self.trims.led_14m1qdb1,
            'SI-14M1:PS-QDB2:DiagStatus-Mon': self.trims.led_14m1qdb2,
            'SI-14M1:PS-QFB:DiagStatus-Mon': self.trims.led_14m1qfb,
            'SI-14M2:PS-QDB1:DiagStatus-Mon': self.trims.led_14m2qdb1,
            'SI-14M2:PS-QDB2:DiagStatus-Mon': self.trims.led_14m2qdb2,
            'SI-14M2:PS-QFB:DiagStatus-Mon': self.trims.led_14m2qfb,
            'SI-14C1:PS-Q1:DiagStatus-Mon': self.trims.led_14c1q1,
            'SI-14C1:PS-Q2:DiagStatus-Mon': self.trims.led_14c1q2,
            'SI-14C2:PS-Q3:DiagStatus-Mon': self.trims.led_14c2q3,
            'SI-14C2:PS-Q4:DiagStatus-Mon': self.trims.led_14c2q4,
            'SI-14C3:PS-Q3:DiagStatus-Mon': self.trims.led_14c3q3,
            'SI-14C3:PS-Q4:DiagStatus-Mon': self.trims.led_14c3q4,
            'SI-14C4:PS-Q1:DiagStatus-Mon': self.trims.led_14c4q1,
            'SI-14C4:PS-Q2:DiagStatus-Mon': self.trims.led_14c4q2,
            'SI-15M1:PS-QDP1:DiagStatus-Mon': self.trims.led_15m1qdp1,
            'SI-15M1:PS-QDP2:DiagStatus-Mon': self.trims.led_15m1qdp2,
            'SI-15M1:PS-QFP:DiagStatus-Mon': self.trims.led_15m1qfp,
            'SI-15M2:PS-QDP1:DiagStatus-Mon': self.trims.led_15m2qdp1,
            'SI-15M2:PS-QDP2:DiagStatus-Mon': self.trims.led_15m2qdp2,
            'SI-15M2:PS-QFP:DiagStatus-Mon': self.trims.led_15m2qfp,
            'SI-15C1:PS-Q1:DiagStatus-Mon': self.trims.led_15c1q1,
            'SI-15C1:PS-Q2:DiagStatus-Mon': self.trims.led_15c1q2,
            'SI-15C2:PS-Q3:DiagStatus-Mon': self.trims.led_15c2q3,
            'SI-15C2:PS-Q4:DiagStatus-Mon': self.trims.led_15c2q4,
            'SI-15C3:PS-Q3:DiagStatus-Mon': self.trims.led_15c3q3,
            'SI-15C3:PS-Q4:DiagStatus-Mon': self.trims.led_15c3q4,
            'SI-15C4:PS-Q1:DiagStatus-Mon': self.trims.led_15c4q1,
            'SI-15C4:PS-Q2:DiagStatus-Mon': self.trims.led_15c4q2,
            'SI-16M1:PS-QDB1:DiagStatus-Mon': self.trims.led_16m1qdb1,
            'SI-16M1:PS-QDB2:DiagStatus-Mon': self.trims.led_16m1qdb2,
            'SI-16M1:PS-QFB:DiagStatus-Mon': self.trims.led_16m1qfb,
            'SI-16M2:PS-QDB1:DiagStatus-Mon': self.trims.led_16m2qdb1,
            'SI-16M2:PS-QDB2:DiagStatus-Mon': self.trims.led_16m2qdb2,
            'SI-16M2:PS-QFB:DiagStatus-Mon': self.trims.led_16m2qfb,
            'SI-16C1:PS-Q1:DiagStatus-Mon': self.trims.led_16c1q1,
            'SI-16C1:PS-Q2:DiagStatus-Mon': self.trims.led_16c1q2,
            'SI-16C2:PS-Q3:DiagStatus-Mon': self.trims.led_16c2q3,
            'SI-16C2:PS-Q4:DiagStatus-Mon': self.trims.led_16c2q4,
            'SI-16C3:PS-Q3:DiagStatus-Mon': self.trims.led_16c3q3,
            'SI-16C3:PS-Q4:DiagStatus-Mon': self.trims.led_16c3q4,
            'SI-16C4:PS-Q1:DiagStatus-Mon': self.trims.led_16c4q1,
            'SI-16C4:PS-Q2:DiagStatus-Mon': self.trims.led_16c4q2,
            'SI-18M1:PS-QDB1:DiagStatus-Mon': self.trims.led_18m1qdb1,
            'SI-18M1:PS-QDB2:DiagStatus-Mon': self.trims.led_18m1qdb2,
            'SI-18M1:PS-QFB:DiagStatus-Mon': self.trims.led_18m1qfb,
            'SI-18M2:PS-QDB1:DiagStatus-Mon': self.trims.led_18m2qdb1,
            'SI-18M2:PS-QDB2:DiagStatus-Mon': self.trims.led_18m2qdb2,
            'SI-18M2:PS-QFB:DiagStatus-Mon': self.trims.led_18m2qfb,
            'SI-18C1:PS-Q1:DiagStatus-Mon': self.trims.led_18c1q1,
            'SI-18C1:PS-Q2:DiagStatus-Mon': self.trims.led_18c1q2,
            'SI-18C2:PS-Q3:DiagStatus-Mon': self.trims.led_18c2q3,
            'SI-18C2:PS-Q4:DiagStatus-Mon': self.trims.led_18c2q4,
            'SI-18C3:PS-Q3:DiagStatus-Mon': self.trims.led_18c3q3,
            'SI-18C3:PS-Q4:DiagStatus-Mon': self.trims.led_18c3q4,
            'SI-18C4:PS-Q1:DiagStatus-Mon': self.trims.led_18c4q1,
            'SI-18C4:PS-Q2:DiagStatus-Mon': self.trims.led_18c4q2,
            'SI-19M1:PS-QDP1:DiagStatus-Mon': self.trims.led_19m1qdp1,
            'SI-19M1:PS-QDP2:DiagStatus-Mon': self.trims.led_19m1qdp2,
            'SI-19M1:PS-QFP:DiagStatus-Mon': self.trims.led_19m1qfp,
            'SI-19M2:PS-QDP1:DiagStatus-Mon': self.trims.led_19m2qdp1,
            'SI-19M2:PS-QDP2:DiagStatus-Mon': self.trims.led_19m2qdp2,
            'SI-19M2:PS-QFP:DiagStatus-Mon': self.trims.led_19m2qfp,
            'SI-19C1:PS-Q1:DiagStatus-Mon': self.trims.led_19c1q1,
            'SI-19C1:PS-Q2:DiagStatus-Mon': self.trims.led_19c1q2,
            'SI-19C2:PS-Q3:DiagStatus-Mon': self.trims.led_19c2q3,
            'SI-19C2:PS-Q4:DiagStatus-Mon': self.trims.led_19c2q4,
            'SI-19C3:PS-Q3:DiagStatus-Mon': self.trims.led_19c3q3,
            'SI-19C3:PS-Q4:DiagStatus-Mon': self.trims.led_19c3q4,
            'SI-19C4:PS-Q1:DiagStatus-Mon': self.trims.led_19c4q1,
            'SI-19C4:PS-Q2:DiagStatus-Mon': self.trims.led_19c4q2,
            'SI-20M1:PS-QDB1:DiagStatus-Mon': self.trims.led_20m1qdb1,
            'SI-20M1:PS-QDB2:DiagStatus-Mon': self.trims.led_20m1qdb2,
            'SI-20M1:PS-QFB:DiagStatus-Mon': self.trims.led_20m1qfb,
            'SI-20M2:PS-QDB1:DiagStatus-Mon': self.trims.led_20m2qdb1,
            'SI-20M2:PS-QDB2:DiagStatus-Mon': self.trims.led_20m2qdb2,
            'SI-20M2:PS-QFB:DiagStatus-Mon': self.trims.led_20m2qfb,
            'SI-20C1:PS-Q1:DiagStatus-Mon': self.trims.led_20c1q1,
            'SI-20C1:PS-Q2:DiagStatus-Mon': self.trims.led_20c1q2,
            'SI-20C2:PS-Q3:DiagStatus-Mon': self.trims.led_20c2q3,
            'SI-20C2:PS-Q4:DiagStatus-Mon': self.trims.led_20c2q4,
            'SI-20C3:PS-Q3:DiagStatus-Mon': self.trims.led_20c3q3,
            'SI-20C3:PS-Q4:DiagStatus-Mon': self.trims.led_20c3q4,
            'SI-20C4:PS-Q1:DiagStatus-Mon': self.trims.led_20c4q1,
            'SI-20C4:PS-Q2:DiagStatus-Mon': self.trims.led_20c4q2,
            'SI-01M1:PS-QDA:DiagStatus-Mon': self.trims.led_01m1qda,
            'SI-01M1:PS-QFA:DiagStatus-Mon': self.trims.led_01m1qfa,
            'SI-01M2:PS-QDA:DiagStatus-Mon': self.trims.led_01m2qda,
            'SI-01M2:PS-QFA:DiagStatus-Mon': self.trims.led_01m2qfa,
            'SI-01C1:PS-Q1:DiagStatus-Mon':  self.trims.led_01c1q1,
            'SI-01C1:PS-Q2:DiagStatus-Mon':  self.trims.led_01c1q2,
            'SI-01C2:PS-Q3:DiagStatus-Mon':  self.trims.led_01c2q3,
            'SI-01C2:PS-Q4:DiagStatus-Mon':  self.trims.led_01c2q4,
            'SI-01C3:PS-Q3:DiagStatus-Mon':  self.trims.led_01c3q3,
            'SI-01C3:PS-Q4:DiagStatus-Mon':  self.trims.led_01c3q4,
            'SI-01C4:PS-Q1:DiagStatus-Mon':  self.trims.led_01c4q1,
            'SI-01C4:PS-Q2:DiagStatus-Mon':  self.trims.led_01c4q2,
            'SI-05M1:PS-QDA:DiagStatus-Mon': self.trims.led_05m1qda,
            'SI-05M1:PS-QFA:DiagStatus-Mon': self.trims.led_05m1qfa,
            'SI-05M2:PS-QDA:DiagStatus-Mon': self.trims.led_05m2qda,
            'SI-05M2:PS-QFA:DiagStatus-Mon': self.trims.led_05m2qfa,
            'SI-05C1:PS-Q1:DiagStatus-Mon': self.trims.led_05c1q1,
            'SI-05C1:PS-Q2:DiagStatus-Mon': self.trims.led_05c1q2,
            'SI-05C2:PS-Q3:DiagStatus-Mon': self.trims.led_05c2q3,
            'SI-05C2:PS-Q4:DiagStatus-Mon': self.trims.led_05c2q4,
            'SI-05C3:PS-Q3:DiagStatus-Mon': self.trims.led_05c3q3,
            'SI-05C3:PS-Q4:DiagStatus-Mon': self.trims.led_05c3q4,
            'SI-05C4:PS-Q1:DiagStatus-Mon': self.trims.led_05c4q1,
            'SI-05C4:PS-Q2:DiagStatus-Mon': self.trims.led_05c4q2,
            'SI-09M1:PS-QDA:DiagStatus-Mon': self.trims.led_09m1qda,
            'SI-09M1:PS-QFA:DiagStatus-Mon': self.trims.led_09m1qfa,
            'SI-09M2:PS-QDA:DiagStatus-Mon': self.trims.led_09m2qda,
            'SI-09M2:PS-QFA:DiagStatus-Mon': self.trims.led_09m2qfa,
            'SI-09C1:PS-Q1:DiagStatus-Mon': self.trims.led_09c1q1,
            'SI-09C1:PS-Q2:DiagStatus-Mon': self.trims.led_09c1q2,
            'SI-09C2:PS-Q3:DiagStatus-Mon': self.trims.led_09c2q3,
            'SI-09C2:PS-Q4:DiagStatus-Mon': self.trims.led_09c2q4,
            'SI-09C3:PS-Q3:DiagStatus-Mon': self.trims.led_09c3q3,
            'SI-09C3:PS-Q4:DiagStatus-Mon': self.trims.led_09c3q4,
            'SI-09C4:PS-Q1:DiagStatus-Mon': self.trims.led_09c4q1,
            'SI-09C4:PS-Q2:DiagStatus-Mon': self.trims.led_09c4q2,
            'SI-13M1:PS-QDA:DiagStatus-Mon': self.trims.led_13m1qda,
            'SI-13M1:PS-QFA:DiagStatus-Mon': self.trims.led_13m1qfa,
            'SI-13M2:PS-QDA:DiagStatus-Mon': self.trims.led_13m2qda,
            'SI-13M2:PS-QFA:DiagStatus-Mon': self.trims.led_13m2qfa,
            'SI-13C1:PS-Q1:DiagStatus-Mon': self.trims.led_13c1q1,
            'SI-13C1:PS-Q2:DiagStatus-Mon': self.trims.led_13c1q2,
            'SI-13C2:PS-Q3:DiagStatus-Mon': self.trims.led_13c2q3,
            'SI-13C2:PS-Q4:DiagStatus-Mon': self.trims.led_13c2q4,
            'SI-13C3:PS-Q3:DiagStatus-Mon': self.trims.led_13c3q3,
            'SI-13C3:PS-Q4:DiagStatus-Mon': self.trims.led_13c3q4,
            'SI-13C4:PS-Q1:DiagStatus-Mon': self.trims.led_13c4q1,
            'SI-13C4:PS-Q2:DiagStatus-Mon': self.trims.led_13c4q2,
            'SI-17M1:PS-QDA:DiagStatus-Mon': self.trims.led_17m1qda,
            'SI-17M1:PS-QFA:DiagStatus-Mon': self.trims.led_17m1qfa,
            'SI-17M2:PS-QDA:DiagStatus-Mon': self.trims.led_17m2qda,
            'SI-17M2:PS-QFA:DiagStatus-Mon': self.trims.led_17m2qfa,
            'SI-17C1:PS-Q1:DiagStatus-Mon': self.trims.led_17c1q1,
            'SI-17C1:PS-Q2:DiagStatus-Mon': self.trims.led_17c1q2,
            'SI-17C2:PS-Q3:DiagStatus-Mon': self.trims.led_17c2q3,
            'SI-17C2:PS-Q4:DiagStatus-Mon': self.trims.led_17c2q4,
            'SI-17C3:PS-Q3:DiagStatus-Mon': self.trims.led_17c3q3,
            'SI-17C3:PS-Q4:DiagStatus-Mon': self.trims.led_17c3q4,
            'SI-17C4:PS-Q1:DiagStatus-Mon': self.trims.led_17c4q1,
            'SI-17C4:PS-Q2:DiagStatus-Mon': self.trims.led_17c4q2,
        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_trims)
        self.atualizar_status()

    def mostrar_janela_trims(self):
        """."""
        self.trims.setVisible(not self.trims.isVisible())

    def atualizar_status(self):
        """."""
        todos_ok = True
        for signal, led in self.sinais_estado_0.items():
            utils.verificar_trims(signal, led, estado_esperado=0)
            if not getattr(led, "state", False):
                todos_ok = False
        self.estado_ok = todos_ok

        if self.botao_menu:
            cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
            self.botao_menu.setStyleSheet(f"background-color: {cor}")

        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel,
                                                  "alarmsips")
        if alarme_widget:
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()


class Si_slowcorr(QtWidgets.QWidget):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__()
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.corrsi = uic.loadUi("corrsi.ui")
        self._registrar_grupos()

    def _registrar_grupos(self):
        self.sinais_estado_0 = {
            'SI-01M1:PS-CH:DiagStatus-Mon': self.corrsi.led_01m1ch,
            'SI-01M2:PS-CH:DiagStatus-Mon': self.corrsi.led_01m2ch,
            'SI-01C1:PS-CH:DiagStatus-Mon': self.corrsi.led_01c1ch,
            'SI-01C2:PS-CH:DiagStatus-Mon': self.corrsi.led_01c2ch,
            'SI-01C3:PS-CH:DiagStatus-Mon': self.corrsi.led_01c3ch,
            'SI-01C4:PS-CH:DiagStatus-Mon': self.corrsi.led_01c4ch,
            'SI-02M1:PS-CH:DiagStatus-Mon': self.corrsi.led_02m1ch,
            'SI-02M2:PS-CH:DiagStatus-Mon': self.corrsi.led_02m2ch,
            'SI-02C1:PS-CH:DiagStatus-Mon': self.corrsi.led_02c1ch,
            'SI-02C2:PS-CH:DiagStatus-Mon': self.corrsi.led_02c2ch,
            'SI-02C3:PS-CH:DiagStatus-Mon': self.corrsi.led_02c3ch,
            'SI-02C4:PS-CH:DiagStatus-Mon': self.corrsi.led_02c4ch,
            'SI-03M1:PS-CH:DiagStatus-Mon': self.corrsi.led_03m1ch,
            'SI-03M2:PS-CH:DiagStatus-Mon': self.corrsi.led_03m2ch,
            'SI-03C1:PS-CH:DiagStatus-Mon': self.corrsi.led_03c1ch,
            'SI-03C2:PS-CH:DiagStatus-Mon': self.corrsi.led_03c2ch,
            'SI-03C3:PS-CH:DiagStatus-Mon': self.corrsi.led_03c3ch,
            'SI-03C4:PS-CH:DiagStatus-Mon': self.corrsi.led_03c4ch,
            'SI-04M1:PS-CH:DiagStatus-Mon': self.corrsi.led_04m1ch,
            'SI-04M2:PS-CH:DiagStatus-Mon': self.corrsi.led_04m2ch,
            'SI-04C1:PS-CH:DiagStatus-Mon': self.corrsi.led_04c1ch,
            'SI-04C2:PS-CH:DiagStatus-Mon': self.corrsi.led_04c2ch,
            'SI-04C3:PS-CH:DiagStatus-Mon': self.corrsi.led_04c3ch,
            'SI-04C4:PS-CH:DiagStatus-Mon': self.corrsi.led_04c4ch,
            'SI-05M1:PS-CH:DiagStatus-Mon': self.corrsi.led_05m1ch,
            'SI-05M2:PS-CH:DiagStatus-Mon': self.corrsi.led_05m2ch,
            'SI-05C1:PS-CH:DiagStatus-Mon': self.corrsi.led_05c1ch,
            'SI-05C2:PS-CH:DiagStatus-Mon': self.corrsi.led_05c2ch,
            'SI-05C3:PS-CH:DiagStatus-Mon': self.corrsi.led_05c3ch,
            'SI-05C4:PS-CH:DiagStatus-Mon': self.corrsi.led_05c4ch,
            'SI-06M1:PS-CH:DiagStatus-Mon': self.corrsi.led_06m1ch,
            'SI-06M2:PS-CH:DiagStatus-Mon': self.corrsi.led_06m2ch,
            'SI-06C1:PS-CH:DiagStatus-Mon': self.corrsi.led_06c1ch,
            'SI-06C2:PS-CH:DiagStatus-Mon': self.corrsi.led_06c2ch,
            'SI-06C3:PS-CH:DiagStatus-Mon': self.corrsi.led_06c3ch,
            'SI-06C4:PS-CH:DiagStatus-Mon': self.corrsi.led_06c4ch,
            'SI-07M1:PS-CH:DiagStatus-Mon': self.corrsi.led_07m1ch,
            'SI-07M2:PS-CH:DiagStatus-Mon': self.corrsi.led_07m2ch,
            'SI-07C1:PS-CH:DiagStatus-Mon': self.corrsi.led_07c1ch,
            'SI-07C2:PS-CH:DiagStatus-Mon': self.corrsi.led_07c2ch,
            'SI-07C3:PS-CH:DiagStatus-Mon': self.corrsi.led_07c3ch,
            'SI-07C4:PS-CH:DiagStatus-Mon': self.corrsi.led_07c4ch,
            'SI-08M1:PS-CH:DiagStatus-Mon': self.corrsi.led_08m1ch,
            'SI-08M2:PS-CH:DiagStatus-Mon': self.corrsi.led_08m2ch,
            'SI-08C1:PS-CH:DiagStatus-Mon': self.corrsi.led_08c1ch,
            'SI-08C2:PS-CH:DiagStatus-Mon': self.corrsi.led_08c2ch,
            'SI-08C3:PS-CH:DiagStatus-Mon': self.corrsi.led_08c3ch,
            'SI-08C4:PS-CH:DiagStatus-Mon': self.corrsi.led_08c4ch,
            'SI-09M1:PS-CH:DiagStatus-Mon': self.corrsi.led_09m1ch,
            'SI-09M2:PS-CH:DiagStatus-Mon': self.corrsi.led_09m2ch,
            'SI-09C1:PS-CH:DiagStatus-Mon': self.corrsi.led_09c1ch,
            'SI-09C2:PS-CH:DiagStatus-Mon': self.corrsi.led_09c2ch,
            'SI-09C3:PS-CH:DiagStatus-Mon': self.corrsi.led_09c3ch,
            'SI-09C4:PS-CH:DiagStatus-Mon': self.corrsi.led_09c4ch,
            'SI-10M1:PS-CH:DiagStatus-Mon': self.corrsi.led_10m1ch,
            'SI-10M2:PS-CH:DiagStatus-Mon': self.corrsi.led_10m2ch,
            'SI-10C1:PS-CH:DiagStatus-Mon': self.corrsi.led_10c1ch,
            'SI-10C2:PS-CH:DiagStatus-Mon': self.corrsi.led_10c2ch,
            'SI-10C3:PS-CH:DiagStatus-Mon': self.corrsi.led_10c3ch,
            'SI-10C4:PS-CH:DiagStatus-Mon': self.corrsi.led_10c4ch,
            'SI-11M1:PS-CH:DiagStatus-Mon': self.corrsi.led_11m1ch,
            'SI-11M2:PS-CH:DiagStatus-Mon': self.corrsi.led_11m2ch,
            'SI-11C1:PS-CH:DiagStatus-Mon': self.corrsi.led_11c1ch,
            'SI-11C2:PS-CH:DiagStatus-Mon': self.corrsi.led_11c2ch,
            'SI-11C3:PS-CH:DiagStatus-Mon': self.corrsi.led_11c3ch,
            'SI-11C4:PS-CH:DiagStatus-Mon': self.corrsi.led_11c4ch,
            'SI-12M1:PS-CH:DiagStatus-Mon': self.corrsi.led_12m1ch,
            'SI-12M2:PS-CH:DiagStatus-Mon': self.corrsi.led_12m2ch,
            'SI-12C1:PS-CH:DiagStatus-Mon': self.corrsi.led_12c1ch,
            'SI-12C2:PS-CH:DiagStatus-Mon': self.corrsi.led_12c2ch,
            'SI-12C3:PS-CH:DiagStatus-Mon': self.corrsi.led_12c3ch,
            'SI-12C4:PS-CH:DiagStatus-Mon': self.corrsi.led_12c4ch,
            'SI-13M1:PS-CH:DiagStatus-Mon': self.corrsi.led_13m1ch,
            'SI-13M2:PS-CH:DiagStatus-Mon': self.corrsi.led_13m2ch,
            'SI-13C1:PS-CH:DiagStatus-Mon': self.corrsi.led_13c1ch,
            'SI-13C2:PS-CH:DiagStatus-Mon': self.corrsi.led_13c2ch,
            'SI-13C3:PS-CH:DiagStatus-Mon': self.corrsi.led_13c3ch,
            'SI-13C4:PS-CH:DiagStatus-Mon': self.corrsi.led_13c4ch,
            'SI-14M1:PS-CH:DiagStatus-Mon': self.corrsi.led_14m1ch,
            'SI-14M2:PS-CH:DiagStatus-Mon': self.corrsi.led_14m2ch,
            'SI-14C1:PS-CH:DiagStatus-Mon': self.corrsi.led_14c1ch,
            'SI-14C2:PS-CH:DiagStatus-Mon': self.corrsi.led_14c2ch,
            'SI-14C3:PS-CH:DiagStatus-Mon': self.corrsi.led_14c3ch,
            'SI-14C4:PS-CH:DiagStatus-Mon': self.corrsi.led_14c4ch,
            'SI-15M1:PS-CH:DiagStatus-Mon': self.corrsi.led_15m1ch,
            'SI-15M2:PS-CH:DiagStatus-Mon': self.corrsi.led_15m2ch,
            'SI-15C1:PS-CH:DiagStatus-Mon': self.corrsi.led_15c1ch,
            'SI-15C2:PS-CH:DiagStatus-Mon': self.corrsi.led_15c2ch,
            'SI-15C3:PS-CH:DiagStatus-Mon': self.corrsi.led_15c3ch,
            'SI-15C4:PS-CH:DiagStatus-Mon': self.corrsi.led_15c4ch,
            'SI-16M1:PS-CH:DiagStatus-Mon': self.corrsi.led_16m1ch,
            'SI-16M2:PS-CH:DiagStatus-Mon': self.corrsi.led_16m2ch,
            'SI-16C1:PS-CH:DiagStatus-Mon': self.corrsi.led_16c1ch,
            'SI-16C2:PS-CH:DiagStatus-Mon': self.corrsi.led_16c2ch,
            'SI-16C3:PS-CH:DiagStatus-Mon': self.corrsi.led_16c3ch,
            'SI-16C4:PS-CH:DiagStatus-Mon': self.corrsi.led_16c4ch,
            'SI-17M1:PS-CH:DiagStatus-Mon': self.corrsi.led_17m1ch,
            'SI-17M2:PS-CH:DiagStatus-Mon': self.corrsi.led_17m2ch,
            'SI-17C1:PS-CH:DiagStatus-Mon': self.corrsi.led_17c1ch,
            'SI-17C2:PS-CH:DiagStatus-Mon': self.corrsi.led_17c2ch,
            'SI-17C3:PS-CH:DiagStatus-Mon': self.corrsi.led_17c3ch,
            'SI-17C4:PS-CH:DiagStatus-Mon': self.corrsi.led_17c4ch,
            'SI-18M1:PS-CH:DiagStatus-Mon': self.corrsi.led_18m1ch,
            'SI-18M2:PS-CH:DiagStatus-Mon': self.corrsi.led_18m2ch,
            'SI-18C1:PS-CH:DiagStatus-Mon': self.corrsi.led_18c1ch,
            'SI-18C2:PS-CH:DiagStatus-Mon': self.corrsi.led_18c2ch,
            'SI-18C3:PS-CH:DiagStatus-Mon': self.corrsi.led_18c3ch,
            'SI-18C4:PS-CH:DiagStatus-Mon': self.corrsi.led_18c4ch,
            'SI-19M1:PS-CH:DiagStatus-Mon': self.corrsi.led_19m1ch,
            'SI-19M2:PS-CH:DiagStatus-Mon': self.corrsi.led_19m2ch,
            'SI-19C1:PS-CH:DiagStatus-Mon': self.corrsi.led_19c1ch,
            'SI-19C2:PS-CH:DiagStatus-Mon': self.corrsi.led_19c2ch,
            'SI-19C3:PS-CH:DiagStatus-Mon': self.corrsi.led_19c3ch,
            'SI-19C4:PS-CH:DiagStatus-Mon': self.corrsi.led_19c4ch,
            'SI-20M1:PS-CH:DiagStatus-Mon': self.corrsi.led_20m1ch,
            'SI-20M2:PS-CH:DiagStatus-Mon': self.corrsi.led_20m2ch,
            'SI-20C1:PS-CH:DiagStatus-Mon': self.corrsi.led_20c1ch,
            'SI-20C2:PS-CH:DiagStatus-Mon': self.corrsi.led_20c2ch,
            'SI-20C3:PS-CH:DiagStatus-Mon': self.corrsi.led_20c3ch,
            'SI-20C4:PS-CH:DiagStatus-Mon': self.corrsi.led_20c4ch,
            'SI-01M1:PS-CV:DiagStatus-Mon': self.corrsi.led_01m1cv,
            'SI-01M2:PS-CV:DiagStatus-Mon': self.corrsi.led_01m2cv,
            'SI-01C1:PS-CV:DiagStatus-Mon': self.corrsi.led_01c1cv,
            'SI-01C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_01c2cv1,
            'SI-01C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_01c2cv2,
            'SI-01C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_01c3cv1,
            'SI-01C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_01c3cv2,
            'SI-01C4:PS-CV:DiagStatus-Mon': self.corrsi.led_01c4cv,
            'SI-02M1:PS-CV:DiagStatus-Mon': self.corrsi.led_02m1cv,
            'SI-02M2:PS-CV:DiagStatus-Mon': self.corrsi.led_02m2cv,
            'SI-02C1:PS-CV:DiagStatus-Mon': self.corrsi.led_02c1cv,
            'SI-02C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_02c2cv1,
            'SI-02C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_02c2cv2,
            'SI-02C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_02c3cv1,
            'SI-02C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_02c3cv2,
            'SI-02C4:PS-CV:DiagStatus-Mon': self.corrsi.led_02c4cv,
            'SI-03M1:PS-CV:DiagStatus-Mon': self.corrsi.led_03m1cv,
            'SI-03M2:PS-CV:DiagStatus-Mon': self.corrsi.led_03m2cv,
            'SI-03C1:PS-CV:DiagStatus-Mon': self.corrsi.led_03c1cv,
            'SI-03C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_03c2cv1,
            'SI-03C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_03c2cv2,
            'SI-03C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_03c3cv1,
            'SI-03C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_03c3cv2,
            'SI-03C4:PS-CV:DiagStatus-Mon': self.corrsi.led_03c4cv,
            'SI-04M1:PS-CV:DiagStatus-Mon': self.corrsi.led_04m1cv,
            'SI-04M2:PS-CV:DiagStatus-Mon': self.corrsi.led_04m2cv,
            'SI-04C1:PS-CV:DiagStatus-Mon': self.corrsi.led_04c1cv,
            'SI-04C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_04c2cv1,
            'SI-04C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_04c2cv2,
            'SI-04C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_04c3cv1,
            'SI-04C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_04c3cv2,
            'SI-04C4:PS-CV:DiagStatus-Mon': self.corrsi.led_04c4cv,
            'SI-05M1:PS-CV:DiagStatus-Mon': self.corrsi.led_05m1cv,
            'SI-05M2:PS-CV:DiagStatus-Mon': self.corrsi.led_05m2cv,
            'SI-05C1:PS-CV:DiagStatus-Mon': self.corrsi.led_05c1cv,
            'SI-05C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_05c2cv1,
            'SI-05C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_05c2cv2,
            'SI-05C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_05c3cv1,
            'SI-05C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_05c3cv2,
            'SI-05C4:PS-CV:DiagStatus-Mon': self.corrsi.led_05c4cv,
            'SI-06M1:PS-CV:DiagStatus-Mon': self.corrsi.led_06m1cv,
            'SI-06M2:PS-CV:DiagStatus-Mon': self.corrsi.led_06m2cv,
            'SI-06C1:PS-CV:DiagStatus-Mon': self.corrsi.led_06c1cv,
            'SI-06C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_06c2cv1,
            'SI-06C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_06c2cv2,
            'SI-06C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_06c3cv1,
            'SI-06C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_06c3cv2,
            'SI-06C4:PS-CV:DiagStatus-Mon': self.corrsi.led_06c4cv,
            'SI-07M1:PS-CV:DiagStatus-Mon': self.corrsi.led_07m1cv,
            'SI-07M2:PS-CV:DiagStatus-Mon': self.corrsi.led_07m2cv,
            'SI-07C1:PS-CV:DiagStatus-Mon': self.corrsi.led_07c1cv,
            'SI-07C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_07c2cv1,
            'SI-07C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_07c2cv2,
            'SI-07C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_07c3cv1,
            'SI-07C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_07c3cv2,
            'SI-07C4:PS-CV:DiagStatus-Mon': self.corrsi.led_07c4cv,
            'SI-08M1:PS-CV:DiagStatus-Mon': self.corrsi.led_08m1cv,
            'SI-08M2:PS-CV:DiagStatus-Mon': self.corrsi.led_08m2cv,
            'SI-08C1:PS-CV:DiagStatus-Mon': self.corrsi.led_08c1cv,
            'SI-08C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_08c2cv1,
            'SI-08C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_08c2cv2,
            'SI-08C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_08c3cv1,
            'SI-08C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_08c3cv2,
            'SI-08C4:PS-CV:DiagStatus-Mon': self.corrsi.led_08c4cv,
            'SI-09M1:PS-CV:DiagStatus-Mon': self.corrsi.led_09m1cv,
            'SI-09M2:PS-CV:DiagStatus-Mon': self.corrsi.led_09m2cv,
            'SI-09C1:PS-CV:DiagStatus-Mon': self.corrsi.led_09c1cv,
            'SI-09C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_09c2cv1,
            'SI-09C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_09c2cv2,
            'SI-09C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_09c3cv1,
            'SI-09C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_09c3cv2,
            'SI-09C4:PS-CV:DiagStatus-Mon': self.corrsi.led_09c4cv,
            'SI-10M1:PS-CV:DiagStatus-Mon': self.corrsi.led_10m1cv,
            'SI-10M2:PS-CV:DiagStatus-Mon': self.corrsi.led_10m2cv,
            'SI-10C1:PS-CV:DiagStatus-Mon': self.corrsi.led_10c1cv,
            'SI-10C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_10c2cv1,
            'SI-10C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_10c2cv2,
            'SI-10C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_10c3cv1,
            'SI-10C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_10c3cv2,
            'SI-10C4:PS-CV:DiagStatus-Mon': self.corrsi.led_10c4cv,
            'SI-11M1:PS-CV:DiagStatus-Mon': self.corrsi.led_11m1cv,
            'SI-11M2:PS-CV:DiagStatus-Mon': self.corrsi.led_11m2cv,
            'SI-11C1:PS-CV:DiagStatus-Mon': self.corrsi.led_11c1cv,
            'SI-11C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_11c2cv1,
            'SI-11C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_11c2cv2,
            'SI-11C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_11c3cv1,
            'SI-11C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_11c3cv2,
            'SI-11C4:PS-CV:DiagStatus-Mon': self.corrsi.led_11c4cv,
            'SI-12M1:PS-CV:DiagStatus-Mon': self.corrsi.led_12m1cv,
            'SI-12M2:PS-CV:DiagStatus-Mon': self.corrsi.led_12m2cv,
            'SI-12C1:PS-CV:DiagStatus-Mon': self.corrsi.led_12c1cv,
            'SI-12C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_12c2cv1,
            'SI-12C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_12c2cv2,
            'SI-12C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_12c3cv1,
            'SI-12C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_12c3cv2,
            'SI-12C4:PS-CV:DiagStatus-Mon': self.corrsi.led_12c4cv,
            'SI-13M1:PS-CV:DiagStatus-Mon': self.corrsi.led_13m1cv,
            'SI-13M2:PS-CV:DiagStatus-Mon': self.corrsi.led_13m2cv,
            'SI-13C1:PS-CV:DiagStatus-Mon': self.corrsi.led_13c1cv,
            'SI-13C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_13c2cv1,
            'SI-13C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_13c2cv2,
            'SI-13C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_13c3cv1,
            'SI-13C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_13c3cv2,
            'SI-13C4:PS-CV:DiagStatus-Mon': self.corrsi.led_13c4cv,
            'SI-14M1:PS-CV:DiagStatus-Mon': self.corrsi.led_14m1cv,
            'SI-14M2:PS-CV:DiagStatus-Mon': self.corrsi.led_14m2cv,
            'SI-14C1:PS-CV:DiagStatus-Mon': self.corrsi.led_14c1cv,
            'SI-14C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_14c2cv1,
            'SI-14C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_14c2cv2,
            'SI-14C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_14c3cv1,
            'SI-14C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_14c3cv2,
            'SI-14C4:PS-CV:DiagStatus-Mon': self.corrsi.led_14c4cv,
            'SI-15M1:PS-CV:DiagStatus-Mon': self.corrsi.led_15m1cv,
            'SI-15M2:PS-CV:DiagStatus-Mon': self.corrsi.led_15m2cv,
            'SI-15C1:PS-CV:DiagStatus-Mon': self.corrsi.led_15c1cv,
            'SI-15C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_15c2cv1,
            'SI-15C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_15c2cv2,
            'SI-15C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_15c3cv1,
            'SI-15C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_15c3cv2,
            'SI-15C4:PS-CV:DiagStatus-Mon': self.corrsi.led_15c4cv,
            'SI-16M1:PS-CV:DiagStatus-Mon': self.corrsi.led_16m1cv,
            'SI-16M2:PS-CV:DiagStatus-Mon': self.corrsi.led_16m2cv,
            'SI-16C1:PS-CV:DiagStatus-Mon': self.corrsi.led_16c1cv,
            'SI-16C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_16c2cv1,
            'SI-16C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_16c2cv2,
            'SI-16C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_16c3cv1,
            'SI-16C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_16c3cv2,
            'SI-16C4:PS-CV:DiagStatus-Mon': self.corrsi.led_16c4cv,
            'SI-17M1:PS-CV:DiagStatus-Mon': self.corrsi.led_17m1cv,
            'SI-17M2:PS-CV:DiagStatus-Mon': self.corrsi.led_17m2cv,
            'SI-17C1:PS-CV:DiagStatus-Mon': self.corrsi.led_17c1cv,
            'SI-17C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_17c2cv1,
            'SI-17C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_17c2cv2,
            'SI-17C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_17c3cv1,
            'SI-17C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_17c3cv2,
            'SI-17C4:PS-CV:DiagStatus-Mon': self.corrsi.led_17c4cv,
            'SI-18M1:PS-CV:DiagStatus-Mon': self.corrsi.led_18m1cv,
            'SI-18M2:PS-CV:DiagStatus-Mon': self.corrsi.led_18m2cv,
            'SI-18C1:PS-CV:DiagStatus-Mon': self.corrsi.led_18c1cv,
            'SI-18C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_18c2cv1,
            'SI-18C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_18c2cv2,
            'SI-18C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_18c3cv1,
            'SI-18C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_18c3cv2,
            'SI-18C4:PS-CV:DiagStatus-Mon': self.corrsi.led_18c4cv,
            'SI-19M1:PS-CV:DiagStatus-Mon': self.corrsi.led_19m1cv,
            'SI-19M2:PS-CV:DiagStatus-Mon': self.corrsi.led_19m2cv,
            'SI-19C1:PS-CV:DiagStatus-Mon': self.corrsi.led_19c1cv,
            'SI-19C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_19c2cv1,
            'SI-19C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_19c2cv2,
            'SI-19C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_19c3cv1,
            'SI-19C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_19c3cv2,
            'SI-19C4:PS-CV:DiagStatus-Mon': self.corrsi.led_19c4cv,
            'SI-20M1:PS-CV:DiagStatus-Mon': self.corrsi.led_20m1cv,
            'SI-20M2:PS-CV:DiagStatus-Mon': self.corrsi.led_20m2cv,
            'SI-20C1:PS-CV:DiagStatus-Mon': self.corrsi.led_20c1cv,
            'SI-20C2:PS-CV-1:DiagStatus-Mon': self.corrsi.led_20c2cv1,
            'SI-20C2:PS-CV-2:DiagStatus-Mon': self.corrsi.led_20c2cv2,
            'SI-20C3:PS-CV-1:DiagStatus-Mon': self.corrsi.led_20c3cv1,
            'SI-20C3:PS-CV-2:DiagStatus-Mon': self.corrsi.led_20c3cv2,
            'SI-20C4:PS-CV:DiagStatus-Mon': self.corrsi.led_20c4cv,
        }

    def configurar_sistema(self):
        """."""
        self.botao_menu.clicked.connect(self.mostrar_janela_corrsi)
        self.atualizar_status()

    def mostrar_janela_corrsi(self):
        """."""
        self.corrsi.setVisible(not self.corrsi.isVisible())

    def atualizar_status(self):
        """."""
        todos_ok = True
        for signal, led in self.sinais_estado_0.items():
            utils.verificar_corrsi(signal, led, estado_esperado=0)
            if not getattr(led, "state", False):
                todos_ok = False
        self.estado_ok = todos_ok

        if self.botao_menu:
            cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
            self.botao_menu.setStyleSheet(f"background-color: {cor}")

        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel,
                                                  "alarmsips")
        if alarme_widget:
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()


class Blocosips:
    """Gerencia o bloco de fontes do Anel e atualiza a label sips."""

    def __init__(self, janela_opr):
        """."""
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto
        self.psfamilysi = Si_psfamily(janela_opr, janela_opr.btnpsfamilysi)
        self.skewquad = Si_skewquad(janela_opr, janela_opr.btnskewquad)
        self.trims = Si_trims(janela_opr, janela_opr.btntrims)
        self.ffwcorr = Si_ffwcorr(janela_opr, janela_opr.btnffwcorr)
        self.corrsi = Si_slowcorr(janela_opr, janela_opr.btncorrsi)

        # Adiciona todas as subjanelas à lista
        self.subjanelas.extend([
            self.psfamilysi,
            self.skewquad,
            self.trims,
            self.ffwcorr,
            self.corrsi,

        ])

        # Configura cada subjanela
        for sub in self.subjanelas:
            sub.configurar_sistema()

    def atualizar_grupo(self):
        """Atualiza todas as subjanelas e a label alarmsips."""
        falha_detectada = False

        for sub in self.subjanelas:
            sub.atualizar_status()
            if not getattr(sub, "estado_ok", True):
                falha_detectada = True

        # Atualiza a label principal do bloco SIPS
        alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel,
                                                  "alarmsips")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if not falha_detectada else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()
