import numpy as np


def MSE(A: np.ndarray, B: np.ndarray, ax: int = None):
    """
    Mean Squared Error
    :param A:
    :param B:
    :param ax:
    ax=0 the average is performed along the row, for each column, returning an array
    ax=1 the average is performed along the column, for each row, returning an array
    ax=None the average is performed element-wise along the array, returning a scalar value
    :return:
    """
    return np.square(A - B).mean(axis=ax)


def PSNR(A: np.ndarray, B: np.ndarray, max_value: int = 255) -> float:
    """
    Peak Signal-to-Noise Ratio
    :param A: original image
    :param B: noise image
    :return:
    """
    assert A.shape == B.shape, "Shapes should be equal"
    return 20 * np.log10(max_value / MSE(A, B))
