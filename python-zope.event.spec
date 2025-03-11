#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define	module zope.event
Summary:	Simple event system
Summary(pl.UTF-8):	Prosty system zdarzeń
Name:		python-%{module}
Version:	4.5.0
Release:	5
License:	ZPL v2.1
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/zope-event/
Source0:	https://files.pythonhosted.org/packages/source/z/zope.event/zope.event-%{version}.tar.gz
# Source0-md5:	bc38324cb29ce2d759c3cb56ea199995
URL:		https://www.zope.org/
%if %{with python2}
BuildRequires:	python >= 1:2.7
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-zope.testrunner
%endif
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.5
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-zope.testrunner
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
Requires:	python-modules >= 1:2.7
Requires:	python-zope-base
Obsoletes:	Zope-Event < 3.5.0
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

%package -n python3-%{module}
Summary:	Simple event system
Summary(pl.UTF-8):	Prosty system zdarzeń
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5
Requires:	python3-zope-base

%description -n python3-%{module}
The zope.event package provides a simple event system. It provides:
- an event publishing system
- a very simple event-dispatching system on which more sophisticated
  event dispatching systems can be built. (For example, a type-based
  event dispatching system that builds on zope.event can be found in
  zope.component)

%description -n python3-%{module} -l pl.UTF-8
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
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python} -m zope.testrunner --test-path=src
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m zope.testrunner --test-path=src
%endif
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install \
	--install-purelib=%{py_sitescriptdir}

%py_postclean
%endif

%if %{with python3}
%py3_install \
	--install-purelib=%{py3_sitescriptdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%{py_sitescriptdir}/zope/event
%{py_sitescriptdir}/zope.event-%{version}-py*.egg-info
%{py_sitescriptdir}/zope.event-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/zope/event
%{py3_sitescriptdir}/zope.event-%{version}-py*.egg-info
%{py3_sitescriptdir}/zope.event-%{version}-py*-nspkg.pth
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,*.html,*.js}
%endif
