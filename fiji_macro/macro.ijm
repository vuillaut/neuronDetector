run("Duplicate...", "title=original duplicate");

selectWindow("original");

// Soustrait à chaque image sa moyenne 
for (i=1; i<=nSlices; i++) {
  setSlice(i);
  run("Measure");
  mean = getResult("Mean");
  run("32-bit");
  run("Subtract...", "value=" + mean);
}

selectWindow("original");

// Mesure la moyenne de chaque pixel selon l'axe Z (temporel)
run("Z Project...", "projection=[Average Intensity]");

// Retire à chaque pixel sa moyenne temporel (seules les variations de luminosité seront visibles)
imageCalculator("Subtract create stack", "original","AVG_original");


for (i = 1; i < 6; i++){ 
	setSlice(i);
	run("Delete Slice");
}


// Threshold à 2 sigma (95%)
 getStatistics(area, mean, min, max, std, histogram);
cut = mean + 2*std;
print(mean, std, cut);

setThreshold(cut, max);
run("NaN Background", "stack");


// Flou gaussien
// selectWindow("Result of original");
// run("Duplicate...", "duplicate");

run("Duplicate...", "duplicate");
run("8-bit");
run("Gaussian Blur 3D...", "x=1 y=1 z=1");

/*
run("Options...", "iterations=1 count=8");
run("Convert to Mask", "method=Default background=Dark");
run("Erode", "stack");
*/
//run("3D Objects Counter", "threshold=2 slice=32 min.=600 max.=68157440 objects statistics summary");



// 3D object counter - https://imagej.net/3D_Objects_Counter