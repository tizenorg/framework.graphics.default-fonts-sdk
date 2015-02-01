#default-fonts-sdk
Name:       default-fonts-sdk
Summary:    fonts for Tizen SDK
Version:    1.2.2.5
Release:    21
Group:      TO_BE/FILLED_IN
License:    Apache License, Version 2.0
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/default-fonts-sdk.manifest
Requires(post): fontconfig

%description
fonts for Tizen SDK
This package is maintained by SDK team


%package -n slp-fonts-arabic
Summary: SLP Arabic fonts
Group: TO_BE / FILLED_IN
Requires(post): fontconfig

%description -n slp-fonts-arabic
Arabic font set for SLP


%package -n slp-fonts-hebrew
Summary: SLP Hebrew fonts
Group: TO_BE / FILLED_IN
Requires(post): fontconfig

%description -n slp-fonts-hebrew
Hebrew font set for SLP


%package -n slp-fonts-india
Summary: SLP India fonts
Group: TO_BE / FILLED_IN
Requires(post): fontconfig

%description -n slp-fonts-india
India font set for SLP


%package -n slp-fonts-korean
Summary: SLP Korean fonts
Group: TO_BE / FILLED_IN
Requires(post): fontconfig

%description -n slp-fonts-korean
Korean font set for SLP


%package -n slp-fonts-thai
Summary: SLP Thai fonts
Group: TO_BE / FILLED_IN
Requires(post): fontconfig

%description -n slp-fonts-thai
Thai font set for SLP


%package -n slp-fonts-armenian
Summary: SLP Armenian fonts
Group: TO_BE / FILLED_IN
Requires(post): fontconfig

%description -n slp-fonts-armenian
Armenian font set for SLP

%package -n slp-fonts-georgian
Summary: SLP Georgian fonts
Group: TO_BE / FILLED_IN
Requires(post): fontconfig

%description -n slp-fonts-georgian
Georgian font set for SLP

%package -n slp-fonts-ethiopic
Summary: SLP Ethiopic fonts
Group: TO_BE / FILLED_IN
Requires(post): fontconfig

%description -n slp-fonts-ethiopic
Ethiopic font set for SLP

%package -n slp-fonts-khmer
Summary: SLP khmer fonts
Group: TO_BE / FILLED_IN
Requires(post): fontconfig

%description -n slp-fonts-khmer
Khmer font set for SLP

%package -n slp-fonts-laos
Summary: SLP laos fonts
Group: TO_BE / FILLED_IN
Requires(post): fontconfig

%description -n slp-fonts-laos
Laos font set for SLP

%package -n slp-fonts-myanmar
Summary: SLP myanmar fonts
Group: TO_BE / FILLED_IN
Requires(post): fontconfig

%description -n slp-fonts-myanmar
Myanmar font set for SLP


%prep
%setup -q

%build
cp %{SOURCE1001} .

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/license && cp LICENSE %{buildroot}/usr/share/license/%{name}
mkdir -p %{buildroot}%{_datadir}/fonts && cp -a fonts %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_datadir}/fallback_fonts && cp -a fallback_fonts %{buildroot}%{_datadir}

%post
/usr/bin/fc-cache -f

%post -n slp-fonts-arabic
/usr/bin/fc-cache -f

%post -n slp-fonts-hebrew
/usr/bin/fc-cache -f

%post -n slp-fonts-india
/usr/bin/fc-cache -f

%post -n slp-fonts-korean
/usr/bin/fc-cache -f

%post -n slp-fonts-thai
/usr/bin/fc-cache -f

%post -n slp-fonts-armenian
/usr/bin/fc-cache -f

%post -n slp-fonts-georgian
/usr/bin/fc-cache -f

%post -n slp-fonts-ethiopic
/usr/bin/fc-cache -f

%post -n slp-fonts-khmer
/usr/bin/fc-cache -f

%post -n slp-fonts-laos
/usr/bin/fc-cache -f

%post -n slp-fonts-myanmar
/usr/bin/fc-cache -f


%files
%manifest default-fonts-sdk.manifest
%defattr(-,root,root,-)
%{_datadir}/fonts/*
%{_datadir}/fallback_fonts/*
/usr/share/license/%{name}

%files -n slp-fonts-arabic
%manifest default-fonts-sdk.manifest
%defattr(-,root,root,-)
%{_datadir}/fallback_fonts/TizenSansArabicRegular.ttf

%files -n slp-fonts-hebrew
%manifest default-fonts-sdk.manifest
%defattr(-,root,root,-)
%{_datadir}/fallback_fonts/TizenSansHebrewMedium.ttf
%{_datadir}/fallback_fonts/TizenSansHebrewRegular.ttf

%files -n slp-fonts-india
%manifest default-fonts-sdk.manifest
%defattr(-,root,root,-)
%{_datadir}/fallback_fonts/TizenSansBengaliRegular.ttf
%{_datadir}/fallback_fonts/TizenSansGujarathiRegular.ttf
%{_datadir}/fallback_fonts/TizenSansHindiRegular.ttf
%{_datadir}/fallback_fonts/TizenSansKannadaRegular.ttf
%{_datadir}/fallback_fonts/TizenSansMalayalamRegular.ttf
%{_datadir}/fallback_fonts/TizenSansOriyaRegular.ttf
%{_datadir}/fallback_fonts/TizenSansPunjabiRegular.ttf
%{_datadir}/fallback_fonts/TizenSansSinhalaRegular.ttf
%{_datadir}/fallback_fonts/TizenSansTamilRegular.ttf
%{_datadir}/fallback_fonts/TizenSansTeluguRegular.ttf

%files -n slp-fonts-korean
%manifest default-fonts-sdk.manifest
%defattr(-,root,root,-)
%{_datadir}/fallback_fonts/TizenSansKoreanMedium.ttf
%{_datadir}/fallback_fonts/TizenSansKoreanRegular.ttf

%files -n slp-fonts-thai
%manifest default-fonts-sdk.manifest
%defattr(-,root,root,-)
%{_datadir}/fallback_fonts/TizenSansThaiRegular.ttf

%files -n slp-fonts-armenian
%manifest default-fonts-sdk.manifest
%defattr(-,root,root,-)
%{_datadir}/fallback_fonts/TizenSansArmenianMedium.ttf
%{_datadir}/fallback_fonts/TizenSansArmenianRegular.ttf

%files -n slp-fonts-georgian
%manifest default-fonts-sdk.manifest
%defattr(-,root,root,-)
%{_datadir}/fallback_fonts/TizenSansGeorgianMedium.ttf
%{_datadir}/fallback_fonts/TizenSansGeorgianRegular.ttf

%files -n slp-fonts-ethiopic
%manifest default-fonts-sdk.manifest
%defattr(-,root,root,-)
%{_datadir}/fallback_fonts/TizenSansEthiopicRegular.ttf

%files -n slp-fonts-khmer
%manifest default-fonts-sdk.manifest
%defattr(-,root,root,-)
%{_datadir}/fallback_fonts/TizenSansKhmerRegular.ttf

%files -n slp-fonts-laos
%manifest default-fonts-sdk.manifest
%defattr(-,root,root,-)
%{_datadir}/fallback_fonts/TizenSansLaoRegular.ttf

%files -n slp-fonts-myanmar
%manifest default-fonts-sdk.manifest
%defattr(-,root,root,-)
%{_datadir}/fallback_fonts/ZawgyiOne2008.ttf

