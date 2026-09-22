#!/bin/bash

# Ensure the script is run as root (sudo) because we are modifying system folders
if [ "$EUID" -ne 0 ]; then
  echo "Error: Please run this script with sudo."
  echo "Command: sudo ./install.sh"
  exit 1
fi

echo "=> Installing Ge'ez Keyboard Configuration..."

# Copy the XML file to the official Linux IBus components directory
# $(dirname "$0") ensures it finds the file even if you run it from another folder
cp "$(dirname "$0")/ibus_engine/geez.xml" /usr/share/ibus/component/geez-custom.xml

# Give the system permission to read the file
chmod 644 /usr/share/ibus/component/geez-custom.xml

echo "=> Installation Complete!"
echo ""
echo "IMPORTANT NEXT STEPS:"
echo "1. Run this command in your terminal (WITHOUT sudo) to restart the keyboard system:"
echo "   ibus restart"
echo ""
echo "2. Open your Linux 'Settings' -> 'Keyboard' (or 'Region & Language')."
echo "3. Click to add a new Input Source, search for 'Amharic', and select 'Ge'ez (Custom)'."
echo "4. You can now use Super+Space (or Win+Space) to switch to it and type anywhere!"
