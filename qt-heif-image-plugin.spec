%undefine __cmake_in_source_build

Name:    qt-heif-image-plugin
Version: 0.3.3
Release: 5%{?dist}
Summary: Qt plugin for HEIF images

License: LGPLv3
URL:     https://github.com/jakar/qt-heif-image-plugin
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# https://github.com/jakar/qt-heif-image-plugin/issues/17
Patch0:  qt-heif-image-plugin-fix-libheif-1.7.0.patch

BuildRequires: cmake3
BuildRequires: gcc-c++
BuildRequires: cmake(Qt5)
BuildRequires: pkgconfig(libheif) >= 1.1
BuildRequires: qt5-rpm-macros

%description
%{summary}.


%prep
%autosetup -p1


%build
%cmake3
%cmake3_build


%install
%cmake3_install


%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_qt5_plugindir}/imageformats/libqheif.so


%changelog
* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.3.3-2
- added patch to work with libheif-1.7.0

* Sun Feb 23 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.3.3-1
- First spec for version 0.3.3

