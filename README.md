# neuronDetector
Detect activated neurons in video files
Project started in May 2018 to analyse videos of neurons on chips.

Find the published stable version here:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1400718.svg)](https://doi.org/10.5281/zenodo.1400718)

## Fiji script

### 2d counter

Steps:
- remove first images


## Do it with Fiji (ImageJ)

### steps

- Plot I(t)
    - Image -> Stacks -> Plot Z-axis profile
    - Shows the evolution of the average of the image with time

- Compute Median (or Mean)
    - Image->Stacks -> Z-project (Average Intensity).
- Substract median
    - Process-> Image Calculator...
    - (Image1:Original_Stack,   Operation: Subtract, Image2: AVG_Original_Stack or Median)
- threshold
    - stack histogram (to apply same threshold to all images)
    - take a value and apply the same to all files (e.g. 60)

### Bibliography
#### Start here
- [introductive lessons in french](http://master-ivi.univ-lille1.fr/fichiers/Cours/ti-atelier-ImageJ-2009-03-18.pdf)
- [intro on segmentation with ImageJ](http://imagej.net/_images/8/87/Arganda-Carreras-Segmentation-Bioimage-course-MDC-Berlin-2016.pdf)
- [segmentation process with ImageJ](http://imagej.net/Segmentation#Preprocessing)

#### Get in the details

- http://imagej.1557.x6.nabble.com/subtracting-average-td3693882.html
- https://imagej.net/Spot_Intensity_Analysis
- https://imagej.net/Image_Intensity_Processing
- https://imagej.nih.gov/ij/developer/api/ij/plugin/filter/MaximumFinder.html
- https://imagej.nih.gov/ij/plugins/multitracker.html
- https://www.unige.ch/medecine/bioimaging/files/1914/1208/6000/Quantification.pdf
- [compute and remove mean for each image](https://imagej.nih.gov/ij/macros/SubractMeasuredBackground.txt)
- [collection of macro](http://microscopynotes.com/imagej/macros/useful_collection_v100.txt)
- [écart-type](https://fr.wikipedia.org/wiki/%C3%89cart_type)


----

# Python developments

## Environment and required libraries
> Make an environment.yml

## Install

## Example of usage

## Licence
?

## Bibliography
List of interesting readings that helped me to build the analysis (or could help to improve it)   
> .tex necessary?
