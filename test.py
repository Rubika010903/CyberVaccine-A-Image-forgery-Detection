import cv2
import numpy as np

def rle_encode(image):
    """Run-Length Encodes a grayscale image."""
    pixels = image.flatten()  # Flatten the 2D image to 1D
    encoded = []
    prev_pixel = pixels[0]
    count = 1
    
    for pixel in pixels[1:]:
        if pixel == prev_pixel:
            count += 1
        else:
            encoded.append((prev_pixel, count))
            prev_pixel = pixel
            count = 1
    encoded.append((prev_pixel, count))  # Append last run
    return encoded

def rle_decode(encoded, shape):
    """Decodes a Run-Length Encoded image."""
    pixels = []
    for pixel, count in encoded:
        pixels.extend([pixel] * count)
    
    return np.array(pixels, dtype=np.uint8).reshape(shape)

# Load image
image_path = "sample/14.jpg"  # Change this to your image file
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Encode the image using RLE
encoded_data = rle_encode(image)
print("Encoded Data (First 20 values):", encoded_data[:20])

# Decode the RLE data
decoded_image = rle_decode(encoded_data, image.shape)

# Show original and decoded images
cv2.imshow("Original Image", image)
cv2.imshow("Decoded Image", decoded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
