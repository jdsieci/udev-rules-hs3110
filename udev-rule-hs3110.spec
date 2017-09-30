Name:		udev-rule-hs3110
Version:	1
Release:	1%{?dist}
Summary:	

License:	GPL
URL:		https://github.com/jdsieci/hs3110_udev
Source0:	https://github.com/jdsieci/hs3110_udev/


%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc



%changelog

