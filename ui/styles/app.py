def get_header_stylesheet(border_image_path):
    stylesheet = f"#header{{\n" \
                 f"    border-radius: 5px;\n" \
                 f"    border-image: url({border_image_path});\n" \
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