# Go compiler sets its own build ID, causing the build to fail.
%undefine _missing_build_ids_terminate_build

%global debug_package %{nil}

Name:           tanka
Version:        0.17.1
Release:        1%{?dist}
Summary:        Flexible, reusable and concise configuration for Kubernetes
License:        ASL 2.0
URL:            https://github.com/grafana/tanka/
Source0:        https://github.com/grafana/tanka/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  git

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%description
The clean, concise and super flexible alternative to YAML for your Kubernetes cluster

Clean: The Jsonnet language expresses your apps more obviously than YAML ever did
Reusable: Build libraries, import them anytime and even share them on GitHub!
Concise: Using the Kubernetes library and abstraction, you will never see boilerplate again!
Confidence: Stop guessing and use tk diff to see what exactly will happen
Helm: Vendor in, modify, and export Helm charts reproducibly
Production ready: Tanka deploys Grafana Cloud and many more production setups


%prep
%autosetup


%build
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
go build -ldflags="-X main.Version=%{version}" -o tk ./cmd/tk


%install
install -Dm0755 tk %{buildroot}%{_bindir}/tk


%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/tk


%changelog
* Fri Jul 30 2021 Ben Reedy <breed808@breed808.com> - 0.17.1-1
- Initial package
