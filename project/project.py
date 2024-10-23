"""
DSC 20 Project
Name(s): Gaku Ueno Yadushan Thillainathan
PID(s):  A17389668 A17880443
Sources: 
https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
"""

import numpy as np
import os
from PIL import Image

NUM_CHANNELS = 3


# --------------------------------------------------------------------------- #

def img_read_helper(path):
    """
    Creates an RGBImage object from the given image file
    """
    # Open the image in RGB
    img = Image.open(path).convert("RGB")
    # Convert to numpy array and then to a list
    matrix = np.array(img).tolist()
    # Use student's code to create an RGBImage object
    return RGBImage(matrix)


def img_save_helper(path, image):
    """
    Saves the given RGBImage instance to the given path
    """
    # Convert list to numpy array
    img_array = np.array(image.get_pixels())
    # Convert numpy array to PIL Image object
    img = Image.fromarray(img_array.astype(np.uint8))
    # Save the image object to path
    img.save(path)


# --------------------------------------------------------------------------- #

# Part 1: RGB Image #
class RGBImage:
    """
    Represents an image in RGB format
    """

    def __init__(self, pixels):
        """
        Initializes a new RGBImage object

        # Test with non-rectangular list
        >>> pixels = [
        ...              [[255, 255, 255], [255, 255, 255]],
        ...              [[255, 255, 255]]
        ...          ]
        >>> RGBImage(pixels)
        Traceback (most recent call last):
        ...
        TypeError

        # Test instance variables
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img.pixels
        [[[255, 255, 255], [0, 0, 0]]]
        >>> img.num_rows
        1
        >>> img.num_cols
        2
        """
        # YOUR CODE GOES HERE #
        # Raise exceptions here
        if type(pixels) != list or len(pixels) < 1:
            raise TypeError()
        if not all([isinstance(x, list) and len(x) >= 1 for x in pixels]):
            raise TypeError()
        if not all(len(x) == len(pixels[0]) for x in pixels):
            raise TypeError()
        if not all(isinstance(x, list) and len(x) == 3 for y in pixels for x in y):
            raise TypeError()
        if not all(0 <= z <= 255 for y in pixels for x in y for z in x):
            raise ValueError()
        self.pixels = pixels
        self.num_rows = len(pixels)
        self.num_cols = len(pixels[0])

    def size(self):
        """
        Returns the size of the image in (rows, cols) format

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img.size()
        (1, 2)
        """
        # YOUR CODE GOES HERE #
        return (self.num_rows, self.num_cols)

    def get_pixels(self):
        """
        Returns a copy of the image pixel array

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img_pixels = img.get_pixels()

        # Check if this is a deep copy
        >>> img_pixels                               # Check the values
        [[[255, 255, 255], [0, 0, 0]]]
        >>> id(pixels) != id(img_pixels)             # Check outer list
        True
        >>> id(pixels[0]) != id(img_pixels[0])       # Check row
        True
        >>> id(pixels[0][0]) != id(img_pixels[0][0]) # Check pixel
        True
        """
        # YOUR CODE GOES HERE #
        return list([[col[:] for col in row] for row in self.pixels])

    def copy(self):
        """
        Returns a copy of this RGBImage object

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img_copy = img.copy()

        # Check that this is a new instance
        >>> id(img_copy) != id(img)
        True
        """
        # YOUR CODE GOES HERE #
        return RGBImage.get_pixels(self)


    def get_pixel(self, row, col):
        """
        Returns the (R, G, B) value at the given position

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)

        # Test with an invalid index
        >>> img.get_pixel(1, 0)
        Traceback (most recent call last):
        ...
        ValueError

        # Run and check the returned value
        >>> img.get_pixel(0, 0)
        (255, 255, 255)
        """
        # YOUR CODE GOES HERE #
        if type(row) != int or type(col) != int:
            raise TypeError()
        if row < 0 or col < 0:
            raise ValueError()
        if row >= len(self.pixels) or col >= len(self.pixels[0]):
            raise ValueError()
        return tuple(self.pixels[row][col])

    def set_pixel(self, row, col, new_color):
        """
        Sets the (R, G, B) value at the given position

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)

        # Test with an invalid new_color tuple
        >>> img.set_pixel(0, 0, (256, 0, 0))
        Traceback (most recent call last):
        ...
        ValueError

        # Check that the R/G/B value with negative is unchanged
        >>> img.set_pixel(0, 0, (-1, 0, 0))
        >>> img.pixels
        [[[255, 0, 0], [0, 0, 0]]]
        """
        # YOUR CODE GOES HERE #
        if type(row) != int or type(col) != int:
            raise TypeError()
        if row < 0 or col < 0:
            raise ValueError()
        if row >= len(self.pixels) or col >= len(self.pixels[0]):
            raise ValueError()
        if type(new_color) != tuple or len(new_color) != 3 or not all([isinstance(x, int) for x in list(new_color)]):
            raise TypeError()
        if any([x > 255 for x in list(new_color)]):
            raise ValueError()
        color_update = []
        for x in range(len(list(new_color))):
            if new_color[x] >= 0:
                color_update.append(new_color[x])
            else:
                color_update.append(self.pixels[row][col][x])
        self.pixels[row][col] = color_update


