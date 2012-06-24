%define name paragui
%define version 1.0.2
%define release 1

Summary: ParaGUI - A complete GUI/Windowing system for SDL
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
URL: http://www.bms-austria.com/projects/paragui
Copyright: LGPL
Group: System Environment/Libraries
BuildRoot: /var/tmp/%{name}-buildroot
Prefix: %{_prefix}
Packager: Alexander Pipelka <pipelka@bms-austria.com>

%description
This library is a complete GUI/Windowing system for SDL

%package devel
Summary: Libraries, includes and more to develop SDL GUI applications.
Group: Development/Libraries
Requires: %{name}

%description devel
This library is a complete GUI/Windowing system for SDL

%prep
rm -rf ${RPM_BUILD_ROOT}

%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix} --disable-opengl
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/%{prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README-ParaGUI.txt COPYING INSTALL
%{prefix}/lib/lib*.so.*
%{prefix}/share/paragui

%files devel
%defattr(-,root,root)
%{prefix}/bin/*-config
%{prefix}/lib/lib*.so
%{prefix}/include
%{prefix}/share/aclocal/*

%changelog
