# neuronDetector
Detect activated neurons in video files
Project started in May 2018 to analyse videos of neurons on chips.



## Do it with Fiji (ImageJ)

### steps

- Plot I(t)
    - Image -> Stacks -> Plot Z-axis profile

- Compute Median (or Mean)
    - Image->Stacks -> Z-project (Average Intensity).
- Substract median
    - Process-> Image Calculator...
    - (Image1:Original_Stack,   Operation: Subtract, Image2: AVG_Original_Stack or Median)
- threshold
    - stack histogram (to apply same threshold to all images)
    - take a value and apply the same to all files (e.g. 60)

### Bibliography
- http://imagej.1557.x6.nabble.com/subtracting-average-td3693882.html
- https://imagej.net/Spot_Intensity_Analysis
- https://imagej.net/Image_Intensity_Processing
- https://imagej.nih.gov/ij/developer/api/ij/plugin/filter/MaximumFinder.html
- https://imagej.nih.gov/ij/plugins/multitracker.html
- https://www.unige.ch/medecine/bioimaging/files/1914/1208/6000/Quantification.pdf
- [compute and remove mean for each image](https://imagej.nih.gov/ij/macros/SubractMeasuredBackground.txt)
- [collection of macro](http://microscopynotes.com/imagej/macros/useful_collection_v100.txt)


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
