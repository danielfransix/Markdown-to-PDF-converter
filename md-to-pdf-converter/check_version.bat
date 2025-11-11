@echo off
echo Setting up environment for WeasyPrint...
set PATH=%PATH%;C:\msys64\mingw64\bin

echo Checking WeasyPrint version...
python -c "import weasyprint; print(f'WeasyPrint version: {weasyprint.__version__}')"

pause