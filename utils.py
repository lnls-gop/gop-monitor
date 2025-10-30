"""Funções utilitárias de leitura de PVs e atualização de LEDs."""
import logging
import epics
from epics import caget
from PyQt5 import uic, QtWidgets


logging.basicConfig(level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")


def verificar_temp(
        signal: str, led: QtWidgets.QLabel, temp_lower:
        float, temp_upper: float, timeout: float = 0):
    """Atualiza estado do LED baseado na faixa de temperatura."""
    try:
        temperatura = caget(signal, timeout=timeout)
        if temperatura is None:
            logging.warning(f"Timeout lendo {signal}.")
            led.state = False
        else:
            led.state = (temp_lower <= temperatura <= temp_upper)
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_ledinfobeam(signal: str, led: QtWidgets.QLabel, estado_esperado,
                          timeout: float = 0):
    """Verifica estado do PV (bool/int) e atualiza o LED."""
    try:
        estado = caget(signal, timeout=timeout)
        if estado is None:
            logging.warning(f"Timeout lendo {signal}.")
            led.state = False
        else:
            led.state = (estado == estado_esperado)
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_ledlowlevel(signal: str, led: QtWidgets.QLabel,
                          estado_esperado: int = 1, timeout: float = 0):
    """."""
    try:
        estado = caget(signal, timeout=timeout)
        if estado is None:
            logging.warning(f"Timeout lendo {signal}.")
            led.state = False
        else:
            led.state = (estado == estado_esperado)
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_vacuo(signal: str, led: QtWidgets.QLabel, pressao_min: float,
                    timeout: float = 0):
    """Verifica se a pressão está dentro do limite e atualiza o LED."""
    try:
        pressao = caget(signal, timeout=timeout)
        if pressao is None:
            logging.warning(f"Timeout lendo {signal}.")
            led.state = False
        else:
            try:
                pressao_float = float(pressao)
                led.state = (pressao_float <= pressao_min)
            except ValueError:
                logging.error(
                    f"Valor inválidopara pressão em {signal}: {pressao}")
                led.state = False
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_ledpslinac(signal: str, led: QtWidgets.QLabel, estado_esperado:
                         int, timeout: float = 0):
    """."""
    try:
        estado = caget(signal, timeout=timeout)
        if estado is None:
            logging.warning(f"Timeout ou falha de conexão com {signal}")
            led.state = False
        else:
            led.state = (estado == estado_esperado)
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_ltbvac(signal: str, led: QtWidgets.QLabel, pressao_min: float,
                     timeout: float = 0):
    """Verifica se a pressão está dentro do limite e atualiza o LED."""
    try:
        pressao = caget(signal, timeout=timeout)
        if pressao is None:
            logging.warning(f"Timeout lendo {signal}.")
            led.state = False
        else:
            try:
                pressao_float = float(pressao)
                led.state = (pressao_float <= pressao_min)
            except ValueError:
                logging.error(
                    f"Valor inválido para pressão em {signal}: {pressao}")
                led.state = False
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_psltb(signal: str, led: QtWidgets.QLabel, estado_esperado:
                    int, timeout: float = 0):
    """."""
    try:
        estado = caget(signal, timeout=timeout)
        if estado is None:
            logging.warning(f"Timeout ou falha de conexão com {signal}")
            led.state = False
        else:
            led.state = (estado == estado_esperado)
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_vaclts(signal: str, led: QtWidgets.QLabel, pressao_min: float,
                     timeout: float = 0):
    """Verifica se a pressão está dentro do limite e atualiza o LED."""
    try:
        pressao = caget(signal, timeout=timeout)
        if pressao is None:
            logging.warning(f"Timeout lendo {signal}.")
            led.state = False
        else:
            try:
                pressao_float = float(pressao)
                led.state = (pressao_float <= pressao_min)
            except ValueError:
                logging.error(
                    f"Valor inválido para pressão em {signal}: {pressao}")
                led.state = False
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_pslts(signal: str, led: QtWidgets.QLabel, estado_esperado:
                    int, timeout: float = 0):
    """."""
    try:
        estado = caget(signal, timeout=timeout)
        if estado is None:
            logging.warning(f"Timeout ou falha de conexão com {signal}")
            led.state = False
        else:
            led.state = (estado == estado_esperado)
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_psbo(signal: str, led: QtWidgets.QLabel, estado_esperado:
                   int, timeout: float = 0):
    """."""
    try:
        estado = caget(signal, timeout=timeout)
        if estado is None:
            logging.warning(f"Timeout ou falha de conexão com {signal}")
            led.state = False
        else:
            led.state = (estado == estado_esperado)
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_vacbo(signal: str, led: QtWidgets.QLabel, pressao_min: float,
                    timeout: float = 0):
    """Verifica se a pressão está dentro do limite e atualiza o LED."""
    try:
        pressao = caget(signal, timeout=timeout)
        if pressao is None:
            logging.warning(f"Timeout lendo {signal}.")
            led.state = False
        else:
            try:
                pressao_float = float(pressao)
                led.state = (pressao_float <= pressao_min)
            except ValueError:
                logging.error(
                    f"Valor inválido para pressão em {signal}:{pressao}")
                led.state = False
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_bocavity(signal: str, led: QtWidgets.QLabel, temp_lower:
                       float, temp_upper: float, timeout: float = 0):
    """Atualiza estado do LED baseado na faixa de temperatura."""
    try:
        temperatura = caget(signal, timeout=timeout)
        if temperatura is None:
            logging.warning(f"Timeout lendo {signal}.")
            led.state = False
        else:
            led.state = (temp_lower <= temperatura <= temp_upper)
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_vacsi(signal: str, led: QtWidgets.QLabel, pressao_max: float,
                    timeout: float = 0):
    """Verifica se a pressão está dentro do limite e atualiza o LED."""
    try:
        pressao = caget(signal, timeout=timeout)
        if pressao is None:
            logging.warning(f"Timeout lendo {signal}.")
            led.state = False
        else:
            try:
                pressao_float = float(pressao)
                led.state = (pressao_float <= pressao_max)
            except ValueError:
                logging.error(
                    f"Valor inválido para pressão em {signal}:{pressao}")
                led.state = False
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_psfamilysi(signal: str, led: QtWidgets.QLabel, estado_esperado:
                         int, timeout: float = 0):
    """."""
    try:
        estado = caget(signal, timeout=timeout)
        if estado is None:
            logging.warning(f"Timeout ou falha de conexão com {signal}")
            led.state = False
        else:
            led.state = (estado == estado_esperado)
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_skewquad(signal: str, led: QtWidgets.QLabel, estado_esperado:
                       int, timeout: float = 0):
    """."""
    try:
        estado = caget(signal, timeout=timeout)
        if estado is None:
            logging.warning(f"Timeout ou falha de conexão com {signal}")
            led.state = False
        else:
            led.state = (estado == estado_esperado)
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_trims(signal: str, led: QtWidgets.QLabel, estado_esperado:
                    int, timeout: float = 0):
    """."""
    try:
        estado = caget(signal, timeout=timeout)
        if estado is None:
            logging.warning(f"Timeout ou falha de conexão com {signal}")
            led.state = False
        else:
            led.state = (estado == estado_esperado)
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_ffwcorr(signal: str, led: QtWidgets.QLabel, estado_esperado:
                      int, timeout: float = 0):
    """."""
    try:
        estado = caget(signal, timeout=timeout)
        if estado is None:
            logging.warning(f"Timeout ou falha de conexão com {signal}")
            led.state = False
        else:
            led.state = (estado == estado_esperado)
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_corrsi(signal: str, led: QtWidgets.QLabel, estado_esperado:
                     int, timeout: float = 0):
    """."""
    try:
        estado = caget(signal, timeout=timeout)
        if estado is None:
            logging.warning(f"Timeout ou falha de conexão com {signal}")
            led.state = False
        else:
            led.state = (estado == estado_esperado)
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_fcorrsi(signal: str, led: QtWidgets.QLabel, estado_esperado:
                      int, timeout: float = 0):
    """."""
    try:
        estado = caget(signal, timeout=timeout)
        if estado is None:
            logging.warning(f"Timeout ou falha de conexão com {signal}")
            led.state = False
        else:
            led.state = (estado == estado_esperado)
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_pwmsi(signal: str, led: QtWidgets.QLabel, temp_lower:
                    float, temp_upper: float, timeout: float = 0):
    """Atualiza estado do LED baseado na faixa de temperatura."""
    try:
        temperatura = caget(signal, timeout=timeout)
        if temperatura is None:
            logging.warning(f"Timeout lendo {signal}.")
            led.state = False
        else:
            led.state = (temp_lower <= temperatura <= temp_upper)
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def atualizar_led_visual(led: QtWidgets.QLabel):
    """Atualiza a cor do LED preservando estilo original."""
    cor = "rgb(0,168,0)" if getattr(led, "state", False) else "rgb(207,0,0)"
    estilo_original = led.styleSheet().strip()

    if not estilo_original:
        # Estilo base para LEDs sem estilo definido no Qt Designer
        estilo_base = f"border-radius: 7px; border: 1px solid black;background-color: {cor};"
        led.setStyleSheet(estilo_base)
    else:
        # Preserva estilo original, substituindo apenas a cor
        partes = [parte.strip() for parte in estilo_original.split(';') if
                  parte and "background-color" not in parte]
        partes.append(f"background-color: {cor}")
        led.setStyleSheet('; '.join(partes))


class ConnWidgetPVs(QtWidgets.QWidget):
    """."""

    def __init__(self, janela_opr, botao_menu, ui_fname, check_type):
        """."""
        super().__init__()
        self.pvs = None
        self.check_type = check_type
        self.janela_opr = janela_opr
        self.botao_menu = botao_menu
        self.uiobj = uic.loadUi(ui_fname)
        self.sinais = None
        self._registrar_grupos()
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

    def _connect_pvs(self):
        self.pvs = dict()
        for pvname, _ in self.sinais.items():
            self.pvs[pvname] = epics.PV(pvname, connection_timeout=None)

    def configurar_sistema(self):
        """Conecta sinais da janela principal e prepara a subjanela."""
        # Botão/ação que mostra/oculta a janela de temperatura
        self.botao_menu.clicked.connect(self.mostrar_janela)
        # Primeira atualização inicial
        self.atualizar_status()

    def mostrar_janela(self):
        """Exibe/oculta a interface gráfica."""
        self.uiobj.setVisible(not self.uiobj.isVisible())

    def atualizar_status(self):
        """Atualiza LEDs da subjanela e define estado_ok."""

        if self.check_type == 'temp':

            todos_ok = True

            for pvname, value in self.sinais.items():
                led, temp_min, temp_max = value
                verificar_temp(pvname, led, temp_min, temp_max)
                if not getattr(led, "state", False):
                    todos_ok = False

            self.estado_ok = todos_ok

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")

        elif self.check_type == 'vacuo':

            todos_ok = True

            for pvname, value in self.sinais.items():
                led, pressao_min = value
                verificar_vacbo(
                    pvname, led, pressao_min=pressao_min)
                if not getattr(led, "state", False):
                    todos_ok = False
            self.estado_ok = todos_ok

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")

            # Atualiza label de alarme da subjanela
            alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel,
                                                      "alarmvacuo")

        elif self.check_type == 'psbo':

            todos_ok = True

            for pvname, value in self.sinais.items():
                led, estado_esperado = value
                verificar_psbo(
                    pvname, led, estado_esperado=estado_esperado)
                if not getattr(led, "state", False):
                    todos_ok = False

            self.estado_ok = todos_ok

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")

            # Atualiza a label de alarme do bloco LOWLEVEL
            alarme_widget = self.janela_opr.findChild(
                QtWidgets.QLabel, "alarmpsbo")

        elif self.check_type == 'bocavity':

            todos_ok = True

            for pvname, value in self.sinais.items():
                led, temp_min, temp_max = value
                verificar_bocavity(pvname, led, temp_min, temp_max)
                if not getattr(led, "state", False):
                    todos_ok = False

            self.estado_ok = todos_ok

            if self.botao_menu:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                self.botao_menu.setStyleSheet(f"background-color: {cor};")

            # Atualiza label de alarme da subjanela
            alarme_widget = self.janela_opr.findChild(QtWidgets.QLabel,
                                                      "alarmbocavity")

            if alarme_widget:
                cor = "rgb(0, 168, 0)" if todos_ok else "rgb(207, 0, 0)"
                alarme_widget.setStyleSheet(f"background-color: {cor};")
                alarme_widget.repaint()
                QtWidgets.QApplication.processEvents()
                alarme_widget.update()
