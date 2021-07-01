%global debug_package %{nil}
Name:           pyright
Version:        1.1.153
Release:        1%{?dist}
Summary:        Type check for the Python language
License:        MIT
URL:            https://github.com/microsoft/pyright
Source0:        https://github.com/microsoft/pyright/archive/%{version}.tar.gz
Provides:       pyright-langserver = %{version}
Requires:       nodejs >= 12

BuildRequires:  npm

%description
Pyright is a fast type checker meant for large Python source bases.
It can run in a “watch” mode and performs fast incremental updates when files are modified.

%prep
%autosetup


%build
npm install
cd packages/pyright
npm run build


%install
install -d "%{buildroot}%{_bindir}"
install -d "%{buildroot}%{_libdir}/node_modules/%{name}"

cd packages/pyright/

cp -r dist "%{buildroot}%{_libdir}/node_modules/%{name}/dist"
install -Dm755 index.js "%{buildroot}%{_libdir}/node_modules/%{name}/index.js"
install -Dm755 langserver.index.js "%{buildroot}%{_libdir}/node_modules/%{name}/langserver.index.js"
ln -s "%{_libdir}/node_modules/%{name}/index.js" "%{buildroot}%{_bindir}/pyright"
ln -s "%{_libdir}/node_modules/%{name}/langserver.index.js" "%{buildroot}%{_bindir}/pyright-langserver"


%files
%doc README.md docs/
%license LICENSE.txt
%{_bindir}/pyright
%{_bindir}/pyright-langserver
%{_libdir}/node_modules/%{name}

%changelog
* Thu Jul 01 2021 Ben Reedy <breed808@breed808.com> - 1.1.153-1
- Update to latest upstream release

* Wed Feb 10 2021 Ben Reedy <breed808@breed808.com> - 1.1.104-1
- Initial package
