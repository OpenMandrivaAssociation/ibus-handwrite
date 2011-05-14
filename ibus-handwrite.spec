Name: ibus-handwrite
Version: 2.1.4
Release: 1
Summary: Hand write recognition/input using ibus IM engine
License: GPLv2+
Group: System/Internationalization
URL: http://code.google.com/p/ibus-handwrite/
Source0: http://ibus-handwrite.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRequires: ibus-devel
BuildRequires: zinnia-devel
BuildRequires: gtkglext-devel
Requires: ibus

%description
IBus handwrite project.

%package zh
Summary: ibus-handwrite Chinese engine
Group: System/Internationalization
Requires: %{name} = %{version}
Requires(post,preun): GConf2

%description zh
ibus-handwrite Chinese engine.

%package ja
Summary: ibus-handwrite Japanese engine
Group: System/Internationalization
Requires: %{name} = %{version}
Requires: zinnia-tomoe
Requires(post,preun): GConf2

%description ja
ibus-handwrite Japanese engine.

%prep
%setup -q

%build
%configure2_5x --enable-zinnia --with-zinnia-tomoe=%{_datadir}/zinnia/model/tomoe/
%make

%install
%makeinstall_std

%find_lang %{name}

%post zh
%post_ibus_register_engine handwrite-zh_CN zh

%preun zh
%preun_ibus_unregister_engine handwrite-zh_CN

%post ja
%post_ibus_register_engine handwrite-ja ja

%preun ja
%preun_ibus_unregister_engine handwrite-ja

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libexecdir}/ibus-engine-handwrite
%dir %{_datadir}/ibus-handwrite
%dir %{_datadir}/ibus-handwrite/data
%{_datadir}/ibus-handwrite/icons

%files zh
%defattr(-,root,root,-)
%{_datadir}/ibus-handwrite/data/table.txt
%{_datadir}/ibus/component/handwrite-zh.xml

%files ja
%defattr(-,root,root,-)
%{_datadir}/ibus/component/handwrite-jp.xml
