Name:          sailfish-weather-widget-patch
Summary:       Patch: Extend number of days in Weather forecast widget
Version:       0.0.2
Release:       1
Group:         System/Tools
BuildArch:     noarch
Requires:      patchmanager
Requires:      sailfish-weather >= 0.2.6
Requires:      sailfish-weather <= 1.0.0

Vendor:        pichlo
Distribution:  SailfishOS
Packager:      Peter Pichler <maemo@pichler.co.uk>
URL:           https://openrepos.net/content/pichlo/patch-extend-number-days-weather-forecast-widget

License:       GPL

%description
Extend number of days in the Weather forecast widget in eventsview

#%prep
#%setup -q -n %{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfish-weather-widget-patch
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfish-weather-widget-patch

%pre
if [ -f /usr/sbin/patchmanager ]; then
    /usr/sbin/patchmanager -u sailfish-weather-widget-patch || true
fi

%preun
if [ -f /usr/sbin/patchmanager ]; then
    /usr/sbin/patchmanager -u sailfish-weather-widget-patch || true
fi

%files
%defattr(644,root,root,-)
%{_datadir}/patchmanager/patches/sailfish-weather-widget-patch

%changelog
* Thu Jan 10 2019 Peter Pichler <maemo@pichler.co.uk> 0.0.2-1
- Made the ratio between portrait and landscape number of icons dynamic, depending on the screen aspect ratio.

* Thu Jan 10 2019 Peter Pichler <maemo@pichler.co.uk> 0.0.1-5
- Update for SFOS 3.0.1.x
- The easiest update in history. No files changed, only the version number dependency.

* Thu Nov 01 2018 Peter Pichler <maemo@pichler.co.uk> 0.0.1-4
- Update for SFOS 3.0.0.x.
- Increase the number of days in landscape from 8 to 9. It matches closer the screen aspect ratio of 16:9 (5 * 16/9 = 8.889).

* Thu Feb 09 2017 Peter Pichler <maemo@pichler.co.uk> 0.0.1-3
- Update for SFOS 2.1.0.x.

* Sun Jun 19 2016 Peter Pichler <maemo@pichler.co.uk> 0.0.1-2
- Update dependencies to satisfy SFOS 2.0.2.x.

* Fri Nov 13 2015 Peter Pichler <maemo@pichler.co.uk> 0.0.1-1
- First build.