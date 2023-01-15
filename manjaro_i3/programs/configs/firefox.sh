# copy backup profile to active profile
# find way to passively backup firefox profile. Maybe syslink active profile into backup location, so it's not a backup but just a redirection of where the profile is stored?

# TODO replace with paretn variables
install_dir="/home/joep/.mozilla/firefox"
local_dir="/Firefox/profiles"
current_dir=$(pwd)

sudo rm -R $install_dir && sudo ln -s "$current_dir$local_dir" $install_dir
