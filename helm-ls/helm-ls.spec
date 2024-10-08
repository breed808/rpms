# Go compiler sets its own build ID, causing the build to fail.
%global _missing_build_ids_terminate_build 0
# Lack of debug files causes build to fail
%global debug_package %{nil}

Name:           helm-ls
Version:        0.1.0
Release:        %autorelease
Summary:        Language server for Helm
License:        MIT
URL:            https://github.com/mrjosh/helm-ls
Source0:        https://github.com/mrjosh/helm-ls/archive/refs/tags/v%{version}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires:  git

%description
Language server for Helm

%prep
%autosetup


%build
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
go mod tidy
go build


%install
install -Dm0755 %{name} %{buildroot}%{_bindir}/%{name}


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
%autochangelog
