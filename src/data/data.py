import numpy as np
import skimage.io as skio
import skimage.color as skcolor

from src.utils import project_root


def forse_rgb(image: np.ndarray) -> np.ndarray:
    if len(image.shape) == 2:
        image = skcolor.gray2rgb(image)
    if image.shape[2] == 4:
        image = skcolor.rgba2rgb(image) * 255
        image = image.astype(np.uint8)
    return image


def imread(fname: str) -> np.ndarray:
    image = skio.imread(fname)
    image = forse_rgb(image)
    return image


def add_noise(image: np.ndarray, p=0.5, value=0) -> np.ndarray:
    indexes = np.random.rand(*image.shape[:2]) > p
    noise_image = image.copy()
    noise_image[indexes < p] = value
    return noise_image
