Summary:	ParaGUI - A complete GUI/Windowing system for SDL
Summary(pl):	ParaGUI - kompletne ¶rodowisko okienkowe dla SDL
Name:		paragui
Version:	1.0.2
Release:	2
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.bms-austria.com/pub/paragui/release/%{name}-%{version}.tar.gz
Patch0:		%{name}-am.patch
URL:		http://www.paragui.org/
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This library is a complete GUI/Windowing system for SDL.

%description -l pl
Kompletne ¶rodowisko okienkowe dla SDL.

%package devel
Summary:	Includes and more to develop SDL GUI applications
Summary(pl):	Pliki nag³ówkowe dla ParaGUI
Group:          X11/Development/Libraries
Requires:       %{name} = %{version}

%description devel
Header files for ParaGUI library - a complete GUI/Windowing system for
SDL.

%description -l pl
Pliki nag³ówkowe dla ParaGUI.

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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README-ParaGUI.txt AUTHORS TODO README 
%{_libdir}/lib*.so.*
%{_datadir}/paragui

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%{_libdir}/lib*.so
%{_includedir}/*
%{_aclocaldir}/*
