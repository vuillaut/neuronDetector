// "BatchProcessFolders"
//
// This macro batch processes all the files in a folder and any
// subfolders in that folder. In this example, it runs the Subtract 
// Background command of TIFF files. For other kinds of processing,
// edit the processFile() function at the end of this macro.

   //requires("1.33s"); 
dir = getDirectory("Choose a Directory ");
// dir = "/Volumes/LaCie/LaCie/Gcampf6/TEST/"


setBatchMode(true);
count = 0;
countFiles(dir);
n = 0;
print(count + " files to process in the directory " + dir);

processFiles(dir);
print(count+" files processed");

function countFiles(dir) {
  list = getFileList(dir);
  for (i=0; i<list.length; i++) {
      if (endsWith(list[i], "/"))
          countFiles(""+dir+list[i]);
      else if (endsWith(list[i], ".tif"))
          count++;
  }
}

function processFiles(dir) {
  list = getFileList(dir);
  for (i=0; i<list.length; i++) {
      if (endsWith(list[i], "/"))
          processFiles(""+dir+list[i]);
      else {
      	 path = dir+list[i];
         processFile(path);
       	 n++;
         print(n, " files analysed");     
      }
  }
}

function processFile(path) {
   if (endsWith(path, ".tif")) {
   	open(path);
	runMacro("/Users/thomasvuillaume/Work/Dev/neuronDetector/fiji_macro/Macro_final.ijm");
	run("Close All");
  }
}
