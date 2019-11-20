%global vimfiles %{_datadir}/nvim/runtime

%define commit f442e98c6c81649985f1cfc735fb4d25f3e27010

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
* Wed Nov 20 2019 Ben Reedy <breed808@breed808.com> - 0.0.1_f442e98c6c81649985f1cfc735fb4d25f3e27010-1
- Initial package
