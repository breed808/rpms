# Go compiler sets its own build ID, causing the build to fail.
%global _missing_build_ids_terminate_build 0
# Lack of debug files causes build to fail
%global debug_package %{nil}

Name:           arduino-cli
Version:        0.22.0
Release:        1%{?dist}
Summary:        Language server for Arduino programming language
License:        Apache2
URL:            https://github.com/arduino/arduino-cli
Source0:        https://github.com/arduino/arduino-cli/archive/refs/tags/%{version}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires:  git

%description
Arduino CLI is an all-in-one solution that provides Boards/Library Managers, sketch builder, board detection, uploader,
and many other tools needed to use any Arduino compatible board and platform from command line or machine interfaces.

%prep
%autosetup


%build
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
go build


%install
install -Dm0755 arduino-cli %{buildroot}%{_bindir}/arduino-cli


%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}


%changelog
* Sun May 29 2022 Ben Reedy <breed808@breed808.com> - 0.22.0-1
- Update to v0.22.0

* Fri Feb 18 2022 Ben Reedy <breed808@breed808.com> - 0.21.0-1
- Initial package
