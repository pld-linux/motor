Summary: Text mode based programming IDE for Linux
Name: motor
Version: 1.2.3
Release: 1
Copyright: GPL
Group: Applications/IDE
Source: motor-1.2.3.tar.gz
URL: http://konst.org.ua/download/motor-1.2.3.tar.gz
Packager: Konstantin Klyagin <konst@konst.org.ua>

%description
Motor is a text mode based programming environment for Linux. It
consists of a powerful editor with syntax highlight feature, project
manager, makefile generator, gdb front-end, etc. Deep CVS integration is
also provided.

%prep
%setup

%build
./configure
make

%install
make install

%files
%doc README README.alpha COPYING INSTALL TODO FAQ ChangeLog

/usr/local/bin/motor
/usr/local/share/motor/syntax
/usr/local/share/motor/build
/usr/local/share/motor/make.lib
/usr/local/share/motor/make.prog
/usr/local/share/motor/tar.gz.genpackage
/usr/local/share/motor/filetypes
