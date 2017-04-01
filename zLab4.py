import PIL
import numpy
from PIL import Image
import matplotlib.pyplot as plt


#task-1 Function
def thresholdConversion(source,destination, threshold):
	im = Image.open(source).convert('L')
	grarray = numpy.asarray(im)
	bw = (grarray > threshold)*255
	output = PIL.Image.fromarray(numpy.uint8(bw));
	output.save(destination);

#task-2 Function

def intensityHistogram(source,destination):
	image = Image.open(source).convert('L')
	grarray = numpy.asarray(image)
	hist = [0 for i in range(256)];
	for x in grarray:
		for y in x:
			hist[y] = hist[y]+1;

	a=numpy.transpose(hist) 
	plt.bar([i for i in range(256)],hist)
	plt.savefig(destination);

#task-3 Functions

def X_Y_cut(source, destination, lower_cross, upper_cross):

	im = Image.open(source).convert('L');
	grarray = numpy.array(im);
	# bw = (grarray > 100)*255;

	for x in range(len(grarray)):
		for y in range(len(grarray[0])):
			if grarray[x][y] < 100:
				grarray[x][y] = 0;
			else:
				grarray[x][y] = 255
	PIL.Image.fromarray(grarray).save("test.png");
	hist = [0 for i in range(im.size[1])];
	index = 0;

	# print bw
	for x in grarray:
		for y in x:
			if(y == 0):
				hist[index] = hist[index]+1;
		index = index+1;
	# print hist
	plt.bar([i for i in range(im.size[1])], hist)
	plt.savefig(destination+'graph.jpg');

	point = [];
	check = True;
	index = 0;
	index2= 0;
	for x in hist:
		if x > upper_cross:
			check = True;
		
		if check == True and x < lower_cross:
			check = False;
			point.append(index2);
			index = index +1;
		index2 = index2+1;

	sub_images(point, im, destination);


def sub_images(point, im, destination):
	for x in range(len(point)-1):
		print x
		box = (0, point[x], im.size[0], point[x+1]);
		region = im.crop(box);
		# print(destination+"x_y_lines"+str(x)+".jpg");
		region.save(destination+"_line_"+str(x)+".png");

#task-1
thresholdConversion("B1.png", "B1_task_1.jpg", 170);
thresholdConversion("B2.jpg", "B2_task_1.jpg", 120);
thresholdConversion("B3.jpg", "B3_task_1.jpg", 50);

#task-2

intensityHistogram("B1.png", "B1_task_2.jpg");
intensityHistogram("B2.jpg", "B2_task_2.jpg");
intensityHistogram("B3.jpg", "B3_task_2.jpg");

#task-3
X_Y_cut("XY-cutss.png", "Task_3_", 20, 100);



