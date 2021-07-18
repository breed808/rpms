# Go compiler sets its own build ID, causing the build to fail.
%global _missing_build_ids_terminate_build 0
# Lack of debug files causes build to fail
%global debug_package %{nil}

Name:           k9s
Version:        0.24.14
Release:        1%{?dist}
Summary:        Kubernetes text-based user interface (TUI)
License:        Apache2
URL:            https://k9scli.io/
Source0:        https://github.com/derailed/k9s/archive/v%{version}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires:  git

%description
K9s provides a terminal UI to interact with your Kubernetes clusters. The aim of this project is to make it easier to navigate, observe and manage your applications in the wild. K9s continually watches Kubernetes for changes and offers subsequent commands to interact with your observed resources.

%prep
%autosetup


%build
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
make VERSION=%{version} build


%install
install -Dm0755 execs/k9s %{buildroot}%{_bindir}/k9s


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
* Mon Jul 19 2021 Ben Reedy <breed808@breed808.com> - 0.24.14-1
- Update to latest upstream release

* Sat June 19 2021 Ben Reedy <breed808@breed808.com> - 0.24.10-1
- Update to latest upstream release

* Sat May 08 2021 Ben Reedy <breed808@breed808.com> - 0.24.9-1
- Update to latest upstream release

* Thu Apr 01 2021 Ben Reedy <breed808@breed808.com> - 0.24.7-1
- Update to latest upstream release

* Sat Mar 27 2021 Ben Reedy <breed808@breed808.com> - 0.24.4-1
- Update to latest upstream release

* Tue Jan 19 2021 Ben Reedy <breed808@breed808.com> - 0.24.2-1
- Update to latest upstream release

* Wed Nov 25 2020 Ben Reedy <breed808@breed808.com> - 0.24.1-1
- Update to latest upstream release

* Thu Nov 19 2020 Ben Reedy <breed808@breed808.com> - 0.23.10-1
- Update to latest upstream release

* Tue Nov 10 2020 Ben Reedy <breed808@breed808.com> - 0.23.9-1
- Update to latest upstream release
