"""Logica das fontes do Anel de Armazenamento."""
from utils import AlarmDelayController
import utils
import logging


# SISTEMAS DE TEMPERATURA

class Si_dclinks(utils.ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura Booster."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/tempdclinks.ui",
                         "temp")

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        self.sinais = {
            "Dipolo_igbtt": {
                'PA-RaPSD01:PS-DCLink-1A:IGBTT-Mon':
                (self._gwidget('led1aigbt_01'), 50, 59),
                'PA-RaPSD01:PS-DCLink-1B:IGBTT-Mon':
                (self._gwidget('led1bigbt_01'), 50, 60),
                'PA-RaPSD01:PS-DCLink-3A:IGBTT-Mon':
                (self._gwidget('led3aigbt_01'), 50, 60),
                'PA-RaPSD01:PS-DCLink-3B:IGBTT-Mon':
                (self._gwidget('led3bigbt_01'), 45, 55),
                'PA-RaPSD03:PS-DCLink-2A:IGBTT-Mon':
                (self._gwidget('led2aigbt_03'), 45, 55),
                'PA-RaPSD03:PS-DCLink-2B:IGBTT-Mon':
                (self._gwidget('led2bigbt_03'), 46, 56),
                'PA-RaPSD03:PS-DCLink-4A:IGBTT-Mon':
                (self._gwidget('led4aigbt_03'), 46, 56),
                'PA-RaPSD03:PS-DCLink-4B:IGBTT-Mon':
                (self._gwidget('led4bigbt_03'), 45, 55),
                'PA-RaPSD05:PS-DCLink-1A:IGBTT-Mon':
                (self._gwidget('led1aigbt_05'), 45, 55),
                'PA-RaPSD05:PS-DCLink-1B:IGBTT-Mon':
                (self._gwidget('led1bigbt_05'), 46, 56),
                'PA-RaPSD05:PS-DCLink-3A:IGBTT-Mon':
                (self._gwidget('led3aigbt_05'), 46, 56),
                'PA-RaPSD05:PS-DCLink-3B:IGBTT-Mon':
                (self._gwidget('led3bigbt_05'), 45, 55),
                'PA-RaPSD07:PS-DCLink-2A:IGBTT-Mon':
                (self._gwidget('led2aigbt_07'), 45, 55),
                'PA-RaPSD07:PS-DCLink-2B:IGBTT-Mon':
                (self._gwidget('led2bigbt_07'), 51, 61),
                'PA-RaPSD07:PS-DCLink-4A:IGBTT-Mon':
                (self._gwidget('led4aigbt_07'), 51, 61),
                'PA-RaPSD07:PS-DCLink-4B:IGBTT-Mon':
                (self._gwidget('led4bigbt_07'), 46, 56),
            },
            "Dipolo_rectifiert": {
                'PA-RaPSD01:PS-DCLink-1A:RectifierT-Mon':
                (self._gwidget('led1arectifier_01'), 39, 49),
                'PA-RaPSD01:PS-DCLink-1B:RectifierT-Mon':
                (self._gwidget('led1brectifier_01'), 39, 49),
                'PA-RaPSD01:PS-DCLink-3A:RectifierT-Mon':
                (self._gwidget('led3arectifier_01'), 39, 49),
                'PA-RaPSD01:PS-DCLink-3B:RectifierT-Mon':
                (self._gwidget('led3brectifier_01'), 40, 50),
                'PA-RaPSD03:PS-DCLink-2A:RectifierT-Mon':
                (self._gwidget('led2arectifier_03'), 39, 49),
                'PA-RaPSD03:PS-DCLink-2B:RectifierT-Mon':
                (self._gwidget('led2brectifier_03'), 40, 50),
                'PA-RaPSD03:PS-DCLink-4A:RectifierT-Mon':
                (self._gwidget('led4arectifier_03'), 40, 50),
                'PA-RaPSD03:PS-DCLink-4B:RectifierT-Mon':
                (self._gwidget('led4brectifier_03'), 43, 53),
                'PA-RaPSD05:PS-DCLink-1A:RectifierT-Mon':
                (self._gwidget('led1arectifier_05'), 41, 51),
                'PA-RaPSD05:PS-DCLink-1B:RectifierT-Mon':
                (self._gwidget('led1brectifier_05'), 41, 51),
                'PA-RaPSD05:PS-DCLink-3A:RectifierT-Mon':
                (self._gwidget('led3arectifier_05'), 41, 51),
                'PA-RaPSD05:PS-DCLink-3B:RectifierT-Mon':
                (self._gwidget('led3brectifier_05'), 41, 51),
                'PA-RaPSD07:PS-DCLink-2A:RectifierT-Mon':
                (self._gwidget('led2arectifier_07'), 40, 50),
                'PA-RaPSD07:PS-DCLink-2B:RectifierT-Mon':
                (self._gwidget('led2brectifier_07'), 39, 49),
                'PA-RaPSD07:PS-DCLink-4A:RectifierT-Mon':
                (self._gwidget('led4arectifier_07'), 38, 48),
                'PA-RaPSD07:PS-DCLink-4B:RectifierT-Mon':
                (self._gwidget('led4brectifier_07'), 44, 54),
            },
            "Dipolo_pcbt": {
                'PA-RaPSD01:PS-DCLink-1A:PCBT-Mon':
                (self._gwidget('led1apcb_01'), 33, 43),
                'PA-RaPSD01:PS-DCLink-1B:PCBT-Mon':
                (self._gwidget('led1bpcb_01'), 45, 55),
                'PA-RaPSD01:PS-DCLink-3A:PCBT-Mon':
                (self._gwidget('led3apcb_01'), 46, 56),
                'PA-RaPSD01:PS-DCLink-3B:PCBT-Mon':
                (self._gwidget('led3bpcb_01'), 42, 52),
                'PA-RaPSD03:PS-DCLink-2A:PCBT-Mon':
                (self._gwidget('led2apcb_03'), 21, 31),
                'PA-RaPSD03:PS-DCLink-2B:PCBT-Mon':
                (self._gwidget('led2bpcb_03'), 30, 40),
                'PA-RaPSD03:PS-DCLink-4A:PCBT-Mon':
                (self._gwidget('led4apcb_03'), 25, 35),
                'PA-RaPSD03:PS-DCLink-4B:PCBT-Mon':
                (self._gwidget('led4bpcb_03'), 25, 35),
                'PA-RaPSD05:PS-DCLink-1A:PCBT-Mon':
                (self._gwidget('led1apcb_05'), 21, 31),
                'PA-RaPSD05:PS-DCLink-1B:PCBT-Mon':
                (self._gwidget('led1bpcb_05'), 27, 37),
                'PA-RaPSD05:PS-DCLink-3A:PCBT-Mon':
                (self._gwidget('led3apcb_05'), 31, 41),
                'PA-RaPSD05:PS-DCLink-3B:PCBT-Mon':
                (self._gwidget('led3bpcb_05'), 21, 31),
                'PA-RaPSD07:PS-DCLink-2A:PCBT-Mon':
                (self._gwidget('led2apcb_07'), 29, 39),
                'PA-RaPSD07:PS-DCLink-2B:PCBT-Mon':
                (self._gwidget('led2bpcb_07'), 38, 48),
                'PA-RaPSD07:PS-DCLink-4A:PCBT-Mon':
                (self._gwidget('led4apcb_07'), 39, 49),
                'PA-RaPSD07:PS-DCLink-4B:PCBT-Mon':
                (self._gwidget('led4bpcb_07'), 32, 42),
            },
            "Quadrupolo_igbtt": {
                'PA-RaPSA01:PS-DCLink-QFAP:IGBTT-Mon':
                (self._gwidget('led01qfap_igbt'), 32, 42),
                'PA-RaPSA01:PS-DCLink-QFB:IGBTT-Mon':
                (self._gwidget('led01qfb_igbt'), 32, 42),
                'PA-RaPSA03:PS-DCLink-QDAP:IGBTT-Mon':
                (self._gwidget('led03qdap_igbt'), 20, 30),
                'PA-RaPSA04:PS-DCLink-QDB:IGBTT-Mon':
                (self._gwidget('led04qdb_igbt'), 25, 35),
                'PA-RaPSA06:PS-DCLink-Q13A:IGBTT-Mon':
                (self._gwidget('led06q13a_igbt'), 23, 33),
                'PA-RaPSA06:PS-DCLink-Q13B:IGBTT-Mon':
                (self._gwidget('led06q13b_igbt'), 28, 38),
                'PA-RaPSA06:PS-DCLink-Q13C:IGBTT-Mon':
                (self._gwidget('led06q13c_igbt'), 27, 37),
                'PA-RaPSA07:PS-DCLink-Q24A:IGBTT-Mon':
                (self._gwidget('led07q24a_igbt'), 43, 53),
                'PA-RaPSA07:PS-DCLink-Q24B:IGBTT-Mon':
                (self._gwidget('led07q24b_igbt'), 48, 58),
                'PA-RaPSA07:PS-DCLink-Q24C:IGBTT-Mon':
                (self._gwidget('led07q24c_igbt'), 43, 53),
            },
            "Quadrupolo_rectifiert": {
                'PA-RaPSA01:PS-DCLink-QFAP:RectifierT-Mon':
                (self._gwidget('led01qfap_rectifier'), 33, 43),
                'PA-RaPSA01:PS-DCLink-QFB:RectifierT-Mon':
                (self._gwidget('led01qfb_rectifier'), 34, 44),
                'PA-RaPSA03:PS-DCLink-QDAP:RectifierT-Mon':
                (self._gwidget('led03qdap_rectifier'), 22, 33),
                'PA-RaPSA04:PS-DCLink-QDB:RectifierT-Mon':
                (self._gwidget('led04qdb_rectifier'), 27, 37),
                'PA-RaPSA06:PS-DCLink-Q13A:RectifierT-Mon':
                (self._gwidget('led06q13a_rectifier'), 21, 31),
                'PA-RaPSA06:PS-DCLink-Q13B:RectifierT-Mon':
                (self._gwidget('led06q13b_rectifier'), 23, 33),
                'PA-RaPSA06:PS-DCLink-Q13C:RectifierT-Mon':
                (self._gwidget('led06q13c_rectifier'), 21, 31),
                'PA-RaPSA07:PS-DCLink-Q24A:RectifierT-Mon':
                (self._gwidget('led07q24a_rectifier'), 28, 38),
                'PA-RaPSA07:PS-DCLink-Q24B:RectifierT-Mon':
                (self._gwidget('led07q24b_rectifier'), 28, 38),
                'PA-RaPSA07:PS-DCLink-Q24C:RectifierT-Mon':
                (self._gwidget('led07q24c_rectifier'), 28, 38),
            },
            "Quadrupolo_pcbt": {
                'PA-RaPSA01:PS-DCLink-QFAP:PCBT-Mon':
                (self._gwidget('led01qfap_pcb'), 22, 32),
                'PA-RaPSA01:PS-DCLink-QFB:PCBT-Mon':
                (self._gwidget('led01qfb_pcb'), 21, 31),
                'PA-RaPSA03:PS-DCLink-QDAP:PCBT-Mon':
                (self._gwidget('led03qdap_pcb'), 34, 44),
                'PA-RaPSA04:PS-DCLink-QDB:PCBT-Mon':
                (self._gwidget('led04qdb_pcb'), 35, 45),
                'PA-RaPSA06:PS-DCLink-Q13A:PCBT-Mon':
                (self._gwidget('led06q13a_pcb'), 32, 42),
                'PA-RaPSA06:PS-DCLink-Q13B:PCBT-Mon':
                (self._gwidget('led06q13b_pcb'), 36, 46),
                'PA-RaPSA06:PS-DCLink-Q13C:PCBT-Mon':
                (self._gwidget('led06q13c_pcb'), 35, 45),
                'PA-RaPSA07:PS-DCLink-Q24A:PCBT-Mon':
                (self._gwidget('led07q24a_pcb'), 40, 50),
                'PA-RaPSA07:PS-DCLink-Q24B:PCBT-Mon':
                (self._gwidget('led07q24b_pcb'), 42, 52),
                'PA-RaPSA07:PS-DCLink-Q24C:PCBT-Mon':
                (self._gwidget('led07q24c_pcb'), 42, 52),
            },
            "SextFoc_ibgtt": {
                'PA-RaPSB03:PS-DCLink-SFAP0:IGBTT-Mon':
                (self._gwidget('led03sfap0_igbt'), 16, 26),
                'PA-RaPSB03:PS-DCLink-SFB0:IGBTT-Mon':
                (self._gwidget('led03sfb0_igbt'), 15, 25),
                'PA-RaPSB07:PS-DCLink-SFA2SDP1:IGBTT-Mon':
                (self._gwidget('led07sfa2dp1_igbt'), 24, 34),
                'PA-RaPSB08:PS-DCLink-SFB1:IGBTT-Mon':
                (self._gwidget('led08sfb1_igbt'), 34, 44),
                'PA-RaPSB10:PS-DCLink-SFP12:IGBTT-Mon':
                (self._gwidget('led10sfp12_igbt'), 33, 43),
                'PA-RaPSB10:PS-DCLink-SFB2:IGBTT-Mon':
                (self._gwidget('led10sfb2_igbt'), 27, 37),
            },
            "SextFoc_rectifiert": {
                'PA-RaPSB03:PS-DCLink-SFAP0:RectifierT-Mon':
                (self._gwidget('led03sfap0_rectifier'), 16, 26),
                'PA-RaPSB03:PS-DCLink-SFB0:RectifierT-Mon':
                (self._gwidget('led03sfb0_rectifier'), 12, 22),
                'PA-RaPSB07:PS-DCLink-SFA2SDP1:RectifierT-Mon':
                (self._gwidget('led07sfa2dp1_rectifier'), 26, 36),
                'PA-RaPSB08:PS-DCLink-SFB1:RectifierT-Mon':
                (self._gwidget('led08sfb1_rectifier'), 28, 38),
                'PA-RaPSB10:PS-DCLink-SFP12:RectifierT-Mon':
                (self._gwidget('led10sfp12_rectifier'), 29, 39.),
                'PA-RaPSB10:PS-DCLink-SFB2:RectifierT-Mon':
                (self._gwidget('led10sfb2_rectifier'), 23, 33),
            },
            "SextFoc_pcbt": {
                'PA-RaPSB03:PS-DCLink-SFB0:PCBT-Mon':
                (self._gwidget('led03sfb0_pcb'), 32, 42),
                'PA-RaPSB03:PS-DCLink-SFAP0:PCBT-Mon':
                (self._gwidget('led03sfap0_pcb'), 18, 28),
                'PA-RaPSB07:PS-DCLink-SFA2SDP1:PCBT-Mon':
                (self._gwidget('led07sfa2sdp1_pcb'), 22, 32),
                'PA-RaPSB08:PS-DCLink-SFB1:PCBT-Mon':
                (self._gwidget('led08sfb1_pcb'), 37, 47),
                'PA-RaPSB10:PS-DCLink-SFB2:PCBT-Mon':
                (self._gwidget('led10sfb2_pcb'), 35, 45),
                'PA-RaPSB10:PS-DCLink-SFP12:PCBT-Mon':
                (self._gwidget('led10sfp12_pcb'), 21, 31),
            },
            "SextDef_igbtt": {
                'PA-RaPSB01:PS-DCLink-SDB0:IGBTT-Mon':
                (self._gwidget('ledsdb0_igbt'), 13, 23),
                'PA-RaPSB01:PS-DCLink-SDAP0:IGBTT-Mon':
                (self._gwidget('ledsdap0_igbt'), 16, 26),
                'PA-RaPSB04:PS-DCLink-SDA12:IGBTT-Mon':
                (self._gwidget('ledsda12_igbt'), 17, 27),
                'PA-RaPSB04:PS-DCLink-SDB1:IGBTT-Mon':
                (self._gwidget('ledsdb1_igbt'), 16, 26),
                'PA-RaPSB05:PS-DCLink-SDA3SFA1:IGBTT-Mon':
                (self._gwidget('ledsda3sfa1_igbt'), 23, 33),
                'PA-RaPSB05:PS-DCLink-SDB2:IGBTT-Mon':
                (self._gwidget('ledsdb2_igbt'), 18, 28),
                # 'PA-RaPSB07:PS-DCLink-SFA2SDP1:IGBTT-Mon':
                # (self._gwidget('ledsfa2sdp1_igbt'), 25, 30),
                'PA-RaPSB07:PS-DCLink-SDB3:IGBTT-Mon':
                (self._gwidget('ledsdb3_igbt'), 22, 32),
                'PA-RaPSB08:PS-DCLink-SDP23:IGBTT-Mon':
                (self._gwidget('ledsdp23_igbt'), 23, 33),
            },
            "SextDef_rectifiert": {
                'PA-RaPSB01:PS-DCLink-SDB0:RectifierT-Mon':
                (self._gwidget('ledsdb0_rectifier'), 12, 22),
                'PA-RaPSB01:PS-DCLink-SDAP0:RectifierT-Mon':
                (self._gwidget('ledsdap0_rectifier'), 14, 24),
                'PA-RaPSB04:PS-DCLink-SDA12:RectifierT-Mon':
                (self._gwidget('ledsda12_rectifier'), 19, 29),
                'PA-RaPSB04:PS-DCLink-SDB1:RectifierT-Mon':
                (self._gwidget('ledsdb1_rectifier'), 16, 26),
                'PA-RaPSB05:PS-DCLink-SDA3SFA1:RectifierT-Mon':
                (self._gwidget('ledsda3sfa1_rectifier'), 24, 33),
                'PA-RaPSB05:PS-DCLink-SDB2:RectifierT-Mon':
                (self._gwidget('ledsdb2_rectifier'), 18, 28),
                # 'PA-RaPSB07:PS-DCLink-SFA2SDP1:RectifierT-Mon':
                # (self._gwidget('ledsfa2sdp1_rectifier'), 25, 30),
                'PA-RaPSB07:PS-DCLink-SDB3:RectifierT-Mon':
                (self._gwidget('ledsdb3_rectifier'), 22, 32),
                'PA-RaPSB08:PS-DCLink-SDP23:RectifierT-Mon':
                (self._gwidget('ledsdp23_rectifier'), 23, 33),
            },
            "SextDef_pcbt": {
                'PA-RaPSB01:PS-DCLink-SDAP0:PCBT-Mon':
                (self._gwidget('ledsdap0_pcb'), 16, 26),
                'PA-RaPSB01:PS-DCLink-SDB0:PCBT-Mon':
                (self._gwidget('ledsdb0_pcb'), 28, 38),
                'PA-RaPSB04:PS-DCLink-SDA12:PCBT-Mon':
                (self._gwidget('ledsda12_pcb'), 17, 27),
                'PA-RaPSB04:PS-DCLink-SDB1:PCBT-Mon':
                (self._gwidget('ledsdb1_pcb'), 30, 40),
                'PA-RaPSB05:PS-DCLink-SDA3SFA1:PCBT-Mon':
                (self._gwidget('ledsda3sfa1_pcb'), 20, 30),
                'PA-RaPSB05:PS-DCLink-SDB2:PCBT-Mon':
                (self._gwidget('ledsdb2_pcb'), 30, 45),
                'PA-RaPSB07:PS-DCLink-SDB3:PCBT-Mon':
                (self._gwidget('ledsdb3_pcb'), 32, 42),
                # 'PA-RaPSB07:PS-DCLink-SFA2SDP1:PCBT-Mon':
                # (self._gwidget('ledsfa2sdp1_pcb'), 24, 29),
                'PA-RaPSB08:PS-DCLink-SDP23:PCBT-Mon':
                (self._gwidget('ledsdp23_pcb'), 23, 33),
            },
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
            "01_MBtemp": {
                'SI-01-MBTemp-22-CH6': (self._gwidget('ledb2c3_22ch6'),
                                        18, 26),
                'SI-01-MBTemp-22-CH7': (self._gwidget('ledb2c3_22ch7'),
                                        18, 26),
                'SI-01-MBTemp-22-CH8': (self._gwidget('ledb2c3_22ch8'),
                                        18, 26),
                'SI-01-MBTemp-14-CH5': (self._gwidget('ledq1c1_14ch5'),
                                        18, 26),
                'SI-01-MBTemp-14-CH6': (self._gwidget('ledq1c1_14ch6'),
                                        18, 26),
                'SI-01-MBTemp-14-CH7': (self._gwidget('ledq1c1_14ch7'),
                                        18, 26),
                'SI-01-MBTemp-23-CH6': (self._gwidget('ledqfbm1_23ch6'),
                                        18, 26),
                'SI-01-MBTemp-23-CH7': (self._gwidget('ledqfbm1_23ch7'),
                                        18, 26),
            },
            "03_MBtemp": {
                'SI-03-MBTemp-23-CH5': (self._gwidget('ledb1c4_23ch5'),
                                        18, 26),
                'SI-03-MBTemp-23-CH6': (self._gwidget('ledb1c4_23ch6'),
                                        18, 26),
                'SI-03-MBTemp-23-CH7': (self._gwidget('ledb1c4_13ch7'),
                                        18, 26),
                'SI-03-MBTemp-13-CH5': (self._gwidget('ledb2c3_13ch5'),
                                        18, 26),
                'SI-03-MBTemp-13-CH6': (self._gwidget('ledb2c3_13ch6'),
                                        18, 26),
                'SI-03-MBTemp-13-CH7': (self._gwidget('ledb2c3_13ch7'),
                                        18, 26),
                'SI-03-MBTemp-22-CH6': (self._gwidget('ledq3c3_22ch6'),
                                        18, 26),
                # 'SI-03-MBTemp-22-CH7': (self._gwidget('ledq3c3_22ch7'),
                #                         18, 26),
                'SI-03-MBTemp-22-CH8': (self._gwidget('ledq3c3_22ch8'),
                                        18, 26),
            },
            "06_MBtemp": {
                'SI-06-MBTemp-23-CH5': (self._gwidget('led06b1c4_23ch5'),
                                        18, 26),
                'SI-06-MBTemp-23-CH6': (self._gwidget('led06b1c4_23ch6'),
                                        18, 26),
                # 'SI-06-MBTemp-23-CH7': (self._gwidget('led06b1c4_23ch7'),
                #                         18, 26),
                'SI-06-MBTemp-11-CH4': (self._gwidget('led06b2c2_11ch4'),
                                        18, 26),
                'SI-06-MBTemp-11-CH5': (self._gwidget('led06b2c2_11ch5'),
                                        18, 26),
                'SI-06-MBTemp-11-CH6': (self._gwidget('led06b2c2_11ch6'),
                                        18, 26),
                'SI-06-MBTemp-22-CH6': (self._gwidget('led06q3c3_22ch6'),
                                        18, 26),
                'SI-06-MBTemp-22-CH7': (self._gwidget('led06q3c3_22ch7'),
                                        18, 26),
                # 'SI-06-MBTemp-22-CH8': (self._gwidget('led06q3c3_22ch8'),
                #                       18, 26),
            },
            "08_MBtemp": {
                'SI-08-MBTemp-23-CH5': (self._gwidget('led08b1c4_23ch5'),
                                        18, 26),
                'SI-08-MBTemp-23-CH6': (self._gwidget('led08b1c4_23ch6'),
                                        18, 26),
                'SI-08-MBTemp-23-CH7': (self._gwidget('led08b1c4_23ch7'),
                                        18, 26),
                'SI-08-MBTemp-10-CH3': (self._gwidget('led08b2c2_10ch3'),
                                        18, 26),
                'SI-08-MBTemp-10-CH4': (self._gwidget('led08b2c2_10ch4'),
                                        18, 26),
                'SI-08-MBTemp-10-CH5': (self._gwidget('led08b2c2_10ch5'),
                                        18, 26),
                'SI-08-MBTemp-22-CH6': (self._gwidget('led08q3c3_22ch6'),
                                        18, 26),
                'SI-08-MBTemp-22-CH7': (self._gwidget('led08q3c3_22ch7'),
                                        18, 26),
                'SI-08-MBTemp-22-CH8': (self._gwidget('led08q3c3_22ch8'),
                                        18, 26),
            },
            "11_MBtemp": {
                'SI-11-MBTemp-23-CH5': (self._gwidget('led11b1c4_23ch5'),
                                        18, 26),
                'SI-11-MBTemp-23-CH6': (self._gwidget('led11b1c4_23ch6'),
                                        18, 26),
                'SI-11-MBTemp-23-CH7': (self._gwidget('led11b1c4_23ch7'),
                                        18, 26),
                'SI-11-MBTemp-13-CH3': (self._gwidget('led11b2c2_13ch3'),
                                        18, 26),
                'SI-11-MBTemp-13-CH5': (self._gwidget('led11b2c2_13ch5'),
                                        18, 26),
                'SI-11-MBTemp-12-CH8': (self._gwidget('led11b2c2_12ch8'),
                                        18, 26),
                'SI-11-MBTemp-22-CH6': (self._gwidget('led11q3c3_22ch6'),
                                        18, 26),
                'SI-11-MBTemp-22-CH7': (self._gwidget('led11q3c3_22ch7'),
                                        18, 26),
                'SI-11-MBTemp-22-CH8': (self._gwidget('led11q3c3_22ch8'),
                                        18, 26),
            },
            "13_MBtemp": {
                # 'SI-13-MBTemp-22-CH7': (self._gwidget('led22b2c3_22ch7'),
                # 18, 26),
                'SI-13-MBTemp-22-CH8': (self._gwidget('led22b2c3_22ch8'),
                                        18, 26),
                'SI-13-MBTemp-13-CH5': (self._gwidget('led13q1c1_13ch5'),
                                        18, 26),
                'SI-13-MBTemp-13-CH6': (self._gwidget('led13q1c1_13ch6'),
                                        18, 26),
                'SI-13-MBTemp-13-CH7': (self._gwidget('led13q1c1_13ch7'),
                                        18, 26),
                'SI-13-MBTemp-23-CH5': (self._gwidget('led13qfbm1_23ch5'),
                                        18, 26),
                # 'SI-13-MBTemp-23-CH6': (self._gwidget('led13qfbm1_23ch6'),
                #                       18, 26),
                'SI-13-MBTemp-23-CH7': (self._gwidget('led13qfbm1_23ch7'),
                                        18, 26),
            },
            "16_MBtemp": {
                'SI-16-MBTemp-22-CH6': (self._gwidget('led16b2c3_22ch6'),
                                        18, 26),
                'SI-16-MBTemp-22-CH7': (self._gwidget('led16b2c3_22ch7'),
                                        18, 26),
                'SI-16-MBTemp-22-CH8': (self._gwidget('led16b2c3_22ch8'),
                                        18, 26),
                'SI-16-MBTemp-11-CH6': (self._gwidget('led16q1c1_11ch6'),
                                        18, 26),
                'SI-16-MBTemp-11-CH7': (self._gwidget('led16q1c1_11ch7'),
                                        24, 28),
                'SI-16-MBTemp-11-CH8': (self._gwidget('led16q1c1_11ch8'),
                                        18, 26),
                'SI-16-MBTemp-23-CH5': (self._gwidget('led16qfbm1_23ch5'),
                                        18, 26),
                'SI-16-MBTemp-23-CH6': (self._gwidget('led16qfbm1_23ch6'),
                                        24, 28),
                'SI-16-MBTemp-23-CH7': (self._gwidget('led16qfbm1_23ch7'),
                                        18, 26),
            },
            "18_MBtemp": {
                'SI-18-MBTemp-23-CH5': (self._gwidget('led18b1c4_23ch5'),
                                        18, 26),
                'SI-18-MBTemp-23-CH6': (self._gwidget('led18b1c4_23ch6'),
                                        18, 26),
                'SI-18-MBTemp-23-CH7': (self._gwidget('led18b1c4_23ch7'),
                                        18, 26),
                'SI-18-MBTemp-11-CH5': (self._gwidget('led18b2c2_11ch5'),
                                        18, 26),
                'SI-18-MBTemp-11-CH6': (self._gwidget('led18b2c2_11ch6'),
                                        18, 26),
                'SI-18-MBTemp-11-CH7': (self._gwidget('led18b2c2_11ch7'),
                                        18, 26),
                'SI-18-MBTemp-22-CH6': (self._gwidget('led18q3c3_22ch6'),
                                        18, 26),
                'SI-18-MBTemp-22-CH7': (self._gwidget('led18q3c3_22ch7'),
                                        18, 26),
                'SI-18-MBTemp-22-CH8': (self._gwidget('led18q3c3_22ch8'),
                                        18, 26),
            },
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
                                               ('led03bcfe'), 10, 42),
            # 'SI-03C1:VA-PT100-ED:Temp-Mon': (self._gwidget('led03c1'), 17,
            #  42),
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
            # 'SI-04M1:VA-PT100-ED:Temp-Mon': (self._gwidget('led04m1'), 17,
            #  42),
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
            # 'SI-05SAFE:VA-PT100-ED:Temp-Mon': (self._gwidget
            #                                   ('led05safe'), 17, 42),
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
                                               ('led07b2fe'), 16, 42),
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
            # ('led17bcfe'), 17, 39),
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
            (self._gwidget('led_ctrl'), 28, 32),
            'CA-RaInter:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led_inter'), 25, 29),
            'CA-RaTim:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led_tim'), 23, 27),
            'RoomSrv:CO-SIMAR-01:AmbientTemp-Mon':
            (self._gwidget('led_server'), 17, 21),
            'CA:CO-SIMAR-01:AmbientTemp-Mon':
            (self._gwidget('led_ambient'), 21, 24),

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
            # 'IA-01RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led01raps02'), 19, 32),
            # 'IA-01RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led01ravac'), 19, 32),
            # 'IA-01RaInjBO:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led01rainjbo'), 19, 32),
            # 'IA-01RaNLK:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led01ranlk'), 19, 32),
            'IA-02RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led02ractrl'), 15, 32),
            'IA-02RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led02rabpm'), 15, 32),
            'IA-02RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led02raps01'), 15, 32),
            'IA-02RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led02raps02'), 15, 32),
            'IA-02RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led02ravac'), 15, 32),
            'IA-03RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led03ractrl'), 15, 32),
            'IA-03RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led03rabpm'), 15, 32),
            'IA-03RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led03raps01'), 15, 32),
            'IA-03RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led03raps02'), 15, 32),
            'IA-03RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led03ravac'), 15, 32),
            'IA-04RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led04ractrl'), 15, 32),
            'IA-04RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led04rabpm'), 15, 32),
            'IA-04RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led04raps01'), 15, 32),
            'IA-04RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led04raps02'), 15, 32),
            'IA-04RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led04ravac'), 15, 32),
            'IA-05RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led05ractrl'), 15, 32),
            'IA-05RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led05rabpm'), 15, 32),
            'IA-05RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led05raps01'), 15, 32),
            'IA-05RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led05raps02'), 15, 32),
            'IA-05RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led05ravac'), 15, 32),
            'IA-06RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led06ractrl'), 15, 32),
            'IA-06RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led06rabpm'), 15, 32),
            'IA-06RaUnd:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led06raund'), 15, 32),
            'IA-06RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led06raps01'), 15, 32),
            'IA-06RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led06raps02'), 15, 32),
            'IA-06RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led06ravac'), 15, 32),
            'IA-07RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led07ractrl'), 15, 32),
            'IA-07RaUnd:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led07raund'), 15, 32),
            'IA-07RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led07raps01'), 15, 32),
            'IA-07RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led07raps02'), 15, 32),
            'IA-07RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led07ravac'), 15, 32),
            'IA-08RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led08ractrl'), 15, 32),
            'IA-08RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led08rabpm'), 15, 32),
            'IA-08RaUnd:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led08raund'), 15, 32),
            # 'IA-08RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led08raps01'), 15, 32),
            # 'IA-08RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led08raps02'), 15, 32),
            'IA-08RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led08ravac'), 15, 32),
            'IA-09RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led09ractrl'), 15, 32),
            'IA-09RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led09rabpm'), 15, 32),
            'IA-09RaUnd:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led09raund'), 15, 32),
            'IA-09RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led09raps01'), 15, 32),
            'IA-09RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led09raps02'), 15, 32),
            'IA-09RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led09ravac'), 15, 32),
            'IA-10RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led10ractrl'), 15, 32),
            'IA-10RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led10rabpm'), 15, 32),
            'IA-10RaUnd:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led10raund'), 15, 32),
            'IA-10RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led10raps01'), 15, 32),
            'IA-10RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led10raps02'), 15, 32),
            'IA-10RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led10ravac'), 15, 32),
            'IA-11RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led11ractrl'), 15, 32),
            'IA-11RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led11rabpm'), 15, 32),
            'IA-11RaUnd:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led11raund'), 15, 32),
            'IA-11RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led11raps01'), 15, 32),
            'IA-11RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led11raps02'), 15, 32),
            'IA-11RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led11ravac'), 15, 32),
            'IA-12RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led12ractrl'), 15, 32),
            'IA-12RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led12rabpm'), 15, 32),
            'IA-12RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led12raps01'), 15, 32),
            'IA-12RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led12raps02'), 15, 32),
            'IA-12RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led12ravac'), 15, 32),
            'IA-13RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led13ractrl'), 15, 32),
            'IA-13RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led13rabpm'), 15, 32),
            'IA-13RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led13raps01'), 15, 32),
            'IA-13RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led13raps02'), 15, 32),
            'IA-13RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led13ravac'), 15, 32),
            # 'IA-14RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led14ractrl'), 15, 32),
            # 'IA-14RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led14rabpm'), 15, 32),
            # 'IA-14RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led14raps01'), 15, 32),
            # 'IA-14RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led14raps02'), 15, 32),
            # 'IA-14RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led14ravac'), 15, 32),
            # 'IA-14RaDiag03:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led14radiag'), 15, 32),
            'IA-15RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led15ractrl'), 15, 32),
            'IA-15RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led15rabpm'), 15, 32),
            'IA-15RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led15raps01'), 15, 32),
            'IA-15RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led15raps02'), 15, 32),
            'IA-15RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led15ravac'), 15, 32),
            'IA-16RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led16ractrl'), 15, 32),
            'IA-16RaBbB:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led16rabbb'), 15, 32),
            'IA-16RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led16rabpm'), 15, 32),
            'IA-16RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led16raps01'), 15, 32),
            # 'IA-16RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led16raps02'), 15, 32),
            'IA-16RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led16ravac'), 15, 32),
            'IA-17RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led17ractrl'), 15, 32),
            'IA-17RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led17rabpm'), 15, 32),
            'IA-17RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led17raps01'), 15, 32),
            'IA-17RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led17raps02'), 15, 32),
            'IA-17RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led17ravac'), 15, 32),
            'IA-18RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led18ractrl'), 15, 32),
            'IA-18RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led18rabpm'), 15, 32),
            'IA-18RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led18raps01'), 15, 32),
            'IA-18RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led18raps02'), 15, 32),
            # 'IA-18RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led18ravac'), 15, 32),
            # 'IA-19RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led19ractrl'), 15, 32),
            # 'IA-19RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led19rabpm'), 15, 32),
            # 'IA-19RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led19raps01'), 15, 32),
            # 'IA-19RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led19raps02'), 15, 32),
            'IA-19RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led19ravac'), 15, 32),
            'IA-19RaEPP:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led19raepp'), 15, 32),
            # 'IA-19RaVAC02:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led19ravac02'), 15, 32),
            'IA-20RaCtrl:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20ractrl'), 15, 32),
            'IA-20RaBPM:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20rabpm'), 15, 32),
            'IA-20RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20raps01'), 15, 32),
            'IA-20RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20raps02'), 15, 32),
            'IA-20RaVAC:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20ravac'), 15, 32),
            'IA-20RaDiag01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20radiag01'), 15, 32),
            'IA-20RaBPMTL:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20rabpmtl'), 15, 32),
            'IA-20RaEPP:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20raepp'), 15, 32),
            'IA-20RaDiag02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led20radiag02'), 15, 32),
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
            # 'IA-01RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led01raps02'), 21, 31),
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
            # 'IA-08RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led08raps01'), 21, 31),
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
            # 'IA-14RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led14raps01'), 21, 31),
            # 'IA-14RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led14raps02'), 21, 31),
            'IA-15RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led15raps01'), 21, 31),
            'IA-15RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led15raps02'), 21, 31),
            'IA-16RaPS01:CO-SIMAR-01:RackInternalTemp-Mon':
            (self._gwidget('led16raps01'), 21, 31),
            # 'IA-16RaPS02:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led16raps02'), 21, 31),
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
            # 'IA-01RaInjBO:CO-SIMAR-01:RackInternalTemp-Mon':
            # (self._gwidget('led_injbo'), 21, 25),
        }


