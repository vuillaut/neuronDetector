// "BatchProcessFolders"
//
// This macro batch processes all the files in a folder and any
// subfolders in that folder.
// It runs the 2d or 3d neuron counter (change it as the end)


dir = getDirectory("Choose a Directory ");
// dir = "/Volumes/LaCie/LaCie/Gcampf6/TEST/"

setBatchMode(true);
count = 0;
countFiles(dir);
n = 0;
print(count + " files to process in the directory " + dir);

processFiles(dir);
print(count+" files processed");

//\\ Function to count the number of .tif files in the directory
function countFiles(dir) {
  list = getFileList(dir);
  for (i=0; i<list.length; i++) {
      if (endsWith(list[i], "/"))
          countFiles(""+dir+list[i]);
      else if (endsWith(list[i], ".tif"))
          count++;
  }
}

//\\ Function to go through all folders and files and lunch process
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

//\\ Function to process .tif files (run the macro indicated below)
function processFile(path) {
   if (endsWith(path, ".tif")) {
   	open(path);
	runMacro("3d_counter.ijm");
	run("Close All");
  }
}
