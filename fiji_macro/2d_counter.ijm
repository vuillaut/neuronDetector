//\\ remove 10 first slides
run("Slice Remover", "first=1 last=10 increment=1");
name=getTitle;
directory=getDirectory("image");

//\\ for each image, subtract its mean intensity
//\\ - this is done in order to compensate the mean luminosity variations
for (i=1; i<=nSlices; i++) {
  setSlice(i);
  run("Measure");
  mean = getResult("Mean");
  run("Subtract...", "value=" + mean);
}

//\\ Subtract the video median to each slice.
//\\ Thus, this operation keeps only intensity variations from the median.
// run("Duplicate...", "title=2.tif duplicate");
run("Z Project...", "projection=Median");
// selectWindow("2.tif");
imageCalculator("Subtract create stack", name,"MED_"+name);
close(name);
selectWindow("Result of " + name);
rename(name);

//\\ Apply a Gaussian blur to remove very small details (= noise)
// run("Duplicate...", "title=4.tif duplicate");
run("Gaussian Blur 3D...", "x=1 y=1 z=0.5");

//\\ Apply a threshold at 5 sigma to keep only intense variations
// run("Duplicate...", "title=5.tif duplicate");
Stack.getStatistics(count, mean, min, max, std);
// print(mean, min, max, std);
cut = mean + 5 * std;
setAutoThreshold("Triangle dark stack");
setThreshold(cut, max);
setOption("BlackBackground", false);
run("Convert to Mask", "method=Triangle background=Dark");

//\\ Remove very small details that are left
// run("Duplicate...", "title=6.tif duplicate");
run("Remove Outliers...", "radius=2 threshold=2 which=Dark stack");

//\\ 2D object counter
//\\ Count the number of neuron in each image and save the results in a .csv file
for (i=1; i<=nSlices; i++) {
	setSlice(i);
	run("Nucleus Counter", "smallest=100 largest=10000 threshold=Current smooth=[Mean 3x3] add show");
}
saveAs("Summary", directory + name + "_short_results.csv");
