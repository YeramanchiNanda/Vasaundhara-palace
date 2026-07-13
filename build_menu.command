#!/bin/bash
# Vasundhara Palace - Double-Click Compiler
CD_PATH="$(cd "$(dirname "$0")" && pwd)"
cd "$CD_PATH"
echo "----------------------------------------"
echo "  Vasundhara Palace Menu Compiler       "
echo "----------------------------------------"
echo ""
python3 update_menu.py
echo ""
echo "Compilation complete. Press any key to exit."
read -n 1
