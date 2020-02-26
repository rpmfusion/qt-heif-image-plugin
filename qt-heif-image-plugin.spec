Name:    qt-heif-image-plugin
Version: 0.3.3
Release: 1%{?dist}
Summary: Qt plugin for HEIF images

License: LGPLv3
URL:     https://github.com/jakar/qt-heif-image-plugin
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: cmake(Qt5)
BuildRequires: pkgconfig(libheif) >= 1.1
BuildRequires: qt5-rpm-macros

%description
%{summary}.


%prep
%autosetup


%build
%cmake .
%make_build


%install
%make_install


%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_qt5_plugindir}/imageformats/libqheif.so


%changelog
* Sun Feb 23 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.3.3-1
- First spec for version 0.3.3

