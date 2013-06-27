#default-fonts-sdk
Name:       default-fonts-sdk
Summary:    free fonts for Tizen SDK
Version:    1.2.2.0
Release:    14
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/default-fonts-sdk.manifest

%description
free fonts for Tizen SDK
This package is maintained by SDK team

%prep
%setup -q

%build
cp %{SOURCE1001} .

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/fonts && cp -a fonts %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_datadir}/fallback_fonts && cp -a fallback_fonts %{buildroot}%{_datadir}

%files
%manifest default-fonts-sdk.manifest
%defattr(0644,root,root,-)
%{_datadir}/fonts/*
%{_datadir}/fallback_fonts/*

