#!/bin/bash
# Dark theme
desktopTheme=org.manjaro.breath-dark.desktop
lookandfeeltool -a org.manjaro.breath-dark.desktop
echo "Set global theme to $desktopTheme"

#remove shutdown options
insertText="offerShutdown=false"
var=$(grep -n "\[General\]" ksmserverrc | cut -f1 -d:)
var=$((var+1))
sed -i "${var}i ${insertText}" ~/.config/ksmserverrc
