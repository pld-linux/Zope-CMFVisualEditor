%include	/usr/lib/rpm/macros.python
%define		zope_subname	CMFVisualEditor
Summary:	A Zope product, a skin for Plone using the DHTML Editing Control
Summary(pl):	Dodatek do Zope umo¿liwiaj±cy wizualn± edycjê DHTML dla Plone
Name:		Zope-%{zope_subname}
Version:	0.2
Release:	7
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	c4dedabced3f11af450e6750e7201f8a
URL:		http://sourceforge.net/projects/collective/
%pyrequires_eq	python-modules
Requires:	Zope-CMF
Requires:	Zope-CMFPlone
Requires:	Zope
Requires(post,postun):  /usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	CMF
Conflicts:	Plone

%description
CMFVisualEditor is a Zope product, a skin for Plone that makes use of
the DHTML Editing Control.

%description -l pl
CMFVisualEditor jest dodatkiem do Zope umo¿liwiaj±cym wizualn± edycjê
DHTML dla Plone.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,i18n,skins,*.py,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
        /usr/sbin/installzopeproduct -d %{zope_subname}
        if [ -f /var/lock/subsys/zope ]; then
                /etc/rc.d/init.d/zope restart >&2
        fi
fi

%files
%defattr(644,root,root,755)
%doc README.txt LICENSE.*
%{_datadir}/%{name}
