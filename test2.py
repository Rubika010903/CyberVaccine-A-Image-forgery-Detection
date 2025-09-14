import cv2
import numpy as np
import json

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
            encoded.append((int(prev_pixel), int(count)))
            prev_pixel = pixel
            count = 1
    encoded.append((int(prev_pixel), int(count)))  # Append last run
    return encoded

def rle_decode(encoded, shape):
    """Decodes a Run-Length Encoded image."""
    pixels = []
    for pixel, count in encoded:
        pixels.extend([pixel] * count)
    
    return np.array(pixels, dtype=np.uint8).reshape(shape)

# Load image
image_path = "sample/14.jpg"  # Change to your image file
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Encode the image using RLE
encoded_data = rle_encode(image)

# Save the encoded data to a text file (JSON format)
with open("encoded_rle.txt", "w") as file:
    json.dump(encoded_data, file)

print("RLE encoding saved to 'encoded_rle.txt'.")

# Load the encoded data from the text file
with open("encoded_rle.txt", "r") as file:
    loaded_encoded_data = json.load(file)

# Decode the RLE data
decoded_image = rle_decode(loaded_encoded_data, image.shape)

# Save the decoded image
cv2.imwrite("decoded_vaccination_card.jpg", decoded_image)
print("Decoded image saved as 'decoded_vaccination_card.jpg'.")

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Decoded Image", decoded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