class Si_circhid(utils.ConnWidgetPVs):
    """Classe responsável pelo controle do sistema de temperatura Booster."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/tempcirchid.ui",
                         "temp")

    def _registrar_grupos(self):
        """Registra os grupos de PVs/LEDs e suas faixas."""
        self.sinais = {
            'SI-08-MBTemp-10-CH6': (self._gwidget('led10ch6'), 20, 25),
            'SI-18-MBTemp-13-CH5': (self._gwidget('led13ch5'), 20, 25),
            'SI-18-MBTemp-13-CH6': (self._gwidget('led13ch6'), 20, 25),
            'SI-08-MBTemp-10-CH8': (self._gwidget('led10ch8'), 20, 25),
            'SI-18-MBTemp-13-CH7': (self._gwidget('led13ch7'), 22, 28),
            # 'UA-21CHall:CR-IHMCtrl:dbAdsSta_strAdsA_m12CP2CW1035T-Mon':
            # (self._gwidget('ledcp21035t'), 24.5, 35.5),
            # 'UA-21CHall:CR-IHMCtrl:dbAdsSta_strAdsA_m12CP1CW1065T-Mon':
            # (self._gwidget('ledcp11065t'), 22.4, 33),
            # 'UA-21CHall:CR-IHMCtrl:dbAdsSta_strAdsA_m12CP2CW1065T-Mon':
            # (self._gwidget('ledcp21065t'), 21, 25),
            'RA-TLSIA:RF-Circulator:Tout-Mon': (self._gwidget('ledcirctout'),
                                                18, 22),
            'RA-TLSIA:RF-Circulator:Tin-Mon': (self._gwidget('ledcirctin'),
                                               18, 21),
            'LA-CN:H1MPS-1:K1Temp1': (self._gwidget('ledk1temp1'), 19, 21),
            'LA-CN:H1MPS-1:K2Temp1': (self._gwidget('ledk2temp1'), 17.5, 19.5),
            'LA-CN:H1MPS-1:K1Temp2': (self._gwidget('ledk1temp2'), 18.7, 20.7),
            'LA-CN:H1MPS-1:K2Temp2': (self._gwidget('ledk2temp2'), 18.5, 20.5),
            'TB-Fam:PS-B:InductorTemperatureIIB-Mon':
            (self._gwidget('ledinductoriib'), 22, 25),
            'BO-15U:VA-PT100-BG:Temp-Mon':
            (self._gwidget('ledbo15vacpt100'), 22, 28),
            'BO-25U:VA-PT100-BG:Temp-Mon':
            (self._gwidget('ledbo25u'), 22, 28),
            'TS-Fam:PS-B:TemperatureIIBMod1-Mon':
            (self._gwidget('ledtsbtempmod1'), 43, 46),
            'TS-Fam:PS-B:TemperatureIIBMod4-Mon':
            (self._gwidget('ledtsbtempmod4'), 36, 39),
            'BO-05U:VA-PT100-BG:Temp-Mon':
            (self._gwidget('led05uvacpt100'), 22, 26),
            'BO-10U:VA-PT100-BG:Temp-Mon':
            (self._gwidget('led10uvacpt100'), 21, 24),
            'BO-14U:VA-PT100-BG:Temp-Mon':
            (self._gwidget('led14uvacpt100'), 21, 24),
            'SI-Fam:PS-QDA:InductorTemperatureIIB-Mon':
            (self._gwidget('ledqdainductor'), 18, 24),
            'SI-Fam:PS-QDA:HeatSinkTemperatureIIB-Mon':
            (self._gwidget('ledqdaheatsink'), 18, 24),
            'SI-Fam:PS-SDA0:HeatSinkTemperatureIIB-Mon':
            (self._gwidget('ledsda0heatsink'), 18, 24),
            'SI-Fam:PS-SFP1:HeatSinkTemperatureIIB-Mon':
            (self._gwidget('ledsfp1heatsink'), 18, 24),
            # 'EMA:A:HVAC01:ESB_180TT1_Agua_Gld_out':
            # (self._gwidget('led_emawater'), 20.9, 21.8),
            # 'IMB:A:HVAC01:OEA_180TT1_Agua_Gld_out':
            # (self._gwidget('led_imbwater'), 16.9, 20.51),
            # 'QUA:A:HVAC01:OEA_130TT1_Agua_Gld_Out':
            # (self._gwidget('led_quawater'), 23, 27),
            # 'PNR:A:HVAC01:OEA_130TT1_Agua_Gld_Out':
            # (self._gwidget('ledpnrwater'), 19, 21),
        }


# SISTEMAS DE FONTES
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
            # 'SI-02C1:PS-Q1:DiagStatus-Mon': (self._gwidget('led_02c1q1'), 0),
            # 'SI-02C1:PS-Q2:DiagStatus-Mon': (self._gwidget('led_02c1q2'), 0),
            # 'SI-02C2:PS-Q3:DiagStatus-Mon': (self._gwidget('led_02c2q3'), 0),
            # 'SI-02C2:PS-Q4:DiagStatus-Mon': (self._gwidget('led_02c2q4'), 0),
            # 'SI-02C3:PS-Q3:DiagStatus-Mon': (self._gwidget('led_02c3q3'), 0),
            # 'SI-02C3:PS-Q4:DiagStatus-Mon': (self._gwidget('led_02c3q4'), 0),
            # 'SI-02C4:PS-Q1:DiagStatus-Mon': (self._gwidget('led_02c4q1'), 0),
            # 'SI-02C4:PS-Q2:DiagStatus-Mon': (self._gwidget('led_02c4q2'), 0),
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
            'SI-14SB:PS-LCH:PwrState-Sts': (self._gwidget('led_ff14sblch'), 1),
            'SI-14SB:PS-CH-1:PwrState-Sts':
            (self._gwidget('led_ff14sbch1'), 1),
            'SI-14SB:PS-CH-2:PwrState-Sts':
            (self._gwidget('led_ff14sbch2'), 1),
            'SI-14SB:PS-CV-1:PwrState-Sts':
            (self._gwidget('led_ff14sbcv1'), 1),
            'SI-14SB:PS-CV-2:PwrState-Sts':
            (self._gwidget('led_ff14sbcv2'), 1),

            'SI-08SB:PS-CH-1:PwrState-Sts':
            (self._gwidget('led_ff08sbch1'), 1),
            'SI-08SB:PS-CH-2:PwrState-Sts':
            (self._gwidget('led_ff08sbch2'), 1),
            'SI-08SB:PS-CV-1:PwrState-Sts':
            (self._gwidget('led_ff08sbcv1'), 1),
            'SI-08SB:PS-CV-2:PwrState-Sts':
            (self._gwidget('led_ff08sbcv2'), 1),
            'SI-08SB:PS-LCH:PwrState-Sts':
            (self._gwidget('led_ff14sblch'), 1),

            'SI-10SB:PS-CH-1:PwrState-Sts':
            (self._gwidget('led_ff10sbch1'), 1),
            'SI-10SB:PS-CH-2:PwrState-Sts':
            (self._gwidget('led_ff10sbch2'), 1),
            'SI-10SB:PS-CV-1:PwrState-Sts':
            (self._gwidget('led_ff10sbcv1'), 1),
            'SI-10SB:PS-CV-2:PwrState-Sts':
            (self._gwidget('led_ff10sbcv2'), 1),
            'SI-10SB:PS-QS-1:PwrState-Sts':
            (self._gwidget('led_ff10sbqs1'), 1),
            'SI-10SB:PS-QS-2:PwrState-Sts':
            (self._gwidget('led_ff10sbqs2'), 1),

            'SI-01M1:PS-FFCH:PwrState-Sts':
            (self._gwidget('led_ff01m1ch'), 1),
            'SI-01M2:PS-FFCH:PwrState-Sts':
            (self._gwidget('led_ff01m2ch'), 1),
            'SI-01M1:PS-FFCV:PwrState-Sts':
            (self._gwidget('led_ff01m1cv'), 1),
            'SI-01M2:PS-FFCV:PwrState-Sts':
            (self._gwidget('led_ff01m2cv'), 1),
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
            'SI-01C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch01c2'), 1),
            'SI-01C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch01c3'), 1),
            # 'SI-01M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch01m1'), 1),
            # 'SI-01M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch01m2'), 1),
            'SI-02C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch02c2'), 1),
            'SI-02C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch02c3'), 1),
            'SI-02M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch02m1'), 1),
            'SI-02M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch02m2'), 1),
            'SI-03C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch03c2'), 1),
            'SI-03C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch03c3'), 1),
            'SI-03M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch03m1'), 1),
            'SI-03M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch03m2'), 1),
            'SI-04C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch04c2'), 1),
            'SI-04C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch04c3'), 1),
            'SI-04M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch04m1'), 1),
            'SI-04M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch04m2'), 1),
            'SI-05C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch05c2'), 1),
            'SI-05C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch05c3'), 1),
            'SI-05M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch05m1'), 1),
            'SI-05M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch05m2'), 1),
            'SI-06C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch06c2'), 1),
            'SI-06C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch06c3'), 1),
            'SI-06M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch06m1'), 1),
            'SI-06M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch06m2'), 1),
            'SI-07C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch07c2'), 1),
            'SI-07C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch07c3'), 1),
            'SI-07M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch07m1'), 1),
            'SI-07M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch07m2'), 1),
            'SI-08C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch08c2'), 1),
            'SI-08C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch08c3'), 1),
            'SI-08M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch08m1'), 1),
            'SI-08M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch08m2'), 1),
            'SI-09C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch09c2'), 1),
            'SI-09C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch09c3'), 1),
            'SI-09M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch09m1'), 1),
            'SI-09M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch09m2'), 1),
            'SI-10C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch10c2'), 1),
            'SI-10C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch10c3'), 1),
            'SI-10M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch10m1'), 1),
            'SI-10M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch10m2'), 1),
            'SI-11C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch11c2'), 1),
            'SI-11C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch11c3'), 1),
            'SI-11M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch11m1'), 1),
            'SI-11M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch11m2'), 1),
            'SI-12C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch12c2'), 1),
            'SI-12C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch12c3'), 1),
            'SI-12M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch12m1'), 1),
            'SI-12M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch12m2'), 1),
            'SI-13C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch13c2'), 1),
            'SI-13C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch13c3'), 1),
            'SI-13M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch13m1'), 1),
            'SI-13M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch13m2'), 1),
            'SI-14C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch14c2'), 1),
            'SI-14C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch14c3'), 1),
            'SI-14M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch14m1'), 1),
            'SI-14M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch14m2'), 1),
            'SI-15C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch15c2'), 1),
            'SI-15C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch15c3'), 1),
            'SI-15M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch15m1'), 1),
            'SI-15M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch15m2'), 1),
            'SI-16C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch16c2'), 1),
            'SI-16C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch16c3'), 1),
            'SI-16M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch16m1'), 1),
            'SI-16M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch16m2'), 1),
            'SI-17C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch17c2'), 1),
            'SI-17C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch17c3'), 1),
            'SI-17M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch17m1'), 1),
            'SI-17M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch17m2'), 1),
            'SI-18C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch18c2'), 1),
            'SI-18C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch18c3'), 1),
            'SI-18M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch18m1'), 1),
            'SI-18M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch18m2'), 1),
            'SI-19C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch19c2'), 1),
            'SI-19C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch19c3'), 1),
            'SI-19M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch19m1'), 1),
            'SI-19M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch19m2'), 1),
            'SI-20C2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch20c2'), 1),
            'SI-20C3:PS-FCH:PwrState-Sts': (self._gwidget('ledfch20c3'), 1),
            'SI-20M1:PS-FCH:PwrState-Sts': (self._gwidget('ledfch20m1'), 1),
            'SI-20M2:PS-FCH:PwrState-Sts': (self._gwidget('ledfch20m2'), 1),
            'SI-01C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv01c2'), 1),
            'SI-01C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv01c3'), 1),
            # 'SI-01M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv01m1'), 1),
            # 'SI-01M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv01m2'), 1),
            'SI-02C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv02c2'), 1),
            'SI-02C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv02c3'), 1),
            'SI-02M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv02m1'), 1),
            'SI-02M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv02m2'), 1),
            'SI-03C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv03c2'), 1),
            'SI-03C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv03c3'), 1),
            'SI-03M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv03m1'), 1),
            'SI-03M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv03m2'), 1),
            'SI-04C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv04c2'), 1),
            'SI-04C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv04c3'), 1),
            'SI-04M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv04m1'), 1),
            'SI-04M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv04m2'), 1),
            'SI-05C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv05c2'), 1),
            'SI-05C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv05c3'), 1),
            'SI-05M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv05m1'), 1),
            'SI-05M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv05m2'), 1),
            'SI-06C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv06c2'), 1),
            'SI-06C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv06c3'), 1),
            'SI-06M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv06m1'), 1),
            'SI-06M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv06m2'), 1),
            'SI-07C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv07c2'), 1),
            'SI-07C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv07c3'), 1),
            'SI-07M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv07m1'), 1),
            'SI-07M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv07m2'), 1),
            'SI-08C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv08c2'), 1),
            'SI-08C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv08c3'), 1),
            'SI-08M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv08m1'), 1),
            'SI-08M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv08m2'), 1),
            'SI-09C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv09c2'), 1),
            'SI-09C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv09c3'), 1),
            'SI-09M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv09m1'), 1),
            'SI-09M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv09m2'), 1),
            'SI-10C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv10c2'), 1),
            'SI-10C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv10c3'), 1),
            'SI-10M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv10m1'), 1),
            'SI-10M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv10m2'), 1),
            'SI-11C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv11c2'), 1),
            'SI-11C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv11c3'), 1),
            'SI-11M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv11m1'), 1),
            'SI-11M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv11m2'), 1),
            'SI-12C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv12c2'), 1),
            'SI-12C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv12c3'), 1),
            'SI-12M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv12m1'), 1),
            'SI-12M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv12m2'), 1),
            'SI-13C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv13c2'), 1),
            'SI-13C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv13c3'), 1),
            'SI-13M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv13m1'), 1),
            'SI-13M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv13m2'), 1),
            'SI-14C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv14c2'), 1),
            'SI-14C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv14c3'), 1),
            'SI-14M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv14m1'), 1),
            'SI-14M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv14m2'), 1),
            'SI-15C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv15c2'), 1),
            'SI-15C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv15c3'), 1),
            'SI-15M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv15m1'), 1),
            'SI-15M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv15m2'), 1),
            'SI-16C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv16c2'), 1),
            'SI-16C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv16c3'), 1),
            'SI-16M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv16m1'), 1),
            'SI-16M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv16m2'), 1),
            'SI-17C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv17c2'), 1),
            'SI-17C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv17c3'), 1),
            'SI-17M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv17m1'), 1),
            'SI-17M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv17m2'), 1),
            'SI-18C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv18c2'), 1),
            'SI-18C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv18c3'), 1),
            'SI-18M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv18m1'), 1),
            'SI-18M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv18m2'), 1),
            'SI-19C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv19c2'), 1),
            'SI-19C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv19c3'), 1),
            'SI-19M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv19m1'), 1),
            'SI-19M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv19m2'), 1),
            'SI-20C2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv20c2'), 1),
            'SI-20C3:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv20c3'), 1),
            'SI-20M1:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv20m1'), 1),
            'SI-20M2:PS-FCV:PwrState-Sts': (self._gwidget('ledfcv20m2'), 1),
        }


class Vacuum(utils.ConnWidgetPVs):
    """Controle da subjanela de leitura de vácuo do Anel."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/vacsi.ui", "vacuo")

    def _registrar_grupos(self):
        """Registra Pvs de vacuo e seus leds correspondentes."""
        self.sinais = {
            'SI-01C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac01c1'), 1.0e-7),
            'SI-01C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac01c3'), 1.0e-7),
            'SI-01SA:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac01sa'), 1.0e-7),
            'SI-02C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac02c1'), 1.0e-7),
            'SI-02C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac02c3'), 1.0e-7),
            'SI-02SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac02sb'), 1.0e-7),
            'SI-03C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac03c1'), 1.0e-7),
            'SI-03C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac03c3'), 1.0e-7),
            'SI-03SP:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac03sp'), 1.0e-7),
            'SI-04C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac04c1'), 1.0e-7),
            'SI-04C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac04c3'), 1.0e-7),
            'SI-04SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac04sb'), 1.0e-7),
            'SI-05C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac05c1'), 1.0e-7),
            'SI-05C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac05c3'), 1.0e-7),
            'SI-05SA:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac05sa'), 1.0e-7),
            'SI-06C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac06c1'), 1.0e-7),
            'SI-06C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac06c3'), 1.0e-7),
            'SI-06SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac06sb'), 1.0e-7),
            'SI-07C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac07c1'), 1.0e-7),
            'SI-07C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac07c3'), 1.0e-7),
            'SI-07SP:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac07sp'), 1.0e-7),
            'SI-08C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac08c1'), 1.0e-7),
            'SI-08C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac08c3'), 1.0e-7),
            'SI-08SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac08sb'), 1.0e-7),
            'SI-09C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac09c1'), 1.0e-7),
            'SI-09C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac09c3'), 1.0e-7),
            'SI-09SA:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac09sa'), 1.0e-7),
            'SI-10C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac10c1'), 1.0e-7),
            'SI-10C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac10c3'), 1.0e-7),
            'SI-10SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac10sb'), 1.0e-7),
            'SI-11C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac11c1'), 1.0e-7),
            'SI-11C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac11c3'), 1.0e-7),
            'SI-11SP:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac11sp'), 1.0e-7),
            'SI-12C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac12c1'), 1.0e-7),
            'SI-12C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac12c3'), 1.0e-7),
            'SI-12SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac12sb'), 1.0e-7),
            'SI-13C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac13c1'), 1.0e-7),
            'SI-13C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac13c3'), 1.0e-7),
            'SI-13SA:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac13sa'), 1.0e-7),
            'SI-14C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac14c1'), 1.0e-7),
            'SI-14C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac14c3'), 1.0e-7),
            'SI-14SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac14sb'), 1.0e-7),
            'SI-15C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac15c1'), 1.0e-7),
            'SI-15C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac15c3'), 1.0e-7),
            'SI-15SP:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac15sp'), 1.0e-7),
            'SI-16C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac16c1'), 1.0e-7),
            'SI-16C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac16c3'), 1.0e-7),
            'SI-16SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac16sb'), 1.0e-7),
            'SI-17C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac17c1'), 1.0e-7),
            'SI-17C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac17c3'), 1.0e-7),
            'SI-17SA:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac17sa'), 1.0e-7),
            'SI-18C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac18c1'), 1.0e-7),
            'SI-18C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac18c3'), 1.0e-7),
            'SI-18SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac18sb'), 1.0e-7),
            'SI-19C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac19c1'), 1.0e-7),
            'SI-19C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac19c3'), 1.0e-7),
            'SI-19SP:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac19sp'), 1.0e-7),
            'SI-20C1:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac20c1'), 1.0e-7),
            'SI-20C3:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac20c3'), 1.0e-7),
            'SI-20SB:VA-CCG-BG:Pressure-Mon':
            (self._gwidget('led_vac20sb'), 1.0e-7),
            'SI-01BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_01bcfe'), 1.0e-7),
            'SI-01C2FE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_01c2fe'), 1.0e-7),
            'SI-01SAFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_01safe'), 1.0e-7),
            'SI-02BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_02bcfe'), 1.0e-7),
            'SI-02SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_02sbfe'), 1.0e-7),
            'SI-03BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_03bcfe'), 1.0e-7),
            'SI-03C2FE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_03c2fe'), 1.0e-7),
            'SI-03SPFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_03spfe'), 1.0e-7),
            'SI-04BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_04bcfe'), 1.0e-7),
            'SI-04SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_04sbfe'), 1.0e-7),
            'SI-05BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_05bcfe'), 1.0e-7),
            'SI-05C2FE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_05c2fe'), 1.0e-7),
            'SI-05SAFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_05safe'), 1.0e-7),
            'SI-06BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_06bcfe'), 1.0e-7),
            'SI-06SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_06sbfe'), 1.0e-7),
            'SI-07BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_07bcfe'), 1.0e-7),
            'SI-07C2FE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_07c2fe'), 1.0e-7),
            'SI-07SPFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_07spfe'), 1.0e-7),
            'SI-08BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_08bcfe'), 1.0e-7),
            'SI-08SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_08sbfe'), 1.0e-7),
            'SI-09BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_09bcfe'), 1.0e-7),
            'SI-09C2FE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_09c2fe'), 1.0e-7),
            'SI-09SAFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_09safe'), 1.0e-7),
            'SI-10BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_10bcfe'), 1.0e-7),
            'SI-10SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_10sbfe'), 1.0e-7),
            'SI-11BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_11bcfe'), 1.0e-7),
            'SI-11C2FE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_11c2fe'), 1.0e-7),
            'SI-11SPFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_11spfe'), 1.0e-7),
            'SI-12BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_12bcfe'), 1.0e-7),
            'SI-12SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_12sbfe'), 1.0e-7),
            'SI-13BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_13bcfe'), 1.0e-7),
            'SI-13C2FE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_13c2fe'), 1.0e-7),
            'SI-13SAFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_13safe'), 1.0e-7),
            'SI-14BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_14bcfe'), 1.0e-7),
            'SI-14SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_14sbfe'), 1.0e-7),
            'SI-15BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_15bcfe'), 1.0e-7),
            'SI-15C2FE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_15c2fe'), 1.0e-7),
            'SI-15SPFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_15spfe'), 1.0e-7),
            'SI-16BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_16bcfe'), 1.0e-7),
            'SI-16SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_16sbfe'), 1.0e-7),
            'SI-17BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_17bcfe'), 1.0e-7),
            'SI-17C2FE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_17c2fe'), 1.0e-7),
            'SI-17SAFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_17safe'), 1.0e-7),
            'SI-18BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_18bcfe'), 1.0e-7),
            'SI-18SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_18sbfe'), 1.0e-7),
            'SI-19BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_19bcfe'), 1.0e-7),
            'SI-19SPFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_19spfe'), 1.0e-7),
            'SI-20BCFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_20bcfe'), 1.0e-7),
            'SI-20SBFE:VA-CCG-MD:Pressure-Mon':
            (self._gwidget('led_20sbfe'), 1.0e-7),
        }


