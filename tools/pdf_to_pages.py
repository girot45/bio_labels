import fitz
import os

def save_pdf_images(pdf_path, output_folder):
    pdf_document = fitz.open(pdf_path)
    total_pages = pdf_document.page_count

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for page_number in range(total_pages):
        page = pdf_document.load_page(page_number)
        pix = page.get_pixmap()
        image_path = os.path.join(output_folder, f"page_{page_number+1}.png")
        pix.save(image_path)


# # Пример использования
# pdf_path = "index.pdf"  # Путь к PDF-файлу
# output_folder = "cards/pages"  # Папка для сохранения изображений
#
# save_pdf_images(pdf_path, output_folder)
