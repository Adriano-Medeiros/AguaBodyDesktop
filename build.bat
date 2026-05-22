@echo off

echo Limpando builds anteriores...

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist AguaBodyDesktop.spec del AguaBodyDesktop.spec

echo Gerando executavel AguaBody Desktop...

pyinstaller ^
--onefile ^
--windowed ^
--name AguaBodyDesktop ^
--icon=app/assets/icons/water.ico ^
--add-data "app/assets;app/assets" ^
main.py

echo.
echo Build finalizado.
echo O executavel esta em: dist\AguaBodyDesktop.exe
echo.

pause