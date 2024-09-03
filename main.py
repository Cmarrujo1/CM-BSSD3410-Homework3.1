from SortFunctions import selection_sort, quick sort
from SearchFunctions import binary_search_sub
from PixelFunction import *

def main():
	IMG_NAME = 'images'

	with Image.open(IMG_NAME + '.jpg') as im:
		pixles - storePixles(im)
		print("stored:", len(pixles), len(sorted_pixles))
		sorted_pixles = pixles.copy()
		selection_sort(sorted_pixles, compare_pixles)
		sorted_im = pixles_to_image(im, sorted_pixles)
		sorted_im.save('sorted_' + IMG_NAME + '.jpg', 'JPEG')
		print("sorted")
		threshold = 180
		subi = binary_search_sub([r[0][0] for r in sorted_pixles],0,
										len(sorted_pixles) - 1, threshold)
		print("Target found at:", subi)

		grayscale(im,pixles)
		pixles_to_point(im, sorted_pixles[subi:])

	im.save('highlighted' + IMG_NAME + '.jpg', 'JPEG')

if __name__ == "__main__":
	main()