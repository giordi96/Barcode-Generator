#!/usr/bin/env python
# -*- coding: utf-8 -*-
from barcode import Code39, Code128
from barcode.writer import ImageWriter


def gen_barcode(text: str,
                format: str = "svg",
                file_name: str = "barcode") -> None:
    with open(f"{file_name}.{format.lower()}", 'wb') as f:
        Code39(text, writer=ImageWriter(),
               add_checksum=False).write(f)


def gen_barcode128(text: str,
                   format: str = "svg",
                   file_name: str = "barcode") -> None:
    with open(f"{file_name}.{format.lower()}", 'wb') as f:
        Code128(text, writer=ImageWriter()).write(f)


if __name__ == '__main__':
    gen_barcode128("Giuba\nsecco", "png")
    print("ciao")
