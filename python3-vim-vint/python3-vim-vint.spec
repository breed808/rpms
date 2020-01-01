%global srcname vim-vint
Name:       python-%{srcname}
Version:    0.3.21
Release:    1%{?dist}
Summary:    Vim script language linter

License:    MIT
URL:        https://pypi.org/project/vim-vint/
Source0:    %{pypi_source}

BuildArch: noarch

%global _description %{expand:
Fast and Highly Extensible Vim script Language Lint implemented in Python}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


# %%check
# %%{__python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/vim_vint-*.egg-info/
%{python3_sitelib}/vint/
%{_bindir}/vint


%changelog
* Wed Jan 01 2020 Ben Reedy <breed808@breed808.com> - 0.3.21-1
- Initial package

