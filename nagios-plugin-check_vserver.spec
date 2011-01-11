%define		plugin	check_vserver
Summary:	Nagios plugin to check vserver guest status
Name:		nagios-plugin-%{plugin}
Version:	1.0
Release:	0.1
License:	GPL v2
Group:		Networking
Source0:	http://exchange.nagios.org/components/com_mtree/attachment.php?link_id=1219&cf_id=24/check_vserver
# Source0-md5:	217f967debd469dbec96e1ad16eadf33
Source1:	%{plugin}.cfg
URL:		http://exchange.nagios.org/directory/Plugins/Uncategorized/Opearting-Systems/Linux/check_vserver/details
BuildRequires:	rpm-pythonprov
Requires:	nagios-common
Requires:	nagios-plugins-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
The plugin check_vserver checks if named vserver is running on a local
machine.

%prep
%setup -qcT
install -p %{SOURCE0} %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin} $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
