# Required to install this packages:
yay -S plplot
sudo pacman -S gcc-fortran
git clone https://github.com/vmagnin/gtk-fortran.git
mkdir build && cd build
cmake ..
make
sudo make install
