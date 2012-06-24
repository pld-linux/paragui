Summary:	ParaGUI - A complete GUI/Windowing system for SDL
Summary(pl):	ParaGUI - kompletne �rodowisko okienkowe dla SDL
Name:		paragui
Version:	1.1.6
Release:	3
License:	LGPL
Group:		X11/Libraries
Source0:	http://savannah.nongnu.org/download/paragui/%{name}-%{version}.tar.gz
# Source0-md5:	6bf00503ff7c8a114b69f080728c48b1
Patch0:		%{name}-am18.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-64bit-workaround.patch
URL:		http://www.paragui.org/
BuildRequires:	SDL-devel >= 1.2.6
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libsigc++-devel >= 1.2.5
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	physfs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is a complete GUI/Windowing system for SDL.

%description -l pl
Kompletne �rodowisko okienkowe dla SDL.

%package devel
Summary:	Includes and more to develop SDL GUI applications
Summary(pl):	Pliki nag��wkowe dla ParaGUI
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2.6
Requires:	expat-devel
Requires:	freetype-devel >= 2.1.0
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libsigc++-devel >= 1.2.5
Requires:	libtiff-devel
Requires:	physfs-devel

%description devel
Header files for ParaGUI library - a complete GUI/Windowing system for
SDL.

%description devel -l pl
Pliki nag��wkowe dla ParaGUI.

%package static
Summary:	Static paragui library
Summary(pl):	Statyczna biblioteka paragui
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of paragui library.

%description static -l pl
Statyczna wersja biblioteki paragui.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%ifarch alpha amd64
%patch2 -p1
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cd src/physfs
# only configured, not built (system physfs is used)
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../..
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
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
