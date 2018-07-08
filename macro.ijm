run("Z Project...", "projection=[Average Intensity]");
imageCalculator("Subtract create stack", "WistarDIV4_3_4.tif","AVG_WistarDIV4_3_4.tif");
selectWindow("Result of WistarDIV4_3_4.tif");
run("Gaussian Blur 3D...", "x=1 y=1 z=1");
run("16-bit");\
run("3D Objects Counter");
