"""Logica das fontes do Anel de Armazenamento."""
from PyQt5 import QtWidgets
import utils
import logging


class Si_psfamily(utils.ConnWidgetPVs):
    """."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/psfamilysi.ui",
                         "estado")

    def _registrar_grupos(self):
        self.sinais = {
            'SI-Fam:PS-B1B2-1:DiagStatus-Mon': (self._gwidget
                                                ('led_psfamb1'), 0),
            'SI-Fam:PS-B1B2-2:DiagStatus-Mon': (self._gwidget
                                                ('led_psfamb2'), 0),
            'SI-Fam:PS-Q1:DiagStatus-Mon': (self._gwidget('led_psfamq1'), 0),
            'SI-Fam:PS-Q2:DiagStatus-Mon': (self._gwidget('led_psfamq2'), 0),
            'SI-Fam:PS-Q3:DiagStatus-Mon': (self._gwidget('led_psfamq3'), 0),
            'SI-Fam:PS-Q4:DiagStatus-Mon': (self._gwidget('led_psfamq4'), 0),
            'SI-Fam:PS-QDA:DiagStatus-Mon': (self._gwidget('led_psfamqda'), 0),
            'SI-Fam:PS-QFP:DiagStatus-Mon': (self._gwidget('led_psfamqfp'), 0),
            'SI-Fam:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamqdb1'), 0),
            'SI-Fam:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamqdb2'), 0),
            'SI-Fam:PS-QDP1:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamqdp1'), 0),
            'SI-Fam:PS-QDP2:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamqdp2'), 0),
            'SI-Fam:PS-QFA:DiagStatus-Mon': (self._gwidget('led_psfamqfa'), 0),
            'SI-Fam:PS-QFB:DiagStatus-Mon': (self._gwidget('led_psfamqfb'), 0),
            'SI-Fam:PS-SFP2:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsfp2'), 0),
            'SI-Fam:PS-SDA0:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsda0'), 0),
            'SI-Fam:PS-SDA1:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsda1'), 0),
            'SI-Fam:PS-SDA2:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsda2'), 0),
            'SI-Fam:PS-SDA3:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsda3'), 0),
            'SI-Fam:PS-SDB0:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsdb0'), 0),
            'SI-Fam:PS-SDB1:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsdb1'), 0),
            'SI-Fam:PS-SDB2:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsdb2'), 0),
            'SI-Fam:PS-SDB3:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsdb3'), 0),
            'SI-Fam:PS-SDP0:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsdp0'), 0),
            'SI-Fam:PS-SDP1:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsdp1'), 0),
            'SI-Fam:PS-SDP2:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsdp2'), 0),
            'SI-Fam:PS-SDP3:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsdp3'), 0),
            'SI-Fam:PS-SFA0:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsfa0'), 0),
            'SI-Fam:PS-SFA1:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsfa1'), 0),
            'SI-Fam:PS-SFA2:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsfa2'), 0),
            'SI-Fam:PS-SFB0:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsfb0'), 0),
            'SI-Fam:PS-SFB1:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsfb1'), 0),
            'SI-Fam:PS-SFB2:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsfb2'), 0),
            'SI-Fam:PS-SFP0:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsfp0'), 0),
            'SI-Fam:PS-SFP1:DiagStatus-Mon': (self._gwidget
                                              ('led_psfamsfp1'), 0),
        }


class Si_skewquad(utils.ConnWidgetPVs):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/skewquad.ui",
                         "estado")

    def _registrar_grupos(self):
        self.sinais = {
            'SI-01M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew01m1'), 0),
            'SI-01M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew01m2'), 0),
            'SI-01C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew01c1'), 0),
            'SI-01C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew01c2'), 0),
            'SI-01C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew01c3'), 0),
            'SI-02M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew02m1'), 0),
            'SI-02M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew02m2'), 0),
            'SI-02C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew02c1'), 0),
            'SI-02C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew02c2'), 0),
            'SI-02C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew02c3'), 0),
            'SI-03M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew03m1'), 0),
            'SI-03M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew03m2'), 0),
            'SI-03C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew03c1'), 0),
            'SI-03C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew03c2'), 0),
            'SI-03C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew03c3'), 0),
            'SI-04M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew04m1'), 0),
            'SI-04M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew04m2'), 0),
            'SI-04C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew04c1'), 0),
            'SI-04C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew04c2'), 0),
            'SI-04C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew04c3'), 0),
            'SI-05M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew05m1'), 0),
            'SI-05M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew05m2'), 0),
            'SI-05C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew05c1'), 0),
            'SI-05C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew05c2'), 0),
            'SI-05C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew05c3'), 0),
            'SI-06M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew06m1'), 0),
            'SI-06M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew06m2'), 0),
            'SI-06C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew06c1'), 0),
            'SI-06C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew06c2'), 0),
            'SI-06C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew06c3'), 0),
            'SI-07M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew07m1'), 0),
            'SI-07M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew07m2'), 0),
            'SI-07C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew07c1'), 0),
            'SI-07C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew07c2'), 0),
            'SI-07C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew07c3'), 0),
            'SI-08M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew08m1'), 0),
            'SI-08M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew08m2'), 0),
            'SI-08C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew08c1'), 0),
            'SI-08C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew08c2'), 0),
            'SI-08C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew08c3'), 0),
            'SI-09M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew09m1'), 0),
            'SI-09M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew09m2'), 0),
            'SI-09C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew09c1'), 0),
            'SI-09C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew09c2'), 0),
            'SI-09C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew09c3'), 0),
            'SI-10M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew10m1'), 0),
            'SI-10M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew10m2'), 0),
            'SI-10C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew10c1'), 0),
            'SI-10C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew10c2'), 0),
            'SI-10C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew10c3'), 0),
            'SI-11M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew11m1'), 0),
            'SI-11M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew11m2'), 0),
            'SI-11C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew11c1'), 0),
            'SI-11C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew11c2'), 0),
            'SI-11C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew11c3'), 0),
            'SI-12M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew12m1'), 0),
            'SI-12M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew12m2'), 0),
            'SI-12C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew12c1'), 0),
            'SI-12C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew12c2'), 0),
            'SI-12C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew12c3'), 0),
            'SI-13M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew13m1'), 0),
            'SI-13M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew13m2'), 0),
            'SI-13C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew13c1'), 0),
            'SI-13C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew13c2'), 0),
            'SI-13C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew13c3'), 0),
            'SI-14M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew14m1'), 0),
            'SI-14M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew14m2'), 0),
            'SI-14C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew14c1'), 0),
            'SI-14C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew14c2'), 0),
            'SI-14C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew14c3'), 0),
            'SI-15M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew15m1'), 0),
            'SI-15M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew15m2'), 0),
            'SI-15C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew15c1'), 0),
            'SI-15C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew15c2'), 0),
            'SI-15C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew15c3'), 0),
            'SI-16M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew16m1'), 0),
            'SI-16M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew16m2'), 0),
            'SI-16C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew16c1'), 0),
            'SI-16C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew16c2'), 0),
            'SI-16C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew16c3'), 0),
            'SI-17M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew17m1'), 0),
            'SI-17M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew17m2'), 0),
            'SI-17C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew17c1'), 0),
            'SI-17C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew17c2'), 0),
            'SI-17C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew17c3'), 0),
            'SI-18M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew18m1'), 0),
            'SI-18M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew18m2'), 0),
            'SI-18C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew18c1'), 0),
            'SI-18C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew18c2'), 0),
            'SI-18C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew18c3'), 0),
            'SI-19M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew19m1'), 0),
            'SI-19M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew19m2'), 0),
            'SI-19C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew19c1'), 0),
            'SI-19C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew19c2'), 0),
            'SI-19C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew19c3'), 0),
            'SI-20M1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew20m1'), 0),
            'SI-20M2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew20m2'), 0),
            'SI-20C1:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew20c1'), 0),
            'SI-20C2:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew20c2'), 0),
            'SI-20C3:PS-QS:DiagStatus-Mon': (self._gwidget('led_skew20c3'), 0),
        }


class Si_trims(utils.ConnWidgetPVs):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/trims.ui",
                         "estado")

    def _registrar_grupos(self):
        self.sinais = {
            'SI-02M1:PS-QFB:DiagStatus-Mon': (self._gwidget('led_02m1qfb'), 0),
            'SI-02M1:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_02m1qdb1'), 0),
            'SI-02M1:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_02m1qdb2'), 0),
            'SI-02M2:PS-QFB:DiagStatus-Mon': (self._gwidget('led_02m2qfb'), 0),
            'SI-02M2:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_02m2qdb1'), 0),
            'SI-02M2:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_02m2qdb2'), 0),
            'SI-02C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_02c1q1'), 0),
            'SI-02C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_02c1q2'), 0),
            'SI-02C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_02c2q3'), 0),
            'SI-02C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_02c2q4'), 0),
            'SI-02C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_02c3q3'), 0),
            'SI-02C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_02c3q4'), 0),
            'SI-02C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_02c4q1'), 0),
            'SI-02C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_02c4q2'), 0),
            'SI-03M1:PS-QFP:DiagStatus-Mon': (self._gwidget('led_03m1qfp'), 0),
            'SI-03M1:PS-QDP1:DiagStatus-Mon': (self._gwidget
                                               ('led_03m1qdp1'), 0),
            'SI-03M1:PS-QDP2:DiagStatus-Mon': (self._gwidget
                                               ('led_03m1qdp2'), 0),
            'SI-03M2:PS-QDP1:DiagStatus-Mon': (self._gwidget
                                               ('led_03m2qdp1'), 0),
            'SI-03M2:PS-QDP2:DiagStatus-Mon': (self._gwidget
                                               ('led_03m2qdp2'), 0),
            'SI-03M2:PS-QFP:DiagStatus-Mon': (self._gwidget('led_03m2qfp'), 0),
            'SI-03C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_03c1q1'), 0),
            'SI-03C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_03c1q2'), 0),
            'SI-03C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_03c2q3'), 0),
            'SI-03C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_03c2q4'), 0),
            'SI-03C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_03c3q3'), 0),
            'SI-03C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_03c3q4'), 0),
            'SI-03C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_03c4q1'), 0),
            'SI-03C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_03c4q2'), 0),
            'SI-04M1:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_04m1qdb1'), 0),
            'SI-04M1:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_04m1qdb2'), 0),
            'SI-04M1:PS-QFB:DiagStatus-Mon': (self._gwidget
                                              ('led_04m1qfb'), 0),
            'SI-04M2:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_04m2qdb1'), 0),
            'SI-04M2:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_04m2qdb2'), 0),
            'SI-04M2:PS-QFB:DiagStatus-Mon': (self._gwidget('led_04m2qfb'), 0),
            'SI-04C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_04c1q1'), 0),
            'SI-04C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_04c1q2'), 0),
            'SI-04C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_04c2q3'), 0),
            'SI-04C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_04c2q4'), 0),
            'SI-04C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_04c3q3'), 0),
            'SI-04C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_04c3q4'), 0),
            'SI-04C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_04c4q1'), 0),
            'SI-04C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_04c4q2'), 0),
            'SI-06M1:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_06m1qdb1'), 0),
            'SI-06M1:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_06m1qdb2'), 0),
            'SI-06M1:PS-QFB:DiagStatus-Mon': (self._gwidget('led_06m1qfb'), 0),
            'SI-06M2:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_06m2qdb1'), 0),
            'SI-06M2:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_06m2qdb2'), 0),
            'SI-06M2:PS-QFB:DiagStatus-Mon': (self._gwidget('led_06m2qfb'), 0),
            'SI-06C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_06c1q1'), 0),
            'SI-06C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_06c1q2'), 0),
            'SI-06C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_06c2q3'), 0),
            'SI-06C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_06c2q4'), 0),
            'SI-06C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_06c3q3'), 0),
            'SI-06C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_06c3q4'), 0),
            'SI-06C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_06c4q1'), 0),
            'SI-06C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_06c4q2'), 0),
            'SI-07M1:PS-QDP1:DiagStatus-Mon': (self._gwidget
                                               ('led_07m1qdp1'), 0),
            'SI-07M1:PS-QDP2:DiagStatus-Mon': (self._gwidget
                                               ('led_07m1qdp2'), 0),
            'SI-07M1:PS-QFP:DiagStatus-Mon': (self._gwidget('led_07m1qfp'), 0),
            'SI-07M2:PS-QDP1:DiagStatus-Mon': (self._gwidget
                                               ('led_07m2qdp1'), 0),
            'SI-07M2:PS-QDP2:DiagStatus-Mon': (self._gwidget
                                               ('led_07m2qdp2'), 0),
            'SI-07M2:PS-QFP:DiagStatus-Mon': (self._gwidget('led_07m2qfp'), 0),
            'SI-07C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_07c1q1'), 0),
            'SI-07C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_07c1q2'), 0),
            'SI-07C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_07c2q3'), 0),
            'SI-07C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_07c2q4'), 0),
            'SI-07C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_07c3q3'), 0),
            'SI-07C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_07c3q4'), 0),
            'SI-07C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_07c4q1'), 0),
            'SI-07C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_07c4q2'), 0),
            'SI-08M1:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_08m1qdb1'), 0),
            'SI-08M1:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_08m1qdb2'), 0),
            'SI-08M1:PS-QFB:DiagStatus-Mon': (self._gwidget('led_08m1qfb'), 0),
            'SI-08M2:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_08m2qdb1'), 0),
            'SI-08M2:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_08m2qdb2'), 0),
            'SI-08M2:PS-QFB:DiagStatus-Mon': (self._gwidget('led_08m2qfb'), 0),
            'SI-08C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_08c1q1'), 0),
            'SI-08C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_08c1q2'), 0),
            'SI-08C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_08c2q3'), 0),
            'SI-08C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_08c2q4'), 0),
            'SI-08C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_08c3q3'), 0),
            'SI-08C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_08c3q4'), 0),
            'SI-08C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_08c4q1'), 0),
            'SI-08C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_08c4q2'), 0),
            'SI-10M1:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_10m1qdb1'), 0),
            'SI-10M1:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_10m1qdb2'), 0),
            'SI-10M1:PS-QFB:DiagStatus-Mon': (self._gwidget('led_10m1qfb'), 0),
            'SI-10M2:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_10m2qdb1'), 0),
            'SI-10M2:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_10m2qdb2'), 0),
            'SI-10M2:PS-QFB:DiagStatus-Mon': (self._gwidget('led_10m2qfb'), 0),
            'SI-10C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_10c1q1'), 0),
            'SI-10C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_10c1q2'), 0),
            'SI-10C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_10c2q3'), 0),
            'SI-10C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_10c2q4'), 0),
            'SI-10C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_10c3q3'), 0),
            'SI-10C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_10c3q4'), 0),
            'SI-10C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_10c4q1'), 0),
            'SI-10C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_10c4q2'), 0),
            'SI-11M1:PS-QDP1:DiagStatus-Mon': (self._gwidget
                                               ('led_11m1qdp1'), 0),
            'SI-11M1:PS-QDP2:DiagStatus-Mon': (self._gwidget
                                               ('led_11m1qdp2'), 0),
            'SI-11M1:PS-QFP:DiagStatus-Mon': (self._gwidget('led_11m1qfp'), 0),
            'SI-11M2:PS-QDP1:DiagStatus-Mon': (self._gwidget
                                               ('led_11m2qdp1'), 0),
            'SI-11M2:PS-QDP2:DiagStatus-Mon': (self._gwidget
                                               ('led_11m2qdp2'), 0),
            'SI-11M2:PS-QFP:DiagStatus-Mon': (self._gwidget('led_11m2qfp'), 0),
            'SI-11C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_11c1q1'), 0),
            'SI-11C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_11c1q2'), 0),
            'SI-11C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_11c2q3'), 0),
            'SI-11C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_11c2q4'), 0),
            'SI-11C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_11c3q3'), 0),
            'SI-11C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_11c3q4'), 0),
            'SI-11C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_11c4q1'), 0),
            'SI-11C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_11c4q2'), 0),
            'SI-12M1:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_12m1qdb1'), 0),
            'SI-12M1:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_12m1qdb2'), 0),
            'SI-12M1:PS-QFB:DiagStatus-Mon': (self._gwidget('led_12m1qfb'), 0),
            'SI-12M2:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_12m2qdb1'), 0),
            'SI-12M2:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_12m2qdb2'), 0),
            'SI-12M2:PS-QFB:DiagStatus-Mon': (self._gwidget('led_12m2qfb'), 0),
            'SI-12C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_12c1q1'), 0),
            'SI-12C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_12c1q2'), 0),
            'SI-12C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_12c2q3'), 0),
            'SI-12C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_12c2q4'), 0),
            'SI-12C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_12c3q3'), 0),
            'SI-12C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_12c3q4'), 0),
            'SI-12C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_12c4q1'), 0),
            'SI-12C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_12c4q2'), 0),
            'SI-14M1:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_14m1qdb1'), 0),
            'SI-14M1:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_14m1qdb2'), 0),
            'SI-14M1:PS-QFB:DiagStatus-Mon': (self._gwidget('led_14m1qfb'), 0),
            'SI-14M2:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_14m2qdb1'), 0),
            'SI-14M2:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_14m2qdb2'), 0),
            'SI-14M2:PS-QFB:DiagStatus-Mon': (self._gwidget('led_14m2qfb'), 0),
            'SI-14C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_14c1q1'), 0),
            'SI-14C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_14c1q2'), 0),
            'SI-14C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_14c2q3'), 0),
            'SI-14C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_14c2q4'), 0),
            'SI-14C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_14c3q3'), 0),
            'SI-14C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_14c3q4'), 0),
            'SI-14C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_14c4q1'), 0),
            'SI-14C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_14c4q2'), 0),
            'SI-15M1:PS-QDP1:DiagStatus-Mon': (self._gwidget
                                               ('led_15m1qdp1'), 0),
            'SI-15M1:PS-QDP2:DiagStatus-Mon': (self._gwidget
                                               ('led_15m1qdp2'), 0),
            'SI-15M1:PS-QFP:DiagStatus-Mon': (self._gwidget('led_15m1qfp'), 0),
            'SI-15M2:PS-QDP1:DiagStatus-Mon': (self._gwidget
                                               ('led_15m2qdp1'), 0),
            'SI-15M2:PS-QDP2:DiagStatus-Mon': (self._gwidget
                                               ('led_15m2qdp2'), 0),
            'SI-15M2:PS-QFP:DiagStatus-Mon': (self._gwidget('led_15m2qfp'), 0),
            'SI-15C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_15c1q1'), 0),
            'SI-15C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_15c1q2'), 0),
            'SI-15C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_15c2q3'), 0),
            'SI-15C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_15c2q4'), 0),
            'SI-15C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_15c3q3'), 0),
            'SI-15C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_15c3q4'), 0),
            'SI-15C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_15c4q1'), 0),
            'SI-15C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_15c4q2'), 0),
            'SI-16M1:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_16m1qdb1'), 0),
            'SI-16M1:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_16m1qdb2'), 0),
            'SI-16M1:PS-QFB:DiagStatus-Mon': (self._gwidget('led_16m1qfb'), 0),
            'SI-16M2:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_16m2qdb1'), 0),
            'SI-16M2:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_16m2qdb2'), 0),
            'SI-16M2:PS-QFB:DiagStatus-Mon': (self._gwidget('led_16m2qfb'), 0),
            'SI-16C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_16c1q1'), 0),
            'SI-16C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_16c1q2'), 0),
            'SI-16C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_16c2q3'), 0),
            'SI-16C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_16c2q4'), 0),
            'SI-16C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_16c3q3'), 0),
            'SI-16C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_16c3q4'), 0),
            'SI-16C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_16c4q1'), 0),
            'SI-16C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_16c4q2'), 0),
            'SI-18M1:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_18m1qdb1'), 0),
            'SI-18M1:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_18m1qdb2'), 0),
            'SI-18M1:PS-QFB:DiagStatus-Mon': (self._gwidget('led_18m1qfb'), 0),
            'SI-18M2:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_18m2qdb1'), 0),
            'SI-18M2:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_18m2qdb2'), 0),
            'SI-18M2:PS-QFB:DiagStatus-Mon': (self._gwidget('led_18m2qfb'), 0),
            'SI-18C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_18c1q1'), 0),
            'SI-18C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_18c1q2'), 0),
            'SI-18C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_18c2q3'), 0),
            'SI-18C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_18c2q4'), 0),
            'SI-18C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_18c3q3'), 0),
            'SI-18C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_18c3q4'), 0),
            'SI-18C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_18c4q1'), 0),
            'SI-18C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_18c4q2'), 0),
            'SI-19M1:PS-QDP1:DiagStatus-Mon': (self._gwidget
                                               ('led_19m1qdp1'), 0),
            'SI-19M1:PS-QDP2:DiagStatus-Mon': (self._gwidget
                                               ('led_19m1qdp2'), 0),
            'SI-19M1:PS-QFP:DiagStatus-Mon': (self._gwidget('led_19m1qfp'), 0),
            'SI-19M2:PS-QDP1:DiagStatus-Mon': (self._gwidget
                                               ('led_19m2qdp1'), 0),
            'SI-19M2:PS-QDP2:DiagStatus-Mon': (self._gwidget
                                               ('led_19m2qdp2'), 0),
            'SI-19M2:PS-QFP:DiagStatus-Mon': (self._gwidget('led_19m2qfp'), 0),
            'SI-19C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_19c1q1'), 0),
            'SI-19C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_19c1q2'), 0),
            'SI-19C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_19c2q3'), 0),
            'SI-19C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_19c2q4'), 0),
            'SI-19C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_19c3q3'), 0),
            'SI-19C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_19c3q4'), 0),
            'SI-19C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_19c4q1'), 0),
            'SI-19C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_19c4q2'), 0),
            'SI-20M1:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_20m1qdb1'), 0),
            'SI-20M1:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_20m1qdb2'), 0),
            'SI-20M1:PS-QFB:DiagStatus-Mon': (self._gwidget('led_20m1qfb'), 0),
            'SI-20M2:PS-QDB1:DiagStatus-Mon': (self._gwidget
                                               ('led_20m2qdb1'), 0),
            'SI-20M2:PS-QDB2:DiagStatus-Mon': (self._gwidget
                                               ('led_20m2qdb2'), 0),
            'SI-20M2:PS-QFB:DiagStatus-Mon': (self._gwidget('led_20m2qfb'), 0),
            'SI-20C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_20c1q1'), 0),
            'SI-20C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_20c1q2'), 0),
            'SI-20C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_20c2q3'), 0),
            'SI-20C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_20c2q4'), 0),
            'SI-20C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_20c3q3'), 0),
            'SI-20C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_20c3q4'), 0),
            'SI-20C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_20c4q1'), 0),
            'SI-20C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_20c4q2'), 0),
            'SI-01M1:PS-QDA:DiagStatus-Mon': (self._gwidget('led_01m1qda'), 0),
            'SI-01M1:PS-QFA:DiagStatus-Mon': (self._gwidget('led_01m1qfa'), 0),
            'SI-01M2:PS-QDA:DiagStatus-Mon': (self._gwidget('led_01m2qda'), 0),
            'SI-01M2:PS-QFA:DiagStatus-Mon': (self._gwidget('led_01m2qfa'), 0),
            'SI-01C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_01c1q1'), 0),
            'SI-01C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_01c1q2'), 0),
            'SI-01C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_01c2q3'), 0),
            'SI-01C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_01c2q4'), 0),
            'SI-01C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_01c3q3'), 0),
            'SI-01C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_01c3q4'), 0),
            'SI-01C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_01c4q1'), 0),
            'SI-01C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_01c4q2'), 0),
            'SI-05M1:PS-QDA:DiagStatus-Mon': (self._gwidget('led_05m1qda'), 0),
            'SI-05M1:PS-QFA:DiagStatus-Mon': (self._gwidget('led_05m1qfa'), 0),
            'SI-05M2:PS-QDA:DiagStatus-Mon': (self._gwidget('led_05m2qda'), 0),
            'SI-05M2:PS-QFA:DiagStatus-Mon': (self._gwidget('led_05m2qfa'), 0),
            'SI-05C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_05c1q1'), 0),
            'SI-05C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_05c1q2'), 0),
            'SI-05C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_05c2q3'), 0),
            'SI-05C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_05c2q4'), 0),
            'SI-05C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_05c3q3'), 0),
            'SI-05C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_05c3q4'), 0),
            'SI-05C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_05c4q1'), 0),
            'SI-05C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_05c4q2'), 0),
            'SI-09M1:PS-QDA:DiagStatus-Mon': (self._gwidget('led_09m1qda'), 0),
            'SI-09M1:PS-QFA:DiagStatus-Mon': (self._gwidget('led_09m1qfa'), 0),
            'SI-09M2:PS-QDA:DiagStatus-Mon': (self._gwidget('led_09m2qda'), 0),
            'SI-09M2:PS-QFA:DiagStatus-Mon': (self._gwidget('led_09m2qfa'), 0),
            'SI-09C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_09c1q1'), 0),
            'SI-09C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_09c1q2'), 0),
            'SI-09C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_09c2q3'), 0),
            'SI-09C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_09c2q4'), 0),
            'SI-09C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_09c3q3'), 0),
            'SI-09C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_09c3q4'), 0),
            'SI-09C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_09c4q1'), 0),
            'SI-09C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_09c4q2'), 0),
            'SI-13M1:PS-QDA:DiagStatus-Mon': (self._gwidget('led_13m1qda'), 0),
            'SI-13M1:PS-QFA:DiagStatus-Mon': (self._gwidget('led_13m1qfa'), 0),
            'SI-13M2:PS-QDA:DiagStatus-Mon': (self._gwidget('led_13m2qda'), 0),
            'SI-13M2:PS-QFA:DiagStatus-Mon': (self._gwidget('led_13m2qfa'), 0),
            'SI-13C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_13c1q1'), 0),
            'SI-13C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_13c1q2'), 0),
            'SI-13C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_13c2q3'), 0),
            'SI-13C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_13c2q4'), 0),
            'SI-13C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_13c3q3'), 0),
            'SI-13C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_13c3q4'), 0),
            'SI-13C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_13c4q1'), 0),
            'SI-13C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_13c4q2'), 0),
            'SI-17M1:PS-QDA:DiagStatus-Mon': (self._gwidget('led_17m1qda'), 0),
            'SI-17M1:PS-QFA:DiagStatus-Mon': (self._gwidget('led_17m1qfa'), 0),
            'SI-17M2:PS-QDA:DiagStatus-Mon': (self._gwidget('led_17m2qda'), 0),
            'SI-17M2:PS-QFA:DiagStatus-Mon': (self._gwidget('led_17m2qfa'), 0),
            'SI-17C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_17c1q1'), 0),
            'SI-17C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_17c1q2'), 0),
            'SI-17C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_17c2q3'), 0),
            'SI-17C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_17c2q4'), 0),
            'SI-17C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_17c3q3'), 0),
            'SI-17C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_17c3q4'), 0),
            'SI-17C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_17c4q1'), 0),
            'SI-17C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_17c4q2'), 0),
        }


class Si_ffwcorr(utils.ConnWidgetPVs):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/ffwcorr.ui",
                         "estado")

    def _registrar_grupos(self):
        self.sinais = {
            'SI-14SB:PS-LCH:DiagStatus-Mon': (self._gwidget
                                              ('led_ff14sblch'), 0),
            'SI-14SB:PS-CH-1:DiagStatus-Mon': (self._gwidget
                                               ('led_ff14sbch1'), 0),
            'SI-14SB:PS-CH-2:DiagStatus-Mon': (self._gwidget
                                               ('led_ff14sbch2'), 0),
            'SI-14SB:PS-CV-1:DiagStatus-Mon': (self._gwidget
                                               ('led_ff14sbcv1'), 0),
            'SI-14SB:PS-CV-2:DiagStatus-Mon': (self._gwidget
                                               ('led_ff14sbcv2'), 0),
            'SI-08SB:PS-CH-1:DiagStatus-Mon': (self._gwidget
                                               ('led_ff08sbch1'), 0),
            'SI-08SB:PS-CH-2:DiagStatus-Mon': (self._gwidget
                                               ('led_ff08sbch2'), 0),
            'SI-08SB:PS-CV-1:DiagStatus-Mon': (self._gwidget
                                               ('led_ff08sbcv1'), 0),
            'SI-08SB:PS-CV-2:DiagStatus-Mon': (self._gwidget
                                               ('led_ff08sbcv2'), 0),
            'SI-08SB:PS-LCH:DiagStatus-Mon': (self._gwidget
                                              ('led_ff14sblch'), 0),
            'SI-10SB:PS-CH-1:DiagStatus-Mon': (self._gwidget
                                               ('led_ff10sbch1'), 0),
            'SI-10SB:PS-CH-2:DiagStatus-Mon': (self._gwidget
                                               ('led_ff10sbch2'), 0),
            'SI-10SB:PS-CV-1:DiagStatus-Mon': (self._gwidget
                                               ('led_ff10sbcv1'), 0),
            'SI-10SB:PS-CV-2:DiagStatus-Mon': (self._gwidget
                                               ('led_ff10sbcv2'), 0),
            'SI-10SB:PS-QS-1:DiagStatus-Mon': (self._gwidget
                                               ('led_ff10sbqs1'), 0),
            'SI-10SB:PS-QS-2:DiagStatus-Mon': (self._gwidget
                                               ('led_ff10sbqs2'), 0),
            'SI-01M1:PS-FFCH:DiagStatus-Mon': (self._gwidget
                                               ('led_ff01m1ch'), 0),
            'SI-01M2:PS-FFCH:DiagStatus-Mon': (self._gwidget
                                               ('led_ff01m2ch'), 0),
            'SI-01M1:PS-FFCV:DiagStatus-Mon': (self._gwidget
                                               ('led_ff01m1cv'), 0),
            'SI-01M2:PS-FFCV:DiagStatus-Mon': (self._gwidget
                                               ('led_ff01m2cv'), 0),
        }


class Si_slowcorr(utils.ConnWidgetPVs):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/corrsi.ui",
                         "estado")

    def _registrar_grupos(self):
        self.sinais = {
            'SI-01M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_01m1ch'), 0),
            'SI-01M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_01m2ch'), 0),
            'SI-01C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_01c1ch'), 0),
            'SI-01C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_01c2ch'), 0),
            'SI-01C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_01c3ch'), 0),
            'SI-01C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_01c4ch'), 0),
            'SI-02M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_02m1ch'), 0),
            'SI-02M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_02m2ch'), 0),
            'SI-02C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_02c1ch'), 0),
            'SI-02C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_02c2ch'), 0),
            'SI-02C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_02c3ch'), 0),
            'SI-02C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_02c4ch'), 0),
            'SI-03M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_03m1ch'), 0),
            'SI-03M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_03m2ch'), 0),
            'SI-03C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_03c1ch'), 0),
            'SI-03C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_03c2ch'), 0),
            'SI-03C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_03c3ch'), 0),
            'SI-03C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_03c4ch'), 0),
            'SI-04M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_04m1ch'), 0),
            'SI-04M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_04m2ch'), 0),
            'SI-04C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_04c1ch'), 0),
            'SI-04C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_04c2ch'), 0),
            'SI-04C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_04c3ch'), 0),
            'SI-04C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_04c4ch'), 0),
            'SI-05M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_05m1ch'), 0),
            'SI-05M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_05m2ch'), 0),
            'SI-05C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_05c1ch'), 0),
            'SI-05C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_05c2ch'), 0),
            'SI-05C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_05c3ch'), 0),
            'SI-05C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_05c4ch'), 0),
            'SI-06M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_06m1ch'), 0),
            'SI-06M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_06m2ch'), 0),
            'SI-06C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_06c1ch'), 0),
            'SI-06C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_06c2ch'), 0),
            'SI-06C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_06c3ch'), 0),
            'SI-06C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_06c4ch'), 0),
            'SI-07M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_07m1ch'), 0),
            'SI-07M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_07m2ch'), 0),
            'SI-07C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_07c1ch'), 0),
            'SI-07C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_07c2ch'), 0),
            'SI-07C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_07c3ch'), 0),
            'SI-07C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_07c4ch'), 0),
            'SI-08M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_08m1ch'), 0),
            'SI-08M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_08m2ch'), 0),
            'SI-08C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_08c1ch'), 0),
            'SI-08C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_08c2ch'), 0),
            'SI-08C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_08c3ch'), 0),
            'SI-08C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_08c4ch'), 0),
            'SI-09M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_09m1ch'), 0),
            'SI-09M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_09m2ch'), 0),
            'SI-09C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_09c1ch'), 0),
            'SI-09C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_09c2ch'), 0),
            'SI-09C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_09c3ch'), 0),
            'SI-09C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_09c4ch'), 0),
            'SI-10M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_10m1ch'), 0),
            'SI-10M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_10m2ch'), 0),
            'SI-10C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_10c1ch'), 0),
            'SI-10C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_10c2ch'), 0),
            'SI-10C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_10c3ch'), 0),
            'SI-10C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_10c4ch'), 0),
            'SI-11M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_11m1ch'), 0),
            'SI-11M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_11m2ch'), 0),
            'SI-11C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_11c1ch'), 0),
            'SI-11C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_11c2ch'), 0),
            'SI-11C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_11c3ch'), 0),
            'SI-11C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_11c4ch'), 0),
            'SI-12M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_12m1ch'), 0),
            'SI-12M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_12m2ch'), 0),
            'SI-12C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_12c1ch'), 0),
            'SI-12C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_12c2ch'), 0),
            'SI-12C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_12c3ch'), 0),
            'SI-12C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_12c4ch'), 0),
            'SI-13M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_13m1ch'), 0),
            'SI-13M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_13m2ch'), 0),
            'SI-13C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_13c1ch'), 0),
            'SI-13C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_13c2ch'), 0),
            'SI-13C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_13c3ch'), 0),
            'SI-13C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_13c4ch'), 0),
            'SI-14M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_14m1ch'), 0),
            'SI-14M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_14m2ch'), 0),
            'SI-14C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_14c1ch'), 0),
            'SI-14C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_14c2ch'), 0),
            'SI-14C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_14c3ch'), 0),
            'SI-14C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_14c4ch'), 0),
            'SI-15M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_15m1ch'), 0),
            'SI-15M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_15m2ch'), 0),
            'SI-15C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_15c1ch'), 0),
            'SI-15C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_15c2ch'), 0),
            'SI-15C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_15c3ch'), 0),
            'SI-15C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_15c4ch'), 0),
            'SI-16M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_16m1ch'), 0),
            'SI-16M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_16m2ch'), 0),
            'SI-16C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_16c1ch'), 0),
            'SI-16C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_16c2ch'), 0),
            'SI-16C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_16c3ch'), 0),
            'SI-16C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_16c4ch'), 0),
            'SI-17M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_17m1ch'), 0),
            'SI-17M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_17m2ch'), 0),
            'SI-17C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_17c1ch'), 0),
            'SI-17C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_17c2ch'), 0),
            'SI-17C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_17c3ch'), 0),
            'SI-17C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_17c4ch'), 0),
            'SI-18M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_18m1ch'), 0),
            'SI-18M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_18m2ch'), 0),
            'SI-18C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_18c1ch'), 0),
            'SI-18C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_18c2ch'), 0),
            'SI-18C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_18c3ch'), 0),
            'SI-18C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_18c4ch'), 0),
            'SI-19M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_19m1ch'), 0),
            'SI-19M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_19m2ch'), 0),
            'SI-19C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_19c1ch'), 0),
            'SI-19C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_19c2ch'), 0),
            'SI-19C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_19c3ch'), 0),
            'SI-19C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_19c4ch'), 0),
            'SI-20M1:PS-CH:DiagStatus-Mon': (self._gwidget('led_20m1ch'), 0),
            'SI-20M2:PS-CH:DiagStatus-Mon': (self._gwidget('led_20m2ch'), 0),
            'SI-20C1:PS-CH:DiagStatus-Mon': (self._gwidget('led_20c1ch'), 0),
            'SI-20C2:PS-CH:DiagStatus-Mon': (self._gwidget('led_20c2ch'), 0),
            'SI-20C3:PS-CH:DiagStatus-Mon': (self._gwidget('led_20c3ch'), 0),
            'SI-20C4:PS-CH:DiagStatus-Mon': (self._gwidget('led_20c4ch'), 0),
            'SI-01M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_01m1cv'), 0),
            'SI-01M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_01m2cv'), 0),
            'SI-01C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_01c1cv'), 0),
            'SI-01C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_01c2cv1'), 0),
            'SI-01C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_01c2cv2'), 0),
            'SI-01C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_01c3cv1'), 0),
            'SI-01C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_01c3cv2'), 0),
            'SI-01C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_01c4cv'), 0),
            'SI-02M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_02m1cv'), 0),
            'SI-02M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_02m2cv'), 0),
            'SI-02C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_02c1cv'), 0),
            'SI-02C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_02c2cv1'), 0),
            'SI-02C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_02c2cv2'), 0),
            'SI-02C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_02c3cv1'), 0),
            'SI-02C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_02c3cv2'), 0),
            'SI-02C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_02c4cv'), 0),
            'SI-03M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_03m1cv'), 0),
            'SI-03M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_03m2cv'), 0),
            'SI-03C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_03c1cv'), 0),
            'SI-03C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_03c2cv1'), 0),
            'SI-03C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_03c2cv2'), 0),
            'SI-03C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_03c3cv1'), 0),
            'SI-03C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_03c3cv2'), 0),
            'SI-03C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_03c4cv'), 0),
            'SI-04M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_04m1cv'), 0),
            'SI-04M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_04m2cv'), 0),
            'SI-04C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_04c1cv'), 0),
            'SI-04C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_04c2cv1'), 0),
            'SI-04C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_04c2cv2'), 0),
            'SI-04C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_04c3cv1'), 0),
            'SI-04C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_04c3cv2'), 0),
            'SI-04C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_04c4cv'), 0),
            'SI-05M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_05m1cv'), 0),
            'SI-05M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_05m2cv'), 0),
            'SI-05C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_05c1cv'), 0),
            'SI-05C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_05c2cv1'), 0),
            'SI-05C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_05c2cv2'), 0),
            'SI-05C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_05c3cv1'), 0),
            'SI-05C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_05c3cv2'), 0),
            'SI-05C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_05c4cv'), 0),
            'SI-06M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_06m1cv'), 0),
            'SI-06M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_06m2cv'), 0),
            'SI-06C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_06c1cv'), 0),
            'SI-06C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_06c2cv1'), 0),
            'SI-06C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_06c2cv2'), 0),
            'SI-06C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_06c3cv1'), 0),
            'SI-06C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_06c3cv2'), 0),
            'SI-06C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_06c4cv'), 0),
            'SI-07M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_07m1cv'), 0),
            'SI-07M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_07m2cv'), 0),
            'SI-07C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_07c1cv'), 0),
            'SI-07C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_07c2cv1'), 0),
            'SI-07C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_07c2cv2'), 0),
            'SI-07C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_07c3cv1'), 0),
            'SI-07C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_07c3cv2'), 0),
            'SI-07C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_07c4cv'), 0),
            'SI-08M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_08m1cv'), 0),
            'SI-08M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_08m2cv'), 0),
            'SI-08C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_08c1cv'), 0),
            'SI-08C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_08c2cv1'), 0),
            'SI-08C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_08c2cv2'), 0),
            'SI-08C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_08c3cv1'), 0),
            'SI-08C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_08c3cv2'), 0),
            'SI-08C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_08c4cv'), 0),
            'SI-09M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_09m1cv'), 0),
            'SI-09M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_09m2cv'), 0),
            'SI-09C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_09c1cv'), 0),
            'SI-09C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_09c2cv1'), 0),
            'SI-09C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_09c2cv2'), 0),
            'SI-09C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_09c3cv1'), 0),
            'SI-09C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_09c3cv2'), 0),
            'SI-09C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_09c4cv'), 0),
            'SI-10M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_10m1cv'), 0),
            'SI-10M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_10m2cv'), 0),
            'SI-10C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_10c1cv'), 0),
            'SI-10C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_10c2cv1'), 0),
            'SI-10C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_10c2cv2'), 0),
            'SI-10C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_10c3cv1'), 0),
            'SI-10C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_10c3cv2'), 0),
            'SI-10C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_10c4cv'), 0),
            'SI-11M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_11m1cv'), 0),
            'SI-11M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_11m2cv'), 0),
            'SI-11C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_11c1cv'), 0),
            'SI-11C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_11c2cv1'), 0),
            'SI-11C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_11c2cv2'), 0),
            'SI-11C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_11c3cv1'), 0),
            'SI-11C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_11c3cv2'), 0),
            'SI-11C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_11c4cv'), 0),
            'SI-12M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_12m1cv'), 0),
            'SI-12M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_12m2cv'), 0),
            'SI-12C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_12c1cv'), 0),
            'SI-12C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_12c2cv1'), 0),
            'SI-12C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_12c2cv2'), 0),
            'SI-12C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_12c3cv1'), 0),
            'SI-12C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_12c3cv2'), 0),
            'SI-12C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_12c4cv'), 0),
            'SI-13M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_13m1cv'), 0),
            'SI-13M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_13m2cv'), 0),
            'SI-13C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_13c1cv'), 0),
            'SI-13C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_13c2cv1'), 0),
            'SI-13C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_13c2cv2'), 0),
            'SI-13C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_13c3cv1'), 0),
            'SI-13C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_13c3cv2'), 0),
            'SI-13C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_13c4cv'), 0),
            'SI-14M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_14m1cv'), 0),
            'SI-14M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_14m2cv'), 0),
            'SI-14C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_14c1cv'), 0),
            'SI-14C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_14c2cv1'), 0),
            'SI-14C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_14c2cv2'), 0),
            'SI-14C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_14c3cv1'), 0),
            'SI-14C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_14c3cv2'), 0),
            'SI-14C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_14c4cv'), 0),
            'SI-15M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_15m1cv'), 0),
            'SI-15M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_15m2cv'), 0),
            'SI-15C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_15c1cv'), 0),
            'SI-15C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_15c2cv1'), 0),
            'SI-15C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_15c2cv2'), 0),
            'SI-15C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_15c3cv1'), 0),
            'SI-15C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_15c3cv2'), 0),
            'SI-15C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_15c4cv'), 0),
            'SI-16M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_16m1cv'), 0),
            'SI-16M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_16m2cv'), 0),
            'SI-16C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_16c1cv'), 0),
            'SI-16C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_16c2cv1'), 0),
            'SI-16C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_16c2cv2'), 0),
            'SI-16C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_16c3cv1'), 0),
            'SI-16C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_16c3cv2'), 0),
            'SI-16C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_16c4cv'), 0),
            'SI-17M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_17m1cv'), 0),
            'SI-17M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_17m2cv'), 0),
            'SI-17C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_17c1cv'), 0),
            'SI-17C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_17c2cv1'), 0),
            'SI-17C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_17c2cv2'), 0),
            'SI-17C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_17c3cv1'), 0),
            'SI-17C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_17c3cv2'), 0),
            'SI-17C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_17c4cv'), 0),
            'SI-18M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_18m1cv'), 0),
            'SI-18M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_18m2cv'), 0),
            'SI-18C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_18c1cv'), 0),
            'SI-18C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_18c2cv1'), 0),
            'SI-18C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_18c2cv2'), 0),
            'SI-18C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_18c3cv1'), 0),
            'SI-18C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_18c3cv2'), 0),
            'SI-18C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_18c4cv'), 0),
            'SI-19M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_19m1cv'), 0),
            'SI-19M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_19m2cv'), 0),
            'SI-19C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_19c1cv'), 0),
            'SI-19C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_19c2cv1'), 0),
            'SI-19C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_19c2cv2'), 0),
            'SI-19C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_19c3cv1'), 0),
            'SI-19C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_19c3cv2'), 0),
            'SI-19C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_19c4cv'), 0),
            'SI-20M1:PS-CV:DiagStatus-Mon': (self._gwidget('led_20m1cv'), 0),
            'SI-20M2:PS-CV:DiagStatus-Mon': (self._gwidget('led_20m2cv'), 0),
            'SI-20C1:PS-CV:DiagStatus-Mon': (self._gwidget('led_20c1cv'), 0),
            'SI-20C2:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_20c2cv1'), 0),
            'SI-20C2:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_20c2cv2'), 0),
            'SI-20C3:PS-CV-1:DiagStatus-Mon':
            (self._gwidget('led_20c3cv1'), 0),
            'SI-20C3:PS-CV-2:DiagStatus-Mon':
            (self._gwidget('led_20c3cv2'), 0),
            'SI-20C4:PS-CV:DiagStatus-Mon': (self._gwidget('led_20c4cv'), 0),
        }


class Si_corrfast(utils.ConnWidgetPVs):
    """."""

    def __init__(self, janela_opr, botao_menu):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/fcorrsi.ui",
                         "estado")

    def _registrar_grupos(self):
        self.sinais = {
            'SI-01C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch01c2'), 0),
            'SI-01C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch01c3'), 0),
            # 'SI-01M1:PS-FCH:DiagStatus-Mon':
            # (self._gwidget('ledfch01m1'), 0),
            # 'SI-01M2:PS-FCH:DiagStatus-Mon':
            # (self._gwidget('ledfch01m2'), 0),
            'SI-02C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch02c2'), 0),
            'SI-02C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch02c3'), 0),
            'SI-02M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch02m1'), 0),
            'SI-02M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch02m2'), 0),
            'SI-03C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch03c2'), 0),
            'SI-03C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch03c3'), 0),
            'SI-03M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch03m1'), 0),
            'SI-03M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch03m2'), 0),
            'SI-04C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch04c2'), 0),
            'SI-04C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch04c3'), 0),
            'SI-04M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch04m1'), 0),
            'SI-04M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch04m2'), 0),
            'SI-05C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch05c2'), 0),
            'SI-05C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch05c3'), 0),
            'SI-05M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch05m1'), 0),
            'SI-05M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch05m2'), 0),
            'SI-06C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch06c2'), 0),
            'SI-06C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch06c3'), 0),
            'SI-06M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch06m1'), 0),
            'SI-06M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch06m2'), 0),
            'SI-07C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch07c2'), 0),
            'SI-07C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch07c3'), 0),
            'SI-07M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch07m1'), 0),
            'SI-07M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch07m2'), 0),
            'SI-08C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch08c2'), 0),
            'SI-08C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch08c3'), 0),
            'SI-08M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch08m1'), 0),
            'SI-08M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch08m2'), 0),
            'SI-09C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch09c2'), 0),
            'SI-09C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch09c3'), 0),
            'SI-09M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch09m1'), 0),
            'SI-09M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch09m2'), 0),
            'SI-10C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch10c2'), 0),
            'SI-10C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch10c3'), 0),
            'SI-10M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch10m1'), 0),
            'SI-10M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch10m2'), 0),
            'SI-11C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch11c2'), 0),
            'SI-11C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch11c3'), 0),
            'SI-11M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch11m1'), 0),
            'SI-11M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch11m2'), 0),
            'SI-12C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch12c2'), 0),
            'SI-12C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch12c3'), 0),
            'SI-12M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch12m1'), 0),
            'SI-12M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch12m2'), 0),
            'SI-13C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch13c2'), 0),
            'SI-13C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch13c3'), 0),
            'SI-13M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch13m1'), 0),
            'SI-13M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch13m2'), 0),
            'SI-14C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch14c2'), 0),
            'SI-14C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch14c3'), 0),
            'SI-14M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch14m1'), 0),
            'SI-14M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch14m2'), 0),
            'SI-15C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch15c2'), 0),
            'SI-15C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch15c3'), 0),
            'SI-15M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch15m1'), 0),
            'SI-15M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch15m2'), 0),
            'SI-16C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch16c2'), 0),
            'SI-16C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch16c3'), 0),
            'SI-16M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch16m1'), 0),
            'SI-16M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch16m2'), 0),
            'SI-17C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch17c2'), 0),
            'SI-17C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch17c3'), 0),
            'SI-17M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch17m1'), 0),
            'SI-17M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch17m2'), 0),
            'SI-18C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch18c2'), 0),
            'SI-18C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch18c3'), 0),
            'SI-18M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch18m1'), 0),
            'SI-18M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch18m2'), 0),
            'SI-19C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch19c2'), 0),
            'SI-19C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch19c3'), 0),
            'SI-19M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch19m1'), 0),
            'SI-19M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch19m2'), 0),
            'SI-20C2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch20c2'), 0),
            'SI-20C3:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch20c3'), 0),
            'SI-20M1:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch20m1'), 0),
            'SI-20M2:PS-FCH:DiagStatus-Mon': (self._gwidget('ledfch20m2'), 0),
            'SI-01C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv01c2'), 0),
            'SI-01C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv01c3'), 0),
            # 'SI-01M1:PS-FCV:DiagStatus-Mon': (self.gwidget('ledfcv01m1'), 0),
            # 'SI-01M2:PS-FCV:DiagStatus-Mon': (self.gwidget('ledfcv01m2'), 0),
            'SI-02C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv02c2'), 0),
            'SI-02C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv02c3'), 0),
            'SI-02M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv02m1'), 0),
            'SI-02M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv02m2'), 0),
            'SI-03C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv03c2'), 0),
            'SI-03C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv03c3'), 0),
            'SI-03M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv03m1'), 0),
            'SI-03M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv03m2'), 0),
            'SI-04C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv04c2'), 0),
            'SI-04C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv04c3'), 0),
            'SI-04M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv04m1'), 0),
            'SI-04M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv04m2'), 0),
            'SI-05C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv05c2'), 0),
            'SI-05C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv05c3'), 0),
            'SI-05M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv05m1'), 0),
            'SI-05M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv05m2'), 0),
            'SI-06C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv06c2'), 0),
            'SI-06C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv06c3'), 0),
            'SI-06M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv06m1'), 0),
            'SI-06M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv06m2'), 0),
            'SI-07C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv07c2'), 0),
            'SI-07C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv07c3'), 0),
            'SI-07M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv07m1'), 0),
            'SI-07M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv07m2'), 0),
            'SI-08C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv08c2'), 0),
            'SI-08C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv08c3'), 0),
            'SI-08M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv08m1'), 0),
            'SI-08M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv08m2'), 0),
            'SI-09C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv09c2'), 0),
            'SI-09C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv09c3'), 0),
            'SI-09M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv09m1'), 0),
            'SI-09M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv09m2'), 0),
            'SI-10C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv10c2'), 0),
            'SI-10C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv10c3'), 0),
            'SI-10M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv10m1'), 0),
            'SI-10M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv10m2'), 0),
            'SI-11C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv11c2'), 0),
            'SI-11C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv11c3'), 0),
            'SI-11M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv11m1'), 0),
            'SI-11M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv11m2'), 0),
            'SI-12C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv12c2'), 0),
            'SI-12C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv12c3'), 0),
            'SI-12M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv12m1'), 0),
            'SI-12M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv12m2'), 0),
            'SI-13C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv13c2'), 0),
            'SI-13C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv13c3'), 0),
            'SI-13M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv13m1'), 0),
            'SI-13M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv13m2'), 0),
            'SI-14C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv14c2'), 0),
            'SI-14C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv14c3'), 0),
            'SI-14M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv14m1'), 0),
            'SI-14M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv14m2'), 0),
            'SI-15C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv15c2'), 0),
            'SI-15C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv15c3'), 0),
            'SI-15M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv15m1'), 0),
            'SI-15M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv15m2'), 0),
            'SI-16C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv16c2'), 0),
            'SI-16C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv16c3'), 0),
            'SI-16M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv16m1'), 0),
            'SI-16M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv16m2'), 0),
            'SI-17C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv17c2'), 0),
            'SI-17C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv17c3'), 0),
            'SI-17M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv17m1'), 0),
            'SI-17M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv17m2'), 0),
            'SI-18C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv18c2'), 0),
            'SI-18C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv18c3'), 0),
            'SI-18M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv18m1'), 0),
            'SI-18M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv18m2'), 0),
            'SI-19C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv19c2'), 0),
            'SI-19C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv19c3'), 0),
            'SI-19M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv19m1'), 0),
            'SI-19M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv19m2'), 0),
            'SI-20C2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv20c2'), 0),
            'SI-20C3:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv20c3'), 0),
            'SI-20M1:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv20m1'), 0),
            'SI-20M2:PS-FCV:DiagStatus-Mon': (self._gwidget('ledfcv20m2'), 0),
        }


class Blocosips:
    """Gerencia o bloco de fontes do Anel e atualiza a label sips."""

    def __init__(self, janela_opr):
        """."""
        janela_opr.alarmsips.clicked.connect(self.aba_sips)
        self.janela_opr = janela_opr
        self.subjanelas = []

        # Instancia as subjanelas passando o botão correto
        self.psfamilysi = Si_psfamily(janela_opr, janela_opr.btnpsfamilysi)
        self.skewquad = Si_skewquad(janela_opr, janela_opr.btnskewquad)
        self.trims = Si_trims(janela_opr, janela_opr.btntrims)
        self.ffwcorr = Si_ffwcorr(janela_opr, janela_opr.btnffwcorr)
        self.corrsi = Si_slowcorr(janela_opr, janela_opr.btncorrsi)
        self.fcorrsi = Si_corrfast(janela_opr, janela_opr.btnfcorrsi)

        # Adiciona todas as subjanelas à lista
        self.subjanelas.extend([
            self.psfamilysi,
            self.skewquad,
            self.trims,
            self.ffwcorr,
            self.corrsi,
            self.fcorrsi,

        ])

        # Configura cada subjanela
        for sub in self.subjanelas:
            sub.configurar_sistema()

    def atualizar_grupo(self):
        """Atualiza todas as subjanelas e a label alarmsips."""
        falha_detectada = False
        for sub in self.subjanelas:
            sub.atualizar_status()
            falha_detectada |= not sub.estado_ok

        # Atualiza a label principal do bloco SIPS
        alarme_widget = self.janela_opr.findChild(QtWidgets.QPushButton,
                                                  "alarmsips")
        if alarme_widget:
            cor = "rgb(0, 168, 0)" if not falha_detectada else "rgb(207, 0, 0)"
            alarme_widget.setStyleSheet(f"background-color: {cor};")
            alarme_widget.repaint()
            QtWidgets.QApplication.processEvents()
            alarme_widget.update()

    def aba_sips(self):
        """."""
        try:
            self.janela_opr.janela_opr.setCurrentIndex(6)
        except Exception as e:
            logging.error(f"Erro ao mudar para aba LTB: {e}")
