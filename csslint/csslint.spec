Name:           csslint
Version:        1.0.5
Release:        1%{?dist}
Summary:        Detecting potential problems in CSS code

Group:          Development/Libraries
License:        MIT
URL:            http://github.com/CSSLint/csslint
Source0:        https://github.com/CSSLint/%{name}/archive/v%{version}.tar.gz
Source1:        %{name}.sh

BuildArch:      noarch
Requires:       rhino

%description
CSSLint is a tool to help point out problems with your CSS code. It does basic
syntax checking as well as applying a set of rules to the code that look for
problematic patterns or signs of inefficiency. The rules are all pluggable, so
you can easily write your own or omit ones you don't want.

%prep
%setup -q
# Executable
cp -p %{SOURCE1} .
sed -i -e 's|@JS_JAR@|%{_datadir}/java/js.jar|g' %{name}.sh
sed -i -e 's|@CSSLINT_RHINO@|%{_datadir}/%{name}/%{name}-rhino.js|g' %{name}.sh

%build

%install
install -d %{buildroot}%{_datadir}/%{name}
install -m644 dist/csslint-rhino.js %{buildroot}%{_datadir}/%{name}/
install -d %{buildroot}%{_bindir}
install -m755 %{name}.sh %{buildroot}%{_bindir}/%{name}

%files
%doc CHANGELOG README.md
%{_datadir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}

%changelog
* Fri Aug 09 2017 Ben Reedy <breed808@breed808.com> - 1.0.5-1
- Updated to latest upstream release

* Thu Jan 12 2017 Ben Reedy <breed808@breed808.com> - 1.0.3-2
- Updated package homepage

* Thu Jan 12 2017 Ben Reedy <breed808@breed808.com> - 1.0.3-1
- Upstream release

* Mon Oct 12 2015 Ben Reedy <breed808@breed808.com> - 0.10.0-1
- Initial package for OpenSUSE, inspired very heavily by the Fedora Project's spec file

