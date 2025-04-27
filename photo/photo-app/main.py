import os
from PIL import Image, ImageEnhance, ImageFilter
import streamlit as st

# Create a folder for saving images if it doesn't exist
output_folder = "generated_images"
os.makedirs(output_folder, exist_ok=True)

# Streamlit UI components
st.title("Image Processing with Streamlit")
st.write("Upload an image, and we will apply various effects to it.")

# Upload an image using Streamlit's file uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the image
    image = Image.open(uploaded_file)

    # Display original image
    st.image(image, caption="Original Image", use_container_width=True)

    # Get the base name (file name without extension)
    base_name = os.path.splitext(os.path.basename(uploaded_file.name))[0]

    # Convert to grayscale
    gray_image = image.convert("L")
    # Apply blur filter
    blurred_image = image.filter(ImageFilter.BLUR)
    # Adjust brightness (1.5 times brighter)
    brightness_enhancer = ImageEnhance.Brightness(image)
    bright_image = brightness_enhancer.enhance(1.5)
    # Adjust contrast (1.8 times higher contrast)
    contrast_enhancer = ImageEnhance.Contrast(image)
    contrast_image = contrast_enhancer.enhance(1.8)

    # Show the processed images
    st.image(gray_image, caption="Grayscale Image", use_container_width=True)
    st.image(blurred_image, caption="Blurred Image", use_container_width=True)
    st.image(bright_image, caption="Brighter Image", use_container_width=True)
    st.image(contrast_image, caption="High Contrast Image", use_container_width=True)

    # Save the edited images with the base name
    gray_image.save(os.path.join(output_folder, f"{base_name}_gray.jpg"))
    blurred_image.save(os.path.join(output_folder, f"{base_name}_blur.jpg"))
    bright_image.save(os.path.join(output_folder, f"{base_name}_bright.jpg"))
    contrast_image.save(os.path.join(output_folder, f"{base_name}_contrast.jpg"))

    st.success(f"✅ Image processing complete! Check the 'generated_images' folder for the new images.")
else:
    st.info("Please upload an image to start processing.")
