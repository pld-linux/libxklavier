#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
#
Summary:	libxklavier library
Summary(pl.UTF-8):	Biblioteka libxklavier
Name:		libxklavier
Version:	4.0
Release:	3
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libxklavier/4.0/%{name}-%{version}.tar.bz2
# Source0-md5:	1b714ba04835fb49511f9e1444a5ea4c
Patch0:		%{name}-enumeration.patch
URL:		http://www.freedesktop.org/Software/LibXklavier
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.10
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.7}
BuildRequires:	iso-codes
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXi-devel >= 1.1.3
BuildRequires:	xorg-lib-libxkbfile-devel
Requires:	iso-codes
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows you to simplify XKB-related development.

%description -l pl.UTF-8
Ta biblioteka pozwala uprościć programowanie związane z XKB.

%package devel
Summary:	Header files to develop libxklavier applications
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia aplikacji z użyciem libxklavier
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxml2-devel >= 1:2.6.26
Requires:	xorg-lib-libxkbfile-devel

%description devel
Header files to develop libxklavier applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia aplikacji z użyciem libxklavier.

%package static
Summary:	Static version of libxklavier library
Summary(pl.UTF-8):	Statyczna wersja biblioteki libxklavier
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libxklavier library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libxklavier.

%package apidocs
Summary:	libxklavier API documentation
Summary(pl.UTF-8):	Dokumentacja API libxklavier
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libxklavier API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libxklavier.

%prep
%setup -q
%patch0 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc \
	--with-xkb-bin-base=%{_bindir} \
	--with-xkb-base=%{_datadir}/X11/xkb \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}/%{name}}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libxklavier.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxklavier.so.15

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxklavier.so
%{_libdir}/libxklavier.la
%{_pkgconfigdir}/libxklavier.pc
%{_includedir}/libxklavier

%files static
%defattr(644,root,root,755)
%{_libdir}/libxklavier.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
%endif
