%global vimfiles %{_datadir}/nvim/runtime

%define commit 4f1ccd2ed70211fd025d052ec725c0b835bea487

Name:           deoplete-go
Version:        0.0.1_%{commit}
Release:        1%{?dist}
Summary:        deoplete.nvim source for Go
License:        MIT
URL:            https://github.com/deoplete-plugins/deoplete-go
Source0:        https://github.com/deoplete-plugins/deoplete-go/archive/%{commit}.zip

BuildArch:      noarch

Requires:       deoplete
Requires:       neovim
Requires:       python3-neovim
Requires:       python3-ujson


%description
Provides a Go completion source for Deoplete, using the popular gocode tool.


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
* Mon May 04 2020 Ben Reedy <breed808@breed808.com> - 0.0.1_4f1ccd2ed70211fd025d052ec725c0b835bea487-1
- Update to latest commit

* Wed Nov 20 2019 Ben Reedy <breed808@breed808.com> - 0.0.1_b82273104b3383ce8fc239243007865f308034ca-1
- Initial package
