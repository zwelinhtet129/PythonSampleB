import os
from PIL import Image
from argparse import ArgumentParser

def resize(path, new_horizontal_size=None, new_vertical_size=None):
	try:
		file = path
		output_dir = os.path.dirname(os.path.realpath(path))

		img = Image.open(file)

		filename = os.path.basename(file)

		[width_img, height_img] = img.size
		hsize = int((float(width_img)) * float((new_vertical_size / float(height_img)))) if new_horizontal_size is None else new_horizontal_size
		vsize = int((float(height_img)) * float((new_horizontal_size / float(width_img)))) if new_vertical_size is None else new_vertical_size
		img = img.resize((hsize, vsize), Image.ANTIALIAS)
		save_path = os.path.join(output_dir,"resized{}".format(filename))
		img.save(save_path)


			#if width_img > height_img:
			#	ratio = (max_size / float(width_img))
			#	new_height = int((float(height_img)) * float(ratio))
			#	img = img.resize((width_img, new_height), Image.ANTIALTAS)
			#	img.save("resized.jpg")

	except IOError:
		print("oops")

parser = ArgumentParser(description="Program that resizes an imgae to a custom size")

parser.add_argument("-f", "--file",
					dest="file",
					help="image to be resized",
					required=True)
parser.add_argument("-sv", "--sizevertical",
					type=int,
					dest="sizevertical",
					help="vertical size in pixels. If argument ' sizehorizontal' is not passed, then the image proportions are maintained.")
parser.add_argument("-sh", "--sizehorizontal",
					type=int,
					dest="sizehorizontal",
					help="horizontal size in pixels. If argument ' sizevertical' is not passed, then the image proportions are maintained.")


args = parser.parse_args()
hsize = None if args.sizehorizontal is None else int(args.sizehorizontal)
vsize = None if args.sizevertical is None else int(args.sizevertical)
resize(path=args.file, new_horizontal_size=hsize, new_vertical_size=vsize)

