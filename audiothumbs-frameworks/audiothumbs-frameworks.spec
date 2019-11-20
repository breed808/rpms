# Debug package breaking on F27 for unknown reason
%global debug_package %{nil}

%define commit 1d77a98f196762af4054624f01b47a64b75f500e

Name: audiothumbs-frameworks
Summary: Plugin for KDE file managers for KF5
License: GPL-2.0+
Url:    https://github.com/eplightning/audiothumbs-frameworks
Version: 0.0.1_%{commit}
Release: 1%{?dist}
Source: https://github.com/eplightning/audiothumbs-frameworks/archive/%{commit}.zip
Conflicts:  audiothumbs

BuildRequires:  automoc
BuildRequires:  kf5-kio-devel
BuildRequires:  qca2
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kde-workspace-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  flac-devel
BuildRequires:  libvorbis-devel
BuildRequires:  taglib-devel


%description
Plugin for KDE file managers (Dolphin and Konqueror) to preview cover arts embedded in Audio (MP3, FLAC, OGG) file tags as Thumbnails.


%prep
%setup -q -n %{name}-%{commit}


%build
mkdir build
cd build
cmake ../../audiothumbs-frameworks-%{commit} \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INCLUDE_PATH=/usr/include/QtCore \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DLIB_INSTALL_DIR=%{_libdir} \
    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
make


%install
cd build
make DESTDIR=%{?buildroot:%{buildroot}} install


%files
%license LICENSE
%doc README.md
%{_libdir}/qt5/plugins/AudioThumbs.so
%{_datadir}/kservices5/AudioThumbs.desktop


%changelog
* Wed Nov 20 2019 Ben Reedy <breed808@breed808.com> 0.0.1_1d77a98f196762af4054624f01b47a64b75f500e-1
- Initial package
