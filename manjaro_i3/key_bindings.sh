# $live_configs_directory=$1
echo "removing kglobalshortcutsrc"

link_target="/home/joep/.config/kglobalshortcutsrc"
sudo rm -R $link_target
echo "making link of kglobalshortcutsrc"
sudo ln -s $1"/kglobalshortcutsrc" $link_target


# ctrl+alt+arrow = move to beginning/end of line (Home/End)
# ctrl+shift+alt+arrow =select from cursor to beginning/end of line (Shift+Home/End)
# meta+space = krunner
# klipper - bind to mod+v
