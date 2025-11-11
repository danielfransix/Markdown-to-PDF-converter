@echo off
echo Converting Markdown to PDF using WeasyPrint 66.0 with JetBrains Mono font...
echo.
echo Converting Markdown to PDF...
"C:\Program Files\Python313\python.exe" -m cli.main convert "..\user-flows\technical\investor flows\UF1_Onboarding_and_Account_Management_Flow.md" -o "..\user-flows\technical\investor flows\UF1_Onboarding_and_Account_Management_Flow.pdf"
echo.
echo Conversion complete!
pause