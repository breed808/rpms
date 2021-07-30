# Go compiler sets its own build ID, causing the build to fail.
%undefine _missing_build_ids_terminate_build

%global debug_package %{nil}

Name:           jsonnet-bundler
Version:        0.4.0
Release:        1%{?dist}
Summary:        Jsonnet package manager
License:        ASL 2.0
URL:            https://github.com/jsonnet-bundler/jsonnet-bundler
Source0:        https://github.com/jsonnet-bundler/jsonnet-bundler/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  git

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%description
The jsonnet-bundler is a package manager for Jsonnet.


%prep
%autosetup


%build
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
go build -o jb ./cmd/jb


%install
install -Dm0755 jb %{buildroot}%{_bindir}/jb


%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/jb


%changelog
* Fri Jul 30 2021 Ben Reedy <breed808@breed808.com> - 0.4.0-1
- Initial package