class Cavity(utils.ConnWidgetPVs):
    """Controle da subjanela de leitura de vácuo do Anel."""

    def __init__(self, janela_opr=None, botao_menu=None):
        """."""
        super().__init__(janela_opr, botao_menu, "ui/cavitysi.ui", "temp")

    def _registrar_grupos(self):
        """."""
        self.sinais = {
            'sensor_flow1': {
                'SI-03SP:RF-CryoMod-1:BF1611_RFWindowWaterFlow-Mon':
                (self._gwidget('ledbf1611'), 11.8, 15),
                'SI-03SP:RF-CryoMod-1:BF1621_FBTWaterFlow-Mon':
                (self._gwidget('ledbf1621'), 1.1, 1.5),
                'SI-03SP:RF-CryoMod-1:BF1622_FBTWaterFlow-Mon':
                (self._gwidget('ledbf1622'), 1.1, 1.5),
                'SI-03SP:RF-CryoMod-1:BF1623_FBTWaterFlow-Mon':
                (self._gwidget('ledbf1623'), 1.1, 1.5),
                'SI-03SP:RF-CryoMod-1:BF1631_RBTWaterFlow-Mon':
                (self._gwidget('ledbf1631'), 1.1, 1.5),
                'SI-03SP:RF-CryoMod-1:BF1632_RBTWaterFlow-Mon':
                (self._gwidget('ledbf1632'), 1.1, 1.5),
                'SI-03SP:RF-CryoMod-1:BF1633_RBTWaterFlow-Mon':
                (self._gwidget('ledbf1633'), 1.1, 1.5),
                'SI-03SP:RF-CryoMod-1:BF1641_TaperWaterFlow-Mon':
                (self._gwidget('ledbf1641'), 3.5, 5),
                'SI-03SP:RF-CryoMod-1:BF135_HexLineGHeFlow-Mon':
                (self._gwidget('ledbf135'), 35, 55),
                'SI-03SP:RF-CryoMod-1:BF176_VentLineLN2Flow-Mon':
                (self._gwidget('ledbf176'), 60, 120),
            },
            'temp_celcius1': {
                'SI-03SP:RF-CryoMod-1:BT106_RFWindowTemp-Mon':
                (self._gwidget('ledbt106'), 0, 115),
                'SI-03SP:RF-CryoMod-1:BT107_RFWindowTemp-Mon':
                (self._gwidget('ledbt107'), 0, 115),
                'SI-03SP:RF-CryoMod-1:BT108_RFWindowTemp-Mon':
                (self._gwidget('ledbt108'), 0, 115),
                'SI-03SP:RF-CryoMod-1:BT109_RFWindowTemp-Mon':
                (self._gwidget('ledbt109'), 0, 115),
                'SI-03SP:RF-CryoMod-1:BT133_HexLineGHeTemp-Mon':
                (self._gwidget('ledbt133'), 15, 45),
                'SI-03SP:RF-CryoMod-1:BT175_VentLineLN2Temp-Mon':
                (self._gwidget('ledbt175'), 10, 45),
                'SI-03SP:RF-CryoMod-1:BT185_WaveguideHexCoilTemp-Mon':
                (self._gwidget('ledbt185'), -240, 25),
                'SI-03SP:RF-CryoMod-1:BT186_WaveguideElbowCoilTemp-Mon':
                (self._gwidget('ledbt186'), -200, 25),
                'SI-03SP:RF-CryoMod-1:BT191_FBTFlangeTemp-Mon':
                (self._gwidget('ledbt191'), 15, 45),
                'SI-03SP:RF-CryoMod-1:BT192_RBTFlangeTemp-Mon':
                (self._gwidget('ledbt192'), 15, 45),
                'SI-03SP:RF-CryoMod-1:BT198_VentLineTemp-Mon':
                (self._gwidget('ledbt198'), 15, 45),
                'SI-03SP:RF-CryoMod-1:BT199_VentLineTemp-Mon':
                (self._gwidget('ledbt199'), 15, 45),
            },
            'temp_kelvin1': {
               'SI-03SP:RF-CryoMod-1:BT110_HeVesselHeaterTemp-Mon':
               (self._gwidget('ledbt110'), 2, 15),
               'SI-03SP:RF-CryoMod-1:BT111_CavBotTemp-Mon':
               (self._gwidget('ledbt111'), 1, 10),
               'SI-03SP:RF-CryoMod-1:BT112_CavTopTemp-Mon':
               (self._gwidget('ledbt112'), 1, 10),
               'SI-03SP:RF-CryoMod-1:BT113_WaveguideCavTemp-Mon':
               (self._gwidget('ledbt113'), 1, 299.5),
               'SI-03SP:RF-CryoMod-1:BT114_WaveguideCavTemp-Mon':
               (self._gwidget('ledbt114'), 1, 10.2),
               'SI-03SP:RF-CryoMod-1:BT171_InLN2Temp-Mon':
               (self._gwidget('ledbt171'), 2, 95),
               'SI-03SP:RF-CryoMod-1:BT172_WaveguideElbowTemp-Mon':
               (self._gwidget('ledbt172'), 2, 95),
               'SI-03SP:RF-CryoMod-1:BT173_WaveguideElbowTemp-Mon':
               (self._gwidget('ledbt173'), 2, 205),
               'SI-03SP:RF-CryoMod-1:BT174_OutLN2Temp-Mon':
               (self._gwidget('ledbt174'), 2, 120),
               'SI-03SP:RF-CryoMod-1:BT181_FBTCavTemp-Mon':
               (self._gwidget('ledbt181'), 2, 40),
               'SI-03SP:RF-CryoMod-1:BT182_FBTCavTemp-Mon':
               (self._gwidget('ledbt182'), 2, 205),
               'SI-03SP:RF-CryoMod-1:BT183_RBTCavTemp-Mon':
               (self._gwidget('ledbt183'), 2, 50),
               'SI-03SP:RF-CryoMod-1:BT184_RBTCavTemp-Mon':
               (self._gwidget('ledbt184'), 2, 100),
               'SI-03SP:RF-CryoMod-1:BT131_WaveguideHexTemp-Mon':
               (self._gwidget('ledbt131'), 2, 20),
               'SI-03SP:RF-CryoMod-1:BT132_WaveguideHexTemp-Mon':
               (self._gwidget('ledbt132'), 2, 50),
            },
            'sensor_flow2': {
                'SI-03SP:RF-CryoMod-2:BF2611_RFWindowWaterFlow-Mon':
                (self._gwidget('ledbf2611'), 12, 15.5),
                'SI-03SP:RF-CryoMod-2:BF2621_FBTWaterFlow-Mon':
                (self._gwidget('ledbf2621'), 1.1, 1.7),
                'SI-03SP:RF-CryoMod-2:BF2622_FBTWaterFlow-Mon':
                (self._gwidget('ledbf2622'), 0.8, 1.5),
                'SI-03SP:RF-CryoMod-2:BF2623_FBTWaterFlow-Mon':
                (self._gwidget('ledbf2623'), 1.1, 1.8),
                'SI-03SP:RF-CryoMod-2:BF2631_RBTWaterFlow-Mon':
                (self._gwidget('ledbf2631'), 1.1, 1.7),
                'SI-03SP:RF-CryoMod-2:BF2632_RBTWaterFlow-Mon':
                (self._gwidget('ledbf2632'), 1.1, 1.7),
                'SI-03SP:RF-CryoMod-2:BF2633_RBTWaterFlow-Mon':
                (self._gwidget('ledbf2633'), 1.1, 1.6),
                'SI-03SP:RF-CryoMod-2:BF2641_TaperWaterFlow-Mon':
                (self._gwidget('ledbf2641'), 3.5, 5),
                'SI-03SP:RF-CryoMod-2:BF235_HexLineGHeFlow-Mon':
                (self._gwidget('ledbf235'), 35, 55),
                'SI-03SP:RF-CryoMod-2:BF276_VentLineLN2Flow-Mon':
                (self._gwidget('ledbf276'), 60, 120),
            },
            'temp_celcius2': {
                'SI-03SP:RF-CryoMod-2:BT206_RFWindowTemp-Mon':
                (self._gwidget('ledbt206'), 0, 115),
                'SI-03SP:RF-CryoMod-2:BT207_RFWindowTemp-Mon':
                (self._gwidget('ledbt207'), 0, 115),
                'SI-03SP:RF-CryoMod-2:BT208_RFWindowTemp-Mon':
                (self._gwidget('ledbt208'), 0, 115),
                'SI-03SP:RF-CryoMod-2:BT209_RFWindowTemp-Mon':
                (self._gwidget('ledbt209'), 0, 115),
                'SI-03SP:RF-CryoMod-2:BT233_HexLineGHeTemp-Mon':
                (self._gwidget('ledbt233'), 15, 45),
                'SI-03SP:RF-CryoMod-2:BT275_VentLineLN2Temp-Mon':
                (self._gwidget('ledbt275'), 10, 45),
                'SI-03SP:RF-CryoMod-2:BT285_WaveguideHexCoilTemp-Mon':
                (self._gwidget('ledbt285'), -240, 25),
                'SI-03SP:RF-CryoMod-2:BT286_WaveguideElbowCoilTemp-Mon':
                (self._gwidget('ledbt286'), -200, 25),
                'SI-03SP:RF-CryoMod-2:BT291_FBTFlangeTemp-Mon':
                (self._gwidget('ledbt291'), 2, 45),
                'SI-03SP:RF-CryoMod-2:BT292_RBTFlangeTemp-Mon':
                (self._gwidget('ledbt292'), 15, 45),
                'SI-03SP:RF-CryoMod-2:BT298_VentLineTemp-Mon':
                (self._gwidget('ledbt298'), 15, 45),
                'SI-03SP:RF-CryoMod-2:BT299_VentLineTemp-Mon':
                (self._gwidget('ledbt299'), 15, 45),
            },
            'temp_kelvin2': {
               'SI-03SP:RF-CryoMod-2:BT210_HeVesselHeaterTemp-Mon':
               (self._gwidget('ledbt210'), 2, 10),
               'SI-03SP:RF-CryoMod-2:BT211_CavBotTemp-Mon':
               (self._gwidget('ledbt211'), 1, 12),
               'SI-03SP:RF-CryoMod-2:BT212_CavTopTemp-Mon':
               (self._gwidget('ledbt212'), 1, 12),
               'SI-03SP:RF-CryoMod-2:BT213_WaveguideCavTemp-Mon':
               (self._gwidget('ledbt213'), 1, 13),
               'SI-03SP:RF-CryoMod-2:BT214_WaveguideCavTemp-Mon':
               (self._gwidget('ledbt214'), 1, 300),
               'SI-03SP:RF-CryoMod-2:BT271_InLN2Temp-Mon':
               (self._gwidget('ledbt271'), 2, 96),
               'SI-03SP:RF-CryoMod-2:BT272_WaveguideElbowTemp-Mon':
               (self._gwidget('ledbt272'), 2, 95),
               'SI-03SP:RF-CryoMod-2:BT273_WaveguideElbowTemp-Mon':
               (self._gwidget('ledbt273'), 2, 120),
               'SI-03SP:RF-CryoMod-2:BT274_OutLN2Temp-Mon':
               (self._gwidget('ledbt274'), 92, 96),
               'SI-03SP:RF-CryoMod-2:BT281_FBTCavTemp-Mon':
               (self._gwidget('ledbt281'), 2, 230),
               'SI-03SP:RF-CryoMod-2:BT282_FBTCavTemp-Mon':
               (self._gwidget('ledbt282'), 2, 40),
               'SI-03SP:RF-CryoMod-2:BT283_RBTCavTemp-Mon':
               (self._gwidget('ledbt283'), 2, 50),
               'SI-03SP:RF-CryoMod-2:BT284_RBTCavTemp-Mon':
               (self._gwidget('ledbt284'), 2, 95),
               'SI-03SP:RF-CryoMod-2:BT231_WaveguideHexTemp-Mon':
               (self._gwidget('ledbt231'), 2, 25),
               'SI-03SP:RF-CryoMod-2:BT232_WaveguideHexTemp-Mon':
               (self._gwidget('ledbt232'), 2, 60),
            }
        }


