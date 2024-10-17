Summary:	Hand write recognition/input using ibus IM engine
Name:		ibus-handwrite
Version:	2.1.4
Release:	5
License:	GPLv2+
Group:		System/Internationalization
Url:		https://code.google.com/p/ibus-handwrite/
Source0:	http://ibus-handwrite.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gdkglext-1.0)
BuildRequires:	pkgconfig(ibus-1.0)
BuildRequires:	pkgconfig(zinnia)
Requires:	ibus

%description
IBus handwrite project.

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_libexecdir}/ibus-engine-handwrite
%dir %{_datadir}/ibus-handwrite
%dir %{_datadir}/ibus-handwrite/data
%{_datadir}/ibus-handwrite/icons

#----------------------------------------------------------------------------

%package zh
Summary:	ibus-handwrite Chinese engine
Group:		System/Internationalization
Requires:	%{name} = %{EVRD}
Requires(post,preun):	GConf2

%description zh
ibus-handwrite Chinese engine.

%files zh
%{_datadir}/ibus-handwrite/data/table.txt
%{_datadir}/ibus/component/handwrite-zh.xml

#----------------------------------------------------------------------------

%package ja
Summary:	ibus-handwrite Japanese engine
Group:		System/Internationalization
Requires:	%{name} = %{EVRD}
Requires:	zinnia-tomoe-ja
Requires(post,preun):	GConf2

%description ja
ibus-handwrite Japanese engine.

%files ja
%{_datadir}/ibus/component/handwrite-jp.xml

#----------------------------------------------------------------------------

%prep
%setup -q

%build
export LDFLAGS="-lm"
%configure2_5x \
	--enable-zinnia \
	--with-zinnia-tomoe=%{_datadir}/zinnia/model/tomoe/
%make

%install
%makeinstall_std

%find_lang %{name}

