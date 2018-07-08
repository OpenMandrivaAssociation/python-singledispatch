%define module	singledispatch

Name:		python-%{module}
Version:	3.4.0.3
Release:	2
Summary:	This library brings functools.singledispatch from Python 3.4 to Python 2.6-3.3
Group:		Development/Python
License:	MIT
URL:		http://docs.python.org/3/library/functools.html#functools.singledispatch
Source0:	https://pypi.python.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
BuildRequires:  pkgconfig(python3)
BuildRequires:  python-setuptools
#BuildRequires:  python2-pkg-resources
BuildRequires:  python3egg(six)


%description
PEP 443 proposed to expose a mechanism in the functools standard library
module in Python 3.4 that provides a simple form of generic programming
known as single-dispatch generic functions.

This library is a backport of this functionality to Python 2.6 - 3.3.

#---------------------------------------------------------------------------

%package -n     python2-%{module}
Summary:        This library brings functools.singledispatch from Python 3.4 to Python 2.6-3.3
Group:          Development/Python
BuildArch:      noarch

%description -n python2-%{module}
PEP 443 proposed to expose a mechanism in the functools standard library
module in Python 3.4 that provides a simple form of generic programming
known as single-dispatch generic functions.

This library is a backport of this functionality to Python 2.6 - 3.3.

This is the Python 3 build of %{module}.

#---------------------------------------------------------------------------
%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
rm -rf %{module}.egg-info

# remove /usr/bin/env python from scripts
sed -i '1d' singledispatch.py
sed -i '1d' singledispatch_helpers.py

cp -a . %{py3dir}

%build
python2 setup.py build

pushd %{py3dir}
python3 setup.py build
popd

%install
python2 setup.py install --root=%buildroot

pushd %{py3dir}
python3 setup.py install --root=%buildroot
popd

%check
%{__python2} setup.py test

pushd %{py3dir}
%{__python3} setup.py test
popd

%files
%doc README.rst
%{python3_sitelib}/%{module}.py*
%{python3_sitelib}/%{module}_helpers.py*
%{python3_sitelib}/%{module}-%{version}-py%{python3_version}.egg-info

%files -n python2-%{module}
%doc README.rst
%{python2_sitelib}/%{module}.py*
%{python2_sitelib}/%{module}_helpers.py*
%{python2_sitelib}/%{module}-%{version}-py%{python2_version}.egg-info
