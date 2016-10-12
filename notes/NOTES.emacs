# Static totally failed. Need to recompile too many packages by hand.

docker run --privileged -it -d --name=janin-build-emacs ubuntu bash

apt-get update
apt-get build-dep emacs24
apt-get install build-essential wget xorg-dev libx11-dev

cd /root
wget http://ftp.gnu.org/gnu/emacs/emacs-24.5.tar.gz
tar xzvf emacs-24.5.tar.gz
cd emacs-24.5

PKG_CONFIG=/usr/bin/pkg-config ./configure --prefix=/opt/emacs --with-x=yes --x-includes=/usr/include/X11 --x-libraries=/usr/lib/X11 --with-x-toolkit=lucid --without-dbus --without-gconf --without-gsettings

cd /opt/emacs
mkdir libs
cd libs
for lib in `ldd ../bin/emacs-24.5  | cut -f3 -d' ' | sort -u | grep -v '^\s*$'`; do
  cp $lib .
done
cd /
tar czf emacs.tar.gz /opt

# on tetra
docker cp b95b166fd1fa:/emacs.tar.gz .

docker run -it --rm=true --net=host --env="DISPLAY" --volume="$HOME:/root" --volume="/:/tetra:rw" --volume="/mnt/disk0:/mnt/disk0:rw" --volume="/mnt/disk1:/mnt/disk1:rw" ubuntu bash

cd /
tar xzf ~/disk0/emacs.tar.gz
export LD_LIBRARY_PATH=/opt/emacs/libs

# Works, except lots of: Fontconfig error: Cannot load default config file
# Need to copy /etc/fonts to /opt/emacs/fonts
# and /usr/share/fonts /usr/local/share/fonts
# maybe /var/cache/fontconfig
# Edit fonts.config
# Set FONTCONFIG_FILE? may be hardwired.



