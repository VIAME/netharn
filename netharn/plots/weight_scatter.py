import numpy as np
from os.path import join


def plot_weight_scatter(harn):
    """
    Draw a scatter plot of the initial weights versus the final weights of a
    network.

    Example:
        >>> import netharn as nh
        >>> harn = nh.FitHarn.demo()
        >>> harn.run()

    Ignore:
        >>> from netharn.examples import mnist
        >>> import kwplot
        >>> kwplot.autompl(force='agg')
        >>> kwplot.set_mpl_backend('agg')
        >>> harn = mnist.setup_harn()
        >>> harn.preferences['eager_dump_tensorboard'] = 0
        >>> harn.run()
    """
    import netharn as nh
    cpu = nh.XPU.coerce('cpu')

    path1 = join(harn.train_dpath, 'initial_state', 'initial_state.pt')
    state1 = cpu.load(path1)
    weights1 = state1['model_state_dict']

    path2 = harn.best_snapshot()
    state2 = cpu.load(path2)
    weights2 = state2['model_state_dict']

    keys1 = set(weights1.keys())
    keys2 = set(weights2.keys())
    keys = keys1 & keys2

    assert keys == keys2

    accum1 = []
    accum2 = []

    for key in keys:
        w1 = weights1[key]
        w2 = weights2[key]
        accum1.append(w1.numpy().ravel())
        accum2.append(w2.numpy().ravel())

    points1 = np.hstack(accum1)
    points2 = np.hstack(accum2)

    # Find cosine of angle between the vectors
    import scipy
    cosangle = scipy.spatial.distance.cosine(points1, points2)

    import kwplot
    plt = kwplot.autoplt()

    import seaborn
    x = points1[::1]
    y = points2[::1]

    ax = plt.gca()
    ax.figure.clf()

    # seaborn.kdeplot(x, y, shade=True, gridsize=20)
    ax = plt.gca()
    ax.scatter(x, y, s=3, alpha=0.5, c='orange')
    ax.set_xlabel('initial weights')
    ax.set_ylabel('trained weights')
