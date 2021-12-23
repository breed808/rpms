%global vimfiles %{_datadir}/nvim/runtime

%define commit 43058915007d92dc167b84dd5b8ada2d2a057a82

Name:           deoplete-jedi
Version:        0.0.1_%{commit}
Release:        1%{?dist}
Summary:        deoplete.nvim source for Python
License:        MIT
URL:            https://github.com/deoplete-plugins/deoplete-jedi
Source0:        https://github.com/deoplete-plugins/deoplete-jedi/archive/%{commit}.zip

BuildArch:      noarch

Requires:       deoplete
Requires:       neovim
Requires:       python3-neovim
Requires:       python3-jedi
Requires:       python3-parso


%description
Provides a Python completion source for Deoplete, using the popular Jedi tool.


%prep
%autosetup -n "%{name}-%{commit}" -p1

%build


%install
mkdir -p %{buildroot}%{vimfiles}/rplugin/python3/deoplete/sources
cp -rp rplugin/python3/deoplete/sources/* %{buildroot}%{vimfiles}/rplugin/python3/deoplete/sources/


%files
%license LICENSE
%doc README.md
%{vimfiles}/rplugin


%changelog
* Fri Dec 24 2021 Ben Reedy <breed808@breed808.com> - 0.0.1_43058915007d92dc167b84dd5b8ada2d2a057a82-1
- Update to latest project commit

* Wed Apr 15 2020 Ben Reedy <breed808@breed808.com> - 0.0.1_42f4c24a951b0fb5e76a70e5234f16193a8a746d-1
- Update to latest project commit

* Wed Nov 20 2019 Ben Reedy <breed808@breed808.com> - 0.0.1_f442e98c6c81649985f1cfc735fb4d25f3e27010-1
- Initial package
