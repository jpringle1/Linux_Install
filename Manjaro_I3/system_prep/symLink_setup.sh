 #setup symlinks in home directory to link Downloads, Documents, pictures and desktop to dropbox contents

 # TODO for each folder, if doesn't already exist in ExtraSSD, create and show warning
 # TODO replace diretory with variable defined in controller
 # create DB link in /home.
ln -s ~/Dropbox /media/ExtraSSD/Dropbox

mkdir ~/Dropbox/"PC files"
cd ~/Dropbox/"PC files"

mkdir /Pictures
mkdir /Documents
mkdir /Downloads
mkdir /Desktop


sudo rm -R ~/Pictures && sudo ln -s ~/Dropbox/"PC files"/Pictures ~/Pictures
sudo rm -R ~/Documents && sudo ln -s ~/Dropbox/"PC files"/Documents ~/Documents
sudo rm -R ~/Downloads && sudo ln -s ~/Dropbox/"PC files"/Downloads ~/Downloads
sudo rm -R ~/Desktop && sudo ln -s ~/Dropbox/"PC files"/Desktop ~/Desktop
