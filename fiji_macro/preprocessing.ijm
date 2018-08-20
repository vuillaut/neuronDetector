//\\ Video preprocessing to reveal objects illumination above 5 sigma

duplicate=0 // set to 1 if you want to create a duplicate image at each processing step

name=getTitle;
directory=getDirectory("image");


if(duplicate==1){
run("Duplicate...", "title=0.tif duplicate");
selectWindow("0.tif");
}

//\\ remove 10 first slides
// run("Slice Remover", "first=1 last=10 increment=1");

/*
// --- part to uncomment in case of calibration issues with the camera,
// such as strong illumination in the first slides
// or varying mean illumination during data taking

//\\ remove 10 first slides
// run("Slice Remover", "first=1 last=10 increment=1");

//\\ for each image, subtract its mean intensity
//\\ - this is done in order to compensate the mean luminosity variations
for (i=1; i<=nSlices; i++) {
  setSlice(i);
  run("Measure");
  mean = getResult("Mean");
  run("Subtract...", "value=" + mean);
}
*/

//\\ Subtract the video median to each slice.
//\\ Thus, this operation keeps only intensity variations from the median.

if(duplicate==1){
run("Duplicate...", "title=1.tif duplicate");
}

run("Z Project...", "projection=Median");


if(duplicate==1){
selectWindow("1.tif");
imageCalculator("Subtract create stack", name,"MED_"+"1.tif");
}

else{
imageCalculator("Subtract create stack", name,"MED_"+name);
close(name);
}


selectWindow("Result of " + name);
rename(name);

if(duplicate==1){
rename("2.tif");
}


//\\ Apply a Gaussian blur to remove very small details (= noise)
if(duplicate==1){
run("Duplicate...", "title=3.tif duplicate");
}

//
run("Gaussian Blur 3D...", "x=1 y=1 z=1");


//\\ Apply a threshold at 5 sigma to keep only intense variations
if(duplicate==1){
run("Duplicate...", "title=4.tif duplicate");
}

Stack.getStatistics(count, mean, min, max, std);
// print(mean, min, max, std);
cut = mean + 5 * std;
setAutoThreshold("Triangle dark stack");
setThreshold(cut, max);
setOption("BlackBackground", false);
run("Convert to Mask", "method=Triangle background=Dark");


//\\ Remove very small details that are left
if(duplicate==1){
run("Duplicate...", "title=5.tif duplicate");
}

run("Remove Outliers...", "radius=2 threshold=2 which=Dark stack");