import numpy as np
from skimage import io
from skimage import filters
from skimage.restoration import denoise_wavelet
from skimage.feature import blob_doh
from skimage.morphology import binary_erosion, binary_dilation
import argparse
import display as d
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input file")
ap.add_argument("-o", "--output", required=True,
	help="path to output video")
args = vars(ap.parse_args())

filename = args('input')


class video_pipeline():

    def __init__(self, filename):
        self.filename = filename
        self.load_video()

    def load_video(self):
        self.original_video = io.imread(self.filename)
        self.current_video = self.original_video
        print("The file {3} contains {0} images of {1}x{2} pixels"
        .format(self.original_video.shape[0], self.original_video.shape[1],
                self.original_video.shape[2], self.filename))

    def filter_video(self):
        """
        apply gaussian filtering to smooth things
        """
        self.current_video = filters.gaussian(self.current_video, 1)

    def calibrate_video(self):
        """
        median correction (could also be mean)
        """
        self.current_video = self.current_video
        - np.median(self.current_video, axis=(1,2))[:,None,None]

    def differentiate_first_frame(self):
        """
        Compute difference with first frame
        """
        self.current_video = self.current_video - self.current_video[0]

    def denoise_video(self):
        """
        Wavelet Denoising
        """
        self.current_video = denoise_wavelet(self.current_video)

    def cut_video(self):
        """
        Apply 3 sigma threshold to each frame
        """
        global_thresh = np.array(list(map((lambda x: np.percentile(x, 95)),
            self.current_video)))
        self.current_video[self.current_video < global_thresh[:,None,None]] = 0

    def erose_video(self):
        self.current_video = np.array([binary_erosion(frame)
            for frame in self.current_video])

    def dilate_video(self):
        self.current_video = np.array([binary_dilation(frame)
            for frame in self.current_video])

    def find_blob(self, **kwargs):
        """
        Use `skimage.feature.blob_doh`
        """
        self.blobs = [blob_doh(image, **kwargs)
            for image in self.current_video]


def main(filename):

    pipeline = video_pipeline(filename)

    pipeline.filter_video()
    print("Video filtered")
    pipeline.calibrate_video()
    print("Video calibrated")
    pipeline.differentiate_first_frame()
    print("Video differentiated")
    pipeline.denoise_video()
    print("Video denoised")
    pipeline.cut_video()
    print("Video thresholded")
    pipeline.erose_video()
    print("Video eroded")
    pipeline.erose_video()
    print("Video eroded")
    pipeline.dilate_video()
    print("Video dilated")

    # Find blobs in each frame. Parameters have been optimized on one file.
    pipeline.find_blob(min_sigma=12, max_sigma=30)

    anim = d.display_video_blobs(pipeline.original_video, pipeline.blobs)
    anim.save(args("output") + "/blobs.mp4")

    return pipeline
