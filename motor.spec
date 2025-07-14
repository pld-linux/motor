Summary:	Text mode based programming IDE for Linux
Summary(pl.UTF-8):	Środowisko programistyczne dla Linuksa
Name:		motor
Version:	3.2.4
Release:	4
License:	GPL
Group:		Development/Tools
Source0:	http://konst.org.ua/download/%{name}-%{version}.tar.gz
# Source0-md5:	cb24eba00be62ff3fab2a1a4c03e1cb3
Patch0:		%{name}-autoconf.patch
Patch1:		%{name}-AC_PROG_MAKE_SET.patch
Patch2:		%{name}-po.patch
URL:		http://konst.org.ua/motor/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Motor is a text mode based programming environment for Linux. It
consists of a powerful editor with syntax highlight feature, project
manager, makefile generator, gdb front-end, etc. Deep CVS integration
is also provided.

%description -l pl.UTF-8
Motor jest środowiskiem programistycznym dla Linuksa pracującym w
trybie tekstowym. Zawiera ono doskonały edytor tekstu, zarządcę
projektów, generator plików Makefile, frontend dla gdb. Istotną cechą
jest głęboka integracja z CVS.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
CPPFLAGS="-I/usr/include/ncurses"; export CPPFLAGS
CXXFLAGS="%{rpmcflags} -fno-rtti"; export CXXFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/motor

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ README TODO tutorial/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/motor
%{_mandir}/man1/*
