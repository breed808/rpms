%global vimfiles %{_datadir}/nvim/runtime

%define commit 4ed62b09b84b8212382d5c3b03278b6eb9ddc08b

Name:           vim-racer
Version:        0.0.1_%{commit}
Release:        1%{?dist}
Summary:        Rust code completion for Vim using Racer
License:        MIT
URL:            https://github.com/racer-rust/vim-racer
Source0:        https://github.com/racer-rust/vim-racer/archive/%{commit}.zip

BuildArch:      noarch

Requires:       deoplete
Requires:       neovim
Requires:       python3-neovim


%description
Provides a Rust completion source for Deoplete, using the popular Racer tool.


%prep
%autosetup -n "%{name}-%{commit}" -p1

%build


%install
mkdir -p %{buildroot}%{vimfiles}/rplugin/python3/deoplete/sources
cp -rp rplugin/python3/deoplete/sources/* %{buildroot}%{vimfiles}/rplugin/python3/deoplete/sources/

install -Dm0644 ftplugin/rust_racer.vim %{buildroot}%{vimfiles}/ftplugin/rust_racer.vim
install -Dm0644 autoload/racer.vim %{buildroot}%{vimfiles}/autoload/racer.vim
install -Dm0644 syntax/rustdoc.vim %{buildroot}%{vimfiles}/syntax/rustdoc.vim


%files
%doc README.md
%{vimfiles}/autoload
%{vimfiles}/ftplugin
%{vimfiles}/rplugin
%{vimfiles}/syntax


%changelog
* Wed Nov 20 2019 Ben Reedy <breed808@breed808.com> - 0.0.1_b82273104b3383ce8fc239243007865f308034ca-1
- Initial package
