run("Duplicate...", "title=original duplicate");

selectWindow("original");

for (i=1; i<=nSlices; i++) {
  setSlice(i);
  run("Measure");
  mean = getResult("Mean");
  run("32-bit");
  run("Subtract...", "value=" + mean);
}

selectWindow("original");

run("Z Project...", "projection=[Average Intensity]");

imageCalculator("Subtract create stack", "original","AVG_original");
selectWindow("Result of original");
run("Gaussian Blur 3D...", "x=1 y=1 z=1");
