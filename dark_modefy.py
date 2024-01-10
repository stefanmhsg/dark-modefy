import os
import fitz  # PyMuPDF
import sys
from PIL import Image, ImageOps, ImageEnhance


def create_output_dir(base_output_dir):
    if not os.path.exists(base_output_dir):
        os.makedirs(base_output_dir)
        return base_output_dir

    user_input = input(f"The folder '{base_output_dir}' already exists. y = Overwrite || n = create new version (y/n):").lower()
    if user_input == 'y':
        return base_output_dir
    else:
        counter = 1
        new_output_dir = f"{base_output_dir}_{counter}"
        while os.path.exists(new_output_dir):
            counter += 1
            new_output_dir = f"{base_output_dir}_{counter}"
        os.makedirs(new_output_dir)
        return new_output_dir


def apply_dark_mode_pdf(input_pdf, output_pdf):
    print(f"Starting dark mode conversion for PDF: '{input_pdf}'.")

    # Open the PDF
    document = fitz.open(input_pdf)

    # Create a new PDF for output
    new_doc = fitz.open()

    # Set desired DPI for higher resolution. Typical screen DPI is 72, print is around 300.
    dpi = 300  # Adjust this value as needed

    # Iterate through each page
    for page_number in range(len(document)):
        print(f"Processing PDF page {page_number + 1}/{len(document)}...")
        page = document[page_number]

        # Invert colors to apply 'dark mode'
        pix = page.get_pixmap(dpi=dpi)
        pix.invert_irect()  # inverts the colors

        # Insert the inverted pixmap as a new page in the output document
        new_page = new_doc.new_page(width=pix.width, height=pix.height)
        new_page.insert_image(new_page.rect, pixmap=pix)

    # Save the modified PDF with compression and garbage collection
    new_doc.save(output_pdf, garbage=4, deflate=True)
    new_doc.close()
    document.close()
    print(f"Dark mode applied to PDF. Output saved as '{output_pdf}'.")

def apply_dark_mode_image(input_image_path, output_image_path):
    print(f"Starting dark mode conversion for image: '{input_image_path}'.")

    img = Image.open(input_image_path)

    # Apply dark mode transformation
    img_inverted = ImageOps.invert(img)
    img_inverted.save(output_image_path)

    img_inverted.save(output_image_path)
    print(f"Dark mode applied to image. Output saved as '{output_image_path}'.")

def process_directory(input_dir, output_dir):
    if not os.path.exists(input_dir):
        print(f"No 'input' folder found in the current directory: '{os.getcwd()}'")
        sys.exit(1)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        output_file = os.path.splitext(filename)[0] + '_dark'
        output_file_path = os.path.join(output_dir, output_file)

        if filename.lower().endswith('.pdf'):
            output_file_path += '.pdf'
            apply_dark_mode_pdf(file_path, output_file_path)
        elif filename.lower().endswith(('.png', '.jpeg', '.jpg')):
            output_file_path += '.png'
            apply_dark_mode_image(file_path, output_file_path)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(base_dir, 'input')
    output_dir = os.path.join(base_dir, 'output')
    output_dir = create_output_dir(output_dir)  # This will handle the output directory creation/renaming

    print("Processing files for dark mode conversion...")
    process_directory(input_dir, output_dir)
    print("Dark mode conversion completed for all files.")
