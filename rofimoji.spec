%global         srcname     rofimoji
Version:        6.3.1
%global         forgeurl    https://github.com/fdw/rofimoji
%global         tag         %{version}
%forgemeta

Name:           %{srcname}
Release:        %autorelease
Summary:        A character picker for rofi 😀

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed

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


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files picker


%files -n %{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/rofimoji


%changelog
%autochangelog
