%global debug_package %{nil}
Name:           sslscan
Version:        2.1.5
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
%autochangelog