# Part 2: Image Processing Template Methods #
class ImageProcessingTemplate:
    """
    Contains assorted image processing methods
    Intended to be used as a parent class
    """

    def __init__(self):
        """
        Creates a new ImageProcessingTemplate object

        # Check that the cost was assigned
        >>> img_proc = ImageProcessingTemplate()
        >>> img_proc.cost
        0
        """
        # YOUR CODE GOES HERE #
        self.cost = 0

    def get_cost(self):
        """
        Returns the current total incurred cost

        # Check that the cost value is returned
        >>> img_proc = ImageProcessingTemplate()
        >>> img_proc.cost = 50 # Manually modify cost
        >>> img_proc.get_cost()
        50
        """
        # YOUR CODE GOES HERE #
        return self.cost

    def negate(self, image):
        """
        Returns a negated copy of the given image

        # Check if this is returning a new RGBImage instance
        >>> img_proc = ImageProcessingTemplate()
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img_negate = img_proc.negate(img)
        >>> id(img) != id(img_negate) # Check for new RGBImage instance
        True

        # The following is a description of how this test works
        # 1 Create a processor
        # 2/3 Read in the input and expected output
        # 4 Modify the input
        # 5 Compare the modified and expected
        # 6 Write the output to file
        # You can view the output in the img/out/ directory
        >>> img_proc = ImageProcessingTemplate()                            # 1
        >>> img = img_read_helper('img/test_image_32x32.png')                 # 2
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_negate.png')  # 3
        >>> img_negate = img_proc.negate(img)                               # 4
        >>> img_negate.pixels == img_exp.pixels # Check negate output       # 5
        True
        >>> img_save_helper('img/out/test_image_32x32_negate.png', img_negate)# 6
        """
        # YOUR CODE GOES HERE #
        #print([[[x * -1 for x in y] for y in z] for z in image.pixels])
        img = RGBImage(image.get_pixels())
        img.pixels = [[[x * -1 + 255 for x in y] for y in z] for z in img.pixels]
        #print(image.pixels)
        return img

    def grayscale(self, image):
        """
        Returns a grayscale copy of the given image

        # See negate for info on this test
        # You can view the output in the img/out/ directory
        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_gray.png')
        >>> img_gray = img_proc.grayscale(img)
        >>> img_gray.pixels == img_exp.pixels # Check grayscale output
        True
        >>> img_save_helper('img/out/test_image_32x32_gray.png', img_gray)
        """
        # YOUR CODE GOES HERE #
        img = RGBImage(image.get_pixels())
        img.pixels = [[[sum(x) // len(x)] * len(x) for x in y] for y in img.pixels]
        return img

    def rotate_180(self, image):
        """
        Returns a rotated version of the given image

        # See negate for info on this test
        # You can view the output in the img/out/ directory
        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_rotate.png')
        >>> img_rotate = img_proc.rotate_180(img)
        >>> img_rotate.pixels == img_exp.pixels # Check rotate_180 output
        True
        >>> img_save_helper('img/out/test_image_32x32_rotate.png', img_rotate)
        """
        # YOUR CODE GOES HERE #
        img = RGBImage(image.get_pixels())
        img.pixels = [x[::-1] for x in img.pixels[::-1]]
        return img

    def get_average_brightness(self, image):
        """
        Returns the average brightness for the given image

        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_proc.get_average_brightness(img)
        86
        """
        # YOUR CODE GOES HERE #
        average_each_pixel = [[[sum(x) // len(x)] for x in y] for y in image.pixels]
        flattened_list = [x for y in average_each_pixel for z in y for x in z]
        return sum(flattened_list) // len(flattened_list)


    def adjust_brightness(self, image, intensity):
        """
        Returns a new image with adjusted brightness level

        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_adjusted.png')
        >>> img_adjust = img_proc.adjust_brightness(img, 75)
        >>> img_adjust.pixels == img_exp.pixels # Check adjust_brightness
        True
        >>> img_save_helper('img/out/test_image_32x32_adjusted.png', img_adjust)
        """
        # YOUR CODE GOES HERE #
        if type(intensity) != int:
            raise TypeError()
        if intensity > 255 or intensity < -255:
            raise ValueError()
        img = RGBImage(image.get_pixels())
        added_intensity = [[[x + intensity for x in y] for y in z] for z in img.pixels]
        new_intensity = [[[max(0, min(255, x)) for x in y] for y in z] for z in added_intensity]
        img.pixels = new_intensity
        return img


    def blur(self, image):
        """
        Returns a new image with the pixels blurred

        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_blur.png')
        >>> img_blur = img_proc.blur(img)
        >>> img_blur.pixels == img_exp.pixels # Check blur
        True
        >>> img_save_helper('img/out/test_image_32x32_blur.png', img_blur)
        """
        # YOUR CODE GOES HERE #

        img = RGBImage(image.get_pixels())
        #print(img)
        #print(image)
        #print(image.pixels[0][0])
        #print(img.pixels[0][0])
        for i in range(len(image.pixels)):
            for j in range(len(image.pixels[i])):
                if i == 0:
                    if j == 0:
                        # top left corner
                        top_left_corner = lambda x: (image.pixels[i][j][x] + image.pixels[i][j+1][x] + image.pixels[i+1][j][x] + image.pixels[i+1][j+1][x]) // 4
                        img.pixels[i][j] = [top_left_corner(0),\
                        top_left_corner(1), \
                        top_left_corner(2)]
                        #print(f'{pixels[i][j][0]}, {pixels[i][j+1][0]}, {pixels[i+1][j][0]}, {pixels[i+1][j+1][0]}, {pixels[i][j-1][0]}, {pixels[i+1][j-1][0]}')
                    elif j == len(img.pixels[j]) - 1:
                        top_right_corner = lambda x: (image.pixels[i][j][x] + image.pixels[i][j-1][x] + image.pixels[i+1][j][x] + image.pixels[i+1][j-1][x]) // 4
                        img.pixels[i][j] = [top_right_corner(0),\
                        top_right_corner(1), \
                        top_right_corner(2)]
                        # top right corner

                    else:
                        top_edge = lambda x: (image.pixels[i][j][x] + image.pixels[i][j+1][x] + image.pixels[i+1][j][x] + image.pixels[i+1][j+1][x] + image.pixels[i][j-1][x] + image.pixels[i+1][j-1][x]) // 6
                        img.pixels[i][j] = [top_edge(0),\
                        top_edge(1), \
                        top_edge(2)]
                        # top edge
                        #print(f'{image.pixels[i][j][0]}, {image.pixels[i][j+1][0]}, {image.pixels[i+1][j][0]}, {image.pixels[i+1][j+1][0]}, {image.pixels[i][j-1][0]}, {image.pixels[i+1][j-1][0]}')
                        #print('first')
                elif i == len(img.pixels) - 1:
                    if j == 0:
                        #bottom left corner
                        bottom_left_corner = lambda x: (image.pixels[i][j][x] + image.pixels[i][j+1][x] + image.pixels[i-1][j][x] + image.pixels[i-1][j+1][x]) // 4
                        img.pixels[i][j] = [bottom_left_corner(0), bottom_left_corner(1), bottom_left_corner(2)]
                    elif j == len(img.pixels[j]) - 1:
                        bottom_right_corner = lambda x: (image.pixels[i][j][x] + image.pixels[i][j-1][x] + image.pixels[i-1][j][x] + image.pixels[i-1][j-1][x]) // 4
                        img.pixels[i][j] = [bottom_right_corner(0), bottom_right_corner(1), bottom_right_corner(2)]
                    else:
                        bottom_edge = lambda x: (image.pixels[i][j][x] + image.pixels[i][j+1][x] + image.pixels[i-1][j][x] + image.pixels[i-1][j+1][x] + image.pixels[i][j-1][x] + image.pixels[i-1][j-1][x]) // 6
                        img.pixels[i][j] = [bottom_edge(0), bottom_edge(1), bottom_edge(2)]
                else:
                    if j == 0:
                        left_edge = lambda x: (image.pixels[i][j][x] + image.pixels[i][j+1][x] + image.pixels[i-1][j][x] + image.pixels[i+1][j][x] + image.pixels[i+1][j+1][x] + image.pixels[i-1][j+1][x]) // 6
                        img.pixels[i][j] = [left_edge(0), left_edge(1), left_edge(2)]
                    elif j == len(img.pixels[j]) - 1:
                        right_edge = lambda x: (image.pixels[i][j][x] + image.pixels[i][j-1][x] + image.pixels[i-1][j][x] + image.pixels[i+1][j][x] + image.pixels[i+1][j-1][x] + image.pixels[i-1][j-1][x]) // 6
                        img.pixels[i][j] = [right_edge(0), right_edge(1), right_edge(2)]
                    else:
                        middle = lambda x: (image.pixels[i][j][x] + image.pixels[i][j-1][x] + image.pixels[i-1][j][x] + image.pixels[i+1][j][x] + image.pixels[i][j+1][x] + image.pixels[i-1][j-1][x] + image.pixels[i-1][j+1][x] + image.pixels[i+1][j-1][x] + image.pixels[i+1][j+1][x]) // 9
                        img.pixels[i][j] = [middle(0), middle(1), middle(2)]
        #print(img.get_pixels())
        return img
                    




# Part 3: Standard Image Processing Methods #
class StandardImageProcessing(ImageProcessingTemplate):
    """
    Represents a standard tier of an image processor
    """

    def __init__(self):
        """
        Creates a new StandardImageProcessing object

        # Check that the cost was assigned
        >>> img_proc = ImageProcessingTemplate()
        >>> img_proc.cost
        0
        """
        # YOUR CODE GOES HERE #
        self.cost = 0
        self.coupons = 0

    def negate(self, image):
        """
        Returns a negated copy of the given image

        # Check the expected cost
        >>> img_proc = StandardImageProcessing()
        >>> img_in = img_read_helper('img/square_32x32.png')
        >>> negated = img_proc.negate(img_in)
        >>> img_proc.get_cost()
        5

        # Check that negate works the same as in the parent class
        >>> img_proc = StandardImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_negate.png')
        >>> img_negate = img_proc.negate(img)
        >>> img_negate.pixels == img_exp.pixels # Check negate output
        True
        """
        # YOUR CODE GOES HERE #
        if self.coupons != 0:
            self.coupons -= 1
        else:
            self.cost += 5
        return super().negate(image)

    def grayscale(self, image):
        """
        Returns a grayscale copy of the given image

        """
        # YOUR CODE GOES HERE #
        if self.coupons != 0:
            self.coupons -= 1
        else:
            self.cost += 6
        return super().grayscale(image)

    def rotate_180(self, image):
        """
        Returns a rotated version of the given image
        """
        # YOUR CODE GOES HERE #
        if self.coupons != 0:
            self.coupons -= 1
        else:
            self.cost += 10
        return super().rotate_180(image)

    def adjust_brightness(self, image, intensity):
        """
        Returns a new image with adjusted brightness level
        """
        # YOUR CODE GOES HERE #
        if self.coupons != 0:
            self.coupons -= 1
        else:
            self.cost += 1
        return super().adjust_brightness(image, intensity)

    def blur(self, image):
        """
        Returns a new image with the pixels blurred
        """
        # YOUR CODE GOES HERE #
        if self.coupons != 0:
            self.coupons -= 1
        else:
            self.cost += 5
        return super().blur(image)

    def redeem_coupon(self, amount):
        """
        Makes the given number of methods calls free

        # Check that the cost does not change for a call to negate
        # when a coupon is redeemed
        >>> img_proc = StandardImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_proc.redeem_coupon(1)
        >>> img = img_proc.rotate_180(img)
        >>> img_proc.get_cost()
        0
        """
        # YOUR CODE GOES HERE #
        if type(amount) != int:
            raise TypeError()
        if amount <= 0:
            raise ValueError()
        self.coupons += amount



# Part 4: Premium Image Processing Methods #
class PremiumImageProcessing(ImageProcessingTemplate):
    """
    Represents a paid tier of an image processor
    """

    def __init__(self):
        """
        Creates a new PremiumImageProcessing object

        # Check the expected cost
        >>> img_proc = PremiumImageProcessing()
        >>> img_proc.get_cost()
        50
        """
        # YOUR CODE GOES HERE #
        self.cost = 50

    def chroma_key(self, chroma_image, background_image, color):
        """
        Returns a copy of the chroma image where all pixels with the given
        color are replaced with the background image.

        # Check output
        >>> img_proc = PremiumImageProcessing()
        >>> img_in = img_read_helper('img/square_32x32.png')
        >>> img_in_back = img_read_helper('img/test_image_32x32.png')
        >>> color = (255, 255, 255)
        >>> img_exp = img_read_helper('img/exp/square_32x32_chroma.png')
        >>> img_chroma = img_proc.chroma_key(img_in, img_in_back, color)
        >>> img_chroma.pixels == img_exp.pixels # Check chroma_key output
        True
        >>> img_save_helper('img/out/square_32x32_chroma.png', img_chroma)
        """
        # YOUR CODE GOES HERE #
        #print(type(chroma_image))
        img = RGBImage(chroma_image.get_pixels())
        if not isinstance(chroma_image, RGBImage) or not isinstance(background_image, RGBImage):
            raise TypeError()
        if len(chroma_image.pixels) != len(background_image.pixels) or len(chroma_image.pixels[0]) != len(background_image.pixels[0]):
            raise ValueError()
        for i in range(len(chroma_image.pixels)):
            for j in range(len(chroma_image.pixels[i])):
                if tuple(chroma_image.pixels[i][j]) == color:
                    img.pixels[i][j] = background_image.pixels[i][j]
        return img




    def sticker(self, sticker_image, background_image, x_pos, y_pos):
        """
        Returns a copy of the background image where the sticker image is
        placed at the given x and y position.

        # Test with out-of-bounds image and position size
        >>> img_proc = PremiumImageProcessing()
        >>> img_sticker = img_read_helper('img/square_6x6.png')
        >>> img_back = img_read_helper('img/test_image_32x32.png')
        >>> x, y = (31, 0)
        >>> img_proc.sticker(img_sticker, img_back, x, y)
        Traceback (most recent call last):
        ...
        ValueError

        # Check output
        >>> img_proc = PremiumImageProcessing()
        >>> img_sticker = img_read_helper('img/square_6x6.png')
        >>> img_back = img_read_helper('img/test_image_32x32.png')
        >>> x, y = (3, 3)
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_sticker.png')
        >>> img_combined = img_proc.sticker(img_sticker, img_back, x, y)
        >>> img_combined.pixels == img_exp.pixels # Check sticker output
        True
        >>> img_save_helper('img/out/test_image_32x32_sticker.png', img_combined)
        """
        # YOUR CODE GOES HERE #
        if not isinstance(sticker_image, RGBImage) or not isinstance(background_image, RGBImage):
            raise TypeError()
        if len(sticker_image.pixels) > len(background_image.pixels) or len(sticker_image.pixels[0]) > len(background_image.pixels[0]):
            raise ValueError()
        if type(x_pos) != int or type(y_pos) != int:
            raise TypeError()
        if len(sticker_image.pixels) + x_pos > len(background_image.pixels) or len(sticker_image.pixels[0]) + y_pos > len(background_image.pixels[0]):
            raise ValueError()
        back_image = RGBImage(background_image.get_pixels())
        for row in range(len(sticker_image.pixels)):
            for col in range(len(sticker_image.pixels[row])):
                back_image.pixels[row + y_pos][col + x_pos] = sticker_image.pixels[row][col]
        
        return back_image


    def edge_highlight(self, image):
        """
        Returns a new image with the edges highlighted

        # Check output
        >>> img_proc = PremiumImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_edge = img_proc.edge_highlight(img)
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_edge.png')
        >>> img_exp.pixels == img_edge.pixels # Check edge_highlight output
        True
        >>> img_save_helper('img/out/test_image_32x32_edge.png', img_edge)
        """
        # YOUR CODE GOES HERE #
        img = RGBImage(image.get_pixels())
        avg_pixels = []

        for row, col in img:
            avg_pixels.append(sum(img[row][col])//3)
        
        print(avg_pixels)
            



# Part 5: Image KNN Classifier #
class ImageKNNClassifier:
    """
    Represents a simple KNNClassifier
    """

    def __init__(self, k_neighbors):
        """
        Creates a new KNN classifier object
        """
        # YOUR CODE GOES HERE #
        self.k_neighbors = k_neighbors

    def fit(self, data):
        """
        Stores the given set of data and labels for later
        """
        # YOUR CODE GOES HERE #
        if len(data) < self.k_neighbors:
            raise ValueError
        self.data = data

    def distance(self, image1, image2):
        """
        Returns the distance between the given images

        >>> img1 = img_read_helper('img/steve.png')
        >>> img2 = img_read_helper('img/knn_test_img.png')
        >>> knn = ImageKNNClassifier(3)
        >>> knn.distance(img1, img2)
        15946.312896716909
        """
        # YOUR CODE GOES HERE #
        if not isinstance(image1, RGBImage) or not isinstance(image2, RGBImage):
            raise TypeError
        elif len(image1.pixels) != len(image2.pixels):
            raise ValueError

        intensity_diff_sq = lambda row, col, color_idx: (image2.pixels[row][col][color_idx] - image1.pixels[row][col][color_idx])**2
        
        distance = (sum([intensity_diff_sq(row, col, 0) + intensity_diff_sq(row, col, 1) + intensity_diff_sq(row, col, 2) for row in range(len(image1.pixels)) for col in range(len(image1.pixels[row]))]))**(1/2)
        return distance


    def vote(self, candidates):
        """
        Returns the most frequent label in the given list

        >>> knn = ImageKNNClassifier(3)
        >>> knn.vote(['label1', 'label2', 'label2', 'label2', 'label1'])
        'label2'
        """
        # YOUR CODE GOES HERE #
        return max(set(candidates), key = candidates.count)

    def predict(self, image):
        """
        Predicts the label of the given image using the labels of
        the K closest neighbors to this image

        The test for this method is located in the knn_tests method below
        """
        # YOUR CODE GOES HERE #
        distances = []
        labels = []
        #ImageKNNClassifier.fit(self, image)
        for i in self.data:
            distances.append(ImageKNNClassifier.distance(self, image, i[0]))
        distances = sorted(distances)[:self.k_neighbors]
        for i in self.data:
            if ImageKNNClassifier.distance(self, image, i[0]) in distances:
                labels.append(i[1])
        return ImageKNNClassifier.vote(self, labels)





def knn_tests(test_img_path):
    """
    Function to run knn tests

    >>> knn_tests('img/knn_test_img.png')
    'nighttime'
    """
    # Read all of the sub-folder names in the knn_data folder
    # These will be treated as labels
    path = 'knn_data'
    data = []
    for label in os.listdir(path):
        label_path = os.path.join(path, label)
        # Ignore non-folder items
        if not os.path.isdir(label_path):
            continue
        # Read in each image in the sub-folder
        for img_file in os.listdir(label_path):
            train_img_path = os.path.join(label_path, img_file)
            img = img_read_helper(train_img_path)
            # Add the image object and the label to the dataset
            data.append((img, label))

    # Create a KNN-classifier using the dataset
    knn = ImageKNNClassifier(5)

    # Train the classifier by providing the dataset
    knn.fit(data)

    # Create an RGBImage object of the tested image
    test_img = img_read_helper(test_img_path)

    # Return the KNN's prediction
    predicted_label = knn.predict(test_img)
    return predicted_label
