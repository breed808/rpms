%global vimfiles %{_datadir}/nvim/runtime

%define commit 09045354c0245ca866104c526bc57c2a06d7f381

Name:           nvim-treesitter
Version:        0.0.2_%{commit}
Release:        1%{?dist}
Summary:        Experimental highlighting plugin for Neovim
License:        MIT
URL:            https://github.com/nvim-treesitter/nvim-treesitter
Source0:        https://github.com/nvim-treesitter/nvim-treesitter/archive/%{commit}.zip

BuildArch:      noarch

Requires:       neovim
Requires:       gcc-c++
Requires:       libstdc++-static

%description
nvim-treesitter provides a simple and easy way to use the interface for tree-sitter in Neovim and provides some basic functionality such as highlighting based on it.


%prep
%autosetup -n "%{name}-%{commit}" -p1

%build


%install
mkdir -p %{buildroot}%{vimfiles}/autoload
mkdir -p %{buildroot}%{vimfiles}/doc

cp -rp after/ %{buildroot}%{vimfiles}/after
cp -rp autoload/* %{buildroot}%{vimfiles}/autoload/
cp -p doc/*.txt %{buildroot}%{vimfiles}/doc/
cp -rp ftdetect/ %{buildroot}%{vimfiles}/ftdetect
cp -rp lua/ %{buildroot}%{vimfiles}/lua
cp -rp plugin/ %{buildroot}%{vimfiles}/plugin
cp -rp queries/ %{buildroot}%{vimfiles}/queries
install -Dm0644 lockfile.json %{buildroot}%{vimfiles}/lockfile.json


%files
%license LICENSE
%doc README.md
%{vimfiles}/after
%{vimfiles}/autoload
%{vimfiles}/doc/*.txt
%{vimfiles}/ftdetect
%{vimfiles}/lua
%{vimfiles}/plugin
%{vimfiles}/queries
%{vimfiles}/lockfile.json


%changelog
* Tue Feb 09 2021 Ben Reedy <breed808@breed808.com> - 0.0.2_09045354c0245ca866104c526bc57c2a06d7f381-1
- Update to latest git commit

* Tue Feb 09 2021 Ben Reedy <breed808@breed808.com> - 0.0.1_6533fb9af7f881c18b761ae94b2a502606f27989-1
- Initial package
