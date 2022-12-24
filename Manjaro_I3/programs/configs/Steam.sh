# TODO inherit variables
install_dir=~/.local/share/Steam
backup_dir=/media/ExtraSSD/Temp/Linux_Install/Manjaro_I3/programs/configs/Steam

sudo rm -R $install_dir && sudo ln -s $backup_dir  $install_dir

