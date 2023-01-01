echo "removing kglobalshortcutsrc"
link_target="~/.config/kglobalshortcutsrc"
sudo rm -R $link_target
echo "making link of kglobalshortcutsrc"
sudo ln -s $live_configs_directory"/kglobalshortcutsrc" $link_target


# ctrl+alt+arrow = move to beginning/end of line (Home/End)
# ctrl+shift+alt+arrow =select from cursor to beginning/end of line (Shift+Home/End)
# meta+space = krunner
# klipper - bind to mod+v
