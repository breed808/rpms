%global vimfiles %{_datadir}/nvim/runtime

%define commit e526dbecda137e37c45492ce72fa92ea32314154

Name:           deoplete-lsp
Version:        0.0.1_%{commit}
Release:        2%{?dist}
Summary:        deoplete.nvim source for LSP clients
License:        MIT
URL:            https://github.com/deoplete-plugins/deoplete-lsp
Source0:        https://github.com/deoplete-plugins/deoplete-lsp/archive/%{commit}.zip

BuildArch:      noarch

Requires:       deoplete
Requires:       neovim-nightly
Requires:       python3-neovim
Requires:       python3-ujson


%description
Provides an LSP completion source for Deoplete, using the Neovim native Language Server Protocol client.


%prep
%autosetup -n "%{name}-%{commit}" -p1

%build


%install
mkdir -p %{buildroot}%{vimfiles}/rplugin/python3/deoplete/source
cp -rp rplugin/python3/deoplete/source/* %{buildroot}%{vimfiles}/rplugin/python3/deoplete/source/
cp -rp autoload/ %{buildroot}%{vimfiles}/autoload
cp -rp plugin/ %{buildroot}%{vimfiles}/plugin
cp -rp lua/ %{buildroot}%{vimfiles}/lua


%files
%license LICENSE
%doc README.md
%{vimfiles}/autoload
%{vimfiles}/lua
%{vimfiles}/plugin
%{vimfiles}/rplugin


%changelog
* Wed Feb 10 2021 Ben Reedy <breed808@breed808.com> - 0.0.1_e526dbecda137e37c45492ce72fa92ea32314154-2
- Set runtime dependency of neovim-nightly (from neovim)

* Tue Feb 09 2021 Ben Reedy <breed808@breed808.com> - 0.0.1_e526dbecda137e37c45492ce72fa92ea32314154-1
- Initial package
