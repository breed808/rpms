# Run tests (requires network connectivity)
%global with_check 0

# Prebuilt binaries break build process for CentOS. Disable debug packages to resolve
%if 0%{?rhel}
%define debug_package %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         helm
%global repo            helm
# https://github.com/prometheus/prometheus/
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           golang-%{provider}-%{project}-%{repo}
Version:        3.6.3
Release:        1%{?dist}
Summary:        The Kubernetes Package Manager
License:        Apache 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/v%{version}.tar.gz

Provides:       helm = %{version}-%{release}

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
# Network build required as offline build fails due to vendor/ dependency issues
BuildRequires:  git


%description
Helm is a tool for managing Charts. Charts are packages of pre-configured Kubernetes resources.

Use Helm to:

    Find and use popular software packaged as Helm Charts to run in Kubernetes
    Share your own applications as Helm Charts
    Create reproducible builds of your Kubernetes applications
    Intelligently manage your Kubernetes manifest files
    Manage releases of Helm packages

Helm in a Handbasket

Helm is a tool that streamlines installing and managing Kubernetes applications. Think of it like apt/yum/homebrew for Kubernetes.

    Helm renders your templates and communicates with the Kubernetes API
    Helm runs on your laptop, CI/CD, or wherever you want it to run.
    Charts are Helm packages that contain at least two things:
        A description of the package (Chart.yaml)
        One or more templates, which contain Kubernetes manifest files
    Charts can be stored on disk, or fetched from remote chart repositories (like Debian or RedHat packages)


%prep
%setup -q -n %{repo}-%{version}


%build
export GO111MODULE=on
cd cmd/helm
go build -ldflags=-linkmode=external -o helm


%install
install -Dpm 0755 cmd/helm/helm %{buildroot}%{_bindir}/helm


%if 0%{?with_check}
%check
export GO111MODULE=on
cd cmd/helm
go test -mod vendor
%endif


%files
%license LICENSE
%doc README.md
%{_bindir}/helm


%changelog
* Fri Jul 30 2021 Ben Reedy <breed808@breed808.com> - 3.6.3-1
- Update to latest upstream release

* Wed Feb 05 2020 Ben Reedy <breed808@breed808.com> - 3.1.1-1
- Initial package
