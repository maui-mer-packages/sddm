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
Requires:   systemd
Requires(preun): systemd
Requires(post): systemd
Requires(postun): systemd
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Declarative)
BuildRequires:  cmake
BuildRequires:  pam-devel

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
# << install post

%preun
if [ "$1" -eq 0 ]; then
systemctl stop sddm.service
fi

%post
systemctl daemon-reload
systemctl reload-or-try-restart sddm.service

%postun
systemctl daemon-reload

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/sddm.conf
%{_bindir}/sddm
%{_bindir}/sddm-greeter
%{_appsdir}/apps/sddm/faces/*
%{_datadir}/apps/sddm/scripts/Xsession
%{_datadir}/apps/sddm/sddm.conf.sample
%{_datadir}/apps/sddm/themes/circles/*
%{_datadir}/apps/sddm/themes/elarun/*
%{_datadir}/apps/sddm/themes/maldives/*
%{_datadir}/apps/sddm/themes/maui/*
%{_sysconfdir}/pam.d/sddm
/lib/systemd/system/sddm.service
/lib/systemd/system/graphical.target.wants/sddm.service
%{_libdir}/qt5/imports/SddmComponents/*
# >> files
# << files
