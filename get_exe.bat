@echo off

REM Virtual environment activation
echo Virtual environment activation
call "venv\socomecenv\Scripts\activate"
python -m PyInstaller --noconsole --onefile __main__.py ^
--name "Barcode_generator" ^
--icon "res\icon.ico" ^
--add-data "gui\barcode_generator_gui.ui;.\gui" ^
--add-data "res/*.png;res/" ^
--add-data "res/*.ico;res/" ^
--add-data "venv\socomecenv\Lib\site-packages\barcode\fonts\DejaVuSansMono.ttf;.\venv\socomecenv\Lib\site-packages\barcode\fonts" ^
--clean
pause

