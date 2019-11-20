%global         vimfiles        %{_datadir}/nvim/runtime

Name:           nvim-ale
Version:        2.6.0
Release:        1%{?dist}
Summary:        Asynchronous Lint Engine for Vim/NeoVim
License:        BSD
URL:            https://github.com/dense-analysis/ale
Source0:        https://github.com/dense-analysis/ale/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  neovim

%description
ALE (Asynchronous Lint Engine) is a plugin for providing linting in NeoVim and
Vim 8 while you edit your text files.

ALE makes use of NeoVim and Vim 8 job control functions and timers to run linters
on the contents of text buffers and return errors as text is changed in Vim.
This allows for displaying warnings and errors in files being edited in Vim before
files have been saved back to a filesystem.

In other words, this plugin allows you to lint while you type.

%define add_subpackage(n:)                                                          \
%package %{-n*}                                                                     \
Summary:        A syntax checker for %{-n*} programming language                    \
Requires:       %{name} =  %{version}-%{release}                                    \
Requires:       %*                                                                  \
%description %{-n*}                                                                 \
Allows checking %{-n*} sources files.                                               \

%add_subpackage -n ansible ansible-lint
%add_subpackage -n asciidoc asciidoc proselint
%add_subpackage -n asm gcc nasm
%add_subpackage -n c gcc
# %%add_subpackage -n chef foodcritic
%add_subpackage -n cpp gcc-c++
%add_subpackage -n cs mono-core
# No stylelint in Fedora repos, only csslint
%add_subpackage -n css csslint
# %%add_subpackage -n d dmd
# %%add_subpackage -n dockerfile hadolint
# %%add_subpackage -n elixir credo dogma
# %%add_subpackage -n elm elm-make
%add_subpackage -n erlang erlang-erts
%add_subpackage -n eruby rubygem-erubis
%add_subpackage -n fish fish
%add_subpackage -n fortran gcc-gfortran
%add_subpackage -n go golang-bin golint
# ale only support hamllint, need to add support for haml upstream
# %%add_subpackage -n haml rubygem-haml
%add_subpackage -n haskell ghc hlint
%add_subpackage -n help proselint
# No htmlhint in repos
%add_subpackage -n html proselint tidy
%add_subpackage -n java java-devel
# %%add_subpackage -n javascript eslint flow jscs jshint standard xo
# jsonlint not in repos
%add_subpackage -n json jq
%add_subpackage -n lua lua luacheck
%add_subpackage -n markdown proselint rubygem-mdl
# Need to add octave as upstream checker. No mlint found in repos
# %%add_subpackage -n matlab octave mlint
# %%add_subpackage -n nim nimcheck
# %%add_subpackage -n nix nix
%add_subpackage -n nroff proselint
# Need to add ocaml checker upstream. Merlin not found in repos.
# %%add_subpackage -n ocaml ocaml merlin
%add_subpackage -n perl perl perl-Task-Perl-Critic
# hack and phpcs not found in repos
%add_subpackage -n php php php-phpmd-PHP-PMD
%add_subpackage -n pod proselint
%add_subpackage -n pug puglint
# puppetlint not found in repos
%add_subpackage -n puppet puppet
%add_subpackage -n pyrex python3-Cython
%add_subpackage -n python python3-flake8 python3-mypy python3-pylint python3-pycodestyle python3-vulture
%add_subpackage -n rst proselint
%add_subpackage -n ruby ruby
%add_subpackage -n rust cargo rls
# %%add_subpackage -n sass sasslint stylelint
# %%add_subpackage -n scss scsslint sasslint stylelint
%add_subpackage -n sh bash ShellCheck
# %%add_subpackage -n slim slimlint
# %%add_subpackage -n sml smlnj
# %%add_subpackage -n sml smlnj
%add_subpackage -n spec rpmlint
# %%add_subpackage -n swift swiftlint
# %%add_subpackage -n testft testlinter
%add_subpackage -n tex texlive-chktex-bin texlive-lacheck-bin
%add_subpackage -n texinfo proselint
%add_subpackage -n text proselint
# %%add_subpackage -n typescript tslint typecheck
%add_subpackage -n verilog iverilog verilator
%add_subpackage -n xhtml proselint
%add_subpackage -n xml libxml2
%add_subpackage -n yaml yamllint
%add_subpackage -n vim vint

%prep
%setup -qn "ale-%{version}"

%build

%install
mkdir -p %{buildroot}%{vimfiles}/autoload
mkdir -p %{buildroot}%{vimfiles}/doc/

