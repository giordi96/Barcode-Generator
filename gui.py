from PyQt5 import uic
from PyQt5.QtWidgets import QFileDialog, QWidget
from barcode import Code128
from barcode.writer import ImageWriter

from res import get_resource_path


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

        self.button_salva.clicked.connect(self.generate_barcode)

    def generate_barcode(self) -> None:
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_name, filter = QFileDialog.getSaveFileName(self,
                                                            "Save file",
                                                            "",
                                                            "PNG (*.png);;PDF (*.pdf)",
                                                            options=options)
            if file_name:

                if filter.startswith("PNG"):
                    format = "PNG"
                    if not file_name.endswith(".png"):
                        file_name = ".".join((file_name, "png"))

                elif filter.startswith("PDF"):
                    format = "PDF"
                    if not file_name.endswith(".pdf"):
                        file_name = ".".join((file_name, "pdf"))

                code = self.input_testo.text()
                code = code.replace("\\n", "\n")
                code = code.replace("\\t", "\t")

                with open(f"{file_name}", 'wb') as file:
                    Code128(code=code,
                            writer=ImageWriter(format=format)).write(file)
        except Exception as e:
            self.input_testo.setText(f"Errore: {str(e)}")
