"""Funções utilitárias de leitura de PVs e atualização de LEDs."""
import logging
from datetime import datetime, timedelta

import epics
from epics import get_pv
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer

from siriuspy.clientarch import ClientArchiver, Time


logging.basicConfig(level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")


def verificar_temp(
        signal: str, led: QtWidgets.QLabel, temp_lower:
        float, temp_upper: float):
    """Atualiza estado do LED baseado na faixa de temperatura."""
    try:
        # temperatura = caget(signal, timeout=timeout)
        pv = get_pv(signal)
        if not pv.connected:
            logging.warning(f"{signal} desconectado.")
            if led:
                led.state = False
            return False

        temperatura = pv.value
        status = (temp_lower <= temperatura <= temp_upper)
        if led:
            led.state = status

    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        if led:
            led.state = False

    return status


def verificar_estado(signal: str, led: QtWidgets.QLabel, estado_esperado):
    """Verifica estado do PV (bool/int) e atualiza o LED."""
    try:
        # estado = caget(signal, timeout=timeout)
        pv = get_pv(signal)
        if not pv.connected:
            logging.warning(f"{signal} desconectado.")
            if led:
                led.state = False
            return False

        estado = pv.value
        status = (estado == estado_esperado)
        if led:
            led.state = status

    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        if led:
            led.state = False

    return status


def verificar_vacuo(signal: str, led: QtWidgets.QLabel, pressao_min: float):
    """Verifica se a pressão está dentro do limite e atualiza o LED."""
    try:
        # pressao = caget(signal, timeout=timeout)
        pv = get_pv(signal)
        if not pv.connected:
            logging.warning(f"{signal} desconectado.")
            if led:
                led.state = False
            return False

        pressao = float(pv.value)
        status = (pressao <= pressao_min)
        if led:
            led.state = status

    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        if led:
            led.state = False

    return status


def atualizar_led_visual(led: QtWidgets.QLabel):
    """Atualiza a cor do LED preservando estilo original."""
    cor = "rgb(0,168,0)" if getattr(led, "state", False) else "rgb(207,0,0)"
    estilo_original = led.styleSheet().strip()

    if not estilo_original:
        # Estilo base para LEDs sem estilo definido no Qt Designer
        estilo_base = f"border-radius: 7px; border: 1px solid black;    background-color: {cor};"
        led.setStyleSheet(estilo_base)
    else:
        # Preserva estilo original, substituindo apenas a cor
        partes = [parte.strip() for parte in estilo_original.split(';') if
                  parte and "background-color" not in parte]
        partes.append(f"background-color: {cor}")
        led.setStyleSheet('; '.join(partes))


class ConnWidgetPVs:
    """."""

    def __init__(self, janela_opr, botao_menu, ui_fname, check_type):
        """."""
        super().__init__()
        self.pvs = None
        self.check_type = check_type
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.uiobj = uic.loadUi(ui_fname) if janela_opr else None
        self.sinais = None
        self._registrar_grupos()
        self._map_pvname_2_checkparams()
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

    def _map_pvname_2_checkparams(self):
        self.pvname2check = dict()
        for key, value_ in self.sinais.items():
            if isinstance(value_, dict):
                for pvname, value in value_.items():
                    self.pvname2check[pvname] = value
                    # led, temp_min, temp_max = value
            else:
                pvname = key
                value = value_
                self.pvname2check[pvname] = value

    def _connect_pvs(self):
        self.pvs = dict()
        self.pvs_status = dict()
        for key, value_ in self.sinais.items():
            if isinstance(value_, dict):
                for pvname, _ in value_.items():
                    self.pvs[pvname] = epics.PV(
                        pvname, connection_timeout=None)
                    self.pvs_status[pvname] = False
            else:
                pvname = key
                self.pvs[pvname] = epics.PV(
                    pvname, connection_timeout=None)
                self.pvs_status[pvname] = False

    @property
    def estado_ok(self):
        """."""
        return all(self.pvs_status.values())

    def _gwidget(self,  widget):
        return getattr(self.uiobj, widget) if self.uiobj else None

    def configurar_sistema(self):
        """Conecta sinais da janela principal e prepara a subjanela."""
        self.botao_menu.clicked.connect(self.mostrar_janela)
        self.atualizar_status()

    def mostrar_janela(self):
        """Exibe/oculta a interface gráfica."""
        self.uiobj.setVisible(not self.uiobj.isVisible())

    def callback_pvname(pvname, **kwargs):
        """."""

    def atualizar_status(self):
        """Atualiza LEDs da subjanela e define estado_ok."""
        if self.check_type == 'temp':

            for key, value_ in self.sinais.items():
                if isinstance(value_, dict):
                    for pvname, value in value_.items():
                        led, temp_min, temp_max = value
                        status = verificar_temp(
                            pvname, led, temp_min, temp_max)
                        self.pvs_status[pvname] = status
                else:
                    pvname, value = key, value_
                    led, temp_min, temp_max = value
                    status = verificar_temp(
                        pvname, led, temp_min, temp_max)
                    self.pvs_status[pvname] = status

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if self.estado_ok else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")

        elif self.check_type == 'vacuo':

            for key, value_ in self.sinais.items():
                if isinstance(value_, dict):
                    for pvname, value in value_.items():
                        led, pressao_min = value
                        status = verificar_vacuo(
                            pvname, led, pressao_min=pressao_min)
                        self.pvs_status[pvname] = status
                else:
                    pvname, value = key, value_
                    led, pressao_min = value
                    status = verificar_vacuo(
                        pvname, led, pressao_min=pressao_min)
                    self.pvs_status[pvname] = status

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if self.estado_ok else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")

        elif self.check_type == 'estado':

            for key, value_ in self.sinais.items():
                if isinstance(value_, dict):
                    for pvname, value in value_.items():
                        led, estado_esperado = value
                        status = verificar_estado(
                            pvname, led, estado_esperado=estado_esperado)
                        self.pvs_status[pvname] = status
                else:
                    pvname, value = key, value_
                    led, estado_esperado = value
                    status = verificar_estado(
                        pvname, led, estado_esperado=estado_esperado)
                    self.pvs_status[pvname] = status

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if self.estado_ok else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")

        else:
            errmsg = (
                'Atualizar status não está implementado para '
                f'{self.check_type}'
            )
            raise ValueError(errmsg)

    @staticmethod
    def create_archviewer_link(pvs_dict, start=None, end=None, ref=None):
        """."""
        if end is None:
            end = Time.now()
        if start is None:
            if isinstance(end, datetime):
                start = end - timedelta(hours=1)
            else:
                start = end - 60*60
        if ref is True:
            ref = start

        pvnames = list(pvs_dict.keys())
        url = ClientArchiver.gen_archviewer_url_link(
            pvnames,
            start,
            end,
            ref,
            None,
            None,
            False,
        )
        return url


class AlarmDelayController:
    """Controla atraso entre botão de condição e botão de alarme."""

    def __init__(self, janela_opr, alarm_btn_name: str, delay_ms: int = 5000):
        """."""
        self.janela_opr = janela_opr
        self.alarm_btn_name = alarm_btn_name
        self.delay_ms = delay_ms

        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self._confirmar_falha)
        self.falha_detectada = False

    def atualizar(self, falha_detectada: bool):
        """Atualiza apenas o botão de alarme geral com atraso."""
        if falha_detectada and not self.falha_detectada:
            self.falha_detectada = True
            self.timer.start(self.delay_ms)
        elif not falha_detectada and self.falha_detectada:
            self.falha_detectada = False
            self.timer.stop()
            self._atualizar_alarm(False)

        # Estado inicial
        if not self.falha_detectada and not falha_detectada:
            self._atualizar_alarm(False)

    def _confirmar_falha(self):
        if self.falha_detectada:
            self._atualizar_alarm(True)

    def _atualizar_alarm(self, falha: bool):
        alarm_btn = self.janela_opr.findChild(
            QtWidgets.QPushButton, self.alarm_btn_name
            )
        if alarm_btn:
            cor = "rgb(0, 168, 0)" if not falha else "rgb(207, 0, 0)"
            alarm_btn.setStyleSheet(f"background-color: {cor};")
