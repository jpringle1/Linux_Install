#!/bin/bash
insertText="offerShutdown=false"
var=$(grep -n "\[General\]" ksmserverrc | cut -f1 -d:)
var=$((var+1))
sed -i "${var}i ${insertText}" ~/.config/ksmserverrc