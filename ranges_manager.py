"""."""
# ranges_manager.py
import logging
import json
import os

RANGES_FILE = "ranges.json"


class RangesManager:
    """Gerencia ranges de temperatura de todos os subsistemas."""

    def __init__(self):
        """."""
        # ranges iniciais para cada subsistema
        self.default_ranges = {
            "linac": {
                'KlyArea': (18, 23),
                'KlyTemp': (18, 23),
                'Tunnel': (22, 24),
                'Umid': (40, 51),
                '45C': (42, 46),
                'Solenoid': (20, 27),
            },
            "ltb": {
                'Septum': (22, 26),
                'Dipolo': (22, 26),
                'Board': (38, 42),
            },
            "lts": {
                'Septts01': (22, 27),
                'SeptEje': (22, 27),
                'Septts04': (22, 27),
                'Septts04b': (22, 27),
            },
            "bo": {
                'Group01_05': (19, 25),
                'Group06_10': (19, 25),
                'Group11_15': (19, 25),
                'Group16_20': (19, 25),
                'Group21_25': (19, 25),
                'Group26_30': (19, 25),
                'Group31_35': (19, 25),
                'Group36_40': (19, 25),
                'Group41_45': (19, 25),
                'Group46_50': (19, 25),
            },
        }

        # tenta carregar ranges salvos
        self.ranges = self._load_ranges()

    def _load_ranges(self):
        """Carrega ranges do arquivo JSON, ou usa os padrões."""
        if os.path.exists(RANGES_FILE):
            try:
                with open(RANGES_FILE, "r") as f:
                    data = json.load(f)
                # converte listas para tuplas
                for subsys, grupos in data.items():
                    for g, vals in grupos.items():
                        data[subsys][g] = (
                            round(float(vals[0]), 2), round(float(vals[1]), 2)
                            )
                return data
            except Exception as e:
                logging.error(f"Erro ao carregar ranges: {e}")
        return self.default_ranges.copy()

    def _save_ranges(self):
        """Salva ranges atuais no arquivo JSON."""
        try:
            # converter todos valores para float antes de salvar
            data = {
                subsys: {
                    g: [round(v[0], 2), round(v[1], 2)] for g, v in grupos.
                    items()
                    }
                for subsys, grupos in self.ranges.items()
            }
            with open(RANGES_FILE, "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logging.error(f"Erro ao salvar ranges: {e}")

    def get_ranges(self, subsys: str):
        """Retorna ranges do subsistema especificado."""
        return self.ranges.get(subsys, {})

    def update_range(
            self, subsys: str, grupo: str, min_val: float, max_val: float
            ):
        """Atualiza range de um grupo específico e salva persistente."""
        if subsys in self.ranges and grupo in self.ranges[subsys]:
            self.ranges[subsys][grupo] = (min_val, max_val)
            logging.info(
                f"Range atualizado para {subsys}/{grupo}: {min_val}-{max_val}"
            )
            self._save_ranges()
