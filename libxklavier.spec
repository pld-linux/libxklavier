Summary:	libXklavier library
Summary(pl):	Biblioteka libXklavier
Name:		libxklavier
Version:	1.04
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/gswitchit/%{name}-%{version}.tar.gz
# Source0-md5:	322078ad3681465f69a65c0758c74460
Patch0:		%{name}-xkb_base.patch
Patch1:		%{name}-free.patch
URL:		http://www.freedesktop.org/Software/LibXklavier
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	pkgconfig
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows you simplify XKB-related development.

%description -l pl
Ta biblioteka pozwala upro¶ciæ programowanie zwi±zane z XKB.

%package devel
Summary:	Header files to develop libxklavier applications
Summary(pl):	Pliki nag³ówkowe do tworzenia aplikacji z u¿yciem libxklavier
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	XFree86-devel
Requires:	libxml2-devel >= 2.0.0

%description devel
Header files to develop libxklavier applications.

%description devel -l pl
Pliki nag³ówkowe do tworzenia aplikacji z u¿yciem libxklavier.

%package static
Summary:	Static version of libxklavier library
Summary(pl):	Statyczna wersja biblioteki libxklavier
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libxklavier library.

%description static -l pl
Statyczna wersja biblioteki libxklavier.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/libxklavier

%files devel
%defattr(644,root,root,755)
%doc doc/html/*.html doc/html/*.png doc/html/*.css
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
