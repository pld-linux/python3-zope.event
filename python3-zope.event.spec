#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

%define	module zope.event
Summary:	Simple event system
Summary(pl.UTF-8):	Prosty system zdarzeń
Name:		python3-%{module}
Version:	5.0
Release:	1
License:	ZPL v2.1
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/zope-event/
Source0:	https://files.pythonhosted.org/packages/source/z/zope.event/zope.event-%{version}.tar.gz
# Source0-md5:	8639012f7c6a762d245f9229a6e900af
URL:		https://www.zope.org/
BuildRequires:	python3 >= 1:3.7
BuildRequires:	python3-devel >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-zope.testrunner
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.7
Requires:	python3-zope-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The zope.event package provides a simple event system. It provides:
- an event publishing system
- a very simple event-dispatching system on which more sophisticated
  event dispatching systems can be built. (For example, a type-based
  event dispatching system that builds on zope.event can be found in
  zope.component)

%description -l pl.UTF-8
Pakiet zope.event udostępnia prosty system zdarzeń. Zawiera:
- system publikacji zdarzeń
- bardzo prosty system przekazywania zdarzeń, w oparciu o który można
  stworzyć bardziej wyszukane systemy przekazywania zdarzeń (na przykład
  system przekazywania zdarzeń oparty na typach, zbudowany w oparciu o
  zope.event, można znaleźć w zope.component)

%package apidocs
Summary:	API documentation for Python zope.event module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona zope.event
Group:		Documentation

%description apidocs
API documentation for Python zope.event module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona zope.event.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m zope.testrunner --test-path=src
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt README.rst
%{py3_sitescriptdir}/zope/event
%{py3_sitescriptdir}/zope.event-%{version}-py*.egg-info
%{py3_sitescriptdir}/zope.event-%{version}-py*-nspkg.pth

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,*.html,*.js}
%endif
