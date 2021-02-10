%global debug_package %{nil}

Name:           neovim-nightly
Version:        0.0.1
Release:        1%{?dist}
Summary:        Nightly version of Neovim
License:        ASL 2.0
URL:            https://github.com/neovim/neovim
Source0:        https://github.com/neovim/neovim/releases/download/nightly/nvim-linux64.tar.gz
Source1:        sysinit.vim
Source2:        spec-template

Provides:       neovim
Conflicts:      neovim

ExclusiveArch:  x86_64


%description
Neovim is a refactor - and sometimes redactor - in the tradition of
Vim, which itself derives from Stevie. It is not a rewrite, but a
continuation and extension of Vim. Many rewrites, clones, emulators
and imitators exist; some are very clever, but none are Vim. Neovim
strives to be a superset of Vim, notwithstanding some intentionally
removed misfeatures; excepting those few and carefully-considered
excisions, Neovim is Vim. It is built for users who want the good
parts of Vim, without compromise, and more.


%prep
%autosetup -n nvim-linux64 -p1

%build


%install
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}

install -Dm0755 bin/nvim %{buildroot}%{_bindir}/nvim
install -Dm0644 lib/nvim/parser/c.so %{buildroot}/lib/nvim/parser/c.so
install -Dm0644 share/applications/nvim.desktop %{buildroot}%{_datadir}/application/nvim.desktop
cp -rp share/locale %{buildroot}%{_datadir}/locale
gzip share/man/man1/nvim.1
install -Dm0644 share/man/man1/nvim.1.gz %{buildroot}%{_mandir}/man1/nvim.1.gz
cp -rp share/nvim %{buildroot}%{_datadir}/nvim
install -Dm0644 share/pixmaps/nvim.png %{buildroot}%{_datadir}/pixmaps/nvim.png

install -p -m 644 %SOURCE1 %{buildroot}%{_datadir}/nvim/sysinit.vim
install -p -m 644 %SOURCE2 %{buildroot}%{_datadir}/nvim/template.spec


%files
%{_bindir}/nvim
/lib/nvim/parser/c.so
%{_datadir}/application/nvim.desktop
%{_datadir}/locale
%{_mandir}/man1/nvim.1.gz
%{_datadir}/nvim
%{_datadir}/pixmaps/nvim.png


%changelog
* Tue Feb 09 2021 Ben Reedy <breed808@breed808.com> - 0.0.1_e526dbecda137e37c45492ce72fa92ea32314154-1
- Initial package
