%global vimfiles %{_datadir}/nvim/runtime

%define commit 5891e2e1601237da229e5de6f242ad8616ea09d2

Name:           nvim-treesitter
Version:        0.0.7_%{commit}
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

cp -rp autoload/* %{buildroot}%{vimfiles}/autoload/
cp -p doc/*.txt %{buildroot}%{vimfiles}/doc/
cp -rp lua/ %{buildroot}%{vimfiles}/lua
cp -rp plugin/ %{buildroot}%{vimfiles}/plugin
cp -rp queries/ %{buildroot}%{vimfiles}/queries
install -Dm0644 lockfile.json %{buildroot}%{vimfiles}/lockfile.json


%files
%license LICENSE
%doc README.md
%{vimfiles}/autoload
%{vimfiles}/doc/*.txt
%{vimfiles}/lua
%{vimfiles}/plugin
%{vimfiles}/queries
%{vimfiles}/lockfile.json


%changelog
* Wed Sep 14 2022 Ben Reedy <breed808@breed808.com> - 0.0.8_5891e2e1601237da229e5de6f242ad8616ea09d2-1
- Update to latest git commit

* Sun May 29 2022 Ben Reedy <breed808@breed808.com> - 0.0.7_a10b603a2cd6d336412e996970e91566492562d2-1
- Update to latest git commit

* Wed May 11 2022 Ben Reedy <breed808@breed808.com> - 0.0.5_aaf5d370f477dd2ff5f7704fed93483f46d0eef0-1
- Update to latest git commit

* Thu Feb 17 2022 Ben Reedy <breed808@breed808.com> - 0.0.5_2298a7584414af40a6a09cbe72a81175382992c7-1
- Update to latest git commit

* Thu Sep 30 2021 Ben Reedy <breed808@breed808.com> - 0.0.4_b291c749230d14566ff2b13a36c98efda2a50196-1
- Update to latest git commit

* Thu Sep 30 2021 Ben Reedy <breed808@breed808.com> - 0.0.3_3a92d77b5684d58d777675c1863d304e0be71250-1
- Update to latest git commit

* Tue Feb 09 2021 Ben Reedy <breed808@breed808.com> - 0.0.2_09045354c0245ca866104c526bc57c2a06d7f381-1
- Update to latest git commit

* Tue Feb 09 2021 Ben Reedy <breed808@breed808.com> - 0.0.1_6533fb9af7f881c18b761ae94b2a502606f27989-1
- Initial package
