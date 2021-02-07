Name:           Lightly 
Version:        0.4 
Release:        1
Summary:        Visually modern and minimalistic plasma style
Group:          System/GUI/KDE
License:        GPL-2.0+
Url:            https://github.com/Luwx/Lightly
Source0:        %{url}/archive/v%{version}.tar.gz
BuildRequires:  cmake(KF5Plasma) 
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KDecoration2)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  fdupes

%if 0%{?suse_version} > 1500 
BuildRequires:  plasma5-workspace-devel
BuildRequires:  kitemmodels-devel
%elif 0%{?fedora}
BuildRequires:  glibc-langpack-en
BuildRequires:  plasma-workspace-devel
BuildRequires:  kf5-kitemmodels-devel
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Lightly is a fork of breeze theme style that aims to be visually modern and minimalistic.
Lightly is a work in progress theme, there is still a lot to change, so expect bugs! Some applications may suddenly crash or flicker.

%prep
%setup -q

%build
%if 0%{?suse_version} > 1500 
%cmake_kf5 -d build -- -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=lib -DBUILD_TESTING=OFF .. 
%elif 0%{?fedora}
%{__mkdir_p} build
pushd build
%{cmake_kf5} -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=lib -DBUILD_TESTING=OFF ..
%endif
make -j$(nproc)

%install
%if 0%{?suse_version} > 1500 
%kf5_makeinstall -C build
%elif 0%{?fedora}
make install/fast DESTDIR=%{buildroot} -C build
find %{buildroot} -size 0 -delete
%endif
%fdupes -s %{buildroot}

%post
/sbin/ldconfig 

%postun
/sbin/ldconfig 

%files
%if 0%{?suse_version} > 1500 
%{_datadir}/color-schemes
%{_datadir}/kstyle
%{_datadir}/kservices5
%{_libdir}/cmake/Lightly
%{_libdir}/kconf_update_bin
%{_libdir}/qt5
%{_datadir}/color-schemes/Lightly.colors
%{_datadir}/kconf_update/kde4lightly.upd
%{_datadir}/kservices5/lightlydecorationconfig.desktop
%{_datadir}/kservices5/lightlystyleconfig.desktop
%{_datadir}/kstyle/themes/lightly.themerc
%{_libdir}/cmake/Lightly/LightlyConfig.cmake
%{_libdir}/cmake/Lightly/LightlyConfigVersion.cmake
%{_libdir}/kconf_update_bin/kde4lightly
%{_libdir}/liblightlycommon5.so.5
%{_libdir}/liblightlycommon5.so.5.19.4
%{_libdir}/qt5/plugins/kstyle_lightly_config.so
%{_libdir}/qt5/plugins/org.kde.kdecoration2/lightlydecoration.so
%{_libdir}/qt5/plugins/styles/lightly.so
%elif 0%{?fedora}
%dir %{_datadir}/color-schemes
%dir %{_datadir}/kstyle
%dir %{_datadir}/kservices5
%dir %{_libdir}/cmake/Lightly
%dir %{_libdir}/kconf_update_bin
%dir %{_libdir}/qt5
%{_datadir}/color-schemes/Lightly.colors
%{_datadir}/kconf_update/kde4lightly.upd
%{_datadir}/kservices5/lightlydecorationconfig.desktop
%{_datadir}/kservices5/lightlystyleconfig.desktop
%{_datadir}/kstyle/themes/lightly.themerc
%{_libdir}/cmake/Lightly/LightlyConfig.cmake
%{_libdir}/cmake/Lightly/LightlyConfigVersion.cmake
%{_libdir}/kconf_update_bin/kde4lightly
%{_libdir}/liblightlycommon5.so.5
%{_libdir}/liblightlycommon5.so.5.19.4
%{_libdir}/qt5/plugins/kstyle_lightly_config.so
%{_libdir}/qt5/plugins/org.kde.kdecoration2/lightlydecoration.so
%{_libdir}/qt5/plugins/styles/lightly.so
%endif