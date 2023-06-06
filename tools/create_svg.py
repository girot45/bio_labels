import json
from PySide6.QtSvg import QSvgGenerator
from PySide6.QtGui import QPainter, QColor, QPen, \
    QFontMetrics, QFont
from PySide6.QtCore import QFile, QRectF, QSize
import SETTINGS


class Card:
    def __init__(
            self,
            text,
            height,
            width,
            name,
            date,
            date_check,
            name_check,
            underline,
            bold,
            italic,
            font,
            font_size,
            copies,
            filename
    ):
        self.filename = filename
        self.text = text
        self.height = height
        self.width = width
        self.name = name
        self.date = date
        self.date_check = date_check
        self.name_check = name_check
        self.underline = underline
        self.bold = bold
        self.italic = italic
        self.font = font
        self.font_size = font_size
        self.copies = copies

    def create_card_json(self):
        filename = SETTINGS.JSON_DIR + f'/{self.filename}'
        with open(filename, 'w') as f:
            f.write(json.dumps(self.__dict__))

    def create_card_svg(self, index):
        # настройка размерности
        dpi = SETTINGS.DPI
        width_in_pixels = int(int(self.width) * dpi / 254)
        height_in_pixels = int(int(self.height) * dpi / 254)

        # настройка шрифтов
        font_main_text = make_font(
            font=self.font,
            font_size=self.font_size,
            bold=self.bold,
            italic=self.italic,
            underline=self.underline,
        )

        # Шрифт для имени
        font_name_text = make_font(
            font=self.font,
            font_size=self.font_size,
            bold=self.bold,
            italic=self.italic,
            underline=self.underline,
        )

        name_font, name_width, name_height, name_font_metrics = \
            make_secondary_font(
                font=font_name_text,
                font_size=self.font_size,
                text=self.date
            )

        # Шрифт для даты
        font_date_text = make_font(
            font=self.font,
            font_size=self.font_size,
            bold=False,
            italic=False,
            underline=False,
        )

        date_font, date_width, date_height, date_font_metrics = \
            make_secondary_font(
                font=font_date_text,
                font_size=int(self.font_size) - 1,
                text=self.date
            )

        # создание генератора svg
        svg_generator = QSvgGenerator()
        filename = SETTINGS.SVG_DIR + f'/card_{index}.svg'
        svg_generator.setFileName(filename)
        svg_generator.setResolution(dpi)

        # создание размеров svg
        dx = 0
        if self.date_check:
            dx = date_font_metrics.height()

        svg_generator.setSize(
            QSize(width_in_pixels + dx*3, height_in_pixels)
        )
        svg_generator.setViewBox(
            QRectF(
                0,  # смещение по x
                0,  # смещение по x
                width_in_pixels + dx*3,  # ширина
                height_in_pixels  # высота
            )
        )

        painter = QPainter()
        painter.begin(svg_generator)
        if self.date_check:
            # создание рамки для даты
            date_rect_width = date_height * 2
            date_rect = QRectF(0, 0, date_rect_width,
                               height_in_pixels)
            painter.setPen(QColor(0, 0, 0))
            painter.drawRect(date_rect)
            # создание текста даты
            painter.rotate(-90)
            painter.setFont(date_font)
            painter.setPen(QColor(128, 128, 128))
            painter.drawText(
                QRectF(
                    -height_in_pixels + 1,
                    0,
                    date_width,
                    date_height
                ),
                self.date
            )
            painter.rotate(90)

        # создание рамки основного текста
        rect = QRectF(0, 0, width_in_pixels, height_in_pixels)
        rect_pen = QPen(QColor(0, 0, 0))
        rect_pen.setWidth(1)

        painter.setPen(rect_pen)
        painter.drawRect(rect)

        # Подготовка текста и перенос по словам
        font_main_text_metrics = QFontMetrics(font_main_text)

        text = prepare_text(
            words=self.text.split(),
            font_metrics=font_main_text_metrics,
            width=width_in_pixels - dx*2,
        )

        # Отрисовка текста
        rect_text = QRectF(dx*2 + 1, 1, width_in_pixels,
                           height_in_pixels)
        painter.setFont(font_main_text)
        painter.setPen(QColor(0, 0, 0))
        painter.drawText(rect_text, text)

        # Добавление имени с более тонким шрифтом
        if self.name_check:
            painter.setFont(name_font)
            painter.setPen(QColor(128, 128, 128))
            painter.drawText(
                QRectF(dx*2 + 1, height_in_pixels - name_height - 2,
                       name_width, name_height), self.name)

        # rect_text.translate(shift, 0)
        # rect.translate(shift, 0)

        painter.end()

        svg_file = QFile(filename)
        svg_file.close()


def make_secondary_font(font_size, font, text):
    font_size_ = int(font_size) - 1
    font_ = QFont(font)
    font_.setPointSize(font_size_)
    font_.setWeight(QFont.Light)
    font_metrics_ = QFontMetrics(font_)
    width_ = font_metrics_.boundingRect(text).width()
    height_ = font_metrics_.height()
    return font_, width_, height_, font_metrics_


def make_font(font, font_size, bold, italic, underline):
    font = QFont(font, int(font_size))
    font.setBold(bold)
    font.setItalic(italic)
    font.setUnderline(underline)
    return font


def prepare_text(words: list, font_metrics, width):
    try:
        text = f'{words[0]}\n'
        line_width = 0
        words.pop(0)
        for word in words:
            word_width = font_metrics.boundingRect(word + " ").width()
            if line_width + word_width <= width:
                text += word + " "
                line_width += word_width
            else:
                text += "\n" + word + " "
                line_width = word_width
    except:
        text = ''
    return text
