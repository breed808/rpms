%global debug_package %{nil}
%bcond_without check

Name:       vivid
Version:    0.5.0
Release:    1%{?dist}
Summary:    LS_COLORS generator

License:    MIT
URL:        https://crates.io/crates/vivid
Source0:    https://github.com/sharkdp/%{name}/archive/v%{version}.tar.gz

BuildRequires:  rust-packaging
BuildRequires:  cmake
BuildRequires:  libssh2-devel

ExclusiveArch:  %{rust_arches}

%description
vivid is a generator for the LS_COLORS environment variable that controls the colorized output of ls, tree, fd, etc.

It uses a YAML-based configuration format for the filetype-database and the color themes.
In contrast to dircolors, the database and the themes are organized in different files.
This allows users to choose and customize color themes independent from the collection of file extensions.
Instead of using (cryptic) ANSI escape codes, colors can be specified in the RRGGBB format and will be translated to either truecolor (24-bit) ANSI codes or 8-bit codes for older terminal emulators.


%prep
%autosetup -n %{name}-%{version} -p1


%build
cargo build --release


%install
install -Dm0755 target/release/vivid %{buildroot}%{_bindir}/vivid
install -Dm644 -t %{buildroot}%{_datadir}/vivid config/filetypes.yml
install -Dm644 -t %{buildroot}%{_datadir}/vivid/themes themes/*


%files
%license LICENSE-MIT
%doc README.md
%{_bindir}/vivid
%{_datadir}/vivid

%changelog
* Tue Mar 24 2020 Ben Reedy <breed808@breed808.com> - 0.5.0-1
- Update to latest upstream release

* Fri Aug 02 2019 Ben Reedy <breed808@breed808.com> - 0.4.0-1
- Initial package
