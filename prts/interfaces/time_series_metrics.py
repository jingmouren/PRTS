from typing import Any

import numpy as np


class InterfaceTimeSeriesMetrics:
    """ This class is interface for time series metrics """

    def score(self, real: np.ndarray, pred: np.ndarray) -> Any:
        """

        Args:
            real:
            pred:

        Returns:

        """
        ...