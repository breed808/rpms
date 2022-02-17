# Go compiler sets its own build ID, causing the build to fail.
%global _missing_build_ids_terminate_build 0
# Lack of debug files causes build to fail
%global debug_package %{nil}

Name:           arduino-language-server
Version:        0.6.0
Release:        1%{?dist}
Summary:        Kubernetes text-based user interface (TUI)
License:        Apache2
URL:            https://arduino-language-servercli.io/
Source0:        https://github.com/derailed/arduino-language-server/archive/v%{version}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires:  git

%description
The Arduino Language Server is the tool that powers the autocompletion of the new Arduino IDE 2.
It implements the standard Language Server Protocol so it can be used with other IDEs as well.

%prep
%autosetup


%build
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
go build


%install
install -Dm0755 arduino-language-server %{buildroot}%{_bindir}/arduino-language-server


%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}


%changelog
* Thu Feb 17 2022 Ben Reedy <breed808@breed808.com> - 0.6.0-1
- Initial package
