%global vimfiles %{_datadir}/nvim/runtime

Name:           deoplete
Version:        5.2
Release:        1%{?dist}
Summary:        Dark powered asynchronous completion framework for neovim/Vim8
License:        MIT
URL:            https://github.com/Shougo/deoplete.nvim
Source0:        https://github.com/Shougo/deoplete.nvim/archive/%{version}.tar.gz

BuildArch:      noarch

Requires:       python3-neovim
Requires:       neovim


%description
Deoplete is the abbreviation of "dark powered neo-completion". It provides an extensible and asynchronous completion framework for neovim/Vim8.
deoplete will display completions via complete() by default.


%prep
%autosetup -n "%{name}.nvim-%{version}"


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
* Wed Apr 15 2020 Ben Reedy <breed808@breed808.com> - 5.2-1
- Update to 5.2

* Wed Nov 20 2019 Ben Reedy <breed808@breed808.com> - 5.1-1
- Initial package
