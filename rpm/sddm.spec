# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       sddm

# >> macros
# << macros

Summary:    Lightweight QML-based display manager
Version:    0.1.0
Release:    1
Group:      System/GUI/Other
License:    LGPL-2.1+
URL:        https://github.com/sddm/sddm
Source0:    %{name}-%{version}.tar.xz
Source100:  sddm.yaml
Source101:  sddm-rpmlintrc
Requires:   xorg-x11-server-Xorg
Requires:   libxcb >= 1.10
Requires(preun): systemd
Requires(post): systemd
Requires(postun): systemd
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  cmake
BuildRequires:  pam-devel
BuildRequires:  qt5-qttools-linguist
BuildRequires:  systemd
Provides:   service(graphical-login) = %{name}

%description
Lightweight QML-based display manager.

%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%cmake .  \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DUSE_QT5:bool=ON

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
sed -i "s/MinimumUid=.*/MinimumUid=100000/g" %{buildroot}/etc/sddm.conf
sed -i "s/MaximumUid=.*/MaximumUid=199999/g" %{buildroot}/etc/sddm.conf
# << install post

%pre
# >> pre
# Create sddm user
/usr/sbin/useradd -m -u 42 -d /var/lib/sddm -s /sbin/nologin -r sddm > /dev/null 2>&1
/usr/sbin/usermod -d /var/lib/sddm -s /sbin/nologin sddm >/dev/null 2>&1
/usr/sbin/usermod -a -G video sddm >/dev/null 2>&1
# ignore errors, as we can't disambiguate between sddm already existed
# and couldn't create account with the current adduser.
exit 0
# << pre

%preun
# >> preun
%systemd_preun sddm.service
# << preun

%post
# >> post
%systemd_post sddm.service
# << post

%postun
# >> postun
%systemd_postun_with_restart sddm.service
# << postun

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/sddm.conf
%config(noreplace) %{_sysconfdir}/pam.d/sddm
%config(noreplace) %{_sysconfdir}/pam.d/sddm-autologin
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.DisplayManager.conf
%{_bindir}/sddm
%{_bindir}/sddm-greeter
%{_datadir}/apps/sddm/faces/*
%{_datadir}/apps/sddm/flags/*
%{_datadir}/apps/sddm/scripts/*
%{_datadir}/apps/sddm/translations/*
%{_datadir}/apps/sddm/sddm.conf.sample
%{_datadir}/apps/sddm/themes/circles/*
%{_datadir}/apps/sddm/themes/elarun/*
%{_datadir}/apps/sddm/themes/maldives/*
%{_datadir}/apps/sddm/themes/maui/*
%{_unitdir}/sddm.service
%{_libdir}/qt5/qml/SddmComponents/*
# >> files
# << files
