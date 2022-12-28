sudo rm -R ~/.config/kglobalshortcutsrc && sudo ln -s /media/ExtraSSD/Dropbox/"PC files"/Projects/Tech/LiveConfigs/kglobalshortcutsrc ~/.config/kglobalshortcutsrc


config_store=$dropbox_main_dir/media/ExtraSSD/Dropbox/"PC files"/Projects/Tech/LiveConfigs
link_dir=~/.config/kglobalshortcutsrc
sudo rm -R $link_dir && sudo ln -s $config_store/keyboard_bindings $link_dir



