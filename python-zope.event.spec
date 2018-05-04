#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define	module zope.event
Summary:	Simple event system
Summary(pl.UTF-8):	Prosty system zdarzeń
Name:		python-%{module}
Version:	4.3.0
Release:	1
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/z/zope.event/zope.event-%{version}.tar.gz
# Source0-md5:	8ca737960741c6fd112972f3313303bd
URL:		http://www.zope.org/
%if %{with python2}
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-modules
Obsoletes:	Zope-Event
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

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif


%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install \
	--install-purelib=%{py_sitedir}

%py_postclean
%endif

%if %{with python3}
%py3_install \
	--install-purelib=%{py3_sitedir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%if %{with python2}
%{py_sitedir}/zope/event
%{py_sitedir}/zope.event-*.egg-info
%{py_sitedir}/zope.event-*-nspkg.pth
%endif

%files -n python3-%{module}
%defattr(644,root,root,755)
%if %{with python3}
%{py3_sitedir}/zope/event
%{py3_sitedir}/zope.event-*.egg-info
%{py3_sitedir}/zope.event-*-nspkg.pth
%endif
