import cv2
import matplotlib.pyplot as plt

def load_and_display_image(image_path):
    # Load the image using cv2
    image = cv2.imread(image_path)

    # Convert BGR image to RGB for displaying with matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the original image
    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title('Original Image')

    return image

def preprocess_image(image):
    # Resize the image
    resized_image = cv2.resize(image, (256, 256))

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization to improve contrast
    equalized_image = cv2.equalizeHist(gray_image)

    # Normalize pixel values to the range [0, 1]
    normalized_image = equalized_image / 255.0

    return resized_image, normalized_image

def display_preprocessed_image(resized_image, normalized_image):
    # Display the preprocessed images
    plt.figure(figsize=(8, 8))
    plt.imshow(resized_image, cmap='gray')
    plt.title('Preprocessed Image')
    plt.savefig('Malignant_preprocess', dpi=400)
    plt.show()


def main():
    # Replace 'path/to/your/image.jpg' with the path to your image file
    image_path = 'Malignant_rawdata.jpg'

    # Load the image
    original_image = load_and_display_image(image_path)

    # Preprocess the image
    resized_image, normalized_image = preprocess_image(original_image)

    # Display the preprocessed image without showing the original image
    display_preprocessed_image(resized_image, normalized_image)

if __name__ == "__main__":
    main()
