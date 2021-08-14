%global         srcname     rofimoji
Version:        5.3.0
%global         forgeurl    https://github.com/fdw/rofimoji
%global         tag         %{version}
%forgemeta

Name:           %{srcname}
Release:        1%{?dist}
Summary:        A character picker for rofi 😀

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

%py_provides    python3-picker

# Requirements for X11
Requires:       rofi
Requires:       xsel
Requires:       xclip
Requires:       xdotool

# Requirements for Wayland
Requires:       wofi
Requires:       wl-clipboard
Requires:       wtype

%description
How often did you want to insert one of those Unicode emoji only to learn that
there is no nice picker for Linux? Fear no more, this script uses the power of
rofi (and other dmenu-derivatives like wofi) to present exactly the picker you
always wanted. Insert the selected emoji directly, or copy it to the clipboard.
And you can use it to pick any weird character someone got into Unicode, too.

%prep
%autosetup -n %{srcname}-%{version}
sed -i -e '/^#!\//, 1d' src/picker/rofimoji.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Move the man page from the python3 sitelib directory
mkdir -vp %{buildroot}%{_mandir}/man1
mv %{buildroot}%{python3_sitelib}/share//man/man1/rofimoji.1 %{buildroot}%{_mandir}/man1

%pyproject_save_files picker

%files -n %{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/rofimoji
%{_mandir}/man1/%{name}.1*

%changelog
* Sat Aug 14 2021 Major Hayden <major@mhtx.net> - 5.3.0-1
- Update to 5.3.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 26 2021 Major Hayden <major@mhtx.net> - 5.2.0-1
- New version 5.2.0.

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.1.0-6
- Rebuilt for Python 3.10

* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 5.1.0-5
- Package 'rofimoji' as a package without a python3-rofimoji subpackage.

* Thu May 27 2021 Major Hayden <major@mhtx.net> - 5.1.0-4
- Switched to using pyproject-rpm-macros.

* Mon May 24 2021 Major Hayden <major@mhtx.net> - 5.1.0-3
- Added extra X11/Wayland requirements.
- Removed shebangs in rofimoji.py.
- Added wildcard for future man page compression changes.

* Fri May 14 2021 Major Hayden <major@mhtx.net> - 5.1.0-2
- Remove check section since upstream has no tests.

* Fri May 14 2021 Major Hayden <major@mhtx.net> - 5.1.0-1
- Initial build.
