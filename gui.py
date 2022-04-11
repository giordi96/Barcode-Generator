from barcode import generate
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QWidget
from barcode import Code128
from barcode.writer import ImageWriter

from path_manager import get_resource_path


class BGGui(QWidget):
    """
    Graphical user interface for barcode generator.
    """

    @property
    def GUI_RELATIVE_PATH(self) -> str:
        return get_resource_path("gui//barcode_generator_gui.ui")

    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(self.GUI_RELATIVE_PATH, self)

        self.icon = QIcon(str(get_resource_path(r"res/icon.png")))
        self.setWindowIcon(self.icon)

        self.save_path = None
        self.button_salva.clicked.connect(self.generate_barcode)

    def generate_barcode(self) -> None:
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_name, filter = QFileDialog.getSaveFileName(
                parent=self,
                caption="Save file",
                directory=self.save_path if self.save_path != None else "",
                filter="SVG (*.svg);;PNG (*.png);;PDF (*.pdf)",
                options=options)

            # refreshes the starting file dialog directory to the last selected folder
            try:
                self.save_path = file_name[:file_name.rfind("\\")]
            except:
                pass

            # formats input code by inserting \t and \n characters
            code = self.input_testo.text()
            code = code.replace("\\n", "\n")
            code = code.replace("\\t", "\t")

            if file_name:

                if filter.startswith("SVG"):

                    generate(name='CODE128',
                            code=code,
                            output=file_name,
                            writer_options={"write_text": False})

                else:

                    if filter.startswith("PNG"):
                        format = "PNG"
                        if not file_name.endswith(".png"):
                            file_name = ".".join((file_name, "png"))

                    elif filter.startswith("PDF"):
                        format = "PDF"
                        if not file_name.endswith(".pdf"):
                            file_name = ".".join((file_name, "pdf"))

                    with open(f"{file_name}", 'wb') as file:
                        Code128(code=code,
                                writer=ImageWriter(format=format)
                                ).write(file,
                                        options={"write_text": False})
        except Exception as e:
            self.input_testo.setText(f"Errore: {str(e)}")
