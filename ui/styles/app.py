import logging
import os


def get_header_stylesheet(border_image_path: str):
    if os.name == 'nt':
        border_image_url = os.path.join('file:///', border_image_path.replace('\\', '/'))
    else:
        border_image_url = os.path.join('file://', border_image_path)
    logging.info(f'Image path: {border_image_url}')
    stylesheet = f"#header{{\n" \
                 f"    border-radius: 5px;\n" \
                 f"    border-image: url({border_image_url});\n" \
                 f"}}\n" \
                 f"\n" \
                 f"#frame{{\n" \
                 f"    border-radius: 5px;\n" \
                 f"    background-color: rgba(0, 0, 0, 102);\n" \
                 f"    border-image: none;\n" \
                 f"}}\n" \
                 f"\n" \
                 f"QPushButton{{\n" \
                 f"    border: none;\n" \
                 f"    background-color: none;\n" \
                 f"    border-image: none;\n" \
                 f"}}\n" \
                 f"QLabel{{\n" \
                 f"    border-image: none;\n" \
                 f"}}"
    return stylesheet