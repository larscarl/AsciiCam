import cv2

ASCII_CHARS = """   .:-=++**##%%@@"""

# Ensure we correctly map pixel values to our ASCII_CHARS range
# We subtract 1 from len(ASCII_CHARS) because string indices are 0-based
ASCII_LEN = len(ASCII_CHARS) - 1


def resize_image(image, new_width=200):
    """Resize image to a new width, maintaining aspect ratio."""
    (old_width, old_height) = image.shape[:2]
    aspect_ratio = old_height / float(old_width)
    # Increase the multiplier for new_height to reduce vertical stretch
    # You may need to experiment with this value to find the best result for your display
    new_height = int(aspect_ratio * new_width * 0.2)  # Adjusted height factor
    return cv2.resize(image, (new_width, new_height))


def pixels_to_ascii(image):
    """Map each pixel to an ASCII char, safely handling the index."""
    pixels = image.flatten()
    ascii_str = "".join(
        [ASCII_CHARS[min(int(pixel / 256 * ASCII_LEN), ASCII_LEN)] for pixel in pixels]
    )
    return ascii_str


def grayify(image):
    """Convert image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def pixels_to_ascii(image):
    """Map each pixel to an ASCII char."""
    pixels = image.flatten()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[int((pixel / 256) * len(ASCII_CHARS))]
    return ascii_str


def main():
    cap = cv2.VideoCapture(0)  # 0 is usually the built-in webcam

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                break

            # Flip the frame horizontally (mirror effect)
            frame = cv2.flip(frame, 1)

            # Convert the image to ASCII
            gray_frame = grayify(frame)
            resized_frame = resize_image(gray_frame)
            ascii_str = pixels_to_ascii(resized_frame)

            # Format the ASCII string to match the image's shape
            img_width = resized_frame.shape[1]
            ascii_str_len = len(ascii_str)
            ascii_img = ""
            for i in range(0, ascii_str_len, img_width):
                ascii_img += ascii_str[i : i + img_width] + "\n"

            # Clear the screen for the next frame
            print("\033c", end="")
            print(ascii_img)

            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
