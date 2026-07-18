@echo off
rem Создаёт репозиторий Faskat/Magi_System на GitHub и пушит сайт.
rem При повторных запусках просто пушит изменения.
cd /d %~dp0
git remote get-url origin >nul 2>&1
if errorlevel 1 (
  gh repo create Magi_System --public --source . --push --description "faskat_navi - personal project hub in Serial Experiments Lain style"
) else (
  git push -u origin main
)
echo.
echo Done. Repo: https://github.com/Faskat/Magi_System
pause
