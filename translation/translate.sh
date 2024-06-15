#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <english_file> <translated_file> <target_file>"
    exit 1
fi

english_file="$1"
translated_file="$2"
target_file="$3"

# Check if input files exist
if [ ! -f "$english_file" ]; then
    echo "Error: English file '$english_file' not found."
    exit 1
fi

if [ ! -f "$translated_file" ]; then
    echo "Error: Translated file '$translated_file' not found."
    exit 1
fi

if [ ! -f "$target_file" ]; then
    echo "Error: Target file '$target_file' not found."
    exit 1
fi

# Function to escape special characters for sed substitution
escape_for_sed() {
    local string="$1"
    printf '%s\n' "$string" | sed -e 's/[\/&]/\\&/g'
}

# Count lines in English file
total_lines=$(wc -l < "$english_file")
current_line=0

# Read English and translated files line by line
while IFS= read -r english_line && IFS= read -r translated_line <&3; do
    current_line=$((current_line + 1))

    # Escape special characters for sed substitution
    escaped_english_line=$(escape_for_sed "$english_line")
    escaped_translated_line=$(escape_for_sed "$translated_line")

    # Perform replacement in target file within double quotes using sed (macOS compatible)
    sed -i '' -e "s/\"$escaped_english_line\"/\"$escaped_translated_line\"/g" "$target_file"

    # Calculate progress percentage
    progress=$(awk "BEGIN { pc=100*${current_line}/${total_lines}; i=int(pc); print (pc-i<0.5)?i:i+1 }")
    echo "Progress: $progress%"

done < "$english_file" 3< "$translated_file"