class AllSubsys:
    """Gerencia o grupo SI e atualiza a label alarmsi."""

    def __init__(self, janela_opr):
        """."""
        janela_opr.alarmsi.clicked.connect(self.aba_si)
        self.janela_opr = janela_opr
        self.subjanelas = []

        self.psfamilysi = Si_psfamily(janela_opr, janela_opr.btnpsfamilysi)
        self.skewquad = Si_skewquad(janela_opr, janela_opr.btnskewquad)
        self.trims = Si_trims(janela_opr, janela_opr.btntrims)
        self.ffwcorr = Si_ffwcorr(janela_opr, janela_opr.btnffwcorr)
        self.corrsi = Si_slowcorr(janela_opr, janela_opr.btncorrsi)
        self.fcorrsi = Si_corrfast(janela_opr, janela_opr.btnfcorrsi)

        self.vacsi = Vacuum(janela_opr, janela_opr.btnvacsi)
        self.cavitysi = Cavity(janela_opr, janela_opr.btncavitysi)

        self.tempdclinks = Si_dclinks(janela_opr, janela_opr.btntempdclinks)
        self.tempmagnets = Si_magnets(janela_opr, janela_opr.btntempmagnets)
        self.tempcamvac = Si_camvac(janela_opr, janela_opr.btntempcamvac)
        self.tempconecserv = Si_conecserv(janela_opr, janela_opr.
                                          btntempconecserv)
        self.temprackint = Si_rackint(janela_opr, janela_opr.btntemprackint)
        self.temprackps = Si_racksimar(janela_opr, janela_opr.btnrackps)
        self.temprackpu = Si_rackpu(janela_opr, janela_opr.btnrackpu)
        self.tempcirchid = Si_circhid(janela_opr, janela_opr.btntempcirchid)

        # Adiciona todas as subjanelas à lista
        self.subjanelas.extend([
            self.psfamilysi,
            self.skewquad,
            self.trims,
            self.ffwcorr,
            self.corrsi,
            self.fcorrsi,

            self.vacsi,
            self.cavitysi,

            self.tempdclinks,
            self.tempmagnets,
            self.tempcamvac,
            self.tempconecserv,
            self.temprackint,
            self.temprackps,
            self.temprackpu,
            self.tempcirchid,
        ])

        # Configura cada subjanela
        for sub in self.subjanelas:
            sub.configurar_sistema()

        self.alarm_ctrl = AlarmDelayController(
            janela_opr,
            alarm_btn_name="alarmsi",
            delay_ms=4500
        )

    def atualizar_grupo(self):
        """Atualiza as subjanelas e delega lógica ao controlador."""
        falha_detectada = False
        for sub in self.subjanelas:
            sub.atualizar_status()
            falha_detectada |= not sub.estado_ok

        # Só o alarme geral é atualizado pelo controlador
        self.alarm_ctrl.atualizar(falha_detectada)

    def aba_si(self):
        """."""
        try:
            self.janela_opr.janela_opr.setCurrentIndex(5)
        except Exception as e:
            logging.error(f"Erro ao mudar para aba SI: {e}")
