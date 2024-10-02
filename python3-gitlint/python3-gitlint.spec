%global srcname gitlint
Name:       python-%{srcname}
Version:    0.19.1
Release:    1%{?dist}
Summary:    Linting for your git commit messages

License:    MIT
URL:        https://pypi.org/project/gitlint/
Source0:    https://github.com/jorisroovers/gitlint/archive/refs/tags/v%{version}.tar.gz

BuildArch: noarch


%global _description %{expand:
Git commit message linter written in python (for Linux and Mac, experimental on Windows), checks your commit messages for style.}

%{?python_disable_dependency_generator}
%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:   python3-arrow >= 0.17
Requires:   python3-sh >= 1.14.1
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}


%build
cd gitlint-core
%py3_build


%install
cd gitlint-core
%py3_install


# %%check
# %%{__python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}_core-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/%{srcname}


%changelog
%autochangelog
