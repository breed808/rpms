# Go compiler sets its own build ID, causing the build to fail.
%global _missing_build_ids_terminate_build 0
# Lack of debug files causes build to fail
%global debug_package %{nil}

Name:           argocd
Version:        3.5.5
Release:        %autorelease
Summary:        Declarative Continuous Deployment for Kubernetes
License:        Apache-2.0
URL:            https://github.com/argoproj/argo-cd
Source0:        https://github.com/argoproj/argo-cd/archive/v%{version}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires:  git

%description
Language server for Helm

%prep
%autosetup -n argo-cd-%{version}


%build
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
go mod tidy
go build -o argocd \
-ldflags "-X github.com/argoproj/argo-cd/v3/common.version=%{version} -X github.com/argoproj/argo-cd/v3/common.gitTag=%{version} -compressdwarf=false -linkmode=external" \
./cmd

# ./%{name} completion bash > %{name}.bash
# ./%{name} completion zsh > %{name}.zsh
# Already provided by Fish package
# ./%{name} completion fish > %{name}.fish

%install
install -Dm0755 %{name} %{buildroot}%{_bindir}/%{name}
# install -Dm0644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
# install -Dm0644 %{name}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
# install -Dm0644 %{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
%autochangelog
