import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


def multiline(xs, ys, c, ax=None, **kwargs):
    """
    Plot lines with different colorings

    Args:
        xs: iterable container of x coordinates
        ys: iterable container of y coordinates
        c: iterable container of numbers mapped to colormap
        ax (optional): Axes to plot on.
        **kwargs (optional): passed to LineCollection

    Returns:
        lc : LineCollection instance.
    """

    # find axes
    ax = plt.gca() if ax is None else ax

    # Ensure every passed values are ``numpy.array``
    xs = np.array(xs)
    ys = np.array(ys)
    c = np.array(c)

    # Check if ``xs`` has the same shape as ``ys``. If not, assume all ``ys``
    # will share the same ``xs``
    if np.shape(xs) != np.shape(ys):
        xs = np.array([xs for i in range(len(ys))])
    else:
        pass

    # create LineCollection
    segments = [np.column_stack([x, y]) for x, y in zip(xs, ys)]
    lc = LineCollection(segments, **kwargs)

    # set coloring of line segments
    lc.set_array(np.asarray(c))

    # add lines to axes and rescale
    ax.add_collection(lc)
    ax.autoscale()
    return lc
