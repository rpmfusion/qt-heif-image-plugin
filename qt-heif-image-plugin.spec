%undefine __cmake_in_source_build

Name:    qt-heif-image-plugin
Version: 0.3.4
Release: 4%{?dist}
Summary: Qt plugin for HEIF images

License: LGPLv3
URL:     https://github.com/jakar/qt-heif-image-plugin
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

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
* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 09 2023 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.3.4-1
- version 0.3.4

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

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

