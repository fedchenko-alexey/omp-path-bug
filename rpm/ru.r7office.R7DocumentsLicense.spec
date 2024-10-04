Name:       ru.r7office.R7DocumentsLicense

Summary:    Лицензии для приложения Р7-Документы
Version:    0.1
Release:    1
License:    Proprietary
URL:        https://r7-office.ru
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch

BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Qml)
Requires: libauroraapp-launcher
Requires: sailfishsilica-qt5 >= 0.10.9


%description
Licenses for R7-Documents application.

%prep
%autosetup

%build
%qmake5
%make_build

%install
%make_install

%files
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%attr(644,-,-) %{_datadir}/common/ru.r7office/R7DocumentsLicense/*.lickey
