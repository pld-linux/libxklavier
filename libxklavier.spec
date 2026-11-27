#
# Conditional build:
%bcond_without	apidocs		# gtk-doc based API documentation
%bcond_without	vala		# Vala API

Summary:	libxklavier library
Summary(pl.UTF-8):	Biblioteka libxklavier
Name:		libxklavier
Version:	5.4
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	https://people.freedesktop.org/~svu/%{name}-%{version}.tar.bz2
# Source0-md5:	13af74dcb6011ecedf1e3ed122bd31fa
URL:		https://www.freedesktop.org/Software/LibXklavier
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	bzip2
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gobject-introspection-devel >= 1.30.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.7}
BuildRequires:	iso-codes
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala >= 2:0.18.0.110}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXi-devel >= 1.1.3
BuildRequires:	xorg-lib-libxkbfile-devel
Requires:	glib2%{?_isa} >= 1:2.16.0
Requires:	iso-codes
Requires:	libxml2%{?_isa} >= 1:2.6.26
Requires:	xorg-lib-libXi%{?_isa} >= 1.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows you to simplify XKB-related development.

%description -l pl.UTF-8
Ta biblioteka pozwala uprościć programowanie związane z XKB.

%package devel
Summary:	Header files to develop libxklavier applications
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia aplikacji z użyciem libxklavier
Group:		X11/Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	glib2-devel%{?_isa} >= 1:2.16.0
Requires:	libxml2-devel%{?_isa} >= 1:2.6.26
Requires:	xorg-lib-libXi-devel%{?_isa} >= 1.1.3
Requires:	xorg-lib-libxkbfile-devel%{?_isa}

%description devel
Header files to develop libxklavier applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia aplikacji z użyciem libxklavier.

%package static
Summary:	Static version of libxklavier library
Summary(pl.UTF-8):	Statyczna wersja biblioteki libxklavier
Group:		X11/Development/Libraries
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static version of libxklavier library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libxklavier.

%package apidocs
Summary:	libxklavier API documentation
Summary(pl.UTF-8):	Dokumentacja API libxklavier
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
libxklavier API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libxklavier.

%prep
%setup -q

# gtkdoc-mktmpl no longer exists
%{__sed} -i -e '/@gtkdoc-mktmpl --module/d' gtk-doc.make

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{__enable_disable apidocs gtk-doc} \
	%{__enable_disable vala vala} \
	--disable-silent-rules \
	--with-xkb-bin-base=%{_bindir} \
	--with-xkb-base=%{_datadir}/X11/xkb \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%if %{without apidocs}
%{__rm} -rf $RPM_BUILD_ROOT%{_gtkdocdir}/%{name}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README
%{_libdir}/libxklavier.so.*.*.*
%ghost %{_libdir}/libxklavier.so.16
%{_libdir}/girepository-1.0/Xkl-1.0.typelib

%files devel
%defattr(644,root,root,755)
%{_libdir}/libxklavier.so
%{_datadir}/gir-1.0/Xkl-1.0.gir
%{_pkgconfigdir}/libxklavier.pc
%{_includedir}/libxklavier
%if %{with vala}
%{_datadir}/vala/vapi/libxklavier.deps
%{_datadir}/vala/vapi/libxklavier.vapi
%endif

%files static
%defattr(644,root,root,755)
%{_libdir}/libxklavier.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libxklavier
%endif
