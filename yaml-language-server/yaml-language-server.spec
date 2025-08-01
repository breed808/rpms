%global debug_package %{nil}
Name:           yaml-language-server
Version:        1.18.0
Release:        %autorelease
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
%autochangelog
