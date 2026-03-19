"""Ranges manager."""

import ast
import logging

# TODO: move alarms ranges file to csconst and loading mechanism to siriuspy


RANGES_FILE = "alarms_ranges.py"


class RangesManager:
    """Gerencia ranges de alarmes de todos os subsistemas."""

    def __init__(self):
        """."""
        self.ranges = ast.literal_eval(open(RANGES_FILE).read())

    def get_ranges(self, regime, subsys: str):
        """Retorna ranges do subsistema especificado."""
        return self.ranges[regime].get(subsys, {})

    def update_range(
        self,
        regime: str,
        subsys: str,
        grupo: str,
        min_val: float,
        max_val: float,
    ):
        """Atualiza range de um grupo específico e salva persistente."""
        if subsys in self.ranges and grupo in self.ranges[subsys]:
            self.ranges[regime][subsys][grupo] = (min_val, max_val)
            logging.info(
                f"Range atualizado para {regime}{subsys}/{grupo}: {min_val}-{max_val}"
            )
