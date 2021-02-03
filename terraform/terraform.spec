# Go compiler sets its own build ID, causing the build to fail.
%global _missing_build_ids_terminate_build 0

Name:           terraform
Version:        0.14.4
Release:        1%{?dist}
Summary:        Tool for building infrastructure safely and efficiently
License:        MPL-2.0
URL:            https://www.terraform.io/
Source0:        https://github.com/hashicorp/terraform/archive/v%{version}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%description
Terraform is a tool for building, changing, and versioning infrastructure
safely and efficiently. Terraform can manage existing and popular service
providers as well as custom in-house solutions.

%prep
%autosetup


%build
export GOFLAGS=-mod=vendor
go build -ldflags=-linkmode=external -o terraform-binary


%install
install -Dm0755 terraform-binary %{buildroot}%{_bindir}/terraform


%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}


%changelog
* Thu Jan 07 2021 Ben Reedy <breed808@breed808.com> - 0.14.4-1
- Update to latest upstream release

* Thu Dec 10 2020 Ben Reedy <breed808@breed808.com> - 0.14.2-1
- Update to latest upstream release

* Thu Dec 03 2020 Ben Reedy <breed808@breed808.com> - 0.14.0-1
- Update to latest upstream release

* Tue Oct 06 2020 Ben Reedy <breed808@breed808.com> - 0.13.4-1
- Update to latest upstream release

* Wed Sep 02 2020 Ben Reedy <breed808@breed808.com> - 0.13.1-1
- Update to latest upstream release

* Thu Aug 20 2020 Ben Reedy <breed808@breed808.com> - 0.13.0-1
- Update to latest upstream release

* Sat Jul 18 2020 Ben Reedy <breed808@breed808.com> - 0.12.28-1
- Update to latest upstream release

* Tue Nov 19 2019 Ben Reedy <breed808@breed808.com> - 0.12.16-1
- Initial package
