Name:       sngrep
Summary:    Ncurses SIP Messages flow viewer
License:    GPL-3
Url:        https://github.com/irontec/sngrep
Version:    1.4.6
Release:    1%{?dist}
Source:     https://github.com/irontec/sngrep/releases/download/v%{version}/sngrep-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libpcap-devel
BuildRequires:  pcre-devel
BuildRequires:  gnutls-devel


%description
sngrep is a tool for displaying SIP calls message flows from terminal.
It supports live capture to display realtime SIP packets and can also be used as PCAP viewer.


%prep
%autosetup


%build
./bootstrap.sh
./configure --enable-unicode --enable-eep --with-gnutls --with-pcre --enable-ipv6 --prefix=/usr
make


%install
make DESTDIR=%{?buildroot:%{buildroot}} install

install -dm0755 %{buildroot}%{_sysconfdir}
# Install script places rc file in /usr/etc for some reason
mv %{buildroot}/usr/etc/sngreprc %{buildroot}%{_sysconfdir}/sngreprc


%files
%license LICENSE
%doc README
%{_bindir}/sngrep
%config(noreplace) %{_sysconfdir}/sngreprc
%{_mandir}/man8/sngrep.8.gz


%changelog
* Wed Jan 22 2020 Ben Reedy <breed808@breed808.com> - 1.4.6-1
- Initial package