cp      -rp       ale_linters/      %{buildroot}%{vimfiles}/ale_linters
cp      -rp       autoload/*        %{buildroot}%{vimfiles}/autoload/
install -p -m0644 doc/*.txt         %{buildroot}%{vimfiles}/doc/
cp      -rp       ftplugin/         %{buildroot}%{vimfiles}/ftplugin
cp      -rp       plugin/           %{buildroot}%{vimfiles}/plugin
cp      -rp       syntax/           %{buildroot}%{vimfiles}/syntax

%post
nvim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %{vimfiles}/doc/' '+qa!' < /dev/null &> /dev/null

%postun
nvim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %{vimfiles}/doc/' '+qa!' < /dev/null &> /dev/null

%files
%license LICENSE
%dir %{vimfiles}/autoload
%dir %{vimfiles}/autoload/ale/
%dir %{vimfiles}/autoload/ale/completion
%dir %{vimfiles}/autoload/ale/engine
%dir %{vimfiles}/doc
%dir %{vimfiles}/plugin
%{vimfiles}/ale_linters/
%{vimfiles}/autoload/asyncomplete/sources/ale.vim
%{vimfiles}/autoload/ale.vim
%{vimfiles}/autoload/ale/*.vim
%{vimfiles}/autoload/ale/engine/ignore.vim
%{vimfiles}/autoload/ale/completion/python.vim
%{vimfiles}/autoload/ale/gradle/init.gradle
%{vimfiles}/autoload/ale/fix/*.vim
%{vimfiles}/autoload/ale/fixers/*.vim
%{vimfiles}/autoload/ale/handlers/*.vim
%{vimfiles}/autoload/ale/lsp/*.vim
%{vimfiles}/doc/ale*.txt
%{vimfiles}/ftplugin/*.vim
%{vimfiles}/plugin/ale.vim
%{vimfiles}/syntax/*.vim

%files ansible
%{vimfiles}/ale_linters/ansible

%files asciidoc
%{vimfiles}/ale_linters/asciidoc

%files asm
%{vimfiles}/ale_linters/asm

%files c
%{vimfiles}/ale_linters/c

%files cpp
%{vimfiles}/ale_linters/cpp

%files cs
%{vimfiles}/ale_linters/cs

%files css
%{vimfiles}/ale_linters/css

%files erlang
%{vimfiles}/ale_linters/erlang

%files fortran
%{vimfiles}/ale_linters/fortran

%files go
%{vimfiles}/ale_linters/go

%files haskell
%{vimfiles}/ale_linters/haskell

%files help
%{vimfiles}/ale_linters/help

%files html
%{vimfiles}/ale_linters/html

%files java
%{vimfiles}/ale_linters/java

%files json
%{vimfiles}/ale_linters/json

%files lua
%{vimfiles}/ale_linters/lua

%files markdown
%{vimfiles}/ale_linters/markdown

%files nroff
%{vimfiles}/ale_linters/nroff

%files perl
%{vimfiles}/ale_linters/perl

%files php
%{vimfiles}/ale_linters/php

%files pod
%{vimfiles}/ale_linters/pod

%files pug
%{vimfiles}/ale_linters/pug

%files puppet
%{vimfiles}/ale_linters/puppet

%files pyrex
%{vimfiles}/ale_linters/pyrex

%files python
%{vimfiles}/ale_linters/python

%files ruby
%{vimfiles}/ale_linters/ruby

%files rst
%{vimfiles}/ale_linters/rst

%files rust
%{vimfiles}/ale_linters/rust

%files sh
%{vimfiles}/ale_linters/sh

%files spec
%{vimfiles}/ale_linters/spec

%files tex
%{vimfiles}/ale_linters/tex

%files texinfo
%{vimfiles}/ale_linters/texinfo

%files text
%{vimfiles}/ale_linters/text

%files verilog
%{vimfiles}/ale_linters/verilog

%files xhtml
%{vimfiles}/ale_linters/xhtml

%files xml
%{vimfiles}/ale_linters/xml

%files yaml
%{vimfiles}/ale_linters/yaml

%files vim
%{vimfiles}/ale_linters/vim

%changelog
* Fri Oct 18 2019 Ben Reedy <breed808@breed808.com> - 2.6.0-1
- Upstream release

* Fri Aug 09 2019 Ben Reedy <breed808@breed808.com> - 2.5.0-3
- Change vim dependecy from python2-vint to vint. vint package is supplied by official Fedora repos.

* Fri Jul 26 2019 Ben Reedy <breed808@breed808.com> - 2.5.0-2
- Add Rust subpackage

* Tue Jun 11 2019 Ben Reedy <breed808@breed808.com> - 2.5.0-1
- Upstream release

* Tue Jun 04 2019 Ben Reedy <breed808@breed808.com> - 2.4.1-1
- Upstream release

* Mon Apr 08 2019 Ben Reedy <breed808@breed808.com> - 2.4.0-1
- Upstream release

* Tue Feb 26 2019 Ben Reedy <breed808@breed808.com> - 2.3.1-1
- Initial nvim package

* Wed Feb 13 2019 Ben Reedy <breed808@breed808.com> - 2.3.0-1
- Initial nvim package
