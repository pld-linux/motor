Summary:	Text mode based programming IDE for Linux
Summary(pl):	�rodowisko programistyczne dla Linuksa
Name:		motor
Version:	3.2.0
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://konst.org.ua/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-autoconf.patch
URL:		http://konst.org.ua/motor/
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	gettext-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Motor is a text mode based programming environment for Linux. It
consists of a powerful editor with syntax highlight feature, project
manager, makefile generator, gdb front-end, etc. Deep CVS integration
is also provided.

%description -l pl
Motor jest �rodowiskiem programistycznym dla Linuksa pracuj�cym w
trybie tekstowym. Zawiera ono doskona�y edytor tekstu, zarz�dc�
projekt�w, generator plik�w Makefile, frontend dla gdb. Istotn� cech�
jest g��boka integracja z CVS.

%prep
%setup -q
%patch -p1

%build
rm -f missing
gettextize --copy --force
aclocal
autoconf
automake -a -c -f
CPPFLAGS="-I%{_includedir}/ncurses"; export CPPFLAGS
CXXFLAGS="%{rpmcflags} -fno-rtti"; export CXXFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/motor

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog FAQ README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz tutorial/*
%attr(755,root,root) %{_bindir}/motor
%{_datadir}/motor
