Summary:	libXklavier library
Summary(pl):	Biblioteka libXklavier
Name:		libxklavier
Version:	2.91
Release:	1
License:	GPLv2 / LGPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/gswitchit/%{name}-%{version}.tar.gz
# Source0-md5:	53d9864d165c86edb6a67f7ebe140814
Patch0:		%{name}-warnings.patch
URL:		http://www.freedesktop.org/Software/LibXklavier
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.11.3
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libxkbfile-devel
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
Requires:	libxml2-devel >= 1:2.6.26
Requires:	xorg-lib-libxkbfile-devel

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

%build
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
