Name:		udev-rule-hs3110
Version:	1.0
Release:	1%{?dist}
Summary:	Udev rules adding support for HP hs3110+ HSPA broadband modem

License:	GPL
URL:		https://github.com/jdsieci/udev-rule-hs3110
Source0:	https://github.com/jdsieci/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

Requires:	systemd-udev

BuildRequires:	systemd

%description
Udev rules adding support for HP hs3110+ HSPA broadband modem

%prep
%setup -q

%build

%install
install -d 755 %{buildroot}%{_udevrulesdir}
install -pm 644 70-hs3110.rules %{buildroot}%{_udevrulesdir}

%files
%defattr(-,root,root,-)
%{_udevrulesdir}/70-hs3110.rules

%changelog
* Sat Sep 30 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.0-1
- initial build
