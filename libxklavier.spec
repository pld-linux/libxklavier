Name:		libxklavier
Summary:	libXklavier library
Version:	0.95
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/gswitchit/%{name}-%{version}.tar.gz
# Source0-md5:	5caeb8aea1caac0c3fb0f9115f846a14
Patch0:		%{name}-xkb_base.patch
Url:		http://gswitchit.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libxml2-devel 
BuildRequires:	libtool
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows you simplify XKB-related development.

%package devel
Summary:	Libraries, includes, etc to develop libxklavier applications
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop libxklavier
applications.

%package static
Summary:	Static version of libxklavier
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of libxklavier.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README 
%{_libdir}/lib*.so.*.*
%{_datadir}/libxklavier

%files devel
%defattr(644,root,root,755)
%doc doc/html/*.html doc/html/*.png doc/html/*.css
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
