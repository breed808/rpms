%global vimfiles %{_datadir}/nvim/runtime
%define commit c4fe2529719e701d5d30994cab9650d82019f495

Name:           deoplete
Version:        6.0_%{commit}
Release:        1%{?dist}
Summary:        Dark powered asynchronous completion framework for neovim/Vim8
License:        MIT
URL:            https://github.com/Shougo/deoplete.nvim
# Source0:        https://github.com/Shougo/deoplete.nvim/archive/%%{version}.tar.gz
Source0:        https://github.com/Shougo/deoplete.nvim/archive/%{commit}.zip

BuildArch:      noarch

Requires:       python3-neovim
Requires:       neovim


%description
Deoplete is the abbreviation of "dark powered neo-completion". It provides an extensible and asynchronous completion framework for neovim/Vim8.
deoplete will display completions via complete() by default.


%prep
%autosetup -n "%{name}.nvim-%{commit}"


%build


%install
mkdir -p %{buildroot}%{vimfiles}/autoload
mkdir -p %{buildroot}%{vimfiles}/doc

cp -rp autoload/* %{buildroot}%{vimfiles}/autoload/
install -p -m0644 doc/*.txt %{buildroot}%{vimfiles}/doc/
cp -rp plugin/ %{buildroot}%{vimfiles}/plugin
cp -rp rplugin/ %{buildroot}%{vimfiles}/rplugin


%files
%license LICENSE
%doc README.md
%{vimfiles}/autoload
%{vimfiles}/doc
%{vimfiles}/plugin
%{vimfiles}/rplugin


%changelog
* Sun Feb 07 2021 Ben Reedy <breed808@breed808.com> - 6.0_c4fe2529719e701d5d30994cab9650d82019f495-1
- Update to latest release & git commit.

* Sun Nov 08 2020 Ben Reedy <breed808@breed808.com> - 5.2_a39f78f5e599ef29cc15c46c352ec5560e0f8e73-1
- Update to latest git commit, as there's been no recent release.

* Wed Apr 15 2020 Ben Reedy <breed808@breed808.com> - 5.2-1
- Update to 5.2

* Wed Nov 20 2019 Ben Reedy <breed808@breed808.com> - 5.1-1
- Initial package
