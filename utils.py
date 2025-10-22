"""Funções utilitárias de leitura de PVs e atualização de LEDs."""
import logging

import epics
from epics import caget
from PyQt5 import QtWidgets

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")


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


def verificar_linactemp(signal: str, led: QtWidgets.QLabel, temp_lower:
                        float, temp_upper: float, timeout: float = 0):
    """Atualiza estado do LED baseado na faixa de temperatura."""
    pv = epics.get_pv(signal)
    if pv.connected:
        temperatura = pv.value
        led.state = (temp_lower <= temperatura <= temp_upper)
    else:
        logging.warning(f"Timeout lendo {signal}.")
        led.state = False
    # try:
    #     temperatura = caget(signal, timeout=timeout)
    #     if temperatura is None:
    #         logging.warning(f"Timeout lendo {signal}.")
    #         led.state = False
    #     else:
    #         led.state = (temp_lower <= temperatura <= temp_upper)
    # except Exception as e:
    #     logging.error(f"Erro lendo {signal}: {e}")
    #     led.state = False


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
                logging.error(f"Valor inválido para pressão em {signal}: {pressao}")
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


def verificar_ltbvac(signal: str, led: QtWidgets.QLabel, pressao_max: float,
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
                logging.error(f"Valor inválido para pressão em {signal}: {pressao}")
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


def verificar_templtb(signal: str, led: QtWidgets.QLabel, temp_lower:
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


def verificar_vaclts(signal: str, led: QtWidgets.QLabel, pressao_max: float,
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
                logging.error(f"Valor inválido para pressão em {signal}: {pressao}")
                led.state = False
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_templts(signal: str, led: QtWidgets.QLabel, temp_lower:
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


def verificar_tempbo(signal: str, led: QtWidgets.QLabel, temp_lower:
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


def verificar_vacbo(signal: str, led: QtWidgets.QLabel, pressao_max: float,
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
                logging.error(f"Valor inválido para pressão em {signal}:{pressao}")
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
                logging.error(f"Valor inválido para pressão em {signal}:{pressao}")
                led.state = False
    except Exception as e:
        logging.error(f"Erro lendo {signal}: {e}")
        led.state = False


def verificar_temprackpu(signal: str, led: QtWidgets.QLabel, temp_lower:
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


def verificar_temprackps(signal: str, led: QtWidgets.QLabel, temp_lower:
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


def verificar_temprackint(signal: str, led: QtWidgets.QLabel, temp_lower:
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


def verificar_tempcamvac(signal: str, led: QtWidgets.QLabel, temp_lower:
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


def verificar_tempcirchid(signal: str, led: QtWidgets.QLabel, temp_lower:
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


def verificar_tempconecserv(signal: str, led: QtWidgets.QLabel, temp_lower:
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


def verificar_tempmagnets(signal: str, led: QtWidgets.QLabel, temp_lower:
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


def verificar_temphls(signal: str, led: QtWidgets.QLabel, temp_lower:
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


def verificar_tempdclinks(signal: str, led: QtWidgets.QLabel, temp_lower:
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
        estilo_base = f"border-radius: 7px; border: 1px solid black; background-color: {cor};"
        led.setStyleSheet(estilo_base)
    else:
        # Preserva estilo original, substituindo apenas a cor
        partes = [parte.strip() for parte in estilo_original.split(';') if
                  parte and "background-color" not in parte]
        partes.append(f"background-color: {cor}")
        led.setStyleSheet('; '.join(partes))
