# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/httpgzip
%global commit          b1c53ac65af9fd3d354d6f9ad30a0cca35e173ed

%global common_description %{expand:
httpgzip provides net/http-like primitives that use gzip compression 
when serving HTTP requests.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        net/http-like primitives with gzip compression for serving HTTP requests
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(golang.org/x/net/http/httpguts)

%if %{with check}
BuildRequires: golang(golang.org/x/tools/godoc/vfs/httpfs)
BuildRequires: golang(golang.org/x/tools/godoc/vfs/mapfs)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitb1c53ac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20180706gitb1c53ac
- Bump to commit b1c53ac65af9fd3d354d6f9ad30a0cca35e173ed

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180417gitd78e9b0
- First package for Fedora

