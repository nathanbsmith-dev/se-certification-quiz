#!/bin/bash

# Systems Engineering Quiz Application Launcher
# This script checks requirements and launches the quiz

echo "=================================================="
echo "  Systems Engineering Certification Quiz"
echo "=================================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3 and try again"
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"

# Check if tkinter is available
if ! python3 -c "import tkinter" 2>/dev/null; then
    echo "❌ Error: tkinter is not installed"
    echo ""
    echo "To install tkinter:"
    echo "  Ubuntu/Debian: sudo apt-get install python3-tk"
    echo "  macOS: brew install python-tk"
    echo "  Windows: Reinstall Python with tcl/tk option checked"
    exit 1
fi

echo "✓ tkinter library found"

# Check if quiz app exists
if [ ! -f "se_quiz_app.py" ]; then
    echo "❌ Error: se_quiz_app.py not found in current directory"
    echo "Please ensure all files are in the same folder"
    exit 1
fi

echo "✓ Quiz application found"

# Check if exam files exist
EXAM_FILES=(
    "systems_engineering_practice_exam.md"
    "systems_engineering_practice_exam_2.md"
    "systems_engineering_practice_exam_3.md"
)

MISSING_FILES=0
for file in "${EXAM_FILES[@]}"; do
    if [ ! -f "/mnt/user-data/outputs/$file" ] && [ ! -f "$file" ]; then
        echo "❌ Warning: $file not found"
        MISSING_FILES=$((MISSING_FILES + 1))
    fi
done

if [ $MISSING_FILES -eq 0 ]; then
    echo "✓ All exam files found"
else
    echo "⚠ Warning: $MISSING_FILES exam file(s) missing"
    echo "Quiz may not load all 300 questions"
fi

echo ""
echo "Starting quiz application..."
echo "=================================================="
echo ""

# Launch the quiz
python3 se_quiz_app.py

echo ""
echo "Quiz application closed."
echo "Thank you for practicing!"
