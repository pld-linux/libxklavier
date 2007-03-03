Summary:	libXklavier library
Summary(pl.UTF-8):	Biblioteka libXklavier
Name:		libxklavier
Version:	3.1
Release:	2
License:	GPLv2 / LGPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/gswitchit/%{name}-%{version}.tar.gz
# Source0-md5:	56c4bea91ccbd0d09e3bcf58dff5732a
URL:		http://www.freedesktop.org/Software/LibXklavier
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.12.4
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libxkbfile-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows you simplify XKB-related development.

%description -l pl.UTF-8
Ta biblioteka pozwala uprościć programowanie związane z XKB.

%package devel
Summary:	Header files to develop libxklavier applications
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia aplikacji z użyciem libxklavier
Group:		Development/Libraries
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
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libxklavier library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libxklavier.

%prep
%setup -q

%build
touch config.rpath
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-xkb-bin-base=%{_bindir} \
	--with-xkb-base=%{_datadir}/X11/xkb \
	--with-html-dir=%{_gtkdocdir}
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
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/*
%{_gtkdocdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
