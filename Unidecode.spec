#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Unidecode
Version  : 1.1.2
Release  : 17
URL      : https://files.pythonhosted.org/packages/45/dd/544c34ddf9ab0ead3746110ad6fbdac26ca5f4a1666db22dc8aaf447d0c9/Unidecode-1.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/45/dd/544c34ddf9ab0ead3746110ad6fbdac26ca5f4a1666db22dc8aaf447d0c9/Unidecode-1.1.2.tar.gz
Summary  : ASCII transliterations of Unicode text
Group    : Development/Tools
License  : GPL-2.0
Requires: Unidecode-bin = %{version}-%{release}
Requires: Unidecode-license = %{version}-%{release}
Requires: Unidecode-python = %{version}-%{release}
Requires: Unidecode-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=======================================================
        
        It often happens that you have text data in Unicode, but you need to
        represent it in ASCII. For example when integrating with legacy code that
        doesn't support Unicode, or for ease of entry of non-Roman names on a US
        keyboard, or when constructing ASCII machine identifiers from human-readable
        Unicode strings that should still be somewhat intelligible. A popular example
        of this is when making an URL slug from an article title.
        
        **Unidecode is not a replacement for fully supporting Unicode for strings in
        your program. There are a number of caveats that come with its use,
        especially when its output is directly visible to users. Please read the rest
        of this README before using Unidecode in your project.**
        
        In most of examples listed above you could represent Unicode characters as
        ``???`` or ``\\15BA\\15A0\\1610``, to mention two extreme cases. But that's
        nearly useless to someone who actually wants to read what the text says.

%package bin
Summary: bin components for the Unidecode package.
Group: Binaries
Requires: Unidecode-license = %{version}-%{release}

%description bin
bin components for the Unidecode package.


%package license
Summary: license components for the Unidecode package.
Group: Default

%description license
license components for the Unidecode package.


%package python
Summary: python components for the Unidecode package.
Group: Default
Requires: Unidecode-python3 = %{version}-%{release}
Provides: unidecode-python

%description python
python components for the Unidecode package.


%package python3
Summary: python3 components for the Unidecode package.
Group: Default
Requires: python3-core
Provides: pypi(unidecode)

%description python3
python3 components for the Unidecode package.


%prep
%setup -q -n Unidecode-1.1.2
cd %{_builddir}/Unidecode-1.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609284851
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Unidecode
cp %{_builddir}/Unidecode-1.1.2/LICENSE %{buildroot}/usr/share/package-licenses/Unidecode/4cc77b90af91e615a64ae04893fdffa7939db84c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/unidecode

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Unidecode/4cc77b90af91e615a64ae04893fdffa7939db84c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
