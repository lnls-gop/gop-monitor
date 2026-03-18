"""Logica das subjanelas do Anel de Armazenamento."""
import logging
from PyQt5 import QtWidgets
import utils


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

        # Instancia as subjanelas passando o botão correto
        self.vacsi = Vacuum(janela_opr, janela_opr.btnvacsi)
        self.cavitysi = Cavity(janela_opr, janela_opr.btncavitysi)

        # Adiciona todas as subjanelas à lista
        self.subjanelas.extend([
            self.vacsi,
            self.cavitysi,
        ])

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

    def aba_si(self):
        """."""
        try:
            self.janela_opr.janela_opr.setCurrentIndex(5)
        except Exception as e:
            logging.error(f"Erro ao mudar para aba SI: {e}")
