%global debug_package %{nil}
Name:           yaml-language-server
Version:        1.11.0
Release:        1%{?dist}
Summary:        Language Server for YAML Files
License:        MIT
URL:            https://github.com/redhat-developer/yaml-language-server
Source0:        https://github.com/redhat-developer/yaml-language-server/archive/refs/tags/%{version}.tar.gz
Requires:       nodejs >= 12

BuildRequires:  nodejs
BuildRequires:  yarnpkg
BuildRequires:  jq

%description
Language Server for YAML Files

%prep
%autosetup


%build
yarn --frozen-lockfile
yarn compile
yarn build:libs

%install
# Emulate `npm prune --production`
cp package.json{,.bak}
read -ra devDependencies < <(jq -r '.devDependencies | keys | join(" ")' package.json)
yarn remove --frozen-lockfile "${devDependencies[@]}"
mv package.json{.bak,}

install -d "%{buildroot}%{_bindir}/node_modules/%{name}"
install -d "%{buildroot}%{_libdir}/node_modules/%{name}"
ln -s %{_libdir}/node_modules/%{name}/bin/%{name} "%{buildroot}"/usr/bin/%{name}
cp -r bin lib node_modules out package.json \
  "%{buildroot}%{_libdir}/node_modules/%{name}"

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/yaml-language-server
%{_libdir}/node_modules/%{name}

%changelog
* Tue Jan 10 2023 Ben Reedy <breed808@breed808.com> - 1.11.0-1
- Upgrade to v1.11.0

* Wed Aug 22 2022 Ben Reedy <breed808@breed808.com> - 1.10.0-1
- Upgrade to v1.10.0

* Fri July 13 2022 Ben Reedy <breed808@breed808.com> - 1.9.0-1
- Upgrade to v1.9.0

* Fri June 10 2022 Ben Reedy <breed808@breed808.com> - 1.8.0-1
- Upgrade to v1.8.0

* Tue Apr 26 2022 Ben Reedy <breed808@breed808.com> - 1.7.0-1
- Upgrade to v1.7.0

* Wed Apr 20 2022 Ben Reedy <breed808@breed808.com> - 1.6.0-1
- Initial package
