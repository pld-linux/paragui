Summary:	ParaGUI - A complete GUI/Windowing system for SDL
Summary(pl):	ParaGUI - kompletne ¶rodowisko okienkowe dla SDL
Name:		paragui
Version:	1.0.2
Release:	1
Source0:	ftp://ftp.bms-austria.com/pub/paragui/release/%{name}-%{version}.tar.gz
Patch0:		%{name}-am.patch
URL:		http://www.paragui.org/
License:	LGPL
Group:		X11/Libraries
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	freetype-devel
BuildRequires:	libtool
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is a complete GUI/Windowing system for SDL

%description -l pl
Kompletne ¶rodowisko okienkowe dla SDL

%package devel
Summary:	Libraries, includes and more to develop SDL GUI applications.
Summary(pl):	Biblioteki, nag³ówki dla ParaGUI.
Group:          X11/Development/Libraries
Requires:       %{name} = %{version}

%description devel
This library is a complete GUI/Windowing system for SDL

%description -l pl
Biblioteki i pliki nag³ówkowe dla ParaGUI.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README-ParaGUI.txt AUTHORS TODO README 
%{_libdir}/lib*.so.*
%{_datadir}/paragui

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%{_libdir}/lib*.so
%{_includedir}
%{_aclocaldir}/*
