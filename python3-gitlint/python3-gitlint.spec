%global srcname gitlint
Name:       python-%{srcname}
Version:    0.17.0
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
* Fri Feb 18 2022 Ben Reedy <breed808@breed808.com> - 0.17.0-1
- Update to v0.17.0

* Tue Nov 23 2021 Ben Reedy <breed808@breed808.com> - 0.16.0-2
- Set package runtime dependencies correctly.

* Wed Nov 17 2021 Ben Reedy <breed808@breed808.com> - 0.16.0-1
- Update to latest release
- Add setuptools build dependency

* Thu Feb 04 2021 Ben Reedy <breed808@breed808.com> - 0.15.0-1
- Update to latest release
- Set manual runtime dependencies, as automatic dependency versioning is too strict.

* Wed Apr 15 2020 Ben Reedy <breed808@breed808.com> - 0.13.1-1
- Update to 0.13.1

* Wed Jan 01 2020 Ben Reedy <breed808@breed808.com> - 0.12.0-1
- Initial package
