3DV 

  Initially i have images with 3.60 degree of intervals between them.
  
  Then i invoke some opencv functions on that images in order to obtain following charaterstics from image:
    	1) Reading and loading the image with their meta properties.
    	2) Then convert each image into gray scale image ( using threshold function or we might say it as binary image ).
    	3) After that , i invoke canny edge detector function in order to find the image edges.
    	4) Finally i extract each and every pixels from each images and filter them out with criteria ( if(pixel > 0 ) ).
  Thats it for opencv
    
  After above operations i got the desired points in the form of x,y coordinates..
  
  Then i iterate them in order to find their intersection points between every consecutive images or we might say as points of images.
  
  Before processing the images points , i substract the width/2 from xth and yth coordinates of each and every points.
  
  Mainly there are three operations which are as follows:-
 	1) Rotating each points acording to there corresponding angles.
	2) Then performing intersection between those points with some suppositions.
	3) Incrementing the angle time to time or w.r.t images.
  
  After getting the result i store them in .pts or .txt or .off or .ply file ..
