%global debug_package %{nil}
%define commit b2e912727aa92a8090cca7c498807b100920fe62
Name:           tmpmail
Version:        0.0.0_%{commit}
Release:        2%{?dist}
Summary:        A temporary email right from your terminal
License:        MIT
URL:            https://github.com/sdushantha/tmpmail
Source0:        https://github.com/sdushantha/tmpmail/archive/%{commit}.zip
BuildRequires:  gzip
BuildArch:      noarch


%description

%prep
%autosetup -n %{name}-%{commit}


%build


%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
gzip %{name}.1
install -Dm644 %{name}.1.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Jan 13 2021 Ben Reedy <breed808@breed808.com> - 0.0.0_b2e912727aa92a8090cca7c498807b100920fe62-2
- Set correct manpage location
- Compress manpage with gzip

* Wed Jan 13 2021 Ben Reedy <breed808@breed808.com> - 0.0.0_b2e912727aa92a8090cca7c498807b100920fe62-1
- Initial package
