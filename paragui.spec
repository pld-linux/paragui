Summary:	ParaGUI - A complete GUI/Windowing system for SDL
Summary(pl):	ParaGUI - kompletne ¶rodowisko okienkowe dla SDL
Name:		paragui
Version:	1.0.2
Release:	3
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.bms-austria.com/pub/paragui/release/%{name}-%{version}.tar.gz
# Source0-md5:	57ca321ef8222d7f8ce55ad620adf63c
Patch0:		%{name}-am.patch
Patch1:		%{name}-64bit-workaround.patch
URL:		http://www.paragui.org/
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	freetype-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This library is a complete GUI/Windowing system for SDL.

%description -l pl
Kompletne ¶rodowisko okienkowe dla SDL.

%package devel
Summary:	Includes and more to develop SDL GUI applications
Summary(pl):	Pliki nag³ówkowe dla ParaGUI
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for ParaGUI library - a complete GUI/Windowing system for
SDL.

%description devel -l pl
Pliki nag³ówkowe dla ParaGUI.

%package static
Summary:	Static paragui library
Summary(pl):	Statyczna biblioteka paragui
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of paragui library.

%description static -l pl
Statyczna wersja biblioteki paragui.

%prep
%setup -q
%patch0 -p1
%ifarch alpha
%patch1 -p1
%endif

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	m4datadir=%{_aclocaldir}

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
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
