echo "$1"
sudo cp ./pull.py /usr/bin/pull
sudo chmod +x /usr/bin/pull
echo "Script copied into /usr/bin/"
./configure.py "$1"