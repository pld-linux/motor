Summary:	Text mode based programming IDE for Linux
Name:		motor
Version:	1.2.3
Release:	1
License:	GPL
Group:		Development/Tools
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	http://konst.org.ua/download/%{name}-%{version}.tar.gz
Patch0:		motor-autoconf.patch
URL:		http://konst.org.ua/eng/software.motor.html
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Motor is a text mode based programming environment for Linux. It
consists of a powerful editor with syntax highlight feature, project
manager, makefile generator, gdb front-end, etc. Deep CVS integration
is also provided.

%prep
%setup -q
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses"
CXXFLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses -fno-rtti"
LDFLAGS="-s"
export CFLAGS CXXFLAGS LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README README.alpha TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/motor
%{_datadir}/motor
