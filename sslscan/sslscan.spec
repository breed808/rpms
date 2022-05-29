%global debug_package %{nil}
Name:           sslscan
Version:        2.0.13
Release:        1%{?dist}
Summary:        SSL/TLS cipher suite scanner

License:        GPLv3
URL:            https://github.com/rbsec/sslscan
Source0:        https://github.com/rbsec/sslscan/archive/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  openssl-devel

%description
sslscan tests SSL/TLS enabled services to discover supported cipher suites.

%prep
%autosetup


%build
%make_build


%install
%make_install


%files
%license LICENSE
%doc README.md INSTALL
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz


%changelog
* Sun May 29 2022 Ben Reedy <breed808@breed808.com> - 2.0.13-1
- Update to latest upstream release

* Wed June 30 2021 Ben Reedy <breed808@breed808.com> - 2.0.10-1
- Update to latest upstream release

* Tue Aug 18 2020 Ben Reedy <breed808@breed808.com> - 2.0.5-1
- Update to latest upstream release

* Tue Aug 18 2020 Ben Reedy <breed808@breed808.com> - 2.0.0-1
- Initial package
