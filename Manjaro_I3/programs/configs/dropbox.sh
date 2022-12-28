# use/download python csript (from https://www.dropbox.com/download?dl=packages/dropbox.py)
# make script exectuable
# link dropbox to account
# dropbox domunation claims correct comman is "dropbox start --link", but i don't know how to get this working so for now i will have to link accounts manually

#daemon management

#download https://gist.githubusercontent.com/anonymous/07f65034cfffb574650ba82f9e618eda/raw/38148d89f7aac88a6a81f459b3664196e89b92fc/dropbox.service
#download https://gist.githubusercontent.com/anonymous/20afb8805ac7dea5bdc3a02271eebe43/raw/647b1db8e8cd448c0019642696edf3b55740965f/dropbox

dropbox_file=/media/ExtraSSD/Temp/Linux_Install/Manjaro_I3/programs/configs/Dropbox/dropbox
dropbox_service=/media/ExtraSSD/Temp/Linux_Install/Manjaro_I3/programs/configs/Dropbox/dropbox.service

#move to appropriate places
sudo cp $dropbox_service /etc/systemd/system/
sudo cp $dropbox_file /etc/init.d
#make exectuable
sudo chmod +x /etc/systemd/system/dropbox.service
sudo chmod +x /etc/init.d/dropbox

systemctl daemon-reload
sudo systemctl start dropbox
systemctl enable dropbox
#copy .py to root of dropbox folder
# in same dir as py, run
#install daemon
./dropbox.py start -i
#./dropbox.py
#/.dropbox.py start --link

#####working
sudo mv $dropbox_service /etc/systemd/system/
sudo chmod +x /etc/systemd/system/dropbox.service

systemctl daemon-reload
sudo systemctl start dropbox
systemctl enable dropbox.
