import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import skimage as sk





def show_image(image, figsize=(12,12)):
    """
    simply display an Image
    """
    plt.figure(figsize=figsize)
    plt.imshow(image, cmap='gray')


def grid_view(video, **kwargs):
    """
    make a grid of 3 columns to display each frame of the video
    """
    nrow = len(video)//3+1*(len(video)%3>0)
    fig, axes = plt.subplots(nrow, 3,
                            figsize=(15,5*nrow))

    for i, im in enumerate(video):
        axes.flatten()[i].imshow(im, **kwargs)

    return axes


def display_video(video, figsize=(8,8), filename=None, **kwargs):
    """
    Display an animation of the video
    If filename is given (as a string), it saves the animation as a file
    Think about %matplotlib notebook in jupyter notebooks
    """
    fig = plt.figure(figsize=figsize)

    # ims is a list of lists
    # each row is a list of artists to draw in the current frame;
    # here we are just animating one artist, the image, in
    # each frame
    ims = []

    for v in video:
        im = plt.imshow(v, animated=True, **kwargs)
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims, interval=40, blit=True,
                                    repeat_delay=100)

    if not filename is None:
        try:
            ani.save(filename)
        except:
            print("Could not save")
            pass

    return ani


def plot_frame_stat(video, stat=np.mean, ax=None, **kwargs):
    """
    Compute the stat (np.mean, np.median, np.sum...) of each frame
    and plot the evolution in time
    You can also pass a lambda function, e.g.: (lambda x: np.min(x)/10)
    """

    ax = plt.gca() if ax is None else ax

    if not 'label' in kwargs:
        kwargs['label'] = str(stat)

    ax.plot(list(map(stat,video)), **kwargs)
    ax.set_xlabel("Frame #")
    ax.legend()

    return ax


def plot_blobs(blobs, ax=None):
    """
    Plot the blobs in an image
    """
    ax = plt.gca() if ax is None else ax

    for b in blobs:
        circle = (plt.Circle((b[1], b[0]), np.sqrt(2) * b[2], color='r', fill=False))
        ax.add_artist(circle)

    return ax


def plot_blobs_scatter(blobs, ax=None, **kwargs):
    """
    Version of blob plotting using only scatter and not Circle
    """
    ax = plt.gca() if ax is None else ax
    assert 's' not in kwargs, "the size of the rings is given by blobs array"

    if len(blobs) > 0:
        ax.scatter(blobs[:,1], blobs[:,0], s=blobs[:,2]*np.sqrt(2), **kwargs)

    return ax



def display_video_blobs(video, blobs, figsize=(8,8), filename=None, **kwargs):
    """
    Display an animation of the video
    If filename is given (as a string), it saves the animation as a file
    Think about %matplotlib notebook in jupyter notebooks
    """
    fig, ax = plt.subplots(figsize=figsize)

    # frame with most blobs
    blob_max = blobs[np.array([len(b) for b in blobs]).argmax()]

    # create as many circle
    patches = []
    for i in range(len(blob_max)):
        b = blob_max[i]
        patches.append(plt.Circle((b[1], b[0]), b[2]*np.sqrt(2), color='r', fill=False))

    def init():
        for patch in patches:
            patch.center = (0, 0)
            ax.add_patch(patch)
        return patches,

    def animate(i):
        [patch.set_visible(False) for patch in patches]
        ax.imshow(video[i], cmap='gray')

        blob = blobs[i]
        if len(blob)>0:
            for j, b in enumerate(blob):
                x = b[1]
                y = b[0]
                r = b[2] * np.sqrt(2)
                patches[j].center = (x,y)
                patches[j].set_radius(r)
                patches[j].set_visible(True)

        return patches,

    anim = animation.FuncAnimation(fig, animate,
                                   init_func=init,
                                   frames=len(video),
                                   interval=20,
                                   # blit=True,
                                   repeat=True,)

    if not filename is None:
        try:
            ani.save(filename)
        except:
            print("Could not save")
            pass

    return anim


def plot_hist_size_blobs(blobs, ax=None, **kwargs):
    """
    plot an histogram of the blobs sizes
    """
    ax = plt.gca() if ax is None else ax

    all_radius = [b[2] for blob in blobs for b in blob  if len(blob)>0]

    ax.hist(all_radius, **kwargs)

    return ax


def plot_number_blob(blobs, ax=None, **kwargs):
    """
    plot the number of blobs as a function of frames
    """
    ax = plt.gca() if ax is None else ax

    number_blob = [len(blob) for blob in blobs]

    ax.plot(number_blob, 'o-')
    ax.set_xlabel("Frame")

    return ax
