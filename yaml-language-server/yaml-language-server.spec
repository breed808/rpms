%global debug_package %{nil}
Name:           yaml-language-server
Version:        1.23.0
Release:        %autorelease
Summary:        Language Server for YAML Files
License:        MIT
URL:            https://github.com/redhat-developer/yaml-language-server
Source0:        https://github.com/redhat-developer/yaml-language-server/archive/refs/tags/%{version}.tar.gz
Requires:       nodejs >= 12

BuildRequires:  nodejs
BuildRequires:  nodejs-npm
BuildRequires:  typescript

%description
Language Server for YAML Files

%prep
%autosetup


%build
npm ci
npm run compile

%install
npm prune --omit=dev

install -d "%{buildroot}%{_libdir}/node_modules/%{name}"
install -d "%{buildroot}%{_bindir}"
cp -r bin l10n node_modules out package.json \
  "%{buildroot}%{_libdir}/node_modules/%{name}"
ln -s "%{_libdir}/node_modules/%{name}/bin/%{name}" "%{buildroot}/usr/bin/%{name}"

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/yaml-language-server
%{_libdir}/node_modules/%{name}

%changelog
%autochangelog
