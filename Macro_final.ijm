run("Slice Remover", "first=1 last=10 increment=1");
name=getTitle;
directory=getDirectory("image");


for (i=1; i<=nSlices; i++) {
  setSlice(i);
  run("Measure");
  mean = getResult("Mean");
  // run("32-bit");
  run("Subtract...", "value=" + mean);
}


// run("Duplicate...", "title=2.tif duplicate");
run("Z Project...", "projection=Median");
// selectWindow("2.tif");
imageCalculator("Subtract create stack", name,"MED_"+name);
close(name);
selectWindow("Result of " + name);
rename(name);

// run("Duplicate...", "title=4.tif duplicate");
run("Gaussian Blur 3D...", "x=1 y=1 z=0.5");

// run("Duplicate...", "title=5.tif duplicate");
Stack.getStatistics(count, mean, min, max, std); 
// print(mean, min, max, std);
cut = mean + 5 * std;

setAutoThreshold("Triangle dark stack");
setThreshold(cut, max);
setOption("BlackBackground", false);
run("Convert to Mask", "method=Triangle background=Dark");


// run("Duplicate...", "title=6.tif duplicate");

run("Remove Outliers...", "radius=2 threshold=2 which=Dark stack");
run("3D Objects Counter", "threshold=2 slice=12 min.=400 max.=10000 objects statistics summary");


setOption("BlackBackground", false);

run("RGB Color");

saveAs("Tiff", directory + name + "_objects_maps.tif");
selectWindow("Statistics for " + name);
saveAs("Results", directory + name + "_results.csv");

