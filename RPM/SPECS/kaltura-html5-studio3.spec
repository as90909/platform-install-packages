%define prefix /opt/kaltura
%define studio_prefix %{prefix}/apps/studioV3

Summary: Kaltura Open Source Video Platform 
Name: kaltura-html5-studio3
Version: v3.16.0
Release: 1
License: AGPLv3+
Group: Server/Platform 
Source0: %{name}-%{version}.tar.bz2 
Source1: studio3.template.ini
URL: https://github.com/kaltura/player-studio/releases/download/%{version}/studio_%{version}.zip 
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
Kaltura is the world's first Open Source Online Video Platform, transforming the way people work, 
learn, and entertain using online video. 
The Kaltura platform empowers media applications with advanced video management, publishing, 
and monetization tools that increase their reach and monetization and simplify their video operations. 
Kaltura improves productivity and interaction among millions of employees by providing enterprises 
powerful online video tools for boosting internal knowledge sharing, training, and collaboration, 
and for more effective marketing. Kaltura offers next generation learning for millions of students and 
teachers by providing educational institutions disruptive online video solutions for improved teaching,
learning, and increased engagement across campuses and beyond. 
For more information visit: http://corp.kaltura.com, http://www.kaltura.org and http://www.html5video.org.

This package installs the Kaltura HTML5 Studio v3.

%prep
%setup -q



%install
mkdir -p $RPM_BUILD_ROOT%{studio_prefix}
rm -f %{_builddir}/%{name}-%{version}/studio.ini
cp -r %{_builddir}/%{name}-%{version} $RPM_BUILD_ROOT%{studio_prefix}/%{version}
cp %{SOURCE1} $RPM_BUILD_ROOT%{studio_prefix}/%{version}/studio.template.ini
sed -i "s#@HTML5_STUDIO3_VER@#%{version}#g" $RPM_BUILD_ROOT%{studio_prefix}/%{version}/studio.template.ini

%clean
rm -rf %{buildroot}

%post


%postun

%files
%defattr(-, root, root, 0755)
%{studio_prefix}/%{version}

%changelog
* Mon Mar 28 2022 jess.portnoy@kaltura.com <Jess Portnoy> - 3.13.0-1
- feat(FEC-11590): Related grid Studio requirements #120
- feat(FEC-12028): Skip Plugin - Studio #122

* Thu Jul 8 2021 jess.portnoy@kaltura.com <Jess Portnoy> - 3.12.2-1
- fix(FEC-11367): "Share and embed" instead of "Share and Embed" (#116)
- fix(FEC-11384): studio is crashing on null pointer (#117)
- https://kaltura.atlassian.net/browse/FEC-9180
- https://kaltura.atlassian.net/browse/FEC-11357
- https://kaltura.atlassian.net/browse/FEC-11369

* Mon Jun 14 2021 jess.portnoy@kaltura.com <Jess Portnoy> - 3.11.0-1
- FEC-11175: add new languages to studio (#111)
- FEC-10955: Deprecate FLASH playback option (#112)

* Mon Feb 1 2021 jess.portnoy@kaltura.com <Jess Portnoy> - 3.9.0-1
- feat(FEC-10695): add screen lock orientation to studio (#103)
- feat(FEC-9451): Bumper Studio Configuration (#102)
- feat(FEC-10709, FEC-10712): player visibility - Auto-pause when player is out of view, Autoplay only when player is in view (#98)
- feat(FEC-10550): [Timeline Markers] Ad break indication on the timeline (#100)

* Wed Oct 14 2020 jess.portnoy@kaltura.com <Jess Portnoy> - 3.8.0-1
- feat(FEC-10401): add analytics plugins in studio (#94)

* Tue Aug 11 2020 jess.portnoy@kaltura.com <Jess Portnoy> - 3.7.0-1
- feat(FEC-10283): add arbitrary studio config in advanced menu (#92)
- feat(FEC-10105): as a platform user I would like to be able to toggle floating player re-positioning capability on and off (#91)


* Fri Jul 31 2020 jess.portnoy@kaltura.com <Jess Portnoy> - 3.6.0-1
- FEC-9649: external css (#90)
- FEC-9732: DFP DAI - Studio Configuration (#87)
- FEC-9972: floating player (#88)

* Mon May 18 2020 jess.portnoy@kaltura.com <Jess Portnoy> - 3.5.0-1
- FEC-9465: Internationalisation (i18n) - player localisation (#78)
- FEC-9622: Localisation studio configuration (#78)
- FEC-9653: https://github.com/kaltura/player-studio/pull/79
- FEC-9621: Translate player labels to default languages (#80)
- FEC-10019: https://github.com/kaltura/player-studio/pull/84
- FRC-10020: https://github.com/kaltura/player-studio/pull/83

* Mon Mar 18 2019 jess.portnoy@kaltura.com <Jess Portnoy> - v3.3.0-1
- FEC-8880: add support for youtube
- FEC-8805: playlist support
- FEC-8894: OVP player identified as OTT after creating OTT player
- FEC-8895: OTT player identified as OVP


* Thu Feb 7 2019 jess.portnoy@kaltura.com <Jess Portnoy> - v3.2.3-1
- First release
