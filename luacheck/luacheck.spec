Name:           luacheck
Version:        0.23.0
Release:        1%{?dist}
Summary:        Linting and static analysis for Lua files

License:        MIT
URL:            http://github.com/mpeterv/luacheck
Source0:        https://github.com/mpeterv/luacheck/archive/%{version}.tar.gz

BuildRequires:  lua-devel
BuildArch:      noarch

%description
Luacheck is a static analyzer and a linter for Lua. Luacheck detects various issues such as usage of undefined global variables, unused variables and values, accessing uninitialized variables, unreachable code and more. Most aspects of checking are configurable: there are options for defining custom project-related globals, for selecting set of standard globals (version of Lua standard library), for filtering warnings by type and name of related variable, etc. The options can be used on the command line, put into a config or directly into checked files as Lua comments.

Luacheck supports checking Lua files using syntax of Lua 5.1, Lua 5.2, Lua 5.3 and LuaJIT. Luacheck itself is written in Lua and runs on all of mentioned Lua versions.


%prep
%setup -q

%build


%install
mkdir -p %{buildroot}%{lua_pkgdir}/
cp -r src/luacheck %{buildroot}%{lua_pkgdir}/
install -Dm755 bin/luacheck.lua %{buildroot}%{_bindir}/luacheck


%files
%license LICENSE
%doc CHANGELOG.md README.md
%{lua_pkgdir}/luacheck
%attr(0755,root,root) %{_bindir}/%{name}


%changelog
* Fri Aug 09 2019 Ben Reedy <breed808@breed808.com> - 0.23.0-1
- Update package to latest upstream version

* Mon Aug 06 2018 Ben Reedy <breed808@breed808.com> - 0.22.1-1
- Initial package
