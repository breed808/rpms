# Go compiler sets its own build ID, causing the build to fail.
%global _missing_build_ids_terminate_build 0
# Lack of debug files causes build to fail
%global debug_package %{nil}

Name:           k9s
Version:        0.50.4
Release:        %autorelease
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
# Hash mismatch in go.sum for tview dependency. Needs to be fixed in k9s upstream.
sed -i '/tview/d' go.sum
go mod tidy
make VERSION=%{version} build


%install
install -Dm0755 execs/k9s %{buildroot}%{_bindir}/k9s


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
%autochangelog
